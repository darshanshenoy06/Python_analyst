try:
    sales_record = int(input("How many Sales records to enter: "))  
    sales_data = {}
    for i in range(sales_record):
        product_name = input(f"Enter the product name for record {i + 1}: ")
        sales_amount = float(input(f"Enter the sales amount for record {i + 1}: "))
        
        if product_name in sales_data:
            sales_data[product_name] += sales_amount
        else:
            sales_data[product_name] = sales_amount


    total_revenue = sum(sales_data.values())
    best_selling_product = max(sales_data, key=sales_data.get)
    worst_selling_product = min(sales_data, key=sales_data.get)
    average_sales_per_product= total_revenue / len(sales_data)

    print(f"Total revenue: {total_revenue}")
    print(f"Best-selling product: {best_selling_product}")
    print(f"Worst-selling product: {worst_selling_product}")
    print(f"Average sales per product: {average_sales_per_product}")
except ValueError: 
    print("Invalid input! Please enter numeric values only.")
except Exception as e:
    print(f"An error occurred: {e}")