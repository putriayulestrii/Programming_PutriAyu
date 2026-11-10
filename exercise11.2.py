from  city_functions import city_country

def test_city_country():
    formatted = city_country('santiago', 'chile')
    assert formatted == 'Santiago, Chile'

def test_city_country_population():
    formatted = city_country('santiago', 'chile', 5000000)
    assert formatted == 'Santiago, Chile - population 5000000'