talent = float(input("Enter the talent: "))
pound = float(input("Enter the pound: "))
lot = float(input("Enter the lot: "))
total_grams = lot * 13.3 + pound * 32 * 13.3 + talent * 20 * 32 * 13.3
kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print ("the weight in mordern unit is:  ", kilograms, "kilograms and", grams, "grams.")