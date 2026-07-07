import math
pos_num = 3.6
neg_num = -3.6

print(f"Original Positive: {pos_num}  |  Original Negative: {neg_num}")
print("-" * 50)

# 1. math.ceil() - Rounds UPWARD towards positive infinity
print(f"math.ceil({pos_num}):   {math.ceil(pos_num)}")   # 3.6 becomes 4
print(f"math.ceil({neg_num}):  {math.ceil(neg_num)}")  # -3.6 becomes -3
print("-" * 50)

# 2. math.floor() - Rounds DOWNWARD towards negative infinity
print(f"math.floor({pos_num}):  {math.floor(pos_num)}")  # 3.6 becomes 3
print(f"math.floor({neg_num}): {math.floor(neg_num)}") # -3.6 becomes -4
print("-" * 50)

# 3. math.trunc() - Chopped off! Just removes the decimal part entirely
# It acts like floor() for positive numbers, and ceil() for negative numbers.
print(f"math.trunc({pos_num}):  {math.trunc(pos_num)}")  # 3.6 becomes 3
print(f"math.trunc({neg_num}): {math.trunc(neg_num)}") # -3.6 becomes -3
print("-" * 50)

# 4. round() - Built-in Python function (no 'math.' needed)
# Rounds to the nearest mathematical integer. 
print(f"round({pos_num}):       {round(pos_num)}")       # 3.6 is closer to 4
print(f"round({neg_num}):      {round(neg_num)}")      # -3.6 is closer to -4
