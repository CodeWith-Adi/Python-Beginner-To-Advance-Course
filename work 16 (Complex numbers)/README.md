# Complex Numbers in Python

Python provides built-in support for complex numbers. A complex number is represented as `a + bj`, where `a` is the real part and `b` is the imaginary part.

## Why complex numbers

Complex numbers are essential in various fields, including:

- **Mathematics**: Solving quadratic equations and advanced mathematical calculations.
- **Signal Processing**: Analyzing waveforms and frequency components.
- **Electrical Engineering**: Working with alternating current and impedance calculations.
- **Quantum Physics**: Representing quantum states and wave functions.
- **Control Systems**: Analyzing system stability and frequency response.

## Creating Complex Numbers

You can create a complex number using:
- The `complex()` function.
- Direct assignment.

```python
# Using the complex() function
z1 = complex(3, 4)

# Direct assignment
z2 = 5 + 6j

print(z1)  # Output: (3+4j)
print(z2)  # Output: (5+6j)
```

## Accessing Real and Imaginary Parts

You can access the real and imaginary parts of a complex number using the `.real` and `.imag` attributes.

```python
z = 7 + 8j
print(z.real)  # Output: 7.0
print(z.imag)  # Output: 8.0
```

## Operations on Complex Numbers

Python supports arithmetic operations on complex numbers.

```python
z1 = 2 + 3j
z2 = 4 + 5j

# Addition
print(z1 + z2)  # Output: (6+8j)

# Subtraction
print(z1 - z2)  # Output: (-2-2j)

# Multiplication
# ( z1 = a + bj ) and ( z2 = c + dj )
# formula : [ z1 * z2 = (a * c - b * d) + (a * d + b * c)j ]
print(z1 * z2)  # Output: (-7+22j)

# Division
# ( z1 = a + bj ) and ( z2 = c + dj )
# formula : [ z1/z2 = (a * c + b * d) / (c^2 + d^2)] + [(b * c - a * d) / (c^2 + d^2)]j ]
print(z1 / z2)  # Output: (0.5609756097560976+0.0487804878048781j)
```

## Watch this video for better understanding : 
# Thanks for Watching.....💝💝