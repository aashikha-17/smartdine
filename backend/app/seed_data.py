from app.database import SessionLocal
from app.models import Restaurant

def seed_restaurants():
    db = SessionLocal()

    if db.query(Restaurant).count() > 0:
        print("Restaurants already seeded")
        return

    restaurants = [
        # -------- INDIAN --------
        Restaurant(
            "Sharma's Dhaba", "north indian", "₹", 4.5,
            11.0168, 76.9558,
            "https://images.unsplash.com/photo-1589778655375-3e622a9fc91c"
        ),

        # -------- CHEESY --------
        Restaurant(
            "Pizza Hub", "pizza", "₹₹", 4.3,
            11.0200, 76.9600,
            "https://plus.unsplash.com/premium_photo-1730829256766-94d297540c23"
        ),
        Restaurant(
            "Domino's", "pizza", "₹₹", 4.0,
            11.0212, 76.9595,
            "https://plus.unsplash.com/premium_photo-1733306588881-0411931d4fed"
        ),
        Restaurant(
            "Burger Point", "burger", "₹", 4.1,
            11.0180, 76.9580,
            "https://images.unsplash.com/photo-1550547660-d9450f859349"
        ),
        Restaurant(
            "KFC", "burger", "₹₹", 4.0,
            11.0190, 76.9570,
            "https://images.unsplash.com/photo-1513639776629-7b61b0ac49cb"
        ),
        Restaurant(
            "Meat & Eat", "burger", "₹₹", 4.1,
            11.0160, 76.9550,
            "https://images.unsplash.com/photo-1568901346375-23c9450c58cd"
        ),

        # -------- BIRYANI --------
        Restaurant(
            "SS Hyderabad Biryani", "biryani", "₹₹", 4.4,
            11.0150, 76.9540,
            "https://images.unsplash.com/photo-1631515243349-e0cb75fb8d3a"
        ),
        Restaurant(
            "Thalappakatti", "biryani", "₹₹₹", 4.5,
            11.0145, 76.9535,
            "https://images.unsplash.com/photo-1628294895950-9805252327bc"
        ),

        # -------- VEGETARIAN / HEALTHY --------
        Restaurant(
            "Sangeetha", "vegetarian", "₹₹", 4.3,
            11.0138, 76.9522,
            "https://images.unsplash.com/photo-1601050690597-df0568f70950"
        ),
        Restaurant(
            "Arya Bhavan", "vegetarian", "₹", 4.2,
            11.0125, 76.9510,
            "https://images.unsplash.com/photo-1589302168068-964664d93dc0"
        ),
        Restaurant(
            "Subway", "healthy", "₹₹", 4.0,
            11.0191, 76.9584,
            "https://images.unsplash.com/photo-1551782450-a2132b4ba21d"
        ),
        Restaurant(
            "FreshMenu", "healthy", "₹₹", 4.1,
            11.0205, 76.9599,
            "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe"
        ),

        # -------- CAFE / DESSERT --------
        Restaurant(
            "Cafe Coffee Day", "cafe", "₹₹", 4.0,
            11.0189, 76.9568,
            "https://images.unsplash.com/photo-1511920170033-f8396924c348"
        ),
        Restaurant(
            "Starbucks", "cafe", "₹₹₹", 4.4,
            11.0195, 76.9579,
            "https://images.unsplash.com/photo-1509042239860-f550ce710b93"
        ),
        Restaurant(
            "Ibaco", "dessert", "₹₹", 4.3,
            11.0172, 76.9563,
            "https://images.unsplash.com/photo-1497034825429-c343d7c6a68f"
        ),
        Restaurant(
            "Cream Stone", "dessert", "₹₹", 4.2,
            11.0183, 76.9575,
            "https://images.unsplash.com/photo-1668887466159-e40db870dfad"
        ),
        Restaurant(
            "The French Door", "dessert", "₹₹₹", 4.7,
            11.0240, 76.9630,
            "https://images.unsplash.com/photo-1509440159596-0249088772ff"
        ),

        # -------- SPECIAL OCCASION --------
        Restaurant(
            "Barbeque Nation", "bbq", "₹₹₹", 4.6,
            11.0220, 76.9615,
            "https://images.unsplash.com/photo-1555939594-58d7cb561ad1"
        ),
        Restaurant(
            "Absolute Barbecue", "bbq", "₹₹₹", 4.5,
            11.0232, 76.9620,
            "https://images.unsplash.com/photo-1544025162-d76694265947"
        ),
        Restaurant(
           "Belgian Waffle Co", "dessert", "₹₹", 4.4, 11.0207, 76.9588,
            "https://images.unsplash.com/photo-1509440159596-0249088772ff"
        ),
        Restaurant(
            "Brownie Heaven", "dessert", "₹₹", 4.3, 11.0219, 76.9596,
            "https://images.unsplash.com/photo-1499636136210-6f4ee915583e"
),

    ]

    db.add_all(restaurants)
    db.commit()
    db.close()

    print("Restaurants seeded successfully")
