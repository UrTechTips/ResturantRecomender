import json
import pandas as pd

def convert_to_csv():
    files = [
        './Data/file1.json',
        './Data/file2.json'
    ]
    extraColumns = ['photos_url', 'url',"apikey", "is_delivering_now", "menu_url", "deeplink", "book_url", "switch_to_order_menu", "offers", "has_table_booking", "zomato_events", "establishment_types", "events_url", "featured_image", "order_deeplink", "order_url", "currency", "R"]
    tempdata = []

    # Load the Datas and make append them to a final Dataset
    for i in files:
        with open(i, 'r+') as file:
            data = json.load(file)
            for j in data:
                if ("restaurants" not in j.keys()):
                    print(j)
                else:
                    if (j["restaurants"]):
                        for restaurant in j["restaurants"]:
                            res = {}
                            for item in restaurant['restaurant']:
                                if item in extraColumns:
                                    continue
                                else:
                                    res[item] = restaurant['restaurant'][item]

                            tempdata.append(res)

    with open('./Data/finalFile.json', 'w+', encoding="utf8") as f:
        json.dump(tempdata, f, indent=4)

    # Convert into CSV file for ease access
    with open('./Data/finalFile.json', "r+", encoding="utf8") as f:
        df = pd.read_json(f)

    df.to_csv("./Data/dataset.csv", encoding="utf8")

def preprocess():
    with open("./Data/dataset.csv", encoding="utf8") as fs:
        df = pd.read_csv(fs)
    
    df.drop(columns=['j', 'thumb', 'location'], inplace=True)
    df.dropna(inplace=True)

    df.to_csv("data.csv", encoding="utf8")
    return df

if __name__ == "__main__":
    df = preprocess()
    print(df)