try:
    log_entries = int(input("Enter number of log entries: "))

    if log_entries <= 0:
        print("No log entries to analyze.")
    else:
        log_data = {}

        for i in range(log_entries):
            entry = input(f"Enter log entry {i + 1}: ").strip()
            log_data[entry] = log_data.get(entry, 0) + 1

        unique_errors = len(log_data)
        most_frequent_error = max(log_data, key=log_data.get)
        least_frequent_error = min(log_data, key=log_data.get)

        print(f"\nUnique Errors: {unique_errors}")
        print(f"Most Frequent Error: {most_frequent_error}")
        print(f"Least Frequent Error: {least_frequent_error}")
        print("Error Frequency:", log_data)

except ValueError:
    print("Invalid input! Please enter a valid number.")
