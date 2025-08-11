from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/") # Connection
db =  client["internship"]                         # Database
collection = db["task_manager"]                    # Collection

# CRUD Operations

def create_task(title, description, status = "In Progress"):
    task = {
        "title" : title,
        "description" : description,
        "status": status
    }
    result = collection.insert_one(task)
    print(f"Inserted task object with reference ObjectID as {str(result.inserted_id)}")
    return str(result.inserted_id)

def read_all_task():
    result = list(collection.find())
    for res in result:
        print(res)
    return result

def read_task(task_id):
    result = collection.find_one({"_id": ObjectId(task_id)})
    if not result:
        print("No ObjectID Found")
        return None
    for key, value in result.items():
        print(f"{key} : {value}")
    return result

def update_task(task_id, title = None, description = None, status = None):
    update_dict = {}
    if title:
        update_dict["title"] = title
    if description:
        update_dict["description"] = description
    if status:
        update_dict["status"] = status

    result = collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": update_dict}
    )

    if result.matched_count:
        print(f"Updated Successfully")
    else:
        print("Failed")

def delete_task(task_id):
    result = collection.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count:
         print(f"Deleted Successfully")
    else:
        print("Failed")

if __name__ == "__main__":
    # create_task("Project Work", "CRUD Operations", "In Progress")
    # read_all_task()
    # read_task("68994fdfa306a3e668c06fb2")
    # update_task("68994fdfa306a3e668c06fb2", title = "Internship Pragram", status = "On Going" )
    delete_task("689950000749b1a81586c775")
    read_all_task()