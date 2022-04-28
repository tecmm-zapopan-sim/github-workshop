from Data.data import get_data

if __name__ == '__main__':
    df = get_data("./Data/data.csv")
    print(df.head())