import unittest

# --------------------------------------------------
# 1. KELAS EMPLOYEE (Kode Utama)
# --------------------------------------------------
class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        self.annual_salary += amount


# --------------------------------------------------
# 2. KELAS PENGUJI (Unit Test menggunakan unittest)
# --------------------------------------------------
class TestEmployee(unittest.TestCase):
    def setUp(self):
        """Method setUp() menggantikan @pytest.fixture."""
        self.employee = Employee('Budi', 'Santoso', 50000)

    def test_give_default_raise(self):
        """Uji apakah kenaikan gaji default ($5000) bekerja dengan benar."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 55000)

    def test_give_custom_raise(self):
        """Uji apakah kenaikan gaji kustom ($10000) bekerja dengan benar."""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 60000)


# --------------------------------------------------
# 3. JALANKAN PENGUJI
# --------------------------------------------------
if __name__ == '__main__':
    unittest.main()