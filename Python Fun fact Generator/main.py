import json
import requests
from pywebio.output import *
from pywebio.session import *


def get_fun_fact(_):
    # Clear the screen
    clear()

    put_html("""
        <p align="left"><h2>
        <img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%">
        Fun Fact Generator</h2></p>
    """)

    # URL from where we will fetch the data
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    # Use GET request
    response = requests.get(url)

    # Load the request in json format
    data = json.loads(response.text)

    # Extract the fact from the json data
    useless_fact = data['text']

    # Display the fact in blue color
    style(put_text(useless_fact), 'color:blue; font-size: 30px')

    # Put the click me button
    put_buttons(
        [{'label': 'Click me', 'value': 'outline-success', 'color': 'outline-success'}],
        onclick=get_fun_fact
    )


# Driver Function
if __name__ == '__main__':
    # Put a heading "Fun Fact Generator"
    put_html("""
        <p align="left"><h2>
        <img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%">
        Fun Fact Generator</h2></p>
    """)

    # Hold the session for long time
    # Put a Click me button
    put_buttons(
        [{'label': 'Click me', 'value': 'outline-success', 'color': 'outline-success'}],
        onclick=get_fun_fact
    )

    hold()
