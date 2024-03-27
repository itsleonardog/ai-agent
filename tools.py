import db
from datetime import datetime

def get_next_coffee(coffee_count: int):
    """
    Call this tool when user wants you to eat another coffee.

    Args:
        coffee_count (int): Value with same name from metadata.

    Returns:
        str: The coffee you should eat next.
    """
    print("== eat_next_coffee ==> tool called")

    if coffee_count == 2:
        return "You have already had coffee twice today. You eat cherry pie now."
    if coffee_count == 1:
        db.coffee_count += 1
        return "You have only had one coffee today. You have second coffee now."

def tell_the_date():
    """
    Call this tool when the user wants to know the date.

    Returns:
        str: The current date
    """
    print("== tell_the_date ==> tool called")
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"The date is {current_date}"
