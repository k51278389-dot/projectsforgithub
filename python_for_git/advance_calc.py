import math
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import re
from datetime import datetime, timedelta
history=[]
def menu():
    print( "=" * 40)
    print("          ADVANCED CALCULATOR             ")
    print("=" * 40)
    print("1. Basic Operations (+, -, *, /)")
    print("2. Scientific Functions")
    print("3. Unit Converter")
    print("4. Graphing ")
    print("5. Program ")
    print("6. Percentage Calculator")
    print("7. View History")
    print("8. Clear History")
    print("9. Exit")
    print("=" * 40)

def basic_op():
    print("\n--- BASIC OPERATIONS ---")
    try:
        operator = input("Enter operator (+, -, *, /):")
        numbers = input("Enter numbers : ")
        numbers = list(map(float, numbers.split(operator)))
        if operator == "+":
            result = sum(numbers)
        elif operator == "-":
            result = numbers[0]
            for n in numbers[1:]:
                result -= n

        elif operator == "*":
            result = 1
            for n in numbers:
                result *= n

        elif operator == "/":
            result = numbers[0]
            for n in numbers[1:]:
                result /= n
        else:
            print("⚠️ Invalid operator!")
            return None

        print(f"Result = {result}")
        history.append(f"{' '.join(map(str, numbers))} {operator} = {result}")
        return result
    except ZeroDivisionError:
        print("⚠️ Cannot divide by zero!")
        return None
    except ValueError:
        print("Please enter valid numbers!")
    except Exception as e:
        print("⚠️ Error:", e)
        return None



def scientific_functions():
        print("\n--- SCIENTIFIC FUNCTIONS ---")
        print("1. Square Root")
        print("2. Power (x^y)")
        print("3. Factorial")
        print("4. Sine, Cosine, Tangent")
        print("5. Logarithm")

        try:
            choice = input("Choose function (1-5): ")

            if choice == "1":
                num = float(input("Enter number: "))
                if num < 0:
                    print("Cannot calculate square root of negative number!")
                    return
                result = math.sqrt(num)
                calculation = f"√{num} = {result}"

            elif choice == "2":
                base = float(input("Enter base: "))
                exponent = float(input("Enter exponent: "))
                result = math.pow(base, exponent)
                calculation = f"{base}^{exponent} = {result}"

            elif choice == "3":
                num = int(input("Enter number: "))
                if num < 0:
                    print("Cannot calculate factorial of negative number!")
                    return
                result = math.factorial(num)
                calculation = f"{num}! = {result}"

            elif choice == "4":
                num = float(input("Enter angle in degrees: "))
                radians = math.radians(num)
                sin_val = math.sin(radians)
                cos_val = math.cos(radians)
                tan_val = math.tan(radians)
                print(f"Sin({num}°) = {sin_val:.4f}")
                print(f"Cos({num}°) = {cos_val:.4f}")
                print(f"Tan({num}°) = {tan_val:.4f}")
                calculation = f"Trig functions for {num}° calculated"
                result = "See above"

            elif choice == "5":
                num = float(input("Enter number: "))
                if num <= 0:
                    print("Logarithm only works for positive numbers!")
                    return
                result = math.log10(num)
                calculation = f"log10({num}) = {result}"

            else:
                print("Invalid choice!")
                return

            history.append(calculation)
            if choice != "4":
                print(f"Result: {result}")

        except ValueError:
            print("Please enter valid numbers!")

        if input("do you want to move to advanced scientific functions?(y/n):  ").lower() == "y":
            def advanced_scientific_functions():
                print("\n--- ADVANCED SCIENTIFIC FUNCTIONS ---")
                print("1. Square Root (sum of multiple square roots allowed)")
                print("2. Power (x^y) (sum of multiple powers allowed)")
                print("3. Factorial (sum of factorials allowed)")
                print("4. Sine, Cosine, Tangent (one angle per choice)")
                print("5. Logarithm (sum of multiple logs allowed)")
                print("6. Advanced (mix any functions and operators)")

                allowed_funcs = {
                    'sqrt': math.sqrt,
                    'pow': math.pow,
                    'factorial': math.factorial,
                    'log': math.log10,
                    'sin': lambda x: math.sin(math.radians(x)),
                    'cos': lambda x: math.cos(math.radians(x)),
                    'tan': lambda x: math.tan(math.radians(x))
                }

                try:
                    choice = input("Choose function (1-6): ").strip()

                    if choice == "1":  # Square Root sum
                        expr = input("Enter sum of square roots (e.g., sqrt(16)+sqrt(25)): ").replace("^", "**")
                        result = eval(expr, {"__builtins__": None}, allowed_funcs)
                        calculation = f"Square Root sum: {expr} = {result}"

                    elif choice == "2":  # Power sum
                        expr = input("Enter sum of powers (e.g., 2^2+3^3): ").replace("^", "**")
                        result = eval(expr, {"__builtins__": None}, allowed_funcs)
                        calculation = f"Power sum: {expr} = {result}"

                    elif choice == "3":  # Factorial sum
                        expr = input("Enter sum of factorials (e.g., factorial(3)+factorial(4)): ")
                        result = eval(expr, {"__builtins__": None}, allowed_funcs)
                        calculation = f"Factorial sum: {expr} = {result}"

                    elif choice == "4":  # Trig
                        expr = input("Enter your trig expression (e.g., sin(60)+cos(45)): ").replace("^", "**")
                        result = eval(expr, {"__builtins__": None}, allowed_funcs)
                        calculation = f"Trig expression: {expr} = {result}"

                    elif choice == "5":  # Log sum
                        expr = input("Enter sum of logs (e.g., log(10)+log(100)): ")
                        result = eval(expr, {"__builtins__": None}, allowed_funcs)
                        calculation = f"Log sum: {expr} = {result}"

                    elif choice == "6":  # Advanced mixed expressions
                        print("\n--- ADVANCED MODE ---")
                        print("You can mix any functions: sqrt(), pow(), factorial(), sin(), cos(), tan(), log()")
                        print("Example: sqrt(16)+5^2+factorial(3)")
                        expr = input("Enter your advanced expression: ").replace("^", "**")
                        result = eval(expr, {"__builtins__": None}, allowed_funcs)
                        calculation = f"Final calculation: {expr} = {result}"

                    else:
                        print("Invalid choice!")
                        return

                    # Save to history and print result
                    history.append(calculation)

                    print(f"Result: {result}")

                except ZeroDivisionError:
                    print("⚠️ Division by zero is not allowed!")
                except Exception as e:
                    print("⚠️ Error:", e)
            advanced_scientific_functions()
        else:
            print("what do you want to do next:")
            menu()


