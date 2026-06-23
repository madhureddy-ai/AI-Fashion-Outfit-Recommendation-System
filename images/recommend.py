import pandas as pd

products_df = pd.read_csv("products.csv")
outfits_df = pd.read_csv("outfits.csv")

gender = "men"
occasion = "office"

result = outfits_df[
    (outfits_df["gender"] == gender) &
    (outfits_df["occasion"] == occasion)
]

if len(result) > 0:
    outfit = result.iloc[0]

    print("\nRecommended Outfit")
    print("------------------")
    print("Topwear :", outfit["hero"])
    print("Bottomwear :", outfit["second"])
    print("Footwear :", outfit["footwear"])
    print("Accessory :", outfit["accessory_1"])
    print("\nReason :")
    print(outfit["stylist_rationale"])

else:
    print("No matching outfit found.")