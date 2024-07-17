from fake_match import divide as fake_
from true_match import divide as true_

result1 = fake_(30, 3)
result2 = fake_(53, 0)
result3 = true_(25, 5)
result4 = true_(25, 0)
print(result1)
print(result2)
print(result3)
print(result4)