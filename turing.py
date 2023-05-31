import random

states = ["q0", "q1"]
alphabet = ["a", "b", "c"]
result = ["lambda"]
for i in range(random.randint(2, 11)):
    result.append(random.choice(alphabet))
result.append("lambda")

state = "q0"
count = 0
while True:
    if result[count] == "lambda" and state == "q0":
        count += 1
        state = "q1"
        continue
    if (
        result[count] == "a" or result[count] == "b" or result[count] == "c"
    ) and state == "q1":
        count += 1
        state = "q2"
        continue

    if (
        result[count] == "a" or result[count] == "b" or result[count] == "c"
    ) and state == "q2":
        count += 1
        state = "q1"
        continue
    if result[count] == "lambda":
        break

word = "".join(result[1:-1])
print(word)
if state == "q2":  # q2 так как если нечётное то оно состояние сделает q2 и наоборот
    print("нечётное количество", len(word))
else:
    print("чётное количество", len(word))