def unit_converter():
    print("\n--- UNIT CONVERTER ---")
    print("1. Temperature ")
    print("2. Distance ")
    print("3. volume ")
    print("4. weight")
    print("5. currency ")
    print("6. energy ")
    print("7. area")
    print("8. speed")
    print("9. time")
    print("10. power")
    print("11. data")
    print("12. pressure")
    print("13. angles")

    choice = input("Choose conversion (1-13): ")

    try:
       if choice == "1":

            # Ask for input temperature with unit
            user_input = input("Enter temperature with unit (e.g., 36 C, 100 F, 0 K): ").strip()

            temp_str = ''.join([c for c in user_input if c.isdigit() or c == '.' or c == '-'])
            unit_str = ''.join([c for c in user_input if c.isalpha()])

            if not temp_str or not unit_str:
                print("Invalid input! Format: <number><unit> (C/F/K)")
                return

            temp = float(temp_str)
            in_unit = unit_str.upper()

            # Ask for target unit
            target_unit = input("Enter unit to convert to (C/F/K): ").strip().upper()

            if in_unit == target_unit:
                print(f"Input and target units are the same. Temperature remains {temp}°{in_unit}")
                return

            # Convert input to Celsius first
            if in_unit == "C":
                celsius = temp
            elif in_unit == "F":
                celsius = (temp - 32) * 5/9
            elif in_unit == "K":
                celsius = temp - 273.15
            else:
                print("Invalid input unit! Use C, F, or K.")
                return

            # Convert Celsius to target unit
            if target_unit == "C":
                result = celsius
            elif target_unit == "F":
                result = (celsius * 9/5) + 32
            elif target_unit == "K":
                result = celsius + 273.15
            else:
                print("Invalid target unit! Use C, F, or K.")


            print(f"{temp}°{in_unit} = {result:.2f}°{target_unit}")

       elif choice == "2":
            print("\n--- LENGTH CONVERTER ---")
            length_inputs = {
                'angstrom': 1e-10,
                'ang': 1e-10,
                'nm': 1e-9,
                'nanometer': 1e-9,
                'micron': 1e-6,
                'um': 1e-6,
                'mm': 0.001,
                'millimeter': 0.001,
                'cm': 0.01,
                'centimeter': 0.01,
                'm': 1,
                'meter': 1,
                'km': 1000,
                'kilometer': 1000,
                'inch': 0.0254,
                'in': 0.0254,
                'ft': 0.3048,
                'foot': 0.3048,
                'yd': 0.9144,
                'yard': 0.9144,
                'mile': 1609.344,
                'mi': 1609.344,
                'nmi': 1852,
                'nauticalmile': 1852
            }
            print("Available units:")
            for unit in length_inputs:
                print(f"  - {unit}")

            try:
                # Step 1: number
                value_2 = float(input("Enter the numeric value: "))

                # Step 2: current unit
                input_unit = input(
                    "Enter the current unit of the number (e.g. ang, nm, um, mm, cm, m, km, inch, ft, yd, mile, nmi): ").strip().lower()

                # Step 3: target unit
                target_unit = input("Enter the unit to convert to: ").strip().lower()

                if input_unit not in length_inputs:
                    print("Unsupported input unit!")
                    return
                if target_unit not in length_inputs:
                    print("Unsupported target unit!")
                    return

                # Convert value to meters first
                value_in_meters = value_2 * length_inputs[input_unit]

                # Convert meters to target unit
                converted_value = value_in_meters / length_inputs[target_unit]

                print(f"{value_2} {input_unit} = {converted_value:.10e} {target_unit}")
                history.append(f"{value_2} {input_unit} = {converted_value:.10e} {target_unit}")
            except ValueError:
                print("Please enter a valid number.")

       elif choice == "3":
           print("\n--- VOLUME CONVERTER ---")
           volume_imputs = {
               "ml": 0.001,  # Milliliters
               "cm³": 0.001,  # Cubic centimeters
               "l": 1.0,  # Liters
               "m³": 1000.0,  # Cubic meters
               "tsp": 0.00492892,  # US Teaspoons
               "tbsp": 0.0147868,  # US Tablespoons
               "fl_oz": 0.0295735,  # US Fluid ounces
               "cup": 0.24,  # US Cups
               "pt": 0.473176,  # US Pints
               "qt": 0.946353,  # US Quarts
               "gal": 3.78541,  # US Gallons
               "in³": 0.0163871,  # Cubic inches
               "ft³": 28.3168,  # Cubic feet
               "yd³": 764.555,  # Cubic yards
               "tsp_uk": 0.00591939,  # UK Teaspoons
               "tbsp_uk": 0.0177582,  # UK Tablespoons
               "fl_oz_uk": 0.0284131,  # UK Fluid ounces
               "pt_uk": 0.568261,  # UK Pints
               "qt_uk": 1.13652,  # UK Quarts
               "gal_uk": 4.54609  # UK Gallons
           }
           print("Available units:")
           for unit in volume_imputs:
               print(f"  - {unit}")

           try:
                value_2 = float(input("Enter the numeric value: "))
                input_unit=input("Enter the current unit of the number (e.g. ml, cm³, L, m³, tsp, tbsp, fl_oz, cup, pints, qt, qt, gal, in³, ft³, yd³, tsp_uk, tbsp_uk, fl_oz_uk, pt_uk, qt_uk,  gal_uk ): ").strip().lower()
                target_unit = input("Enter the unit to convert to: ").strip().lower()

                if input_unit not in volume_imputs:
                    print("Unsupported input unit!")
                    return
                if target_unit not in volume_imputs:
                    print("Unsupported target unit!")
                    return

                # Convert value to meters first
                value_in_litres = value_2 * volume_imputs[input_unit]

                # Convert meters to target unit
                converted_value = value_in_litres / volume_imputs[target_unit]

                print(f"{value_2} {input_unit} = {converted_value:.2f} {target_unit}")
                history.append(f"{value_2} {input_unit} = {converted_value:.2f} {target_unit}")
           except ValueError:
               print("Please enter a valid number.")

       elif choice == "4":
           print("\n--- WEIGHT CONVERTER ---")
           weight_inputs = {
               "ct": 0.2,  # Carats
               "carat": 0.2,
               "mg": 0.001,  # Milligrams
               "milligram": 0.001,
               "cg": 0.01,  # Centigrams
               "centigram": 0.01,
               "dg": 0.1,  # Decigrams
               "decigram": 0.1,
               "g": 1.0,  # Grams
               "gram": 1.0,
               "dag": 10.0,  # Dekagrams
               "dekagram": 10.0,
               "hg": 100.0,  # Hectograms
               "hectogram": 100.0,
               "kg": 1000.0,  # Kilograms
               "kilogram": 1000.0,
               "t": 1000000.0,  # Metric tonnes
               "tonne": 1000000.0,
               "oz": 28.3495,  # Ounces
               "ounce": 28.3495,
               "lb": 453.592,  # Pounds
               "pound": 453.592,
               "st": 6350.29,  # Stone
               "stone": 6350.29,
               "ton_us": 907184.74,  # Short tons (US)
               "shortton": 907184.74
           }
           print("Available units:")
           for unit in weight_inputs:
               print(f"  - {unit}")

           try:
                value_3 = float(input("Enter the numeric value: "))
                input_unit = input(
                    "Enter the current unit of the number (e.g. ct, mg, cg, dg, g, dag, hg, kg, t, oz, lb, st, ton_us  ): ").strip().lower()
                target_unit = input("Enter the unit to convert to: ").strip().lower()

                if input_unit not in weight_inputs:
                    print("Unsupported input unit!")
                    return
                if target_unit not in weight_inputs:
                    print("Unsupported target unit!")
                    return

                # Convert value to meters first
                value_in_litres = value_3 * weight_inputs[input_unit]

                # Convert meters to target unit
                converted_value = value_in_litres / weight_inputs[target_unit]

                print(f"{value_3} {input_unit} = {converted_value} {target_unit}")
                history.append(f"{value_3} {input_unit} = {converted_value} {target_unit}")
           except ValueError:
                    print("Please enter a valid number.")


       elif choice == "5":
           print("\n--- CURRENT CONVERTER ---")
           c = CurrencyRates()
           b = BtcConverter()

            # Create a dictionary of currency names and their codes for display
           currency_names = {
                'AFN': 'Afghan Afghani', 'ALL': 'Albanian Lek', 'DZD': 'Algerian Dinar',
                'AOA': 'Angolan Kwanza', 'ARS': 'Argentine Peso', 'AMD': 'Armenian Dram',
                'AWG': 'Aruban Florin', 'AUD': 'Australian Dollar', 'AZN': 'Azerbaijani Manat',
                'BSD': 'Bahamian Dollar', 'BHD': 'Bahraini Dinar', 'BBD': 'Bajan Dollar',
                'BDT': 'Bangladeshi Taka', 'BYN': 'Belarusian Ruble', 'BZD': 'Belize Dollar',
                'BMD': 'Bermuda Dollar', 'BTN': 'Bhutanese Ngultrum', 'BOB': 'Bolivian Boliviano',
                'BAM': 'Bosnia-Herzegovina Convertible Mark', 'BWP': 'Botswana Pula', 'BRL': 'Brazilian Real',
                'BND': 'Brunei Dollar', 'BGN': 'Bulgarian Lev', 'BIF': 'Burundian Franc',
                'XPF': 'CFP Franc', 'KHR': 'Cambodian Riel', 'CAD': 'Canadian Dollar',
                'CVE': 'Cape Verdean Escudo', 'ANG': 'Caribbean Guilder', 'KYD': 'Cayman Islands Dollar',
                'XAF': 'Central African CFA Franc', 'CLP': 'Chilean Peso', 'CNY': 'Chinese Yuan',
                'COP': 'Colombian Peso', 'KMF': 'Comorian Franc', 'CDF': 'Congolese Franc',
                'CRC': 'Costa Rican Colón', 'CUP': 'Cuban Peso', 'CZK': 'Czech Koruna',
                'DKK': 'Danish Krone', 'DJF': 'Djiboutian Franc', 'DOP': 'Dominican Peso',
                'XCD': 'East Caribbean Dollar', 'EGP': 'Egyptian Pound', 'ETB': 'Ethiopian Birr',
                'EUR': 'Euro', 'FJD': 'Fijian Dollar', 'GMD': 'Gambian Dalasi',
                'GEL': 'Georgian Lari', 'GHS': 'Ghanaian Cedi', 'GTQ': 'Guatemalan Quetzal',
                'GNF': 'Guinean Franc', 'HTG': 'Haitian Gourde', 'HNL': 'Honduran Lempira',
                'HKD': 'Hong Kong Dollar', 'HUF': 'Hungarian Forint', 'ISK': 'Icelandic Króna',
                'INR': 'Indian Rupee', 'IDR': 'Indonesian Rupiah', 'IRR': 'Iranian Rial',
                'IQD': 'Iraqi Dinar', 'ILS': 'Israeli New Shekel', 'JMD': 'Jamaican Dollar',
                'JPY': 'Japanese Yen', 'JOD': 'Jordanian Dinar', 'KZT': 'Kazakhstani Tenge',
                'KES': 'Kenyan Shilling', 'KWD': 'Kuwaiti Dinar', 'KGS': 'Kyrgystani Som',
                'LAK': 'Laotian Kip', 'LBP': 'Lebanese Pound', 'LSL': 'Lesotho Loti',
                'LRD': 'Liberian Dollar', 'LYD': 'Libyan Dinar', 'MOP': 'Macanese Pataca',
                'MKD': 'Macedonian Denar', 'MGA': 'Malagasy Ariary', 'MWK': 'Malawian Kwacha',
                'MYR': 'Malaysian Ringgit', 'MVR': 'Maldivian Rufiyaa', 'MRO': 'Mauritanian Ouguiya',
                'MUR': 'Mauritian Rupee', 'MXN': 'Mexican Peso', 'MDL': 'Moldovan Leu',
                'MAD': 'Moroccan Dirham', 'MZN': 'Mozambican Metical', 'MMK': 'Myanmar Kyat',
                'NAD': 'Namibian Dollar', 'NPR': 'Nepalese Rupee', 'NZD': 'New Zealand Dollar',
                'NIO': 'Nicaraguan Córdoba', 'NGN': 'Nigerian Naira', 'NOK': 'Norwegian Krone',
                'OMR': 'Omani Rial', 'PKR': 'Pakistani Rupee', 'PAB': 'Panamanian Balboa',
                'PGK': 'Papua New Guinean Kina', 'PYG': 'Paraguayan Guarani', 'PHP': 'Philippine Peso',
                'PLN': 'Polish Złoty', 'GBP': 'Pound Sterling', 'QAR': 'Qatari Riyal',
                'RON': 'Romanian Leu', 'RUB': 'Russian Ruble', 'RWF': 'Rwandan Franc',
                'SAR': 'Saudi Riyal', 'RSD': 'Serbian Dinar', 'SCR': 'Seychellois Rupee',
                'SLL': 'Sierra Leonean Leone', 'SGD': 'Singapore Dollar', 'SBD': 'Solomon Islands Dollar',
                'SOS': 'Somali Shilling', 'ZAR': 'South African Rand', 'KRW': 'South Korean Won',
                'VEF': 'Sovereign Bolivar', 'XDR': 'Special Drawing Rights', 'LKR': 'Sri Lankan Rupee',
                'SHP': 'St. Helena Pound', 'SDG': 'Sudanese Pound', 'SRD': 'Suriname Dollar',
                'SZL': 'Swazi Lilangeni', 'SEK': 'Swedish Krona', 'CHF': 'Swiss Franc',
                'TJS': 'Tajikistani Somoni', 'TZS': 'Tanzanian Shilling', 'THB': 'Thai Baht',
                'TOP': 'Tongan Pa\'anga', 'TTD': 'Trinidad & Tobago Dollar', 'TND': 'Tunisian Dinar',
                'TRY': 'Turkish Lira', 'TMT': 'Turkmenistani Manat', 'UGX': 'Ugandan Shilling',
                'UAH': 'Ukrainian Hryvnia', 'AED': 'United Arab Emirates Dirham', 'USD': 'United States Dollar',
                'UYU': 'Uruguayan Peso', 'UZS': 'Uzbekistani Som', 'VND': 'Vietnamese Dong',
                'XOF': 'West African CFA franc', 'YER': 'Yemeni Rial', 'ZMW': 'Zambian Kwacha'
            }

            # Print a list of available currencies
           print("Available currencies:")
           for code, name in sorted(currency_names.items()):
                print(f"  - {code}: {name}")

           try:
                # Step 1: Get the numeric value
                value = float(input("\nEnter the amount you want to convert: "))

                # Step 2: Get the currency to convert from
                from_currency = input("Enter the currency code to convert from (e.g., USD, EUR): ").strip().upper()

                # Step 3: Get the target currency
                to_currency = input("Enter the currency code to convert to (e.g., JPY, GBP): ").strip().upper()

                # Check for invalid currency codes
                if from_currency not in currency_names:
                    print(f"Error: '{from_currency}' is not a valid currency code.")
                    return
                if to_currency not in currency_names:
                    print(f"Error: '{to_currency}' is not a valid currency code.")
                    return

                # Perform the conversion
                try:
                    converted_value = c.convert(from_currency, to_currency, value)
                    print(f"\n{value} {from_currency} is equal to {converted_value:.2f} {to_currency}.")
                except Exception as e:
                    print(f"Error during conversion: {e}. The API may be unavailable or an invalid currency was entered.")

           except ValueError:
                print("Please enter a valid numeric value.")


       elif choice == "6":
           print("\n--- ENERGY CONVERTER ---")
           energy_units = {
                "eV": 1.60218e-19,  # Electron volt
                "J": 1,  # Joule
                "kJ": 1e3,  # Kilojoule
                "cal": 4.184,  # Thermal calorie
                "kcal": 4184,  # Food calorie (kilocalorie)
                "ft-lb": 1.35582,  # Foot-pound
                "BTU": 1055.06,  # British thermal unit
                "kWh": 3.6e6  # Kilowatt-hour
            }

            # Print available units
           print("Available units:")
           for unit in energy_units:
                print(f"  - {unit}")

           try:
                # Step 1: Get numeric value
                value = float(input("\nEnter the numeric value: "))

                # Step 2: Get source unit
                from_unit = input("Enter the current unit: ").strip()

                # Step 3: Get target unit
                to_unit = input("Enter the unit to convert to: ").strip()

                # Check if units are valid
                if from_unit not in energy_units:
                    print(f"Error: '{from_unit}' is not a valid unit.")
                    return
                if to_unit not in energy_units:
                    print(f"Error: '{to_unit}' is not a valid unit.")
                    return

                # Convert to Joules first, then to target unit
                value_in_joules = value * energy_units[from_unit]
                converted_value = value_in_joules / energy_units[to_unit]

                # Print result
                print(f"\n{value} {from_unit} = {converted_value:.6g} {to_unit}")

           except ValueError:
                print("Please enter a valid numeric value.")



       elif choice == "7" :
           print("\n--- AREA CONVERTER ---")

            # Conversion factors (all relative to square meters)
           area_units = {
                "mm2": 1e-6,  # Square millimeter
                "cm2": 1e-4,  # Square centimeter
                "m2": 1,  # Square meter
                "ha": 1e4,  # Hectare
                "km2": 1e6,  # Square kilometer
                "in2": 0.00064516,  # Square inch
                "ft2": 0.092903,  # Square foot
                "yd2": 0.836127,  # Square yard
                "acre": 4046.86,  # Acre
                "mi2": 2.59e6  # Square mile
            }

            # Print available units
           print("Available units:")
           for unit in area_units:
                print(f"  - {unit}")

           try:
                # Step 1: Get numeric value
                value = float(input("\nEnter the numeric value: "))

                # Step 2: Get source unit
                from_unit = input("Enter the current unit: ").strip()

                # Step 3: Get target unit
                to_unit = input("Enter the unit to convert to: ").strip()

                # Check if units are valid
                if from_unit not in area_units:
                    print(f"Error: '{from_unit}' is not a valid unit.")
                    return
                if to_unit not in area_units:
                    print(f"Error: '{to_unit}' is not a valid unit.")
                    return

                # Convert to square meters first, then to target unit
                value_in_sq_meters = value * area_units[from_unit]
                converted_value = value_in_sq_meters / area_units[to_unit]

                # Print result
                print(f"\n{value} {from_unit} = {converted_value:.6g} {to_unit}")

           except ValueError:
                print("Please enter a valid numeric value.")


       elif choice == "8" :
           print("\n--- SPEED CONVERTER ---")
           speed_units = {
                "cm/s": 0.01,  # centimeters per second
                "m/s": 1.0,  # meters per second (base unit)
                "km/h": 0.277778,  # kilometers per hour
                "ft/s": 0.3048,  # feet per second
                "mph": 0.44704,  # miles per hour
                "knot": 0.514444,  # nautical miles per hour
                "mach": 343.0  # approx at sea level (m/s)
            }
           print("Available units:")
           for unit in speed_units:
               print(f"  - {unit}")
           try:
           # Step 1: get numeric input
               value = float(input("Enter the numeric value: "))

                # Step 2: get input unit
               input_unit = input(
                    "Enter the current unit of the number (e.g. cm/s, m/s, km/h, ft/s, mph, knot, mach): "
                ).strip().lower()

                # Step 3: get target unit
               target_unit = input("Enter the unit to convert to: ").strip().lower()
               if input_unit not in speed_units:
                    print("Unsupported input unit!")
                    return
               if target_unit not in speed_units:
                    print("Unsupported target unit!")
                    return

                        # Convert value to base unit (m/s)
               value_in_mps = value * speed_units[input_unit]

                        # Convert from m/s to target unit
               converted_value = value_in_mps / speed_units[target_unit]

                        # Print result with clean formatting
               print(f"{value} {input_unit} = {converted_value:.6g} {target_unit}")

                        # If you're keeping history, append it
                        # history.append(f"{value} {input_unit} = {converted_value:.6g} {target_unit}")

           except ValueError:
                    print("Please enter a valid number.")




       elif choice == "9" :
           print("\n--- TIME CONVERTER ---")

            # Time units in seconds
           time_units = {
                "microseconds": 1e-6,
                "us": 1e-6,
                "milliseconds": 1e-3,
                "ms": 1e-3,
                "seconds": 1,
                "sec": 1,
                "minutes": 60,
                "min": 60,
                "hours": 3600,
                "hrs": 3600,
                "days": 86400,
                "weeks": 604800,
                "years": 31536000  # ignoring leap years
            }

            # Print available units
           print("Available units:")
           for unit in time_units:
                print(f"  - {unit}")

           try:
                # Step 1: Get numeric value
                value = float(input("\nEnter the numeric value: "))

                # Step 2: Get source unit
                from_unit = input("Enter the current unit: ").strip().lower()

                # Step 3: Get target unit
                to_unit = input("Enter the unit to convert to: ").strip().lower()

                # Check if units are valid
                if from_unit not in time_units:
                    print(f"Error: '{from_unit}' is not a valid unit.")
                elif to_unit not in time_units:
                    print(f"Error: '{to_unit}' is not a valid unit.")
                else:
                    # Convert to seconds first, then to target unit
                    value_in_seconds = value * time_units[from_unit]
                    converted_value = value_in_seconds / time_units[to_unit]

                    # Print result
                    print(f"\n{value} {from_unit} = {converted_value:.6g} {to_unit}")

           except ValueError:
                print("Please enter a valid numeric value.")

       elif choice == "10":
           print("\n--- POWER CONVERTER ---")

            # Power units in Watts
           power_units = {
                "watts": 1,
                "w": 1,
                "kilowatts": 1e3,
                "kwh": 1e3,
                "horsepower": 745.7,
                "hp": 745.7,   # US mechanical HP
                "ft-lb/min": 0.022597,  # 1 ft-lb/min = 0.022597 W
                "btu/min": 17.5843  # 1 BTU/min = 17.5843 W
            }

            # Print available units
           print("Available units:")
           for unit in power_units:
                print(f"  - {unit}")

           try:
                # Step 1: Get numeric value
                value = float(input("\nEnter the numeric value: "))

                # Step 2: Get source unit
                from_unit = input("Enter the current unit: ").strip().lower()

                # Step 3: Get target unit
                to_unit = input("Enter the unit to convert to: ").strip().lower()

                # Check if units are valid
                if from_unit not in power_units:
                    print(f"Error: '{from_unit}' is not a valid unit.")
                elif to_unit not in power_units:
                    print(f"Error: '{to_unit}' is not a valid unit.")
                else:
                    # Convert to Watts first, then to target unit
                    value_in_watts = value * power_units[from_unit]
                    converted_value = value_in_watts / power_units[to_unit]

                    # Print result
                    print(f"\n{value} {from_unit} = {converted_value:.6g} {to_unit}")

           except ValueError:
                print("Please enter a valid numeric value.")


       elif choice == "11":
            print("\n--- DATA CONVERTER ---")
            data_units = {
                "bit": 1,
                "nibble": 4,
                "byte": 8,

                # SI Units (10^3)
                "kb": 1e3,
                "mb": 1e6,
                "gb": 1e9,
                "tb": 1e12,
                "pb": 1e15,
                "eb": 1e18,
                "zb": 1e21,
                "yb": 1e24,

                # Binary Units (2^10)
                "kib": 1024,
                "mib": 1024 ** 2,
                "gib": 1024 ** 3,
                "tib": 1024 ** 4,
                "pib": 1024 ** 5,
                "eib": 1024 ** 6,
                "zib": 1024 ** 7,
                "yib": 1024 ** 8,

                # Bytes versions (just divide bits by 8)
                "kB": 8e3,
                "MB": 8e6,
                "GB": 8e9,
                "TB": 8e12,
                "PB": 8e15,
                "EB": 8e18,
                "ZB": 8e21,
                "YB": 8e24,

                "KiB": 8 * 1024,
                "MiB": 8 * 1024 ** 2,
                "GiB": 8 * 1024 ** 3,
                "TiB": 8 * 1024 ** 4,
                "PiB": 8 * 1024 ** 5,
                "EiB": 8 * 1024 ** 6,
                "ZiB": 8 * 1024 ** 7,
                "YiB": 8 * 1024 ** 8,
            }
            print("Available units:")
            for unit in data_units:
                print(f"  - {unit}")

            try:
                # Step 1: numeric input
                value = float(input("Enter the numeric value: "))

                # Step 2: input unit
                input_unit = input(
                    "Enter the current unit of the number (e.g. bit, nibble, byte): "
                ).strip().lower()

                # Step 3: target unit
                target_unit = input("Enter the unit to convert to: ").strip().lower()
                if input_unit not in data_units:
                    print(f"Error!{input_unit} is not a valid unit.")

                if target_unit not in data_units:
                    print(f"Error!{target_unit} is not a valid unit.")




                else:

                    # Convert to base unit (bits)
                    value_in_bits = value * data_units[input_unit]

                    # Convert to target unit
                    converted_value = value_in_bits / data_units[target_unit]

                    # Print result
                    print(f"{value} {input_unit} = {converted_value:.6g} {target_unit}")

            # If you're tracking history
            # history.append(f"{value} {input_unit} = {converted_value:.6g} {target_unit}")

            except ValueError:
                print("Please enter a valid number.")


       elif choice == "12":
            print("\n--- PRESSURE CONVERTER ---")
            pressure_units = {
                "atm": 101325,  # Atmospheres
                "bar": 100000,  # Bars
                "kpa": 1000,  # Kilopascals
                "mmhg": 133.322,  # Millimeters of mercury
                "pa": 1,  # Pascals (base unit)
                "psi": 6894.76  # Pounds per square inch
            }
            print("Available units:")
            for unit in pressure_units:
                print(f"  - {unit}")
            try:
                # Step 1: number
                value = float(input("Enter the numeric value: "))

                # Step 2: current unit
                input_unit = input(
                    "Enter the current unit of the number : "
                ).strip().lower()

                # Step 3: target unit
                target_unit = input("Enter the unit to convert to : ").strip().lower()
                if input_unit not in pressure_units:
                    print(f"Error!{input_unit} is not a valid unit.")
                    return
                if target_unit not in pressure_units:
                    print(f"Error!{target_unit} is not a valid unit.")
                    return

                    # Step 4: Convert input value → Pascals
                value_in_pa = value * pressure_units[input_unit]

                # Step 5: Convert Pascals → target unit
                converted_value = value_in_pa / pressure_units[target_unit]

                # Step 6: Print result
                print(f"{value} {input_unit} = {converted_value:.6g} {target_unit}")

            except ValueError:
                print("Please enter a valid number.")




       elif choice == "13":
            print("\n--- ANGLE CONVERTER ---")
            angle_units = {
                "deg": math.pi / 180,  # Degrees → Radians
                "rad": 1,  # Radians (base)
                "grad": math.pi / 200  # Gradians → Radians
            }
            print("Available units:")
            for unit in angle_units:
                print(f"  - {unit}")
            try:
                # Step 1: number
                value = float(input("Enter the numeric value: "))

                # Step 2: current unit
                input_unit = input(
                    "Enter the current unit of the number (deg, rad, grad): "
                ).strip().lower()

                # Step 3: target unit
                target_unit = input("Enter the unit to convert to (deg, rad, grad): ").strip().lower()
                if input_unit not in angle_units:
                    print("Unsupported input unit!")
                    return
                if target_unit not in angle_units:
                    print("Unsupported target unit!")
                    return

                # Step 4: Convert input value → radians
                value_in_rad = value * angle_units[input_unit]

                # Step 5: Convert radians → target unit
                converted_value = value_in_rad / angle_units[target_unit]

                # Step 6: Print result
                print(f"{value} {input_unit} = {converted_value:.6g} {target_unit}")

            except ValueError:
                print("Please enter a valid number.")
    except Exception as e:
        print("⚠️ Error:", e)

