def linear_search(student_ids, target_id):

    for i in range(len(student_ids)):
        if student_ids[i] == target_id:
            return i + 1  # Return 1-indexed position
    return -1

def binary_search(scores, target_score):

    left, right = 0, len(scores) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if scores[mid] == target_score:
            return mid + 1  # Return 1-indexed position
        elif scores[mid] < target_score:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def display_menu():
    """Display the main menu options"""
    print("\n" + "="*40) # Adds spacing and a separator line
    print("SEARCHING ALGORITHMS IMPLEMENTATION")
    print("="*40)
    print("1. Linear Search - Find a Student ID")
    print("2. Binary Search - Find a Score")
    print("3. Exit")
    print("="*40)  # Another line below the title

def get_student_ids():
    """Return a hardcoded list of 20 student IDs (unsorted)"""
    return [1001, 1005, 1002, 1008, 1003, 1010, 1004, 1009, 1006, 1007,
            1011, 1015, 1012, 1018, 1013, 1020, 1014, 1019, 1016, 1017]

def get_scores():
    """Return a hardcoded sorted list of 20 test scores"""
    return [65, 68, 72, 75, 78, 80, 82, 85, 86, 88,
            90, 92, 93, 95, 96, 98, 99, 100, 100, 100]

def main():
    """Main program function"""
    # Initialize data
    student_ids = get_student_ids()
    scores = get_scores()
    
    print("Welcome to the Searching Algorithms Program!")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '3':
                print("Thank you for using the program. Goodbye!")
                break
            
            if choice == '1':
                # Linear Search for Student ID
                print(f"\nAvailable Student IDs: {student_ids}")
                try:
                    target_id = int(input("Enter the Student ID to search for: "))
                except ValueError:
                    print("Error: Please enter a valid numeric Student ID.")
                    continue
                
                position = linear_search(student_ids, target_id)
                
                print("\n" + "-"*30) # New line + 30 dashes
                print("LINEAR SEARCH RESULTS")
                print("-"*30)
                if position != -1:
                    print(f"Student ID {target_id} found at position {position}")
                else:
                    print(f"Student ID {target_id} not found")
                print("-"*30)  # Another line below the title
                
            elif choice == '2':
                # Binary Search for Score
                print(f"\nAvailable Scores (sorted): {scores}")
                try:
                    target_score = int(input("Enter the Score to search for: "))
                except ValueError:
                    print("Error: Please enter a valid numeric Score.")
                    continue
                
                position = binary_search(scores, target_score)
                
                print("\n" + "-"*30)
                print("BINARY SEARCH RESULTS")
                print("-"*30)
                if position != -1:
                    print(f"Score {target_score} found at position {position}")
                else:
                    print(f"Score {target_score} not found")
                print("-"*30)
                
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
                continue
            
            # Ask if user wants to continue
            while True:
                continue_choice = input("\nDo you want to perform another search? (y/n): ").strip().lower()
                if continue_choice in ['y', 'yes']:
                    break
                elif continue_choice in ['n', 'no']:
                    print("Thank you for using the program. Goodbye!")
                    return
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
                    
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    # Run the main program
    main()