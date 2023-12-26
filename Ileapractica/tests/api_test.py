import requests
import logging
from faker import Faker
import pytest
import allure
import os

logs_dir = 'logs'
os.makedirs(logs_dir, exist_ok=True)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(os.path.join(logs_dir, 'logs_api.log'))
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


fake = Faker()
base_url = 'http://localhost:3000'


# CREATE
def create_user(user_data):
    response = requests.post(f"{base_url}/users", json=user_data)
    logger.info(f"Create User - Request: {user_data}, Response: {response.text}")
    return response.json()

def create_product(product_data):
    response = requests.post(f"{base_url}/products", json=product_data)
    logger.info(f"Create Product - Request: {product_data}, Response: {response.text}")
    return response.json()

def create_order(order_data):
    response = requests.post(f"{base_url}/orders", json=order_data)
    logger.info(f"Create Order - Request: {order_data}, Response: {response.text}")
    return response.json()

def create_category(category_data):
    response = requests.post(f"{base_url}/categories", json=category_data)
    logger.info(f"Create Category - Request: {category_data}, Response: {response.text}")
    return response.json()

def create_review(review_data):
    response = requests.post(f"{base_url}/reviews", json=review_data)
    logger.info(f"Create Review - Request: {review_data}, Response: {response.text}")
    return response.json()

# READ
def get_user(user_id):
    response = requests.get(f"{base_url}/users/{user_id}")
    logger.info(f"Read User - Request: {user_id}, Response: {response.text}")
    return response.json()

def get_product(product_id):
    response = requests.get(f"{base_url}/products/{product_id}")
    logger.info(f"Read Product - Request: {product_id}, Response: {response.text}")
    return response.json()

def get_order(order_id):
    response = requests.get(f"{base_url}/orders/{order_id}")
    logger.info(f"Read Order - Request: {order_id}, Response: {response.text}")
    return response.json()

def get_category(category_id):
    response = requests.get(f"{base_url}/categories/{category_id}")
    logger.info(f"Read Category - Request: {category_id}, Response: {response.text}")
    return response.json()

def get_review(review_id):
    response = requests.get(f"{base_url}/reviews/{review_id}")
    logger.info(f"Read Review - Request: {review_id}, Response: {response.text}")
    return response.json()

# UPDATE
def update_user(user_id, updated_user_data):
    response = requests.put(f"{base_url}/users/{user_id}", json=updated_user_data)
    logger.info(f"Update User - Request: {user_id}, Response: {response.text}")
    return response.json()

def update_product(product_id, updated_product_data):
    response = requests.put(f"{base_url}/products/{product_id}", json=updated_product_data)
    logger.info(f"Update Product - Request: {product_id}, Response: {response.text}")
    return response.json()

def update_order(order_id, updated_order_data):
    response = requests.put(f"{base_url}/orders/{order_id}", json=updated_order_data)
    logger.info(f"Update Order - Request: {order_id}, Response: {response.text}")
    return response.json()

def update_category(category_id, updated_category_data):
    response = requests.put(f"{base_url}/categories/{category_id}", json=updated_category_data)
    logger.info(f"Update Category - Request: {category_id}, Response: {response.text}")
    return response.json()

def update_review(review_id, updated_review_data):
    response = requests.put(f"{base_url}/reviews/{review_id}", json=updated_review_data)
    logger.info(f"Update Review - Request: {review_id}, Response: {response.text}")
    return response.json()

# DELETE
def delete_user(user_id):
    response = requests.delete(f"{base_url}/users/{user_id}")
    logger.info(f"Delete User - Request: {user_id}")
    return response.status_code

def delete_product(product_id):
    response = requests.delete(f"{base_url}/products/{product_id}")
    logger.info(f"Delete Product - Request: {product_id}")
    return response.status_code

def delete_order(order_id):
    response = requests.delete(f"{base_url}/orders/{order_id}")
    logger.info(f"Delete Order - Request: {order_id}")
    return response.status_code

def delete_category(category_id):
    response = requests.delete(f"{base_url}/categories/{category_id}")
    logger.info(f"Delete Category - Request: {category_id}")
    return response.status_code

def delete_review(review_id):
    response = requests.delete(f"{base_url}/reviews/{review_id}")
    logger.info(f"Delete Review - Request: {review_id}")
    return response.status_code



@pytest.fixture
def random_user():
    return {
        'name': fake.name(),
        'email': fake.email(),
        'address': fake.address()
    }

@pytest.fixture
def random_product():
    return {
        'name': fake.word(),
        'price': fake.random_number(2),
        'category_id': fake.random_number(2),
    }

@pytest.fixture
def random_order():
    return {
        'product_id': fake.random_number(2),
        'quantity': fake.random_number(2),
        'customer_name': fake.name(),
    }

@pytest.fixture
def random_category():
    return {
        'name': fake.word(),
    }

@pytest.fixture
def random_review():
    return {
        'product_id': fake.random_number(2),
        'user_id': fake.random_number(2),
        'text': fake.text(),
    }



#Крудка в Геншине
@allure.feature("CRUD Operations")
@allure.story("Create User")
def test_create_user(random_user):
    created_user = create_user(random_user)
    assert created_user
    logger.info(f"Test - Create User: {created_user}")


@allure.feature("CRUD Operations")
@allure.story("Read User")
def test_read_user(random_user):
    created_user = create_user(random_user)
    user_id = created_user['id']
    retrieved_user = get_user(user_id)
    assert retrieved_user == created_user
    logger.info(f"Test - Read User: {retrieved_user}")


