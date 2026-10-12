# DSA Notes: Time Complexity (Big-O)

**Course:** MCA DSA Practice\
**Topic:** Time Complexity\
**Purpose:** Simple revision notes for exams and MCQs

------------------------------------------------------------------------

## 1. What Is Time Complexity?

Time complexity describes how the number of operations performed by an
algorithm grows as the input size `n` increases.

Big-O notation describes the growth rate, usually focusing on the
dominant term for large inputs.

## 2. Important Complexity Types

  -----------------------------------------------------------------------
  Complexity              Name                    Common example
  ----------------------- ----------------------- -----------------------
  `O(1)`                  Constant                Access one array
                                                  element by index

  `O(log n)`              Logarithmic             Repeatedly multiply or
                                                  divide a loop variable
                                                  by a constant

  `O(√n)`                 Square root             Loop while `i * i <= n`

  `O(n)`                  Linear                  One loop that runs
                                                  about `n` times

  `O(n log n)`            Linearithmic            An `n`-iteration loop
                                                  containing a
                                                  logarithmic loop

  `O(n²)`                 Quadratic               Two nested loops that
                                                  each run about `n`
                                                  times

  `O(n³)`                 Cubic                   Three nested loops that
                                                  each run about `n`
                                                  times

  `O(2ⁿ)`                 Exponential             Recursion that branches
                                                  into two calls at each
                                                  level

  `O(n!)`                 Factorial               Examining every
                                                  permutation of `n`
                                                  distinct elements
  -----------------------------------------------------------------------

## 3. Golden Rules

1.  **One loop:** A loop that runs about `n` times is usually `O(n)`.
2.  **Nested loops:** Multiply the iteration counts when each loop runs
    independently of the others.
3.  **Sequential loops:** Add their costs, then keep the dominant term.
4.  **Constant increments:** Increasing by 1, 2, or another fixed amount
    is usually `O(n)`.
5.  **Multiplying or dividing by a constant:** `i *= 2`, `i *= 3`, or
    repeatedly dividing by 3 gives `O(log n)`.
6.  **Fixed inner loop:** A loop that runs 5 or 10 times is constant
    time.
7.  **Ignore constants:** `O(5n)` becomes `O(n)`.
8.  **Ignore smaller terms:** `O(n² + n)` becomes `O(n²)`.
9.  **Square-root condition:** `i * i <= n` gives `O(√n)`.
10. **Cube-root condition:** `i * i * i <= n` gives `O(n^(1/3))`.

> **Important:** For nested loops whose bounds depend on outer
> variables, count the total iterations carefully. Do not automatically
> multiply all loop bounds.

------------------------------------------------------------------------

# 4. All 30 Practice Questions Explained

## Q1. Nested loop with doubling

``` c
for (int i = 0; i < n; i++) {
    for (int j = 1; j < n; j *= 2) {
        printf("*");
    }
}
```

**Answer: `O(n log n)`**

-   Outer loop runs `n` times.
-   Inner loop doubles: `1, 2, 4, 8, ...`, so it runs about `log n`
    times.
-   Total: `n × log n`.

## Q2. Access one array element

``` c
int x = arr[n / 2];
printf("%d", x);
```

**Answer: `O(1)`**

Only one array element is accessed by its index. The array is not
scanned.

## Q3. Two separate loops

``` c
for (int i = 0; i < n; i++)
    printf("A");

for (int j = 0; j < n * n; j++)
    printf("B");
```

**Answer: `O(n²)`**

-   First loop: `O(n)`.
-   Second loop: `O(n²)`.
-   Total: `O(n + n²) = O(n²)`.

Sequential loops are added, not multiplied.

## Q4. Divide by 3 repeatedly

``` c
int i = n;
while (i > 1) {
    i = i / 3;
}
```

**Answer: `O(log n)`**

The values shrink like `n, n/3, n/9, n/27, ...`. It takes about `log₃ n`
divisions to reach 1.

## Q5. Square-root loop

``` c
for (int i = 1; i * i <= n; i++) {
    printf("%d", i);
}
```

**Answer: `O(√n)`**

The condition `i * i <= n` means `i <= √n`. The loop runs about `√n`
times.

## Q6. Inner loop runs a fixed number of times

``` c
for (int i = 0; i < n; i++) {
    for (int j = 0; j < 5; j++) {
        printf("*");
    }
}
```

