def linear_search_product(products, target_product):
    indices = []
    
    for index, product in enumerate(products):
        if product == target_product:
            indices.append(index)
    
    return indices
products = ["apple", "banana", "orange", "apple", "grape"]
target_product = "apple"

result = linear_search_product(products, target_product)
print(result)
