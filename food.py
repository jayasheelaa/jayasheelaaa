def suggest_food(time_of_day):
    if time_of_day.lower() == "breakfast":
        return "How about some pancakes and scrambled eggs?"
    elif time_of_day.lower() == "lunch":
        return "A sandwich and salad would be a great lunch!"
    elif time_of_day.lower() == "dinner":
        return "For dinner, you could have pasta or grilled chicken."
    else:
        return "Sorry, I can only suggest food for breakfast, lunch, or dinner."

 
time_of_day = input("What time of day is it (breakfast, lunch, dinner)? ")

 
food_suggestion = suggest_food(time_of_day)

 
print(food_suggestion)