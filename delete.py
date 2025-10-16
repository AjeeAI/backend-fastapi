from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
    {"name": "Sam Larry", "track": "AI Developer"},
    {"name": "Jane Doe", "track": "Web Developer"},
    {"name": "John Smith", "track": "Data Scientist"}
    
]
class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status = 200):
        self.send_response(status)
        self.send_header('content-type', "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())
        
    def do_DELETE(self):
        content_size = int(self.headers.get("content-length", 0))
        parsed_data = self.rfile.read(content_size)
        delete_data = json.loads(parsed_data)
        
        if "index" not in delete_data:
            self.send_data({
                "Message": "Invalid request. 'index' field is required."
            }, status=400)
            return
        
        index = delete_data["index"]
        
        if not isinstance(index, int) or index < 0 or index >= len(data):
            self.send_data({
                "Message": "Index out of range."
            }, status=400)
            return
        
        removed_data = data.pop(index)
        self.send_data({
            "Message": "Data Deleted",
            "data": removed_data
        })
        
def run():
    HTTPServer(("localhost", 8000), BasicAPI).serve_forever()
print("Application is running")
run()