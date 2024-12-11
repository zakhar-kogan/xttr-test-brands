import pandas as pd


def get_top_brands(
    df, n: int, brand_col: str = "brand", sales_col: str = "total_sales"
):
    """Get top N brands by total sales from a DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame containing brand and sales data
    n : int
        Number of top brands to return
    brand_col : str, default="brand"
        Name of the column containing brand information
    sales_col : str, default="total_sales"
        Name of the column containing sales values

    Returns
    -------
    pandas.Series
        A series containing top N brands with their total sales,
        indexed by brand names and sorted in descending order

    Examples
    --------
    >>> df = pd.DataFrame({
    ...     'brand': ['A', 'B', 'A', 'C'],
    ...     'total_sales': [100, 200, 150, 300]
    ... })
    >>> get_top_brands(df, n=2)
    brand
    C    300
    A    250
    """
    return df.groupby("brand")["total_sales"].sum().sort_values(ascending=False).head(n)


def slice_last_mo(df, months: int):
    """Slices a DataFrame to include only records from the last specified number of months.

    Parameters:
    ----------
        df (pandas.DataFrame): Input DataFrame containing a 'date' column
        months (int): Number of months to look back from the most recent date

    Returns:
    -------
        pandas.DataFrame: 
        Filtered DataFrame containing only records from the specified recent months

    Example:
    --------
        >>> df = pd.DataFrame({'date': ['2023-01-01', '2023-06-01', '2023-12-01']})
        >>> slice_last_mo(df, 6)
        Will return records after 2023-06-01 if called on 2023-12-01
    """

    last_date = df["date"].max()
    months_ago = last_date - pd.DateOffset(months=months)
    return df[df["date"] > months_ago]


def get_top_regions(df, nregions, brandcol, regioncol, salescol, particular_brand=None):
    """Get top N regions by sales for all brands or a specific brand.

    This function groups sales data by brand and region, then returns the top N regions
    based on total sales value.

    Parameters:
    ----------
        df (pandas.DataFrame): Input DataFrame containing sales data
        nregions (int): Number of top regions to return
        brandcol (str): Name of the column containing brand information
        regioncol (str): Name of the column containing region information
        salescol (str): Name of the column containing sales values
        particular_brand (str, optional): If specified, filter results for this brand only. Defaults to None.

    Returns:
    -------
        pandas.Series: Series containing top N regions with their sales values,
                      indexed by brand and region
    """
    if particular_brand:
        df = df[df[brandcol] == particular_brand]
    return df.groupby([brandcol, regioncol])[salescol].sum().nlargest(nregions)


def get_regions(df, brandcol, regioncol, salescol, particular_brand=None):
    """Get sales aggregated by brand and region from a DataFrame.
    
    Parameters:
    ----------
    df : pandas.DataFrame
        Input DataFrame containing brand, region and sales data.
    brandcol : str
        Name of the column containing brand information.
    regioncol : str
        Name of the column containing region information.
    salescol : str
        Name of the column containing sales values.
    particular_brand : str, optional
        If specified, filters data for this brand only. Default is None.
    
    Returns:
    -------
    pandas.Series
        A Series with multi-index (brand, region) containing aggregated sales values.
    """

    if particular_brand:
        df = df[df[brandcol] == particular_brand]
    return df.groupby([brandcol, regioncol])[salescol].sum()
