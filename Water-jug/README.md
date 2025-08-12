# Two Jug Water Problem (C++ Implementation)

## Problem Statement
You are given *two jugs* with capacities x and y litres. The goal is to measure **exactly z litres** of water using the following operations:

1. *Fill* a jug completely.
2. *Empty* a jug completely.
3. *Pour* water from one jug into the other until either:
   - the first jug becomes empty, or  
   - the second jug becomes full.  

If it is possible to measure exactly z litres, print the sequence of steps. Otherwise, output *"Not possible"*.

---

## Mathematical Foundation
The classic water jug problem is based on *Number Theory*.  

It can be solved *if and only if*:
1. z <= max(x, y)  
2. z % gcd(x, y) == 0  

This comes from *Bézout’s identity*, which states that for two integers x and y, the smallest measurable quantity using their linear combination is gcd(x, y).

 This means we can only measure z if it is a multiple of the greatest common divisor of x and y.

---

## Approach (Simulation Method)
The program simulates the water jug process step by step:

1. *Initialization*: Start with both jugs empty (a = 0, b = 0).  
2. **Repeat until one jug has z litres**:
   - If Jug A is empty → *fill Jug A*.
   - Else if Jug B is full → *empty Jug B*.
   - Else → *pour water from Jug A into Jug B* (either until Jug A is empty or Jug B is full).
3. Continue until either Jug A or Jug B contains exactly z litres.  
4. If no solution is possible, print *"Not possible"*.

---