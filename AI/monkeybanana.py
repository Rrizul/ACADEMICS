 # Monkey Banana Problem (Simple Version)

# Initial positions
monkey = 'A'
chair = 'B'
banana = 'C'
on_chair = False
has_banana = False

print("Initial state")
print("Monkey =", monkey)
print("Chair =", chair)
print("Banana =", banana)
print("On the chair =", on_chair)
print("Has banana =", has_banana)

print("\nInitial state space:")
print("{Monkey, Chair, On the chair, has banana} = {a,b,f,f}")

# Step 1: Monkey moves to chair
print("\nAction performed: Move")
monkey = chair
print("Next state space:")
print("{Monkey, Chair, On the chair, has banana} = {b,b,f,f}")

# Step 2: Monkey pushes chair to banana
print("\nAction performed: Push")
monkey = banana
chair = banana
print("{Monkey, Chair, On the chair, has banana} = {c,c,f,f}")

# Step 3: Monkey climbs chair
print("\nAction performed: Climb")
on_chair = True
print("{Monkey, Chair, On the chair, has banana} = {c,c,t,f}")

# Step 4: Monkey grabs banana
print("\nAction performed: Grab")
has_banana = True
print("Goal state:")
print("{Monkey, Chair, On the chair, has banana} = {c,c,t,t}")