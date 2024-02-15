from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

# Connect to the database
engine = create_engine('sqlite:///db/restaurants.db')
Base.metadata.bind = engine

# Create a session to interact with db
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Seed data for customers
customer1 = Customer(first_name='Doris', last_name='Jeptoo')
customer2 = Customer(first_name='Donald', last_name='Kiprop')
customer3 = Customer(first_name='Weldon', last_name='Korir')
customer4 = Customer(first_name='Gideon', last_name='Limo')
customer5 = Customer(first_name='Idah', last_name='Jepkurui')

session.add_all([customer1, customer2, customer3, customer4, customer5])
session.commit()

# Seed data for restaurants
restaurant1 = Restaurant(name='Restaurant 1', price=10)
restaurant2 = Restaurant(name='Restaurant 2', price=20)
restaurant3 = Restaurant(name='Restaurant 3', price=30)
restaurant4 = Restaurant(name='Restaurant 4', price=40)
restaurant5 = Restaurant(name='Restaurant 5', price=50)

session.add_all([restaurant1, restaurant2, restaurant3, restaurant4, restaurant5])
session.commit()

# Seed data for restaurant_users
# Establish the many-to-many relationship between customers and restaurants
restaurant1.customers.append(customer1)
restaurant2.customers.append(customer2)
restaurant3.customers.append(customer3)
restaurant4.customers.append(customer4)
restaurant5.customers.append(customer5)

# session.execute(restaurant_user.insert().values(restaurant_id=restaurant1.id, customer_id=customer1.id))
# session.execute(restaurant_user.insert().values(restaurant_id=restaurant2.id, customer_id=customer2.id))
# session.execute(restaurant_user.insert().values(restaurant_id=restaurant3.id, customer_id=customer3.id))
# session.execute(restaurant_user.insert().values(restaurant_id=restaurant4.id, customer_id=customer4.id))
# session.execute(restaurant_user.insert().values(restaurant_id=restaurant5.id, customer_id=customer5.id))

session.commit()

# Seed data for reviews
review1 = Review(star_rating=1, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=2, restaurant=restaurant2, customer=customer2)
review3 = Review(star_rating=3, restaurant=restaurant3, customer=customer3)
review4 = Review(star_rating=4, restaurant=restaurant4, customer=customer4)
review5 = Review(star_rating=5, restaurant=restaurant5, customer=customer5)

session.add_all([review1, review2, review3, review4, review5])
session.commit()

# Close the session
session.close()
