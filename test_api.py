import requests

def test_create_and_get_order():
    BASE_URL = "https://e16f8dfb-6d76-42fa-b8bd-e762a0822825.serverhub.praktikum-services.ru"
    
    # 1. Создаем заказ
    order_data = {
        "firstName": "Иван",
        "lastName": "Иванов", 
        "address": "Москва, ул. Ленина, 1",
        "metroStation": 4,
        "phone": "+79999999999",
        "rentTime": 5,
        "deliveryDate": "2024-01-01",
        "comment": "Тестовый заказ",
        "color": ["BLACK"]
    }
    
    response = requests.post(f"{BASE_URL}/api/v1/orders", json=order_data)
    track = response.json()['track']
    
    # 2. Получаем заказ по треку
    response = requests.get(f"{BASE_URL}/api/v1/orders/track?t={track}")
    
    # 3. Проверяем что код ответа 200
    assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
    print("✅ Тест пройден!")

test_create_and_get_order()