from Data.data import get_data

if __name__ == '__main__':
    df = get_data("./Data/data.csv")
    df = df[df.iloc[:,0]>=5]
    df = df.iloc[:,0] + 5
    print(df.head())