import pandas as pd
df = pd.read_csv("ecommerce_data.csv")
print(df.info())
df["OrderDate"]=pd.to_datetime(df["OrderDate"])
df = df[df['Price'].notna() & (df['Price'] > 0)]
df = df[df['Quantity'] > 0]
df['Category'] = df['Category'].fillna('Other')
df = df.drop_duplicates()
df["TotalAmount"]=df["Price"]*df["Quantity"]*(1-df["Discount"])
df["NetProfit"] = df["TotalAmount"] - df["ShippingCost"]
print(df.head())
print(df.groupby("Category")["TotalAmount"].sum())
result = df.query('NetProfit < 0').groupby('Region')['NetProfit'].sum()
print(result)
print(df.groupby("CustomerID")["TotalAmount"].sum().sort_values(ascending=False).head())