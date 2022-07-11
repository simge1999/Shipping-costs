international_shipping = True
total = 34
shipping_cost = 0 
if international_shipping :
	shipping_cost += 15
	print("Internatinonal base cost applied.")
if total <= 50:
	shipping_cost += 20
elif total <= 100:
	shipping_cost += 15
else:
	shipping_cost += 5
print(f"shipping_cost: {shipping_cost}")
print(f"Your price: {total}")