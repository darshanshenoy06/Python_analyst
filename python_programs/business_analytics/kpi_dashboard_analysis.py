try:
    number_of_months = int(input("Enter the number of months: "))
    monthly_revenue = {}
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    def analyze_kpi(data):
            total_revenue = sum(data.values())
            average_revenue = total_revenue / len(data)
            best_performing_month = max(data, key=data.get)
            worst_performing_month = min(data, key=data.get)
            return total_revenue, average_revenue, best_performing_month, worst_performing_month
    
    for i in range(number_of_months):
        month = months[i%12]    
        revenue = float(input(f"Enter the revenue for {months[i%12]}: "))
        monthly_revenue[month] = revenue
        
        
    total_revenue, average_revenue, best_performing_month, worst_performing_month = analyze_kpi(monthly_revenue)
    print("\nKPI Dashboard Analysis:")
    print(f"Total revenue: {total_revenue}")
    print(f"Average revenue: {average_revenue}")
    print(f"Best-performing month: {best_performing_month}")
    print(f"Worst-performing month: {worst_performing_month}")
except ValueError:
    print("Invalid input! Please enter numeric values only.")
except Exception as e:
    print(f"An error occurred: {e}")    