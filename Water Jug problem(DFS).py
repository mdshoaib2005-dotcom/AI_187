def water_jug_dfs():
    jug1_capacity = 4
    jug2_capacity = 3
    goal = 2

    start = (0, 0)

    stack = [(start, [])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)

        # Check goal
        if state[0] == goal or state[1] == goal:
            print("Solution found:")
            for step in path:
                print(step)
            print("Final State:", state)
            return

        a, b = state

        # Generate possible states
        next_states = [
            ((jug1_capacity, b), "Fill Jug 1"),
            ((a, jug2_capacity), "Fill Jug 2"),
            ((0, b), "Empty Jug 1"),
            ((a, 0), "Empty Jug 2")
        ]

        # Pour Jug 1 -> Jug 2
        amount = min(a, jug2_capacity - b)
        next_states.append(
            ((a - amount, b + amount), "Pour Jug 1 -> Jug 2")
        )

        # Pour Jug 2 -> Jug 1
        amount = min(b, jug1_capacity - a)
        next_states.append(
            ((a + amount, b - amount), "Pour Jug 2 -> Jug 1")
        )

        # Add states to stack
        for new_state, action in next_states:
            if new_state not in visited:
                stack.append(
                    (new_state, path + [action + " : " + str(new_state)])
                )


# Run DFS
water_jug_dfs()
