import random
import tkinter as tk

# Define the knowledge base with more food items and nutritional information
knowledge_base = {
    "protein": {
        "chicken breast": 31,
        "salmon": 22,
        "tofu": 8,
        "lentils": 9,
        "black beans": 7,
        "beef": 26,
        "turkey": 29,
    },
    "carbohydrates": {
        "brown rice": 45,
        "quinoa": 39,
        "sweet potato": 27,
        "whole wheat bread": 18,
        "oats": 17,
        "pasta": 25,
        "potato": 17,
    },
    "fats": {
        "avocado": 15,
        "almonds": 14,
        "peanut butter": 8,
        "olive oil": 0,
        "chia seeds": 5,
        "butter": 7,
        "coconut oil": 13,
    },
    "vitamins and minerals": {
        "spinach": 145,
        "kale": 200,
        "broccoli": 81,
        "bell pepper": 95,
        "carrot": 41,
        "tomato": 18,
        "asparagus": 20,
    }
}

# Define the suggest_diet function


def suggest_diet(weight, height, age, gender, activity_level):
    # Calculate the basal metabolic rate
    if gender.lower() == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    # Calculate the total daily calorie needs based on activity level
    total_calorie_need = calculate_total_calorie_need(bmr, activity_level)

    return total_calorie_need

# Define the calculate_total_calorie_need function


def calculate_total_calorie_need(bmr, activity_level):
    activity_factors = {
        "Little/no exercise": 1.2,
        "Light exercise": 1.375,
        "Moderate exercise (3-5 days/wk)": 1.55,
        "Very active (6-7 days/wk)": 1.725,
        "Extra active (very active & physical job)": 1.9,
    }
    if activity_level in activity_factors:
        return bmr * activity_factors[activity_level]
    else:
        print("Invalid activity level. Using Little/no exercise as default.")
        return bmr * 1.2

# Define the suggest_meal_plan function


def suggest_meal_plan(total_calorie_need, num_courses):
    meal_plan = []

    # Generate the meal plan based on the user's input for the number of courses
    for course_num in range(1, num_courses + 1):
        course = {}
        for nutrient in knowledge_base.keys():
            food_options = knowledge_base[nutrient]
            random_food = random.choice(list(food_options.keys()))
            # Random serving size between 1 and 4
            serving_size = random.randint(1, 4)
            course[nutrient] = {"food": random_food,
                                "serving_size": serving_size}
        meal_plan.append(course)

    return meal_plan

# Create a function to calculate and display the meal plan when the "Calculate" button is pressed


def calculate_meal_plan():
    weight = int(weight_entry.get())
    height = int(height_entry.get())
    age = int(age_entry.get())
    gender = gender_entry.get()
    activity_level = activity_levels.get(
        activity_var.get(), "Little/no exercise")

    total_calorie_need = suggest_diet(
        weight, height, age, gender, activity_level)
    num_courses = int(num_courses_entry.get())

    meal_plan = suggest_meal_plan(total_calorie_need, num_courses)

    # Clear any previous results
    result_text.delete(1.0, tk.END)

    # Display the meal plan with the suggestions
    result_text.insert(tk.END, "Suggested Meal Plan:\n")
    for meal_num, course in enumerate(meal_plan):
        result_text.insert(tk.END, f"Course {meal_num + 1}:\n")
        for nutrient, details in course.items():
            food = details["food"]
            serving_size = details["serving_size"]
            calories = serving_size * knowledge_base[nutrient][food]
            result_text.insert(
                tk.END, f"{nutrient.capitalize()}: {food} ({serving_size} serving(s), {calories:.2f} kcal)\n")


# Create the Tkinter window
window = tk.Tk()
window.title("Meal Planner")

# Create label and entry widgets for user information
weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

height_label = tk.Label(window, text="Height (cm):")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

age_label = tk.Label(window, text="Age (years):")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

gender_label = tk.Label(window, text="Gender (Male/Female):")
gender_label.pack()
gender_entry = tk.Entry(window)
gender_entry.pack()

# Activity level
activity_label = tk.Label(window, text="Select your activity level:")
activity_label.pack()

activity_var = tk.StringVar()
activity_var.set("1")  # Default to "Little/no exercise"

activity_levels = {
    "1": "Little/no exercise",
    "2": "Light exercise",
    "3": "Moderate exercise (3-5 days/wk)",
    "4": "Very active (6-7 days/wk)",
    "5": "Extra active (very active & physical job)",
}

for key, value in activity_levels.items():
    radio_button = tk.Radiobutton(
        window, text=value, variable=activity_var, value=key)
    radio_button.pack()

# Number of courses
num_courses_label = tk.Label(window, text="Number of Courses:")
num_courses_label.pack()
num_courses_entry = tk.Entry(window)
num_courses_entry.pack()

# Create a label for the suggested meal plan
meal_plan_label = tk.Label(window, text="Suggested Meal Plan:")
meal_plan_label.pack()

# Create a text widget to display the meal plan
result_text = tk.Text(window, height=10, width=40, wrap=tk.WORD)
result_text.pack()

# Calculate button
calculate_button = tk.Button(
    window, text="Calculate", command=calculate_meal_plan)
calculate_button.pack()

# Run the Tkinter main loop
window.mainloop()
