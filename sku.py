from pyscript import document

def generate_sku(e):
    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    stock_qty = document.getElementById("stock_qty").value
    receipt = document.getElementById("sku_receipt")
    receipt.innerHTML = ""
    if stock_qty == "":
        receipt.innerHTML = "Please enter the stock quantity."
        return
    if not stock_qty.isdigit():
        receipt.innerHTML = "Stock must be a whole number."
        return
    SKU = category[:4].upper() + "-" + product_name[:5].upper() + "-" + stock_qty
    receipt.innerHTML = (
        "<h3>Generated SKU</h3>"
        + "<p>Product: " + product_name + "</p>"
        + "<p>Category: " + category + "</p>"
        + "<p>Stock Quantity: " + stock_qty + "</p>"
        + "<div class='sku-code'>" + SKU + "</div>"
        + "<p>SKU successfully generated!</p>"
    )