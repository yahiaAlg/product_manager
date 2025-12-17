from django.core.management.base import BaseCommand
from decimal import Decimal
import random
from ...models import Product  # Replace 'yourapp' with your actual app name


class Command(BaseCommand):
    help = "Seeds the database with 20 realistic products"

    def handle(self, *args, **kwargs):
        # Clear existing products (optional)
        Product.objects.all().delete()
        self.stdout.write(self.style.WARNING("Cleared existing products"))

        products = [
            {
                "name": "Apple iPhone 15 Pro",
                "description": "Latest flagship smartphone with A17 Pro chip, titanium design, and advanced camera system. Features 6.1-inch Super Retina XDR display.",
                "price": Decimal("999.99"),
                "stock": random.randint(10, 100),
            },
            {
                "name": "Sony WH-1000XM5 Headphones",
                "description": "Industry-leading noise canceling wireless headphones with exceptional sound quality and 30-hour battery life.",
                "price": Decimal("399.99"),
                "stock": random.randint(10, 100),
            },
            {
                "name": 'Samsung 55" 4K Smart TV',
                "description": "Crystal UHD 4K TV with HDR support, smart hub, and built-in streaming apps. Perfect for home entertainment.",
                "price": Decimal("549.99"),
                "stock": random.randint(5, 50),
            },
            {
                "name": "Dell XPS 13 Laptop",
                "description": "13.4-inch laptop with Intel Core i7, 16GB RAM, 512GB SSD. Ultra-portable with stunning InfinityEdge display.",
                "price": Decimal("1299.99"),
                "stock": random.randint(8, 40),
            },
            {
                "name": "Nintendo Switch OLED",
                "description": "Enhanced gaming console with vibrant 7-inch OLED screen, 64GB storage, and improved audio.",
                "price": Decimal("349.99"),
                "stock": random.randint(15, 80),
            },
            {
                "name": "Instant Pot Duo 7-in-1",
                "description": "Multi-functional pressure cooker that replaces 7 kitchen appliances. 6-quart capacity, perfect for families.",
                "price": Decimal("89.99"),
                "stock": random.randint(20, 150),
            },
            {
                "name": "Dyson V15 Vacuum Cleaner",
                "description": "Cordless vacuum with laser dust detection and powerful suction. Ideal for whole-home deep cleaning.",
                "price": Decimal("649.99"),
                "stock": random.randint(5, 30),
            },
            {
                "name": "Kindle Paperwhite",
                "description": "Waterproof e-reader with 6.8-inch display and adjustable warm light. Holds thousands of books.",
                "price": Decimal("139.99"),
                "stock": random.randint(25, 120),
            },
            {
                "name": "Fitbit Charge 6",
                "description": "Advanced fitness tracker with heart rate monitoring, GPS, and sleep tracking. 7-day battery life.",
                "price": Decimal("159.99"),
                "stock": random.randint(30, 100),
            },
            {
                "name": "Nespresso Vertuo Coffee Maker",
                "description": "Single-serve coffee and espresso maker with barcode technology for perfect brewing every time.",
                "price": Decimal("179.99"),
                "stock": random.randint(15, 70),
            },
            {
                "name": "Bose SoundLink Bluetooth Speaker",
                "description": "Portable wireless speaker with 360-degree sound and 12-hour battery. Water-resistant design.",
                "price": Decimal("149.99"),
                "stock": random.randint(20, 90),
            },
            {
                "name": "Canon EOS R6 Camera",
                "description": "Full-frame mirrorless camera with 20.1MP sensor, 4K video, and advanced autofocus system.",
                "price": Decimal("2499.99"),
                "stock": random.randint(3, 20),
            },
            {
                "name": "Apple AirPods Pro (2nd Gen)",
                "description": "Premium wireless earbuds with active noise cancellation, spatial audio, and MagSafe charging.",
                "price": Decimal("249.99"),
                "stock": random.randint(40, 150),
            },
            {
                "name": 'iPad Air 10.9"',
                "description": "Powerful tablet with M1 chip, stunning Liquid Retina display, and all-day battery life.",
                "price": Decimal("599.99"),
                "stock": random.randint(12, 60),
            },
            {
                "name": "KitchenAid Stand Mixer",
                "description": "Classic 5-quart stand mixer in Empire Red. 10-speed control for precise mixing. Includes multiple attachments.",
                "price": Decimal("429.99"),
                "stock": random.randint(10, 50),
            },
            {
                "name": "Logitech MX Master 3S Mouse",
                "description": "Ergonomic wireless mouse with ultra-quiet clicks, 8K DPI sensor, and multi-device connectivity.",
                "price": Decimal("99.99"),
                "stock": random.randint(35, 120),
            },
            {
                "name": "Ring Video Doorbell Pro",
                "description": "Smart doorbell with 1080p HD video, two-way talk, and advanced motion detection.",
                "price": Decimal("249.99"),
                "stock": random.randint(18, 75),
            },
            {
                "name": "Lululemon Yoga Mat",
                "description": "Premium 5mm yoga mat with superior grip and cushioning. Natural rubber construction.",
                "price": Decimal("78.00"),
                "stock": random.randint(25, 100),
            },
            {
                "name": "Philips Hue Smart Bulb Starter Kit",
                "description": "Set of 4 color-changing LED smart bulbs with bridge. Control with voice or smartphone app.",
                "price": Decimal("199.99"),
                "stock": random.randint(15, 80),
            },
            {
                "name": "Herman Miller Aeron Chair",
                "description": "Ergonomic office chair with PostureFit support and breathable mesh. Size B (medium).",
                "price": Decimal("1395.00"),
                "stock": random.randint(4, 25),
            },
        ]

        created_count = 0
        for product_data in products:
            product = Product.objects.create(**product_data)
            created_count += 1
            self.stdout.write(
                self.style.SUCCESS(f"Created: {product.name} (Stock: {product.stock})")
            )

        self.stdout.write(
            self.style.SUCCESS(f"\nSuccessfully seeded {created_count} products!")
        )
