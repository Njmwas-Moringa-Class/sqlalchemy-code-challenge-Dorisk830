from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

# Connect to the database
engine = create_engine('sqlite:///db/restaurants.db')
Base.metadata.bind = engine

# Create a session to interact with the database
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Seed data for restaurants
restaurant1 = Restaurant(name='Restaurant 1', price=10)
restaurant2 = Restaurant(name='Restaurant 2', price=20)
restaurant3 = Restaurant(name='Restaurant 3', price=30)
restaurant4 = Restaurant(name='Restaurant 4', price=40)
restaurant5 = Restaurant(name='Restaurant 5', price=50)

session.add_all([restaurant1, restaurant2, restaurant3])
session.commit()

# Seed data for customers
customer1 = Customer(first_name='Doris', last_name='Jeptoo')
customer2 = Customer(first_name='Donald', last_name='Kiprop')
customer3 = Customer(first_name='Weldon', last_name='Korir')
customer4 = Customer(first_name='Gideon', last_name='Limo')
customer5 = Customer(first_name='Idah', last_name='Jepkurui')

session.add_all([customer1, customer2, customer3])
session.commit()

# Seed data for reviews
review1 = Review(star_rating=1, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=2, restaurant=restaurant2, customer=customer2)
review3 = Review(star_rating=3, restaurant=restaurant3, customer=customer3)
review3 = Review(star_rating=2, restaurant=restaurant4, customer=customer4)
review5 = Review(star_rating=3, restaurant=restaurant5, customer=customer5)

session.add_all([review1, review2, review3])
session.commit()

# Close the session
session.close()