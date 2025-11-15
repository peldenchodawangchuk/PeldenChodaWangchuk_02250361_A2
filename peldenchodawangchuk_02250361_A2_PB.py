def bubble_sort_student_names():
    # Hardcoded list of 15 student names
    students = ["Kado", "Bobchu", "Zamu", "Nado", "Lemo", "Alice", "Charlie", 
                "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack", "Karen"]

    print("\n" + "="*50)
    print("BUBBLE SORT - STUDENT NAMES")
    print("="*50)
    print("Original list:", students)
    
    # Make a copy to preserve original
    sorted_students = students.copy()
    n = len(sorted_students)
    
    # Bubble Sort algorithm
    for i in range(n):
        # Flag to optimize - if no swaps in a pass, list is sorted
        swapped = False
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if sorted_students[j] > sorted_students[j+1]:
                # Swap if they are in wrong order
                sorted_students[j], sorted_students[j+1] = sorted_students[j+1], sorted_students[j]
                swapped = True
        
        # If no swapping occurred, list is sorted
        if not swapped:
            break
    
    print("Sorted list (alphabetically):", sorted_students)
    return sorted_students


def insertion_sort_test_scores():

    # Hardcoded list of 20 test scores
    scores = [85, 92, 78, 65, 95, 88, 72, 60, 98, 82, 
              75, 90, 68, 87, 79, 93, 55, 84, 71, 89]
    
    print("\n" + "="*50)
    print("INSERTION SORT - TEST SCORES")
    print("="*50)
    print("Original list:", scores)
    
    # Make a copy to preserve original
    sorted_scores = scores.copy()
    
    # Insertion Sort algorithm
    for i in range(1, len(sorted_scores)):
        key = sorted_scores[i]  # Current element to be positioned
        j = i - 1
        
        # Move elements that are greater than key one position ahead
        while j >= 0 and key < sorted_scores[j]:
            sorted_scores[j + 1] = sorted_scores[j]
            j -= 1
        
        # Place key in its correct position
        sorted_scores[j + 1] = key
    
    print("Sorted list (ascending order):", sorted_scores)
    print("\nTop 5 Scores:")
    for i, score in enumerate(sorted_scores[-5:][::-1], 1):
        print(f"{i}. {score}")
    
    return sorted_scores

def quick_sort_book_price():
    # Hardcoded list of 15 book prices
    book_prices = [24.99, 15.50, 32.75, 12.99, 45.00, 29.95, 18.25, 
                   39.99, 22.50, 14.75, 35.25, 27.99, 19.95, 42.50, 16.99]
    
    print("\n" + "="*50)
    print("QUICK SORT - BOOK PRICES")
    print("="*50)
    print("Original list:", book_prices)
    
    # Counter to track recursive calls
    recursive_calls = [0]
    
    def quick_sort_helper(arr):
        """Helper function for Quick Sort implementation with call tracking"""
        recursive_calls[0] += 1
        
        if len(arr) <= 1:
            return arr
        
        # Choose middle element as pivot
        pivot = arr[len(arr) // 2]
        
        # Partition the array
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        # Recursively sort left and right partitions
        return quick_sort_helper(left) + middle + quick_sort_helper(right)
    
    sorted_prices = quick_sort_helper(book_prices.copy())
    
    print("Sorted list (ascending order):", sorted_prices)
    print(f"Number of recursive calls made: {recursive_calls[0]}")
    
    return sorted_prices, recursive_calls[0]

def display_menu():
    """Display the main menu options"""
    print("\n" + "="*60)
    print("SORTING ALGORITHMS IMPLEMENTATION")
    print("="*60)
    print("1. Bubble Sort - Sort Student Names (Alphabetically)")
    print("2. Insertion Sort - Sort Test Scores (Ascending) + Top 5")
    print("3. Quick Sort - Sort Book Prices")
    print("4. Exit")
    print("="*60)


def main():
    """Main program function"""
    print("Welcome to the Sorting Algorithms Program!")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == '1':
                bubble_sort_student_names()
            elif choice == '2':
                insertion_sort_test_scores()
            elif choice == '3':
                quick_sort_book_price()
            elif choice == '4':
                print("\nThank you for using the Sorting Algorithms Program! Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1-5.")
                continue
            
            # Ask if user wants to continue
            while True:
                continue_choice = input("\nWould you like to perform another sort? (y/n): ").strip().lower()
                if continue_choice in ['y', 'yes']:
                    break
                elif continue_choice in ['n', 'no']:
                    print("\nThank you for using the Sorting Algorithms Program! Goodbye!")
                    return
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
                    
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()