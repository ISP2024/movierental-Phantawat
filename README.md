## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale

### 2.1 What refactoring signs (code smells) suggest this refactoring?

- **Feature Envy**: The `Rental` class was heavily relying on the `Movie` class to determine pricing and rental points. Since the rental duration and the pricing logic are more directly tied to a specific rental instance rather than the movie itself, this dependence indicated a misplaced responsibility.
- **Middle Man**: The `Movie` class acted as an unnecessary intermediary. It merely forwarded calls to the price strategy classes, making it a "middle man" that added no value to the calculation logic.
- **Inappropriate Intimacy**: The tight coupling between `Rental` and `Movie` through the `price_code` attribute indicated that the `Rental` class knew too much about how the `Movie` class operated.

### 2.2 What design principle suggests this refactoring? Why?

- **Single Responsibility Principle (SRP)**: Each class should have only one reason to change. Moving the `price_code` and pricing logic to the `Rental` class means that `Movie` is now only responsible for holding movie information, while `Rental` is responsible for managing rental-related operations, including price calculations.
- **Encapsulation**: By moving the `price_code` and pricing logic into `Rental`, we encapsulate the logic where it is most relevant. This reduces unnecessary interactions between `Rental` and `Movie`, leading to a more cohesive design.
- **Tell, Don’t Ask**: The refactoring encourages the `Rental` class to perform actions directly related to rental pricing without needing to ask for information from `Movie`. This helps in reducing the dependency between the two classes, following the principle that objects should be responsible for their own data.