**Answer: `O(n)`**

The total work is `n × 5 = 5n`. Ignore the constant 5.

## Q7. Three nested loops

``` c
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        for (int k = 0; k < n; k++) {
            printf("*");
        }
    }
}
```

**Answer: `O(n³)`**

Each loop runs `n` times: `n × n × n = n³`.

## Q8. Simplify Big-O

`O(7n³ + 4n² + 20n + 50)`

**Answer: `O(n³)`**

Keep the highest-growing term, `n³`. Ignore coefficients and smaller
terms.

## Q9. Two separate doubling loops

``` c
for (int i = 1; i < n; i *= 2)
    printf("A");

for (int j = 1; j < n; j *= 2)
    printf("B");
```

**Answer: `O(log n)`**

Each loop takes `O(log n)`. Total: `O(log n + log n) = O(log n)`.

## Q10. One normal loop

``` c
for (int i = 0; i < n; i++) {
    printf("%d", i);
}
```

**Answer: `O(n)`**

The loop executes `n` times.

## Q11. Doubling outer loop; inner loop runs up to `i`

``` c
for (int i = 1; i < n; i *= 2) {
    for (int j = 0; j < i; j++)
        printf("*");
}
```

**Answer: `O(n)`**

The inner loop runs `1, 2, 4, 8, ...` times across the outer iterations.
The total is approximately `1 + 2 + 4 + ... + n`, which is less than
`2n`.

So the total is `O(n)`, not `O(n log n)`.

## Q12. Inner loop starts from `i`

``` c
for (int i = 0; i < n; i++) {
    for (int j = i; j < n; j++) {
        printf("*");
    }
}
```

**Answer: `O(n²)`**

The inner loop runs `n, n-1, n-2, ..., 1` times.

The sum is `n(n + 1) / 2`, whose dominant term is `n²`.

## Q13. Simplify `O(n + log n)`

**Answer: `O(n)`**

Linear growth is faster than logarithmic growth, so keep `n`.

## Q14. One loop followed by two nested loops

``` c
for (int i = 0; i < n; i++)
    printf("A");

for (int j = 0; j < n; j++) {
    for (int k = 0; k < n; k++) {
        printf("B");
    }
}
```

**Answer: `O(n²)`**

The first loop costs `O(n)`. The nested loops cost `O(n²)`. Total:
`O(n + n²) = O(n²)`.

## Q15. Multiply the loop variable by 3

``` c
for (int i = 1; i < n; i *= 3) {
    printf("*");
}
```

**Answer: `O(log n)`**

Values are `1, 3, 9, 27, ...`. The loop runs about `log₃ n` times.

## Q16. Two `n`-loops and one fixed loop

``` c
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        for (int k = 0; k < 10; k++) {
            printf("*");
        }
    }
}
```

**Answer: `O(n²)`**

Total work: `n × n × 10 = 10n²`. Ignore the constant 10.

## Q17. Every permutation

**Answer: `O(n!)`**

There are `n! = n × (n-1) × (n-2) × ... × 1` permutations of `n`
distinct elements. Examining all of them takes factorial time if each
permutation requires at least constant work.

Example: `4! = 24` permutations.

## Q18. Three nested loops: `n`, `log n`, and `n`

``` c
for (int i = 0; i < n; i++) {
    for (int j = 1; j < n; j *= 2) {
        for (int k = 0; k < n; k++) {
            printf("*");
        }
    }
}
```

**Answer: `O(n² log n)`**

The loop counts are `n × log n × n = n² log n`.

## Q19. Increment by 2

``` c
for (int i = 0; i < n; i += 2) {
    printf("%d", i);
}
```

**Answer: `O(n)`**

The loop runs about `n/2` times. Ignore the constant factor 1/2.

## Q20. Recursive function calls itself twice

``` c
void fun(int n) {
    if (n <= 0) return;
    fun(n - 1);
    fun(n - 1);
}
```

**Answer: `O(2ⁿ)`**

Each call creates two more calls until the base case. The recurrence is
`T(n) = 2T(n-1) + O(1)`, which gives exponential growth.

## Q21. Doubling loop with an `n`-loop inside

``` c
for (int i = 1; i < n; i *= 2) {
    for (int j = 0; j < n; j++) {
        printf("*");
    }
}
```

