import pandas as pd


# ============================================================
# 0. Display configuration
# ============================================================
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# ============================================================
# 1. Load data & basic inspection
# ============================================================
az_sales = pd.read_csv(
    "C:\\Users\\Admin\\Searches\\Downloads\\amazon_sales_data 2025.csv",
    index_col="Order ID"
)

print(az_sales.head())
print(az_sales.info())
print(az_sales.shape)
print(az_sales.describe())
print(az_sales.columns)

# ============================================================
#  Indexing, slicing & selection
# ============================================================
print(az_sales['Price'])
print(az_sales.iloc[1])
print(az_sales.iloc[:5, 2:5])
print(az_sales.loc['ORD0002':'ORD0010',
      ['Customer Location','Product','Price','Customer Name']])

print(az_sales.loc[
    (az_sales.Category == 'Electronics') | (az_sales.Price > 150)
])

print(az_sales.loc[
    (az_sales.Product.isin(['Laptop','Headphones'])) &
    (az_sales.Status.isin(['Completed']))
])




# ============================================================
# Missing values & type operations
# ============================================================


print(az_sales.loc[az_sales.Price.notnull()])
print(az_sales[pd.isnull(az_sales['Customer Location'])])
print(az_sales.isna().any().any())

print(
    az_sales.Price.astype(str) +
    ' USD - ' +
    az_sales['Product'] +
    ' -- ' +
    az_sales['Customer Name']
)

# ============================================================
# Renaming & index manipulation
# ============================================================

print(
    az_sales
    .rename(columns={
        'Customer Location':'Location',
        'Order Date':'Date'
    })
    .rename_axis('Order No.')
)


# ============================================================
#  Order status filtering & core KPIs
# ============================================================

n_c = az_sales[az_sales['Status'] != 'Cancelled']
n_p_c = n_c[n_c['Status'] != 'Pending']

o_canc = az_sales[az_sales['Status'] == 'Cancelled']
o_p_c = az_sales[az_sales['Status'] == 'Pending']
o_completed = az_sales[az_sales['Status'] == 'Completed']

t_s = az_sales['Total Sales'].sum()
t_o = n_c.index.nunique()
avg_o_v = t_s / t_o

print(f"Total Sales: {t_s}")
print(f"Total Orders: {t_o}")
print(f"Average Order Value: {avg_o_v}")

# ============================================================
# GroupBy fundamentals
# ============================================================

print(
    az_sales
    .groupby(['Category', 'Product', 'Price'])
    .apply(lambda x: x['Customer Name'].iloc[:3])
)

print(
    az_sales
    .groupby('Category')
    .Price
    .agg([len, max, min])
)


# ============================================================
#  Customer-level analysis
# ============================================================
customer_sales = (
    az_sales
    .groupby('Customer Name')['Total Sales']
    .sum()
    .sort_values(ascending=False)
)

completed_orders = az_sales[az_sales['Status'] == 'Completed']
orders_per_customer = completed_orders.groupby('Customer Name').size()
print(customer_sales)
print(orders_per_customer)

# ============================================================
#  Product & category analysis
# ============================================================
rev_by_category = (
    az_sales
    .groupby('Category')['Total Sales']
    .sum()
)

revenue_vs_volume = (
    az_sales
    .groupby('Category')
    .agg(
        total_revenue=('Total Sales', 'sum'),
        total_units=('Quantity', 'sum'),
        avg_price=('Price', 'mean')
    )
    .sort_values('total_revenue', ascending=False)
)

top_products = (
    az_sales
    .groupby('Product')
    .agg(total_revenue=('Total Sales', 'sum'))
    .sort_values('total_revenue', ascending=False)
)

bottom_products = (
    az_sales
    .groupby('Product')
    .agg(total_revenue=('Total Sales', 'sum'))
    .sort_values('total_revenue', ascending=True)
)

print(rev_by_category)
print(revenue_vs_volume)
print(top_products)
print(bottom_products)


# ============================================================
#  Product performance & dead-weight detection
# ============================================================
product_stats = (
    az_sales
    .groupby('Product')
    .agg(
        total_units=('Quantity', 'sum'),
        total_revenue=('Total Sales', 'sum'),
        avg_price=('Price', 'mean')
    )
)

low_volume_threshold = product_stats['total_units'].quantile(0.25)
low_revenue_threshold = product_stats['total_revenue'].quantile(0.25)

dead_weight_products = product_stats[
    (product_stats['total_units'] <= low_volume_threshold) &
    (product_stats['total_revenue'] <= low_revenue_threshold)
]

print(product_stats)
print(dead_weight_products)

# ============================================================
#  Location & payment analysis
# ============================================================
rev_by_payment_method = (
    az_sales
    .groupby('Payment Method')
    .agg(total_revenue=('Total Sales', 'sum'))
    .sort_values('total_revenue', ascending=False)
)

rev_by_location = (
    az_sales
    .groupby('Customer Location')
    .agg(total_revenue=('Total Sales', 'sum'))
    .sort_values('total_revenue', ascending=False)
)

location_product_sales = (
    az_sales
    .groupby(['Customer Location', 'Product'])
    .agg(
        total_revenue=('Total Sales', 'sum'),
        total_units=('Quantity', 'sum')
    )
)

print(rev_by_payment_method)
print(rev_by_location)
print(location_product_sales)

# ============================================================
#  Location segmentation using quantiles
# ============================================================
location_stats = (
    az_sales
    .groupby('Customer Location')
    .agg(
        total_revenue=('Total Sales', 'sum'),
        total_units=('Quantity', 'sum')
    )
)

rev_25 = location_stats['total_revenue'].quantile(0.25)
rev_75 = location_stats['total_revenue'].quantile(0.75)
vol_25 = location_stats['total_units'].quantile(0.25)
vol_75 = location_stats['total_units'].quantile(0.75)

core_markets = location_stats[
    (location_stats['total_revenue'] >= rev_75) &
    (location_stats['total_units'] >= vol_75)
]

premium_markets = location_stats[
    (location_stats['total_revenue'] >= rev_75) &
    (location_stats['total_units'] >= vol_25) &
    (location_stats['total_units'] < vol_75)
]

dormant_markets = location_stats[
    (location_stats['total_revenue'] <= rev_25) &
    (location_stats['total_units'] <= vol_25)
]
print(location_stats)
print(core_markets)
print(premium_markets)
print(dormant_markets)
