import pandas as pd

# Load datasets
products_df = pd.read_csv("products.csv")
outfits_df = pd.read_csv("outfits.csv")

# Basic info
print("Products shape:", products_df.shape)
print("Outfits shape:", outfits_df.shape)

print("\nProducts columns:")
print(products_df.columns)

print("\nOutfits columns:")
print(outfits_df.columns)

print("\nFirst 5 products:")
print(products_df.head())

print("\nFirst 5 outfits:")
print(outfits_df.head())