def grapphing():
    print("="*30)
    print("\n--------- GRAPHING -----------")
    print()
    print("=" * 30)

    def fix_functions(expr_str):
        """
        Fix cases like 'sin 45' -> 'sin(45)', 'cos x' -> 'cos(x)'.
        """
        expr_str = re.sub(r'\b(sin|cos|tan|cot|sec|csc|log|ln|exp)\s*([0-9x\(])', r'\1(\2', expr_str)
        # Add closing parenthesis if missing
        # Only if it's not already properly closed
        open_parens = expr_str.count("(")
        close_parens = expr_str.count(")")
        if open_parens > close_parens:
            expr_str += ")" * (open_parens - close_parens)
        return expr_str

    def multi_graph_and_diff():
        x = sp.symbols('x')
        functions = []

        print("Enter functions of x (e.g., sin(x), cos 45, x**2+3*x+2).")
        print("Type 'done' when finished.\n")

        # Collect functions
        while True:
            expr_str = input("Enter function: ").strip()
            if expr_str.lower() == "done":
                break
            try:
                expr_str = fix_functions(expr_str)  # Auto-fix missing parentheses
                expr = sp.sympify(expr_str)
                derivative = sp.diff(expr, x)
                functions.append((expr, derivative))
                print(f"✅ Added f(x) = {expr}, f'(x) = {derivative}\n")
            except Exception as e:
                print(f"⚠️ Error: {e}\n")

        if not functions:
            print("No functions entered. Exiting...")
            return

        # Plotting
        x_vals = np.linspace(-10, 10, 1000)
        plt.figure(figsize=(10, 6))

        for i, (expr, derivative) in enumerate(functions, start=1):
            if expr.has(x):
                f = sp.lambdify(x, expr, modules=['numpy'])
                y_vals = f(x_vals)
            else:
                const_val = float(expr.evalf())
                y_vals = np.full_like(x_vals, const_val)

            plt.plot(x_vals, y_vals, label=f"f{i}(x) = {expr}")

        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Graphs of Entered Functions")
        plt.legend()
        plt.grid(True)
        plt.show()

    # Run the program
    multi_graph_and_diff()


