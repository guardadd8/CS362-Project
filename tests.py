import unittest
from task import my_datetime
from task import conv_num
from task import conv_endian


class TestCase(unittest.TestCase):

    def testTwoDecimals(self):
        '''
        Test strings with two decimals returns None
        '''
        self.assertIsNone(conv_num("12.3.45"))

    def testOneDigit(self):
        '''
            Test 1 digit integer string returns integer
        '''
        self.assertEqual(conv_num("1"), 1)

    def testTwoDigits(self):
        '''
            Test 2 digit integer string returns integer
        '''
        self.assertEqual(conv_num("12"), 12)

    def testZeroInMiddle(self):
        '''
            Test string with 0 in middle
        '''
        self.assertEqual(conv_num("102"), 102)

    def testZerosAtEnd(self):
        '''
            Test string with 0s at the end
        '''
        self.assertEqual(conv_num("10200"), 10200)

    def testOneDecimal(self):
        '''
            Test a string with one decimal place.
        '''
        self.assertEqual(conv_num("1.2"), 1.2)

    def testMultipleDecimalPlaces(self):
        '''
            Test a string with multiple decimal places.
        '''
        self.assertEqual(conv_num("1.25670"), 1.2567)

    def testDecimalLessThanOne(self):
        '''
            Test a string that is a decimal less than 1.
        '''
        self.assertEqual(conv_num("0.12"), 0.12)

    def testNegativeInteger(self):
        '''
            Test a string that is a negative number.
        '''
        self.assertEqual(conv_num("-105"), -105)

    def testNegativeDecimal(self):
        '''
            Test a negative decimal number
        '''
        self.assertEqual(conv_num("-1.05"), -1.05)

    def testNegDecGreaterThanOne(self):
        '''
            Test a negative decimal number greater than -1
        '''
        self.assertEqual(conv_num("-.05"), -.05)

    def testNegativeDecimalLessThanOne(self):
        '''
            Test a negative decimal number less than -1.
        '''
        self.assertEqual(conv_num("-120.678"), -120.678)

    def testInvalidDash(self):
        '''
            Test invalid number with a negative in the middle of the string.
            returns None
        '''
        self.assertIsNone(conv_num("-120-670"))

    def testFloatNoDecimals(self):
        '''
            Test a number that ends with a decimal returns number.0
        '''

        self.assertEqual(conv_num("123."), 123.0)
        self.assertTrue(isinstance(conv_num("123."), float))

    def testNegativeFloatNoDecimals(self):
        '''
            Test a negative number that ends with a decimal returns number.0
        '''

        self.assertEqual(conv_num("-123."), -123.0)
        self.assertTrue(isinstance(conv_num("-123."), float))

    def testStandardHex(self):
        '''
            Test a string for a hexidecimal number with upper case letters.
        '''
        self.assertEqual(conv_num("0xAD4"), 2772)

    def testLowerHex(self):
        '''
            Test a string for a hexidecimal number with lower case letters.
        '''
        self.assertEqual(conv_num("0Xad4"), 2772)

    def testUpperHex(self):
        '''
            Test a string for a hexidecimal number with a negative.
        '''
        self.assertEqual(conv_num("-0xad4"), -2772)

    def testInvalidLetter(self):
        '''
            Test a string for a hexidecimal number with an invalid letter.
        '''
        self.assertIsNone(conv_num("-0xag4"))

    def testNo0X(self):
        '''
            Test a string that has a hexidecimal letter but isnt'
            in the right format.
        '''
        self.assertIsNone(conv_num("AD3"))

    def testNo0Hex(self):
        '''
            Test a string that starts with x returns None.
        '''
        self.assertIsNone(conv_num("x12AD6"))

    def testNegativeNo0Hex(self):
        '''
            Test a string that starts with a
            negative then an x returns None.
        '''
        self.assertIsNone(conv_num("-x1DE"))

    def testNegativeInvalidDecimalHex(self):
        '''
            Test a mix of decimals and hex returns
            None.
        '''
        self.assertIsNone(conv_num("-0x12A.456"))

    def testHexWithNo0X(self):
        '''
            Test a string with a hex value without
            the prefix of 0x returns None.
        '''
        self.assertIsNone(conv_num("-123E"))

    def testMultipleDecimals(self):
        '''
            Test a string containing multiple
            decimal points returns None.
        '''
        self.assertIsNone(conv_num("1.34.5.6"))

    def datetime_test1(self):
        """
        Tests an input of 0 seconds.
        """
        self.assertEqual(my_datetime(0), '01-01-1970')

    def datetime_test2(self):
        """
        Tests an input that passes after one leap year.
        """
        self.assertEqual(my_datetime(123456789), '11-29-1973')

    def datetime_test3(self):
        """
        Tests a large input that passes multipe leap years."
        """
        self.assertEqual(my_datetime(9876543210), '12-22-2282')

    def datetime_test4(self):
        """
        Tests a larger input that passes multiple leap years.
        """
        self.assertEqual(my_datetime(201653971200), '02-29-8360')

    def datetime_test5(self):
        """
        Tests an input of one day.
        """
        self.assertEqual(my_datetime(86400), '01-02-1970')

    def datetime_test6(self):
        """
        Tests an input of one second less than one day.
        """
        self.assertEqual(my_datetime(86399), '01-01-1970')

    def test_big_endian(self):
        """
            Test positive integer.
        """
        self.assertEqual(conv_endian(1000, 'big'), '03 E8')

    def test_big_endian_zero(self):
        """
            Test integer with value '0'.
        """
        self.assertEqual(conv_endian(0, 'big'), '00')

    def test_big_endian_negative(self):
        """
            Test integer with value that is less than 0.
        """
        self.assertEqual(conv_endian(-10, 'big'), "-0A")

    def test_big_endian_zero_negative(self):
        """
            Test integer with value that is "-0".
        """
        self.assertEqual(conv_endian(-0, 'big'), "00")

    def test_big_endian_addition(self):
        """
            Test an integer from an addition operation in big endian.
        """
        self.assertEqual(conv_endian(100+100, 'big'), "C8")

    def test_little_endian_multiplication(self):
        """
            Test an integer from a multiplication operation in little endian.
        """
        self.assertEqual(conv_endian(20*10, 'little'), "C8")

    def test_little_endian_division(self):
        """
            Test a float from a division operation in little endian.
        """
        self.assertEqual(conv_endian(20/10, 'little'), None)

    def test_little_endian_positive(self):
        """
            Test a posiive integer in little endian.
        """
        self.assertEqual(conv_endian(1000, 'little'), "E8 03")

    def test_little_endian_negative(self):
        """
            Test a negative integer in little endian.
        """
        self.assertEqual(conv_endian(-1000, 'little'), "-E8 03")

    def test_little_endian_zero(self):
        """
            Test zero integer value in little endian.
        """
        self.assertEqual(conv_endian(0, 'little'), "00")

    def test_endian_example_one(self):
        """
            Test integer value "954786".
        """
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test_endian_example_two(self):
        """
            Test integer value "954786".
        """
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test_endian_example_four(self):
        """
            Test integer value "954786" in little endian order.
        """
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test_endian_example_five(self):
        """
            Test negative integer value "-954786" in little endian order.
        """
        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')

    def test_endian_example_six(self):
        """
            Test integer value "-954786" with passed assignments
            arguments for type hinting.
        """
        self.assertEqual(conv_endian(num=-954786, endian='little'),
                         '-A2 91 0E')

    def test_endian_example_seven(self):
        """
            Test integer value "-954786" and endian value
            of "small".
        """
        self.assertEqual(conv_endian(num=-954786, endian='small'), None)


if __name__ == '__main__':
    unittest.main()
