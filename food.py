import random
def get_food_reccommendation(meal_type):
    if meal_type.lower()=='breakfast':
        return random.choice(['Omlette','Pancakes','Avocado toast'])
    elif meal_type.lower()=='lunch':
        return random.choice(['Chicken caesar salad','Vegetarian wrap','Sushi bowl'])
    elif meal_type.lower()=='dinner':
        return random.choice(['Grilled salmon','Pasta carbonara','Stir-fry Tofu'])
    else:
        return "Sorry I can only recommend meals for breakfast,lunch or dinner."
user_input=input("enter the meal type(breakfast,lunch or dinner):")
recommendation=get_food_reccommendation(user_input)
print(f"Recommended food for {user_input}:{recommendation}")    