def programming():
    print("=" * 30)
    print("\n-------- PROGRAMMING ---------")
    print()
    print("=" * 30)

    def converter():
        while True:
            print("\n--- Number System Converter ---")
            print("1. Decimal to Binary / Octal / Hexadecimal")
            print("2. Binary to Decimal / Octal / Hexadecimal")
            print("3. Octal to Decimal / Binary / Hexadecimal")
            print("4. Hexadecimal to Decimal / Binary / Octal")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                try:
                    dec = int(input("Enter a Decimal number: "))
                    print("Binary      :", bin(dec)[2:])
                    print("Octal       :", oct(dec)[2:])
                    print("Hexadecimal :", hex(dec)[2:].upper())
                except ValueError:
                    print("Error: Invalid decimal number!")
                except Exception as e:
                    print(f"⚠️ Unexpected error: {e}")

            elif choice == "2":
                binary = input("Enter a Binary number: ")
                try:
                    dec = int(binary, 2)
                    print("Decimal     :", dec)
                    print("Octal       :", oct(dec)[2:])
                    print("Hexadecimal :", hex(dec)[2:].upper())
                except ValueError:
                    print("Error: Invalid binary number! Use only 0 and 1.")
                except Exception as e:
                    print(f"⚠️ Unexpected error: {e}")

            elif choice == "3":
                octal = input("Enter an Octal number: ")
                try:
                    dec = int(octal, 8)
                    print("Decimal     :", dec)
                    print("Binary      :", bin(dec)[2:])
                    print("Hexadecimal :", hex(dec)[2:].upper())
                except ValueError:
                    print("Error: Invalid octal number! Use digits 0-7.")
                except Exception as e:
                    print(f"⚠️ Unexpected error: {e}")

            elif choice == "4":
                hexa = input("Enter a Hexadecimal number: ")
                try:
                    dec = int(hexa, 16)
                    print("Decimal     :", dec)
                    print("Binary      :", bin(dec)[2:])
                    print("Octal       :", oct(dec)[2:])
                except ValueError:
                    print("Error: Invalid hexadecimal number! Use digits 0-9 and letters A-F.")
                except Exception as e:
                    print(f"⚠️ Unexpected error: {e}")


            elif choice == "5":
                print("Exiting converter. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

    # Run the converter
    converter()

def date_calculator():
    print("=" * 30)
    print("\n------ DATA CALCULATOR -------")
    print()
    print("=" * 30)
    while True:
        print("\n--- Date Calculation Program ---")
        print("1. Difference between two dates ")
        print("2. Difference between two dates in hours/min/sec")
        print("3. Add days to a date")
        print("4. Subtract days from a date")
        print("5. Show today's date")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                date1_str = input("Enter first date (DD-MM-YYYY): ")
                date2_str = input("Enter second date (DD-MM-YYYY): ")
                date1 = datetime.strptime(date1_str, "%d-%m-%Y")
                date2 = datetime.strptime(date2_str, "%d-%m-%Y")
                diff = abs((date2 - date1).days)
                print(f"Difference: {diff} day(s)")
            except ValueError:
                print("Error: Please enter dates in the correct format (DD-MM-YY).")


        elif choice == "2":
            try:
                date1_str = input("Enter first date (DD-MM-YYYY HH:MM:SS): ")
                date2_str = input("Enter second date (DD-MM-YYYY HH:MM:SS): ")
                date1 = datetime.strptime(date1_str, "%d-%m-%Y %H:%M:%S")
                date2 = datetime.strptime(date2_str, "%d-%m-%Y %H:%M:%S")
                diff = abs(date2 - date1)
                total_seconds = diff.total_seconds()  # total seconds
                weeks = diff.days // 7
                days = diff.days % 7
                hours = int(total_seconds // 3600) % 24
                minutes = int(total_seconds // 60) % 60
                seconds = int(total_seconds % 60)
                microseconds = diff.microseconds

                # Display
                print(f"Difference is:")
                print(
                    f"{weeks} week(s), {days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s), {microseconds} microsecond(s)")


            except ValueError:
                print("Error: Please enter dates in the correct format (DD-MM-YYYY HH:MM:SS1).")

        elif choice == "3":
            try:
                date_str = input("Enter date (YYYY-MM-DD): ")
                days = int(input("Enter number of days to add: "))
                date = datetime.strptime(date_str, "%Y-%m-%d")
                new_date = date + timedelta(days=days)
                print(f"New date: {new_date.strftime('%Y-%m-%d')}")
            except ValueError:
                print("Error: Invalid input. Make sure the date is YYYY-MM-DD and days is a number.")

        elif choice == "4":
            try:
                date_str = input("Enter date (YYYY-MM-DD): ")
                days = int(input("Enter number of days to subtract: "))
                date = datetime.strptime(date_str, "%Y-%m-%d")
                new_date = date - timedelta(days=days)
                print(f"New date: {new_date.strftime('%Y-%m-%d')}")
            except ValueError:
                print("Error: Invalid input. Make sure the date is YYYY-MM-DD and days is a number.")

        elif choice == "5":
            today = datetime.today()
            print(f"Today's date: {today.strftime('%Y-%m-%d')}")

        elif choice == "6":
            print("Exiting Date Calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
def percentage_calculator():
    print("\n--- PERCENTAGE CALCULATOR ---")
    print("1. Find X% of a number")
    print("2. What % is X of Y?")
    print("3. Percentage increase/decrease")

    choice = input("Choose calculation (1-3): ")

    try:
        if choice == "1":
            percentage = float(input("Enter percentage: "))
            number = float(input("Enter number: "))
            result = (percentage / 100) * number
            calculation = f"{percentage}% of {number} = {result}"

        elif choice == "2":
            part = float(input("Enter the part: "))
            whole = float(input("Enter the whole: "))
            if whole == 0:
                print("Cannot divide by zero!")
                return
            result = (part / whole) * 100
            calculation = f"{part} is {result:.2f}% of {whole}"

        elif choice == "3":
            original = float(input("Enter original value: "))
            new = float(input("Enter new value: "))
            if original == 0:
                print("Original value cannot be zero!")
                return
            change = ((new - original) / original) * 100
            if change > 0:
                result = f"Increase of {change:.2f}%"
            else:
                result = f"Decrease of {abs(change):.2f}%"
            calculation = f"{original} → {new}: {result}"

        else:
            print("Invalid choice!")
            return

        history.append(calculation)
        print(f"Result: {calculation}")

    except ValueError:
        print("Please enter valid numbers!")
    if input("do you want to move to advanced scientific functions?(y/n):  ").lower() == "y":
        def advanced_percentage_calculator():
            while True:
                print("\n--- Percentage of Number Calculator ---")
                print("1. Add percentages")
                print("2. Subtract percentages")
                print("3. Multiply percentages")
                print("4. Divide percentages")
                print("5. scramble percentage operations")
                print("6. Exit")

                choice = input("Enter your choice: ")

                if choice in ["1", "2", "3", "4" ]:
                    try:
                        # Input in format: 10%100 20%50 5%200
                        entries = input("Enter percentages with numbers (e.g., 10%100 20%50): ").split()
                        values = []
                        for e in entries:
                            if "%" not in e:
                                raise ValueError("Invalid format! Use X%Y")
                            percent_str, num_str = e.split("%")
                            percent = float(percent_str)
                            num = float(num_str)
                            values.append(percent * num / 100)

                        if choice == "1":  # Add
                            result = sum(values)
                        elif choice == "2":  # Subtract
                            result = values[0]
                            for v in values[1:]:
                                result -= v
                        elif choice == "3":  # Multiply
                            result = 1
                            for v in values:
                                result *= v
                        elif choice == "4":  # Divide
                            result = values[0]
                            for v in values[1:]:
                                if v == 0:
                                    raise ZeroDivisionError
                                result /= v
                        print(f"Result: {result}")

                    except ZeroDivisionError:
                        print("Error: Division by zero!")
                    except ValueError as ve:
                        print(f"Error: {ve}")
                    except Exception as e:
                        print(f"⚠️ Unexpected error: {e}")



                elif choice == "5":
                            # Scramble Operations
                    expr = input("Enter expression (e.g., 10%100 + 44.7%234 - 5%50): ")

                    def replace_percentage(match):
                        percent = float(match.group(1))
                        number = float(match.group(2))
                        return f"({percent}/100*{number})"

                    expr = re.sub(r"(\d+\.?\d*)%(\d+\.?\d*)", replace_percentage, expr)

                    try:
                        result = eval(expr)
                        print(f"Result: {result}")
                    except ZeroDivisionError:
                            print("Error: Division by zero!")
                    except Exception:
                            print("Error: Invalid expression!")



                elif choice == "6":
                    print("Exiting Calculator. Goodbye!")
                    break
                else:
                    print("Invalid choice. Try again.")

    else:
        print("what do you want to do next: ")
        menu()

        # Run the program
def view_history():
    print("\n--- CALCULATION HISTORY ---")
    if not history:
        print("No calculations yet!")
        return

    for i, calc in enumerate(history, 1):
        print(f"{i}. {calc}")


def clear_history():
    global history
    confirm = input("Are you sure you want to clear history? (y/n): ").lower()
    if confirm == 'y':
        history.clear()
        print("History cleared!")
    else:
        print("History not cleared.")

def main():
    print("Welcome to Advanced Calculator!")

    while True:
        menu()
        choice = input("\nEnter your choice (1-9): ")

        if choice == "1":
            basic_op()
        elif choice == "2":
            scientific_functions()
        elif choice == "3":
            unit_converter()
        elif choice == "4":
            grapphing()
        elif choice == "5":
            programming()
        elif choice == "6":
            percentage_calculator()
        elif choice == "7":
            view_history()
        elif choice == "8":
            clear_history()
        elif choice == "9":
            print("Thank you for using Advanced Calculator!")
            break
        else:
            print("Invalid choice! Please choose 1-7.")

        input("\nPress Enter to continue...")



main()