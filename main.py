from pyscript import display, document

def create_order(e):

    prices = {
        "grilledcheese": 120,
        "grilledmackerel": 150,
        "cheeseomelette": 130,
        "veggieomelette": 150,
        "chickennuggets": 130,
        "crispytofu": 120,
        "friedchicken": 150,
        "seafoodboil": 250,
        "spicyramen": 180,
        "cupofrice": 50,
        "fishandchips": 180,
        "frenchfries": 100
    }

    names = {
        "grilledcheese": "Grilled Cheese",
        "grilledmackerel": "Grilled Mackerel",
        "cheeseomelette": "Cheese Omelette",
        "veggieomelette": "Omelette w/ Veggies",
        "chickennuggets": "Chicken Nuggets",
        "crispytofu": "Crispy Tofu",
        "friedchicken": "Fried Chicken",
        "seafoodboil": "Seafood Boil",
        "spicyramen": "Spicy Ramen",
        "cupofrice": "Cup of Rice",
        "fishandchips": "Fish and Chips",
        "frenchfries": "French Fries"
    }

    subtotal = 0
    order = []

    if document.getElementById("grilledcheese").checked:
        subtotal = subtotal + prices["grilledcheese"]
        order.append(names["grilledcheese"])

    if document.getElementById("grilledmackerel").checked:
        subtotal = subtotal + prices["grilledmackerel"]
        order.append(names["grilledmackerel"])

    if document.getElementById("cheeseomelette").checked:
        subtotal = subtotal + prices["cheeseomelette"]
        order.append(names["cheeseomelette"])

    if document.getElementById("veggieomelette").checked:
        subtotal = subtotal + prices["veggieomelette"]
        order.append(names["veggieomelette"])

    if document.getElementById("chickennuggets").checked:
        subtotal = subtotal + prices["chickennuggets"]
        order.append(names["chickennuggets"])

    if document.getElementById("crispytofu").checked:
        subtotal = subtotal + prices["crispytofu"]
        order.append(names["crispytofu"])

    if document.getElementById("friedchicken").checked:
        subtotal = subtotal + prices["friedchicken"]
        order.append(names["friedchicken"])

    if document.getElementById("seafoodboil").checked:
        subtotal = subtotal + prices["seafoodboil"]
        order.append(names["seafoodboil"])

    if document.getElementById("spicyramen").checked:
        subtotal = subtotal + prices["spicyramen"]
        order.append(names["spicyramen"])

    if document.getElementById("cupofrice").checked:
        subtotal = subtotal + prices["cupofrice"]
        order.append(names["cupofrice"])

    if document.getElementById("fishandchips").checked:
        subtotal = subtotal + prices["fishandchips"]
        order.append(names["fishandchips"])

    if document.getElementById("frenchfries").checked:
        subtotal = subtotal + prices["frenchfries"]
        order.append(names["frenchfries"])

    tax = subtotal * 0.12
    total = subtotal + tax

    receipt = ""

    for item in order:
        receipt = receipt + item + "<br>"

    receipt = receipt + "<br>"
    receipt = receipt + "Subtotal: ₱" + str(subtotal) + "<br>"
    receipt = receipt + "Tax: ₱" + str(tax) + "<br>"
    receipt = receipt + "<br>"
    receipt = receipt + "<b>Total: ₱" + str(total) + "</b>"

    document.getElementById("receipt").innerHTML = receipt




    # SOURCES USED: https://www.w3schools.com/python/ref_list_append.asp https://www.w3schools.com/Jsref/met_document_getelementbyid.asp https://mimo.org/glossary/python/if-statement