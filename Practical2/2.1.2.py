# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}
def insert(std):
	key = int(input())
	value = input()
	std[key] = value
	print("After Insertion:",std)
	
def update(std):
	key = int(input())
	value = input()
	std.update({key:value})
	print("After Update:",std)
	

def Deletion(std):
	key = int(input())
	if key in std:
		std.pop(key)
	
	print("After Deletion:",std)
	


print("Original Dictionary:",student)

insert(student)
update(student)
Deletion(student)

print("Traversing Dictionary:")
for x, y in student.items():
  print(f"{x} : {y}")