@allure.feature("CRUD Operations")
@allure.story("Update User")
def test_update_user(random_user):
    created_user = create_user(random_user)
    user_id = created_user['id']
    updated_data = {
        'name': 'Updated Name',
        'address': 'Updated Address'
    }
    updated_user = update_user(user_id, updated_data)
    assert updated_user['name'] == 'Updated Name'
    logger.info(f"Test - Update User: {updated_user['name']}")


@allure.feature("CRUD Operations")
@allure.story("Delete User")
def test_delete_user(random_user):
    created_user = create_user(random_user)
    user_id = created_user['id']
    status_code = delete_user(user_id)
    assert status_code == 200
    logger.info(f"Test - Delete User: {status_code}")

@allure.feature("CRUD Operations")
@allure.story("Create Product")
def test_create_product(random_product):
    created_product = create_product(random_product)
    assert created_product
    logger.info(f"Test - Create Product: {created_product}")

@allure.feature("CRUD Operations")
@allure.story("Read Product")
def test_read_product(random_product):
    created_product = create_product(random_product)
    product_id = created_product['id']
    retrieved_product = get_product(product_id)
    assert retrieved_product == created_product
    logger.info(f"Test - Read Product: {retrieved_product}")

@allure.feature("CRUD Operations")
@allure.story("Update Product")
def test_update_product(random_product):
    created_product = create_product(random_product)
    product_id = created_product['id']
    updated_data = {
        'name': 'Updated Product',
        'price': 99,
    }
    updated_product = update_product(product_id, updated_data)
    assert updated_product['name'] == 'Updated Product'
    logger.info(f"Test - Update Product: {updated_product['name']}")

@allure.feature("CRUD Operations")
@allure.story("Delete Product")
def test_delete_product(random_product):
    created_product = create_product(random_product)
    product_id = created_product['id']
    status_code = delete_product(product_id)
    assert status_code == 200
    logger.info(f"Test - Delete Product: {status_code}")

@allure.feature("CRUD Operations")
@allure.story("Create Order")
def test_create_order(random_order):
    created_order = create_order(random_order)
    assert created_order
    logger.info(f"Test - Create Order: {created_order}")

@allure.feature("CRUD Operations")
@allure.story("Read Order")
def test_read_order(random_order):
    created_order = create_order(random_order)
    order_id = created_order['id']
    retrieved_order = get_order(order_id)
    assert retrieved_order == created_order
    logger.info(f"Test - Read Order: {retrieved_order}")

@allure.feature("CRUD Operations")
@allure.story("Update Order")
def test_update_order(random_order):
    created_order = create_order(random_order)
    order_id = created_order['id']
    updated_data = {
        'quantity': 10,
        'customer_name': 'Updated Customer'
    }
    updated_order = update_order(order_id, updated_data)
    assert updated_order['quantity'] == 10
    logger.info(f"Test - Update Order: {updated_order['quantity']}")

@allure.feature("CRUD Operations")
@allure.story("Delete Order")
def test_delete_order(random_order):
    created_order = create_order(random_order)
    order_id = created_order['id']
    status_code = delete_order(order_id)
    assert status_code == 200
    logger.info(f"Test - Delete Operations: {status_code}")

@allure.feature("CRUD Operations")
@allure.story("Create Category")
def test_create_category(random_category):
    created_category = create_category(random_category)
    assert created_category
    logger.info(f"Test - Create Category: {created_category}")

@allure.feature("CRUD Operations")
@allure.story("Read Category")
def test_read_category(random_category):
    created_category = create_category(random_category)
    category_id = created_category['id']
    retrieved_category = get_category(category_id)
    assert retrieved_category == created_category
    logger.info(f"Test - Read Category: {retrieved_category}")

@allure.feature("CRUD Operations")
@allure.story("Update Category")
def test_update_category(random_category):
    created_category = create_category(random_category)
    category_id = created_category['id']
    updated_data = {
        'name': 'Updated Category',
    }
    updated_category = update_category(category_id, updated_data)
    assert updated_category['name'] == 'Updated Category'
    logger.info(f"Test - Update Category: {updated_category['name']}")

@allure.feature("CRUD Operations")
@allure.story("Delete Category")
def test_delete_category(random_category):
    created_category = create_category(random_category)
    category_id = created_category['id']
    status_code = delete_category(category_id)
    assert status_code == 200
    logger.info(f"Test - Delete Category: {status_code}")

@allure.feature("CRUD Operations")
@allure.story("Create Review")
def test_create_review(random_review):
    created_review = create_review(random_review)
    assert created_review
    logger.info(f"Test - Create Review: {created_review}")

@allure.feature("CRUD Operations")
@allure.story("Read Review")
def test_read_review(random_review):
    created_review = create_review(random_review)
    review_id = created_review['id']
    retrieved_review = get_review(review_id)
    assert retrieved_review == created_review
    logger.info(f"Test - Read Review : {retrieved_review }")

@allure.feature("CRUD Operations")
@allure.story("Update Review")
def test_update_review(random_review):
    created_review = create_review(random_review)
    review_id = created_review['id']
    updated_data = {
        'text': 'Updated Review Text',
    }
    updated_review = update_review(review_id, updated_data)
    assert updated_review['text'] == 'Updated Review Text'
    logger.info(f"Test - Update Review: {updated_review['text']}")

@allure.feature("CRUD Operations")
@allure.story("Delete Review")
def test_delete_review(random_review):
    created_review = create_review(random_review)
    review_id = created_review['id']
    status_code = delete_review(review_id)
    assert status_code == 200
    logger.info(f"Test - Delete Operations: {status_code}")



if __name__ == "__main__":
    import subprocess
    json_server_process = subprocess.Popen(["json-server", "--watch", "db.json", "--port", "3000"])
    pytest.main(["-s", "--alluredir=allure-results"])
    json_server_process.terminate()
    subprocess.run(["allure", "serve", "allure-results"])
