import main
import pytest
import requests

highest_mhero_employed = main.find_highest_superhero("Male",1)
highest_mhero_unemployed = main.find_highest_superhero("Male",0)
highest_whero_employed = main.find_highest_superhero("Female",1)
highest_whero_unemployed = main.find_highest_superhero("Female",0)
# есть другие гендеры? 

def test_low_capital_m_gender_employed_input():# сделать параметр ввода пола регистронезависимым
    assert main.find_highest_superhero("male",1) == highest_mhero_employed


def test_low_capital_w_gender_employed_input():# аналогично для женского пола
    assert main.find_highest_superhero("female",1) == highest_whero_employed


def test_low_capital_m_gender_unemployed_input():# аналогичный вариант с безработным мужским полом
    assert main.find_highest_superhero("male",0) == highest_mhero_unemployed

def test_low_capital_w_gender_unemployed_input():# аналогичный вариант с безработным женским полом
    assert main.find_highest_superhero("female",0) == highest_whero_unemployed


def test_employed_and_unemployed():# герой не может одновременно иметь и не иметь работу. Тест ложный => разные герои выводятся.
    assert main.find_highest_superhero("Male",1) == highest_mhero_unemployed


def test_input_boolean_as_str():# тест верный. Парсится логический и числовой ввод.
    assert main.find_highest_superhero("Male",True) == highest_mhero_employed


def test_wrong_int_input():# ввод значения больше единицы
    assert main.find_highest_superhero("Male",2) is None
def test_negative_int_input():#
    assert main.find_highest_superhero("Male",-1) is None
#лучше сделать ввод аргумента только через true/false
def test_wrong_int_input4():#Вывод не равен безработному мужскому супергерою при вводе "-"" в качестве отсутствия работы
    assert main.find_highest_superhero("Male","-") is None


def test_api_is_working():# тестирование ответа от api - косвенно связано с апи
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    assert response.status_code == 200
