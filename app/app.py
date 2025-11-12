from flask import Flask, jsonify, request, render_template
import redis

app = Flask(__name__)

# Conexión a Redis
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products', methods=['GET'])
def get_products():
    products = []
    for key in redis_client.scan_iter("producto:*"):
        products.append(redis_client.hgetall(key))
    return jsonify(products)

@app.route('/cart', methods=['GET'])
def get_cart():
    cart_items = []
    cart_data = redis_client.hgetall("cart")
    for product_id, quantity in cart_data.items():
        product = redis_client.hgetall(f"producto:{product_id}")
        if product:
            cart_items.append({
                "id": product_id,
                "name": product.get("name"),
                "price": float(product.get("price", 0)),
                "quantity": int(quantity)
            })
    return jsonify(cart_items)

@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get("product_id")

    if not product_id or not redis_client.exists(f"producto:{product_id}"):
        return jsonify({"status": "error"}), 400

    # Añadir o incrementar cantidad en la cesta
    redis_client.hincrby("cart", product_id, 1)
    return jsonify({"status": "added"}), 200

@app.route('/checkout', methods=['POST'])
def checkout():
    cart_data = redis_client.hgetall("cart")
    if not cart_data:
        return jsonify({"status": "empty"}), 200

    # Reducir stock de productos según la cesta
    for product_id, quantity in cart_data.items():
        redis_client.hincrby(f"producto:{product_id}", "stock", -int(quantity))

    # Limpiar la cesta
    redis_client.delete("cart")
    return jsonify({"status": "completed"}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
