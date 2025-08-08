import pandas as pd

file_path = "backend/task.csv"

def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except:
        data  = {
    "id" : [],
    "title" : [],
    "description" : [],
    "status" : []
}
        return pd.DataFrame(data)
    
def export_df(df):
    try:
        df.to_csv(file_path, index=False)
    except:
        print("Failed while creating csv")
        return False

def save_task(data):
    try:
        df = load_csv(file_path)
        id_list = list(df["id"])
        if "id" not in data:
            for i in range(1, 100):
                if i not in id_list:
                    id_list.append(i)
                    data["id"]  = i
                    break
    
        df = df._append(data, ignore_index = True)
        df['id'] = df["id"].astype("int64")
        export_df(df)
        return True
    except:
        print("Failed while creating task")
        return False

def get_tasks():
    df = pd.read_csv(file_path)
    df = df[["id", "title", "description", "status"]]
    return df.to_dict()

def update_tasks(data):
    try:
        df = pd.read_csv(file_path)
        # _id = int(data["id"])
        # df2 = df[df["id"] == _id]
        # for i in list(data.keys()):
        #     df2[i] = data[i]
        # df[df["id"] == _id] = df2

        indexed_row = df[df["id"] == int(data["id"])]
        ind = indexed_row.index[0]
        for i in list(data.keys()):
            df.at[ind, i] = data[i]
        
        export_df(df)
        return True, df.to_dict()
    except:
        print("Failed while updating task")
        return False, df.to_dict()
 

def remove_task(task_id:int):
    try:
        df = pd.read_csv(file_path)
        if task_id in list(df['id']):
            df = df[df['id'] != task_id]
        export_df(df)
        return True
    except:
        print("Failed while deleting task")
        return False
