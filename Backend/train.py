train_data = [
    # Food items
    ("BISCUITS", {"entities": [(0, 9, "FOOD")]}),
    ("BURGER", {"entities": [(0, 6, "FOOD")]}),
    ("PIZZA", {"entities": [(0, 5, "FOOD")]}),
    ("PASTA", {"entities": [(0, 5, "FOOD")]}),
    ("SALAD", {"entities": [(0, 5, "FOOD")]}),
    ("SOUP", {"entities": [(0, 4, "FOOD")]}),
    ("STEAK", {"entities": [(0, 5, "FOOD")]}),
    ("FRIES", {"entities": [(0, 5, "FOOD")]}),
    ("SANDWICH", {"entities": [(0, 8, "FOOD")]}),
    ("TACOS", {"entities": [(0, 5, "FOOD")]}),
    ("CHICKEN", {"entities": [(0, 7, "FOOD")]}),
    ("WINGS", {"entities": [(0, 5, "FOOD")]}),
    ("SUSHI", {"entities": [(0, 5, "FOOD")]}),
    ("CAESAR SALAD", {"entities": [(0, 12, "FOOD")]}),
    ("CUPCAKES", {"entities": [(0, 8, "FOOD")]}),
    ("BROWNIE", {"entities": [(0, 7, "FOOD")]}),
    ("CHEESECAKE", {"entities": [(0, 10, "FOOD")]}),
    ("BAGEL", {"entities": [(0, 5, "FOOD")]}),
    ("DONUT", {"entities": [(0, 5, "FOOD")]}),
    ("PASTRY", {"entities": [(0, 6, "FOOD")]}),
    ("CROISSANT", {"entities": [(0, 9, "FOOD")]}),
    ("MUFFIN", {"entities": [(0, 6, "FOOD")]}),
    ("OATMEAL", {"entities": [(0, 7, "FOOD")]}),
    ("PANCAKES", {"entities": [(0, 8, "FOOD")]}),
    ("WAFFLES", {"entities": [(0, 7, "FOOD")]}),
    ("EGGS", {"entities": [(0, 4, "FOOD")]}),
    ("BACON", {"entities": [(0, 5, "FOOD")]}),
    ("SAUSAGE", {"entities": [(0, 7, "FOOD")]}),
    ("HASH BROWNS", {"entities": [(0, 11, "FOOD")]}),
    ("GRITS", {"entities": [(0, 5, "FOOD")]}),
    ("FRUIT SALAD", {"entities": [(0, 11, "FOOD")]}),
    ("YOGURT", {"entities": [(0, 6, "FOOD")]}),
    ("SMOOTHIE", {"entities": [(0, 8, "FOOD")]}),
    ("MILKSHAKE", {"entities": [(0, 9, "FOOD")]}),
    ("ICE CREAM", {"entities": [(0, 9, "FOOD")]}),
    ("JELLO", {"entities": [(0, 4, "FOOD")]}),
    ("CARAMEL SAUCE", {"entities": [(0, 13, "FOOD")]}),
    ("MOZZARELLA STICKS", {"entities": [(0, 17, "FOOD")]}),
    ("GARLIC BREAD", {"entities": [(0, 11, "FOOD")]}),
    ("ONION RINGS", {"entities": [(0, 11, "FOOD")]}),
    ("CHILI", {"entities": [(0, 5, "FOOD")]}),
    ("QUESADILLA", {"entities": [(0, 10, "FOOD")]}),
    ("NACHOS", {"entities": [(0, 6, "FOOD")]}),
    ("GUACAMOLE", {"entities": [(0, 9, "FOOD")]}),
    ("SALSA", {"entities": [(0, 5, "FOOD")]}),
    ("TORTILLA", {"entities": [(0, 8, "FOOD")]}),
    ("SOUR CREAM", {"entities": [(0, 10, "FOOD")]}),
    ("BEAN BURGER", {"entities": [(0, 10, "FOOD")]}),
    ("POTATO WEDGES", {"entities": [(0, 13, "FOOD")]}),
    ("ROAST BEEF", {"entities": [(0, 9, "FOOD")]}),
    ("MEATBALLS", {"entities": [(0, 9, "FOOD")]}),
    ("LASAGNA", {"entities": [(0, 7, "FOOD")]}),
    ("RAVIOLI", {"entities": [(0, 7, "FOOD")]}),
    ("MANICOTTI", {"entities": [(0, 9, "FOOD")]}),
    ("SPAGHETTI", {"entities": [(0, 9, "FOOD")]}),
    ("FETTUCCINE", {"entities": [(0, 10, "FOOD")]}),
    ("MACARONI", {"entities": [(0, 8, "FOOD")]}),
    ("CHEESE", {"entities": [(0, 6, "FOOD")]}),
    ("FRITTATA", {"entities": [(0, 8, "FOOD")]}),
    ("HAM", {"entities": [(0, 3, "FOOD")]}),
    ("TURKEY", {"entities": [(0, 6, "FOOD")]}),
    ("ROAST CHICKEN", {"entities": [(0, 13, "FOOD")]}),
    ("BBQ RIBS", {"entities": [(0, 8, "FOOD")]}),
    ("POT ROAST", {"entities": [(0, 8, "FOOD")]}),
    ("STIR-FRY", {"entities": [(0, 8, "FOOD")]}),
    ("FRIED RICE", {"entities": [(0, 9, "FOOD")]}),
    ("DIM SUM", {"entities": [(0, 7, "FOOD")]}),
    ("SPRING ROLLS", {"entities": [(0, 11, "FOOD")]}),
    ("DUMPLINGS", {"entities": [(0, 9, "FOOD")]}),
    ("KOREAN BBQ", {"entities": [(0, 11, "FOOD")]}),
    ("JAPANESE NOODLES", {"entities": [(0, 16, "FOOD")]}),
    ("CHICKEN WINGS", {"entities": [(0, 12, "FOOD")]}),
    ("BBQ CHICKEN", {"entities": [(0, 11, "FOOD")]}),
    ("MARGHERITA PIZZA", {"entities": [(0, 17, "FOOD")]}),
    ("PEPPERONI PIZZA", {"entities": [(0, 16, "FOOD")]}),
    ("VEGGIE PIZZA", {"entities": [(0, 11, "FOOD")]}),
    ("BUFFALO WINGS", {"entities": [(0, 13, "FOOD")]}),
    ("CHICKEN NUGGETS", {"entities": [(0, 15, "FOOD")]}),
    ("MOZZARELLA", {"entities": [(0, 9, "FOOD")]}),
    ("CHEDDAR", {"entities": [(0, 7, "FOOD")]}),
    ("PARMESAN", {"entities": [(0, 8, "FOOD")]}),
    ("PROVOLONE", {"entities": [(0, 9, "FOOD")]}),
    ("FETA", {"entities": [(0, 4, "FOOD")]}),
    ("GOAT CHEESE", {"entities": [(0, 10, "FOOD")]}),
    ("RANCH DRESSING", {"entities": [(0, 14, "FOOD")]}),
    ("ITALIAN DRESSING", {"entities": [(0, 15, "FOOD")]}),
    ("BALSAMIC VINAIGRETTE", {"entities": [(0, 21, "FOOD")]}),
    ("COMBO", {"entities": [(0, 5, "FOOD")]}),
    ("HONEY MUSTARD", {"entities": [(0, 12, "FOOD")]}),
    ("MAYONNAISE", {"entities": [(0, 9, "FOOD")]}),
    ("BBQ SAUCE", {"entities": [(0, 9, "FOOD")]}),
    ("SIRACHA", {"entities": [(0, 7, "FOOD")]}),
    ("HOT SAUCE", {"entities": [(0, 9, "FOOD")]}),
    ("SWEET CHILI SAUCE", {"entities": [(0, 17, "FOOD")]}),
    ("PICKLES", {"entities": [(0, 7, "FOOD")]}),
    ("OLIVES", {"entities": [(0, 6, "FOOD")]}),
    ("CAPERS", {"entities": [(0, 6, "FOOD")]}),
    ("ARTICHOKES", {"entities": [(0, 10, "FOOD")]}),
    ("SUNDRIED TOMATOES", {"entities": [(0, 16, "FOOD")]}),

    # Non-food items
    ("Good", {"entities": []}),
    ("Restaurant", {"entities": []}),
    ("Table", {"entities": []}),
    ("Ticket", {"entities": []}),
    ("Server", {"entities": []}),
    ("Date", {"entities": []}),
    ("Sub Total", {"entities": []}),
    ("Sales Tax", {"entities": []}),
    ("Check Total", {"entities": []}),
    ("Thanks", {"entities": []}),
    ("Stay updated", {"entities": []}),
    ("Check", {"entities": []}),
    ("Order", {"entities": []}),
    ("Total", {"entities": []}),
    ("Amount", {"entities": []}),
    ("Receipt", {"entities": []}),
    ("Cash", {"entities": []}),
    ("Credit", {"entities": []}),
    ("Debit", {"entities": []}),
    ("Payment", {"entities": []}),
    ("Charge", {"entities": []}),
    ("Amount Paid", {"entities": []}),
    ("Change", {"entities": []}),
    ("Tip", {"entities": []}),
    ("Customer", {"entities": []}),
    ("Name", {"entities": []}),
    ("Phone", {"entities": []}),
    ("Address", {"entities": []}),
    ("Date", {"entities": []}),
    (";:{}[]", {"entities": []}),
    ("Time", {"entities": []}),
    ("..", {"entities": []}),
    ("At", {"entities": []}),
    ("Invoice", {"entities": []}),
    ("Order Number", {"entities": []}),
    ("Transaction", {"entities": []}),
    ("Discount", {"entities": []}),
    ("Promotion", {"entities": []}),
    ("3.23", {"entities": []}),
    ("Coupon", {"entities": []}),
    ("Voucher", {"entities": []}),
    ("Terms", {"entities": []}),
    ("Conditions", {"entities": []}),
    ("Policy", {"entities": []}),
    ("Refund", {"entities": []}),
    ("Exchange", {"entities": []}),
    ("Warranty", {"entities": []}),
    ("Service", {"entities": []}),
    ("Hours", {"entities": []}),
    ("Operation", {"entities": []}),
    ("Manager", {"entities": []}),
    ("Staff", {"entities": []}),
    ("Employee", {"entities": []}),
    ("Branch", {"entities": []}),
    ("Location", {"entities": []}),
    ("Website", {"entities": []}),
    ("Email", {"entities": []}),
    ("Support", {"entities": []}),
    ("Help", {"entities": []}),
    ("Assistance", {"entities": []}),
    ("Feedback", {"entities": []}),
    ("Review", {"entities": []}),
    ("Rating", {"entities": []}),
    ("Survey", {"entities": []}),
    ("Form", {"entities": []}),
    ("Questionnaire", {"entities": []}),
    ("Request", {"entities": []}),
    ("Inquiry", {"entities": []}),
    ("Complaint", {"entities": []}),
    (":", {"entities": []}),
    (".", {"entities": []}),
    ("Good", {"entities": []}),
    ("Restaurant", {"entities": []}),
    ("Table", {"entities": []}),
    ("Ticket", {"entities": []}),
    ("Server", {"entities": []}),
    ("Date", {"entities": []}),
    ("Sub Total", {"entities": []}),
    ("Sales Tax", {"entities": []}),
    ("Check Total", {"entities": []}),
    ("Thanks", {"entities": []}),
    ("Stay updated", {"entities": []}),
    ("Check", {"entities": []}),
    ("Order", {"entities": []}),
    ("Total", {"entities": []}),
    ("Amount", {"entities": []}),
    ("Receipt", {"entities": []}),
    ("Cash", {"entities": []}),
    ("Credit", {"entities": []}),
    ("Debit", {"entities": []}),
    ("Payment", {"entities": []}),
    ("Charge", {"entities": []}),
    ("Amount Paid", {"entities": []}),
    ("Change", {"entities": []}),
    ("Tip", {"entities": []}),
    ("Customer", {"entities": []}),
    ("Name", {"entities": []}),
    ("Phone", {"entities": []}),
    ("Address", {"entities": []}),
    ("Date", {"entities": []}),
    ("Time", {"entities": []}),
    ("Invoice", {"entities": []}),
    ("Order Number", {"entities": []}),
    ("Transaction", {"entities": []}),
    ("Discount", {"entities": []}),
    ("Promotion", {"entities": []}),
    ("Coupon", {"entities": []}),
    ("Voucher", {"entities": []}),
    ("Terms", {"entities": []}),
    ("Conditions", {"entities": []}),
    ("Policy", {"entities": []}),
    ("Refund", {"entities": []}),
    ("Exchange", {"entities": []}),
    ("Warranty", {"entities": []}),
    ("Service", {"entities": []}),
    ("Hours", {"entities": []}),
    ("Operation", {"entities": []}),
    ("Manager", {"entities": []}),
    ("Staff", {"entities": []}),
    ("Employee", {"entities": []}),
    ("Branch", {"entities": []}),
    ("Location", {"entities": []}),
    ("Website", {"entities": []}),
    ("Email", {"entities": []}),
    ("Support", {"entities": []}),
    ("Help", {"entities": []}),
    ("Assistance", {"entities": []}),
    ("Feedback", {"entities": []}),
    ("Review", {"entities": []}),
    ("Rating", {"entities": []}),
    ("Survey", {"entities": []}),
    ("Form", {"entities": []}),
    ("Questionnaire", {"entities": []}),
    ("Request", {"entities": []}),
    ("Inquiry", {"entities": []}),
    ("Complaint", {"entities": []}),
    ("30.25", {"entities": []}),
    ("39.87", {"entities": []}),
    ("08/10/08", {"entities": []}),
    ("11:34 AM", {"entities": []}),
    ("goodrestaurantnyc.com", {"entities": []}),
    ("Table 102", {"entities": []}),
    ("Ticket 4003", {"entities": []}),
    ("REG101", {"entities": []}),
    ("#4003", {"entities": []}),
    ("#102", {"entities": []}),
    ("-", {"entities": []}),
    ("/", {"entities": []}),
]