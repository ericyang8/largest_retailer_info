from bs4 import BeautifulSoup
import requests
import pandas as pd



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "https://nrf.com/research-insights/top-retailers/top-100-retailers/top-100-retailers-2023-list"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    # retrieves the information for top 100 retailers in 2023 as determined by the NRF

    data = {
        "rank": [],
        "name": [],
        "hq_location": [],
        "sale_growth": [],
        "retail_sale": [],
        "us_%_of_world_sale": [],
        "store_count": [],
        "store_growth": [],
        "note": []
    }

    store_info = doc.find_all(class_="data-cell-0")

    for i in range(0, len(store_info)):
        current_store = store_info[i].parent
        print(current_store)
        data["rank"].append(int(current_store.find(class_="data-cell-0").string))
        data["name"].append(current_store.find(class_="data-cell-1").string)
        data["hq_location"].append(current_store.find(class_="data-cell-2").string)
        data["sale_growth"].append(current_store.find(class_="data-cell-3").string)
        data["retail_sale"].append(current_store.find(class_="data-cell-4").string)
        data["us_%_of_world_sale"].append(current_store.find(class_="data-cell-6").string)
        data["store_count"].append(current_store.find(class_="data-cell-7").string)
        data["store_growth"].append(current_store.find(class_="data-cell-8").string)
        data["note"].append(current_store.find(class_="data-cell-9").string)


    df = pd.DataFrame(data)
    df.to_csv("top100retailer.csv")
