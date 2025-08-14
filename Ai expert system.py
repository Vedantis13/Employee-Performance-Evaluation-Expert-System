# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define the rules for performance evaluation
rules = {
    'work_quality': {
        'Excellent': 'work_quality >= 90',
        'Good': 'work_quality >= 80 and work_quality < 90',
        'Needs improvement': 'work_quality < 80'
    },
    'attendance': {
        'Excellent': 'attendance >= 95',
        'Good': 'attendance >= 90 and attendance < 95',
        'Needs improvement': 'attendance < 90'
    },
    'teamwork': {
        'Excellent': 'teamwork >= 90',
        'Good': 'teamwork >= 80 and teamwork < 90',
        'Needs improvement': 'teamwork < 80'
    },
    'initiative': {
        'Excellent': 'initiative >= 90',
        'Good': 'initiative >= 80 and initiative < 90',
        'Needs improvement': 'initiative < 80'
    },
    'punctuality': {
        'Excellent': 'punctuality >= 95',
        'Good': 'punctuality >= 90 and punctuality < 95',
        'Needs improvement': 'punctuality < 90'
    },
    'problem_solving': {
        'Excellent': 'problem_solving >= 90',
        'Good': 'problem_solving >= 80 and problem_solving < 90',
        'Needs improvement': 'problem_solving < 80'
    },
    'leadership': {
        'Excellent': 'leadership >= 90',
        'Good': 'leadership >= 80 and leadership < 90',
        'Needs improvement': 'leadership < 80'
    },
    'innovation': {
        'Excellent': 'innovation >= 90',
        'Good': 'innovation >= 80 and innovation < 90',
        'Needs improvement': 'innovation < 80'
    }
}

# Define the function to evaluate performance
def evaluate_performance(answers):
    category_scores = {}
    
    for key, value in answers.items():
        for grade, rule in rules[key].items():
            if eval(rule.replace(key, str(value))):
                category_scores[key] = grade
                break
    return category_scores

# Define the questions to ask
questions = {
    'work_quality': 'What is the employee\'s work quality (0-100)? ',
    'attendance': 'What is the employee\'s attendance rate (0-100)? ',
    'teamwork': 'How would you rate the employee\'s teamwork (0-100)? ',
    'initiative': 'How would you rate the employee\'s initiative (0-100)? ',
    'punctuality': 'How would you rate the employee\'s punctuality (0-100)? ',
    'problem_solving': 'How would you rate the employee\'s problem-solving skills (0-100)? ',
    'leadership': 'How would you rate the employee\'s leadership skills (0-100)? ',
    'innovation': 'How would you rate the employee\'s innovation (0-100)? '
}

# Function to evaluate multiple employees
def evaluate_employees(num_employees):
    employee_data = {}
    
    for i in range(num_employees):
        print(f"\n--- Evaluating Employee {i + 1} ---")
        employee_name = input("Enter employee name: ")
        answers = {}
        for key, question in questions.items():
            while True:
                try:
                    answer = int(input(question))
                    if 0 <= answer <= 100:
                        answers[key] = answer
                        break
                    else:
                        print("Please enter a value between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 100.")

        category_scores = evaluate_performance(answers)
        employee_data[employee_name] = category_scores

    return employee_data

# Function to generate a performance report
def generate_report(employee_data):
    print("\n--- Performance Report ---")
    for employee, scores in employee_data.items():
        print(f"\nEmployee: {employee}")
        print("Category Scores:")
        for category, score in scores.items():
            print(f"  {category}: {score}")
    print("\n")

# function to visualize performance 
def plot_performance(data, title, is_individual=True):
    categories = list(questions.keys())
    scores = []
    
    for category in categories:
        if is_individual:
            # For individual employee performance
            score = data[category]
            if score == 'Excellent':
                scores.append(100)
            elif score == 'Good':
                scores.append(75)
            else:
                scores.append(50)
        else:
            # For overall employee performance
            if category in data:
                scores.append(data[category])
            else:
                scores.append(0)  
    
    # Plotting
    plt.figure(figsize=(12, 6))
    bars = plt.bar(categories, scores, color=['green' if s >= 90 else 'orange' if s >= 75 else 'red' for s in scores])
    plt.xlabel('Performance Categories', fontsize=14)
    plt.ylabel('Scores', fontsize=14)
    plt.title(title, fontsize=16)
    plt.xticks(rotation=45, ha='right')
    plt.ylim(0, 100)

   
    for bar in bars:
        height = bar.get_height()
        if height >= 90:
            label = 'Excellent'
        elif height >= 75:
            label = 'Good'
        else:
            label = 'Needs\nimprovement'
        
        plt.text(bar.get_x() + bar.get_width()/2, height/2,
                 label,
                 ha='center', va='center',
                 fontsize=10 if label != 'Needs\nimprovement' else 8,
                 color='white',
                 fontweight='bold')

    plt.axhline(y=75, color='red', linestyle='--', label='Threshold (75)')
    plt.legend()
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def plot_individual_performance(employee_name, employee_data):
    plot_performance(employee_data[employee_name], f'Performance of {employee_name}', is_individual=True)


def plot_all_employees_performance(employee_data):
    categories = list(questions.keys())
    average_scores = {category: 0 for category in categories}
    num_employees = len(employee_data)

    # Calculate average score for each category
    for scores in employee_data.values():
        for category in categories:
            if category in scores:
                if scores[category] == 'Excellent':
                    average_scores[category] += 100
                elif scores[category] == 'Good':
                    average_scores[category] += 75
                else:
                    average_scores[category] += 50

    # Calculate the average scores
    average_scores = {category: score / num_employees for category, score in average_scores.items()}
    
    # Plotting the average scores
    plot_performance(average_scores, 'Average Employee Performance in Various Categories', is_individual=False)


def main():
    num_employees = int(input("Enter the number of employees to evaluate: "))
    employee_data = evaluate_employees(num_employees)
    

    generate_report(employee_data)
    
    while True:
        
        print("\nSelect an option:")
        print("1. Individual employee performance graph")
        print("2. All employees' performance graph (average scores)")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice (1, 2, or 3): "))
            
            if choice == 1:
                employee_name = input("Enter the employee name for individual performance graph: ")
                if employee_name in employee_data:
                    plot_individual_performance(employee_name, employee_data)
                else:
                    print("Employee not found.")
            elif choice == 2:
                plot_all_employees_performance(employee_data)
            elif choice == 3:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

if __name__ == "__main__":
    main()