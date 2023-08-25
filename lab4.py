print("Anshika sharma -E22CSEU1438")

# Sample data representing the Flight Table
data = [
    {'P_ID': 'P1', 'Process': 'VSCode', 'Start Time (ms)': 100, 'Priority': 'MID'},
    {'P_ID': 'P23', 'Process': 'Eclipse', 'Start Time (ms)': 234, 'Priority': 'MID'},
    {'P_ID': 'P93', 'Process': 'Chrome', 'Start Time (ms)': 189, 'Priority': 'High'},
    {'P_ID': 'P42', 'Process': 'JDK', 'Start Time (ms)': 9, 'Priority': 'High'},
    {'P_ID': 'P9', 'Process': 'CMD', 'Start Time (ms)': 7, 'Priority': 'High'},
    {'P_ID': 'P87', 'Process': 'NotePad', 'Start Time (ms)': 23, 'Priority': 'Low'},
    # Add more data entries as needed
]

def sort_data(data, key):
    if key == 1:
        return sorted(data, key=lambda x: x['P_ID'])
    elif key == 2:
        return sorted(data, key=lambda x: x['Start Time (ms)'])
    elif key == 3:
        return sorted(data, key=lambda x: x['Priority'])
    else:
        raise ValueError("Invalid sorting parameter")

def print_data(data):
    print("{:<5} {:<10} {:<20} {:<10}".format("P_ID", "Process", "Start Time (ms)", "Priority"))
    print("="*50)
    for entry in data:
        print("{:<5} {:<10} {:<20} {:<10}".format(entry['P_ID'], entry['Process'], entry['Start Time (ms)'], entry['Priority']))

def main():
    print("Choose a sorting parameter:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")
    
    sorting_key = int(input("Enter your choice: "))
    
    sorted_data = sort_data(data, sorting_key)
    
    print("\nSorted Flight Table:")
    print_data(sorted_data)

if __name__ == "__main__":
    main()
