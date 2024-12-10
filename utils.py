import pandas as pd


def get_top_brands(
    df, n: int, brand_col: str = "brand", sales_col: str = "total_sales"
):
    return df.groupby("brand")["total_sales"].sum().sort_values(ascending=False).head(n)


def slice_last_mo(df, months: int):
    last_date = df["date"].max()
    months_ago = last_date - pd.DateOffset(months=months)
    return df[df["date"] > months_ago]

def get_top_regions(df, nregions, brandcol, regioncol, salescol, particular_brand=None):
    if particular_brand:
        df = df[df[brandcol] == particular_brand]
    return df.groupby([brandcol, regioncol])[salescol].sum().nlargest(nregions)

def get_regions(df, brandcol, regioncol, salescol, particular_brand=None):
    if particular_brand:
        df = df[df[brandcol] == particular_brand]
    return df.groupby([brandcol, regioncol])[salescol].sum()