# Monkey Banana Problem (Very Easy Version)

def show_state(monkey, chair, on_chair, has_banana):
    if on_chair:
        on = "t"
    else:
        on = "f"

    if has_banana:
        hb = "t"
    else:
        hb = "f"

    print("{Monkey, Chair, On the chair, has banana}={" +
          monkey.lower() + "," + chair.lower() + "," + on + "," + hb + "}")


def move(monkey, chair, on_chair, has_banana):
    print("\nAction performed: Move")
    monkey = chair
    show_state(monkey, chair, on_chair, has_banana)
    return monkey, chair, on_chair, has_banana


def push(monkey, chair, banana, on_chair, has_banana):
    print("\nAction performed: Push")
    monkey = banana
    chair = banana
    show_state(monkey, chair, on_chair, has_banana)
    return monkey, chair, on_chair, has_banana


def climb(monkey, chair, on_chair, has_banana):
    print("\nAction performed: Climb")
    on_chair = True
    show_state(monkey, chair, on_chair, has_banana)
    return monkey, chair, on_chair, has_banana


def grab(monkey, chair, on_chair, has_banana):
    print("\nAction performed: Grab")
    has_banana = True
    print("Goal state:")
    show_state(monkey, chair, on_chair, has_banana)


# Initial state
monkey = "A"
chair = "B"
banana = "C"
on_chair = False
has_banana = False

print("Initial state")
print("Monkey=A")
print("Chair=B")

print("\nInitial state space:")
show_state(monkey, chair, on_chair, has_banana)

# Steps
monkey, chair, on_chair, has_banana = move(monkey, chair, on_chair, has_banana)
monkey, chair, on_chair, has_banana = push(monkey, chair, banana, on_chair, has_banana)
monkey, chair, on_chair, has_banana = climb(monkey, chair, on_chair, has_banana)
grab(monkey, chair, on_chair, has_banana)









