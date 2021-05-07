# Main file for Rookie

# Import statement
from flask import (
    Flask,
    render_template,
    Markup,
    url_for,
    flash,
    redirect,
    request
)
'''
import sendgrid
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
'''
from datetime import date

# App setup
app = Flask(__name__)
app.config["SECRET_KEY"] = "some_really_long_random_string_here"

'''
# Get details for sendgrid details
sendgrid_file = "sendgrid.txt"
sendgrid_details = []

with open(sendgrid_file) as f:
    sendgrid_details = f.readlines()
    sendgrid_details = [x.strip("\n") for x in sendgrid_details]
'''
# Global Variables
products_info = [
    {
        "id": "101",
        "name": "Pizza Jamón y Queso",
        "img": "pizza-101.jpg",
        "price": 18,
        "paypal": "LNRBY7XSXS5PA",
        "sizes": ["Small", "Medium", "Large"]
    },

    {
        "id": "102",
        "name": "Burger",
        "img": "burger-102.jpg",
        "price": 20,
        "paypal": "XP8KRXHEXMQ4J",
        "sizes": ["Small", "Medium", "Large"]
    },

    {
        "id": "103",
        "name": "Taco",
        "img": "taco-103.jpg",
        "price": 20,
        "paypal": "95C659J3VZGNJ",
        "sizes": ["Small", "Medium", "Large"]
    },

    {
        "id": "104",
        "name": "Hot Dog",
        "img": "hotdog-104.jpg",
        "price": 18,
        "paypal": "Z5EY4SJN64SLU",
        "sizes": ["Small", "Medium", "Large"]
    },

    {
        "id": "105",
        "name": "Empanada",
        "img": "empanada-105.jpg",
        "price": 25,
        "paypal": "RYAGP5EWG4V4G",
        "sizes": ["Small", "Medium", "Large"]
    },

    {
        "id": "106",
        "name": "Cheese Fingers",
        "img": "deditos-106.jpg",
        "price": 20,
        "paypal": "QYHDD4N4SMUKN",
        "sizes": ["Small", "Medium", "Large"]
    },

    {
        "id": "107",
        "name": "Sopa do Macaco - Uma delicia",
        "img": "sopaemacaco-107.jpg",
        "price": 20,
        "paypal": "RSDD7RPZFPQTQ",
        "sizes": ["Small", "Medium", "Large"]
    },

    {
        "id": "108",
        "name": "Lasaña",
        "img": "lasaña-108.jpg",
        "price": 25,
        "paypal": "LFRHBPYZKHV4Y",
        "sizes": ["Small", "Medium", "Large"]
    }
]

# Functions


def get_list_view_html(product):
    """Function to return html for given dish

    The product argument should be a dictionary in this structure:
    {
        "id": "dish_id",
        "name": "name_of_dish",
        "img": "image_name.jpg",
        "price": price_of_dish_as_int_or_flat,
        "paypal": "paypal_id"
        "sizes": ["array_of_sizes"]
    }

    The html is returned in this structure:
    <li>
      <a href="dish/dish_id">
        <img src="/static/dish_img" alt="dish_name">
        <p>View Details</p>
      </a>
    </li>
    """
    output = ""
    image_url = url_for("static", filename=product["img"])
    dish_url = url_for("dish", product_id=product["id"])
    output = output + "<li>"
    output = output + '<a href="' + dish_url + '">'
    output = (
        output + '<img src="' + image_url +
        '" al  t="' + product["name"] + '">')
    output = output + "<p>View Details</p>"
    output = output + "</a>"
    output = output + "</li>"

    return output


# Routes
# All functions should have a page_title variables if they render templates

@app.route("/")
def index():
    """Function for Rookie App Homepage"""
    context = {"page_title": "Rookie App", "current_year": date.today().year}
    counter = 0
    product_data = []
    for product in products_info:
        counter += 1
        if counter < 5:  
            product_data.append(
                Markup(get_list_view_html(product))
            )
    context["product_data"] = Markup("".join(product_data))
   
    return render_template("index.html", **context)


@app.route("/dishes")
def dishes():
    """Function for the rookie Listing Page"""
    context = {"page_title": "Rookie App", "current_year": date.today().year}
    product_data = []
    for product in products_info:
        product_data.append(Markup(get_list_view_html(product)))
    context["product_data"] = Markup("".join(product_data))
    
    return render_template("dishes.html", **context)


@app.route("/dish/<product_id>")
def dish(product_id):
    """Function for Individual Dishes Page"""
    context = {"page_title": "Rookie App", "current_year": date.today().year}
    my_product = ""
    for product in products_info:
        if product["id"] == product_id:
            my_product = product
    context["product"] = my_product
    
    return render_template("dish.html", **context)


@app.route("/receipt")
def receipt():
    """Function to display receipt after purchase"""
    context = {"page_title": "Rookie App", "current_year": date.today().year}
    return render_template("receipt.html", **context)


@app.route("/contact")
def contact():
    """Function for contact page"""
    context = {"page_title": "Rookie App", "current_year": date.today().year}
    return render_template("contact.html", **context)

'''
# Route to send email
@app.route("/send", methods=['POST'])
def send():
    """Function to send email using sendgrid API"""
    sendgrid_object = sendgrid.SendGridClient(
        sendgrid_details[0], sendgrid_details[1])
    message = sendgrid.Mail()
    sender = request.form["email"]
    subject = request.form["name"]
    body = request.form["message"]
    message.add_to("charlie.thomas@attwoodthomas.net")
    message.set_from(sender)
    message.set_subject(subject)
    message.set_html(body)
    sendgrid_object.send(message)
    flash("Email sent.")
    return redirect(url_for("contact"))
'''

# Run application
if __name__ == "__main__":
    app.run(debug=True)
