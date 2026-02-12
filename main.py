fruits = ["Apple","Mango","Banana"]
print("Length of List", len(fruits))
print("First Element", fruits[0])

fruits.append("Papaya")
print("Updated List", fruits)

fruits.remove("Mango")
print("Updated List", fruits)

fruits.sort()
print("Sorted List", fruits)

fruits.pop(1)
print("Updated List", fruits)

fruits.reverse()
print("Updated List", fruits)

print("Multiplication of List", fruits*2)

fruits = fruits[:2]
print("Sliced List", fruits)

fruits.clear()
print("Updated List", fruits)


