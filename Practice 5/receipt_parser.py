import re
import json

def clean_price(price_str):
    price_str = price_str.replace(" ", "")
    return float(price_str.replace(",", "."))

def extract_products(text):
    product_pattern = re.compile(
        r'\d+\.\s*\n'
        r'(.+?)\n'
        r'([\d, ]+)\s*x\s*([\d, ]+)\n'
        r'([\d, ]+)',
        re.MULTILINE
    )

    products = []
    prices = []

    for match in product_pattern.findall(text):
        name = match[0].strip()
        quantity = clean_price(match[1])
        unit_price = clean_price(match[2])
        total_price = clean_price(match[3])

        products.append({
            "name": name,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_price": total_price
        })

        prices.append(total_price)

    return products, prices

def extract_total(text):
    total_match = re.search(r'ИТОГО:\s*\n?\s*([\d, ]+)', text)
    return clean_price(total_match.group(1)) if total_match else None

def extract_payment_method(text):
    payment_match = re.search(r'(Банковская карта|Наличные)', text)
    return payment_match.group(1) if payment_match else None

def extract_datetime(text):
    datetime_match = re.search(
        r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})',
        text
    )
    if datetime_match:
        return {
            "date": datetime_match.group(1),
            "time": datetime_match.group(2)
        }
    return None


def main():
   
    with open("raw.txt", "r", encoding="utf-8") as file:
        receipt_text = file.read()

    products, prices = extract_products(receipt_text)

    result = {
        "products": products,
        "total_calculated": sum(prices),
        "total_receipt": extract_total(receipt_text),
        "payment_method": extract_payment_method(receipt_text),
        "datetime": extract_datetime(receipt_text)
    }

    print(json.dumps(result, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()