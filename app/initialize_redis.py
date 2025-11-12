import redis

def initialize_products(redis_client):
    productos = [
        {"id": "1", "name": "Teclado mecánico", "price": 49.99, "description": "Teclado RGB con switches rojos", "stock": 30},
        {"id": "2", "name": "Ratón inalámbrico", "price": 29.50, "description": "Ratón ergonómico Bluetooth", "stock": 50},
        {"id": "3", "name": "Monitor 24''", "price": 129.00, "description": "Full HD, 75Hz", "stock": 20},
        {"id": "4", "name": "SSD 1TB", "price": 89.90, "description": "Disco sólido NVMe PCIe 3.0", "stock": 15},
        {"id": "5", "name": "Auriculares gaming", "price": 59.99, "description": "Con micrófono y cancelación de ruido", "stock": 25},
        {"id": "6", "name": "Webcam HD", "price": 35.00, "description": "720p con micrófono integrado", "stock": 40},
        {"id": "7", "name": "Fuente 650W", "price": 74.95, "description": "80+ Bronze modular", "stock": 10},
        {"id": "8", "name": "Silla gaming", "price": 199.99, "description": "Ergonómica, color negro y rojo", "stock": 5},
        {"id": "9", "name": "Alfombrilla XL", "price": 14.90, "description": "Antideslizante 900x400mm", "stock": 60},
        {"id": "10", "name": "Router WiFi 6", "price": 119.00, "description": "Dual band 3000 Mbps", "stock": 8},
    ]

    for p in productos:
        redis_client.hset(f"producto:{p['id']}", mapping=p)

    print(f"{len(productos)} productos cargados correctamente en Redis.")

if __name__ == "__main__":
    try:
        # Conexión a Redis local (contenedor o instalación local)
        redis_client = redis.StrictRedis(
            host="redis",  # o "redis" si estás usando docker-compose
            port=6379,
            decode_responses=True
        )

        # Inicializa los productos en Redis
        initialize_products(redis_client)
        print("¡Productos inicializados en Redis!")

    except Exception as e:
        print(f"Error al conectarse a Redis: {e}")
