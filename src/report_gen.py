def calculate_kpis(df):
    total_sales = df['Sales'].sum()
    num_orders = df['Order ID'].nunique()
    avg_order_value = total_sales / num_orders if num_orders else 0

    kpis = {
        "Total Sales": round(total_sales, 2),
        "Number of Orders": num_orders,
        "Average Order Value": round(avg_order_value, 2)
    }
    return kpis
