import pandas as pd

# Preprocessing

def preprocess():
    zdf = pd.read_csv("./zomato.csv", encoding="latin-1")

    zdf.drop(columns=['Locality Verbose', 'Switch to order menu', 'Rating color', 'Rating text'], inplace=True)
    zdf.dropna(inplace=True)

    countryDF = pd.read_excel("./Data/Country-Code.xlsx")
    df = pd.merge(zdf, countryDF, how="left", on='Country Code')

    return df

if __name__ == "__main__":
    df = preprocess()
    print(df.head(10))
