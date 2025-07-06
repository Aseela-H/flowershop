from flask import Flask, render_template

app = Flask(__name__)

# Categorized flower data
flower_categories = {
    "Single Flowers": [
        {"name": "Rose", "price": "₹200", "image": "https://i.ibb.co/YTwvM7j9/closeup-shot-red-rose-with-dew-top-black-181624-28079.jpg"},
        {"name": "Tulip", "price": "₹150", "image": "https://i.ibb.co/Dg1MjjW7/tulip.jpg"},
        {"name": "Lily", "price": "₹550", "image": "https://i.ibb.co/ccZZ7VB4/pngtree-lily-flower-isolated-on-transparent-background-png-image-13093937.png"},
        {"name": "Sunflower", "price": "₹700", "image": "https://i.ibb.co/prZ3TZJb/il-fullxfull-1577281449-6522.jpg"},
    ],
    "Bouquets": [
        {"name": "Orchid Bouquet", "price": "₹2000", "image": "https://i.ibb.co/XkzxsNLq/DSC-3008-Photoroom.jpg"},
        {"name": "Peony Bunch", "price": "₹2500", "image": "https://i.ibb.co/Xr9WzS4Q/Dry-Peony-Bunch-13-Watermarked.jpg"},
        {"name": "Daisy Delight", "price": "₹2999", "image": "https://i.ibb.co/x8rRspHh/UFN1011.jpg"},
        {"name": "Carnation Mix", "price": "₹2000", "image": "https://i.ibb.co/5P8rjGQ/mix-carnation-hand-bunch.webp"},
    ],
    "Gift Combos": [
        {"name": "Hydrangea Gift Box", "price": "₹3500", "image": "https://i.ibb.co/1GJdSMp1/41.jpg"},
        {"name": "Lavender Basket", "price": "₹4500", "image": "https://i.ibb.co/W4B0tccJ/illustration-basket-high-detailed-lavender-600nw-2261384917.jpg"},
        {"name": "Iris Gift Set", "price": "₹5000", "image": "https://i.ibb.co/83PJ6vw/91-AV6za-Q9-IL.jpg"},
        {"name": "Marigold Combo", "price": "₹8500", "image":"https://i.ibb.co/hRHLrY8Q/auspicious-vibes-mixed-marigold-thali-vase-1.jpg"},
    ],
    "Decoratives": [
        {"name": "Chrysanthemum Pot", "price": "₹7500", "image": "https://i.ibb.co/fdFN8H0y/chrysanthemum-potted-plant-chrysanthemums-assorted-colours-0900445-pe667989-s5.jpg"},
        {"name": "Begonia Planter", "price": "₹8999", "image": "https://i.ibb.co/QFBZRjVp/Whopper-Rose-Cordyline.png"},
        {"name": "Anemone Decor", "price": "₹7800", "image": "https://i.ibb.co/6JBzq8gz/61h-JQqn7-Sw-L-UF1000-1000-QL80.jpg"},
        {"name": "Freesia Set", "price": "₹9000", "image": "https://i.ibb.co/24fYy7X/61cj3o-byd-L-UF1000-1000-QL80.jpg"},
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/collection')
def collection():
    return render_template('collection.html', flower_categories=flower_categories)

if __name__ == '__main__':
    app.run(debug=True)