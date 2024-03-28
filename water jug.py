from collections import deque

class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

    def __repr__(self):
        return f"({self.jug1}, {self.jug2})"

    def is_goal(self, target):
        return self.jug1 == target or self.jug2 == target

    def successors(self, capacities):
        successors = []
        # Fill jug1
        successors.append(State(capacities[0], self.jug2))
        # Fill jug2
        successors.append(State(self.jug1, capacities[1]))
        # Empty jug1
        successors.append(State(0, self.jug2))
        # Empty jug2
        successors.append(State(self.jug1, 0))
        # Pour jug1 to jug2 until full or jug1 is empty
        amount_to_pour = min(self.jug1, capacities[1] - self.jug2)
        successors.append(State(self.jug1 - amount_to_pour, self.jug2 + amount_to_pour))
        # Pour jug2 to jug1 until full or jug2 is empty
        amount_to_pour = min(self.jug2, capacities[0] - self.jug1)
        successors.append(State(self.jug1 + amount_to_pour, self.jug2 - amount_to_pour))
        return successors

def bfs(capacities, initial_state, target):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()
        if current_state.is_goal(target):
            return path + [current_state]
        visited.add(current_state)
        for successor in current_state.successors(capacities):
            if successor not in visited:
                queue.append((successor, path + [successor]))

    return None

def main():
    jug1_capacity = int(input("Enter capacity of jug 1: "))
    jug2_capacity = int(input("Enter capacity of jug 2: "))
    target = int(input("Enter the target amount: "))

    initial_state = State(0, 0)
    capacities = (jug1_capacity, jug2_capacity)

    solution = bfs(capacities, initial_state, target)

    if solution:
        print("Solution:")
        for state in solution:
            print(state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
