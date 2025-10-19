data = [{"name": "Sam Larry", "Age": 20, "track": "AI Developer"},
    {"name": "Bahubali", "Age": 21, "track": "Backend Developer"},
    {"name": "John Doe", "Age": 22, "track": "Frontend Developer"}]

# data_dict = {"name": "John Doe", "Age": 22, "track": "Frontend Developer"}
# print(data_dict)
# print(data)
id = 1
new_name = "Ajee"
# print(data[id])
for i in range(len(data)):
    if i == id:
        print(data[i])
        print(data[i]["name"])
        # data[i].name = new_name
        data[i]["name"] = new_name
        
        print(data)   
    else:
        print("Data not found")
print("Working...")
print(data)