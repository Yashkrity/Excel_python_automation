import pandas as pd

def clean_sales_data(file_path):
    # reads csv
    if file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        df = pd.read_csv(file_path)

    # remove nulls and dups
    df = df.dropna(how='all').drop_duplicates()

    # standardizing text columns
    text_cols = ['Ship Mode', 'Customer ID', 'Customer Name', 'Segment', 
                 'Country', 'City', 'State', 'Region', 'Category', 
                 'Sub-Category', 'Product Name', 'Product ID', 'Order ID']
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    # date column standards
    for date_col in ['Order Date', 'Ship Date']:
        if date_col in df.columns:
            df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

    # handling numerical cols
    for num_col in ['Sales', 'Quantity', 'Discount', 'Profit', 'Postal Code']:
        if num_col in df.columns:
            df[num_col] = pd.to_numeric(df[num_col], errors='coerce').fillna(0)

    return df