**Answer: `O(n log n)`**

Outer loop: `O(log n)`. Inner loop: `O(n)`. Total: `n × log n`.

## Q22. Simplify Big-O

`O(4n² + 100n + 500)`

**Answer: `O(n²)`**

The highest-growing term is `n²`. Ignore its coefficient and the smaller
terms.

## Q23. Two nested doubling loops

``` c
for (int i = 1; i < n; i *= 2) {
    for (int j = 1; j < n; j *= 2) {
        printf("*");
    }
}
```

**Answer: `O((log n)²)`**

Both loops run `O(log n)` times. Total: `log n × log n`.

## Q24. Linear loop followed by logarithmic loop

``` c
for (int i = 0; i < n; i++)
    printf("A");

for (int j = 1; j < n; j *= 2)
    printf("B");
```

**Answer: `O(n)`**

Total: `O(n + log n)`. The linear term dominates.

## Q25. Cube-root loop

``` c
for (int i = 1; i * i * i <= n; i++) {
    printf("%d", i);
}
```

**Answer: `O(n^(1/3))`**

The condition `i³ <= n` means `i <= ∛n`. So the loop runs about
`n^(1/3)` times.

## Q26. Three dependent nested loops

``` c
for (int i = 0; i < n; i++) {
    for (int j = 0; j < i; j++) {
        for (int k = 0; k < j; k++) {
            printf("*");
        }
    }
}
```

**Answer: `O(n³)`**

The bounds depend on the outer variables, so the loops do not each run
exactly `n` times. However, the total work grows proportionally to `n³`.

## Q27. Polynomial time complexity

**Answer: `O(n⁴)`**

Polynomial complexity has the form `O(n^k)`, where `k` is a fixed
constant.

Examples: `O(n)`, `O(n²)`, `O(n³)`, and `O(n⁴)`. By contrast, `O(2ⁿ)` is
exponential.

## Q28. One logarithmic loop and two linear loops

``` c
for (int i = 1; i < n; i *= 2)
    printf("A");

for (int j = 0; j < n; j++)
    printf("B");

for (int k = 0; k < n; k++)
    printf("C");
```

**Answer: `O(n)`**

Total: `O(log n + n + n) = O(n)`. The linear terms dominate.

## Q29. One linear loop and two logarithmic loops

``` c
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j *= 2) {
        for (int k = 1; k <= n; k *= 2) {
            printf("*");
        }
    }
}
```

**Answer: `O(n(log n)²)`**

The loop counts are `n × log n × log n`.

## Q30. Simplify the operation count

`O(3n² + 5n log n + 10n + 20)`

**Answer: `O(n²)`**

The dominant term is `n²`. It grows faster than `n log n`, `n`, and the
constant 20.

------------------------------------------------------------------------

# 5. Quick Revision Table

  Code pattern                                  Complexity
  --------------------------------------------- ---------------
  Direct array access                           `O(1)`
  One loop up to `n`                            `O(n)`
  Increment by a fixed amount                   `O(n)`
  Multiply/divide loop variable by a constant   `O(log n)`
  Two nested loops up to `n`                    `O(n²)`
  Three nested loops up to `n`                  `O(n³)`
  `i * i <= n`                                  `O(√n)`
  `i * i * i <= n`                              `O(n^(1/3))`
  Linear loop inside a doubling loop            `O(n log n)`
  Two nested doubling loops                     `O((log n)²)`
  Examine every permutation                     `O(n!)`
  Two recursive calls on `n-1`                  `O(2ⁿ)`

## 6. Mini Practice Quiz

Try these questions without looking at the answers.

1.  What is the complexity of a loop that runs from `0` to `n-1`?
2.  What is the complexity if `i` doubles each iteration?
3.  What is the complexity of two nested loops that each run `n` times?
4.  Simplify `O(8n³ + 2n² + 9)`.
5.  What is the complexity of an `n`-iteration loop containing a
    logarithmic loop?

### Answers

1.  `O(n)`
2.  `O(log n)`
3.  `O(n²)`
4.  `O(n³)`
5.  `O(n log n)`

------------------------------------------------------------------------

## Final Tip

Learn to identify whether each loop is **constant, linear, or
logarithmic**. Then combine the costs carefully. This is more useful
than memorizing the 30 answers.
