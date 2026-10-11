# DSA Foundations: Study Notes

**FY MCA | Division A**

## 1. What is DSA?

**Data Structures and Algorithms (DSA)** combines ways to organize data with step-by-step methods for solving problems.

- **Data structure:** A way to store and organize data so it can be accessed or changed efficiently.
- **Algorithm:** A finite sequence of clear steps that solves a problem.

Example: A list stores student marks. An algorithm finds the highest mark in that list.

## 2. Time Complexity

Time complexity describes how the number of operations performed by an algorithm grows as input size `n` grows. It is not normally a measurement of exact seconds.

Examples:
- Accessing an array element by index: `O(1)`
- Scanning a list once: `O(n)`
- Binary search on sorted data: `O(log n)`
- Two nested loops over `n` items: often `O(n²)`

## 3. Space Complexity

Space complexity describes how memory usage grows as input size grows.

- **Auxiliary space** means extra memory used by the algorithm, excluding the input itself.
- An algorithm using a few variables may use `O(1)` auxiliary space.
- An algorithm creating a new list of `n` elements may use `O(n)` auxiliary space.

Different textbooks sometimes use “space complexity” to include input storage too, so state which convention you use.

## 4. Time Complexity vs Space Complexity

| Time complexity | Space complexity |
|---|---|
| Growth in operations/work | Growth in memory use |
| Asks: how does work grow with `n`? | Asks: how does memory grow with `n`? |
| Examples: `O(1)`, `O(n)`, `O(n²)` | Examples: `O(1)`, `O(n)` |

An algorithm can be fast but use more memory, or save memory while doing more work. This is a time–space trade-off.

## 5. Mathematical Notations

These notations describe asymptotic growth as input size becomes large.

- **Big O — `O(g(n))`:** asymptotic upper bound. Often used to describe an algorithm's worst-case growth.
- **Big Omega — `Ω(g(n))`:** asymptotic lower bound.
- **Big Theta — `Θ(g(n))`:** tight asymptotic bound, when both upper and lower bounds match.

Common growth rates, from generally slower to faster growth:

`O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)`

This ordering is about sufficiently large `n`, ignoring constant factors and lower-order terms.

### Example
For `f(n) = 3n² + 5n + 2`, the dominant term is `n²`, so `f(n) = Θ(n²)`.

## 6. Data Structures and Their Types

A common introductory classification is **linear** and **nonlinear**. Some structures can be classified differently depending on the perspective or implementation.

### Linear data structures
Elements are arranged in a sequence.

#### Array
- Stores elements in indexed positions.
- Index access is typically `O(1)`.
- Inserting/deleting in the middle usually requires shifting elements: `O(n)`.
- Uses: marks, lists of values, lookup by index.

#### String
- A sequence of characters or text.
- Common operations include searching, slicing, concatenation, and comparing.
- Uses: names, messages, text processing.
- Exact costs depend on the language and operation.

#### Stack
- Follows **LIFO**: Last In, First Out.
- Operations: `push`, `pop`, `peek/top`.
- Uses: undo, function calls, expression evaluation, browser history patterns.

#### Queue
- Follows **FIFO**: First In, First Out.
- Operations: enqueue and dequeue.
- Uses: task scheduling, print queues, request processing.

#### Linked List
- Nodes store data and links to other nodes.
- Efficient insertion/removal when the relevant node/position is already known.
- Accessing the element at a position requires traversal, typically `O(n)`.
- Uses: situations where nodes are inserted or removed frequently.

### Nonlinear data structures
Relationships are not simply one sequence.

#### Tree
- A hierarchical structure of nodes and edges.
- Terms: root, parent, child, leaf, subtree.
- Uses: file systems, hierarchical data, search trees.
- Search performance depends on the tree's structure and balancing.

#### Graph
- A set of vertices (nodes) connected by edges.
- Can be directed/undirected and weighted/unweighted.
- Uses: maps, social networks, dependencies, routing.

#### Trie
- A tree-like structure used to store strings by shared prefixes.
- Uses: autocomplete, prefix search, dictionaries.

## 7. Is a Hash Table Linear or Nonlinear?

A hash table is generally classified as a **nonlinear or associative data structure** in many introductory classifications because it stores key–value pairs and does not represent data as a sequential list or hierarchy. However, classifications vary by textbook; its key–value abstraction is more important than forcing it into a universal category.

- A **hash function** maps a key to an index/bucket.
- Average-case search, insertion, and deletion are often `O(1)`.
- Worst-case operations can be `O(n)` if many keys collide.
- Collision handling may use chaining (often a linked list or another structure) or open addressing.
- Uses: dictionaries/maps, caches, counting frequencies, fast key-based lookup.

## 8. DSA Across Different Programming Languages

The concepts are language-independent, but syntax, libraries, memory management, and performance details vary.

- **Python:** `list`, `tuple`, `dict`, `set`; convenient built-in collections.
- **C:** arrays, structs, pointers; many structures are implemented manually.
- **C++:** `vector`, `list`, `stack`, `queue`, `map`, `unordered_map`, `set`.
- **Java:** arrays, `ArrayList`, `LinkedList`, `Stack`/`Deque`, `Queue`, `HashMap`, `TreeMap`.
- **JavaScript:** `Array`, `Map`, `Set`, objects; stacks/queues can be built with arrays or suitable libraries.
- **C#:** arrays, `List<T>`, `Queue<T>`, `Stack<T>`, `Dictionary<TKey,TValue>`.

Learn the underlying operation and complexity first; then learn the idiomatic implementation in each language.

## 9. Reading the Whiteboard Example

The classroom image shows input values `1, 4, 2, 3` and the output `4, 3, 2, 1`, followed by `1, 2, 3, 4`. It also shows comparisons such as `1 < 4`, `1 < 2`, and `1 < 3`, and asks about time and space complexity.

This appears to be an illustration of comparing values and arranging the sequence, but the image alone does not specify the complete algorithm or every step. Do not assign an exact complexity to the classroom example until the teacher confirms which algorithm is being demonstrated.

## 10. Practice Questions

1. Define a data structure and an algorithm.
2. Explain time complexity with an example.
3. Explain space complexity and auxiliary space.
4. Differentiate time and space complexity.
5. Explain Big O, Big Omega, and Big Theta.
6. Classify arrays, stacks, queues, linked lists, trees, and graphs.
7. What is LIFO? Give a real-world example.
8. What is FIFO? Give a real-world example.
9. Why is a hash table useful? What is a collision?
10. Is hash table classification identical in every textbook? Explain.
11. Give examples of DSA collections in Python and C++.
12. Find the time complexity of a loop that visits each of `n` elements once.


## 11. Answers to Practice Questions

### 1. Define a data structure and an algorithm.

A **data structure** is a way to organize and store data so it can be accessed and modified efficiently. Examples include arrays, stacks, queues, trees, and hash tables.

An **algorithm** is a finite sequence of clear steps used to solve a problem. For example, finding the largest number in a list is an algorithm.

### 2. Explain time complexity with an example.

**Time complexity** describes how the number of operations performed by an algorithm grows as the input size `n` increases.

Example: If a loop visits each of `n` elements once, the number of operations grows proportionally to `n`. Its time complexity is **O(n)**.

```python
numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)
```

### 3. Explain space complexity and auxiliary space.

**Space complexity** describes how an algorithm's memory requirement grows with the input size.

**Auxiliary space** is the extra memory used by the algorithm, excluding the memory occupied by the input itself.

Example: Finding the maximum using one variable requires **O(1) auxiliary space**, because it uses a constant amount of extra memory regardless of the list length.

### 4. Differentiate time complexity and space complexity.

| Time Complexity | Space Complexity |
|---|---|
| Measures how the amount of work grows with input size. | Measures how memory usage grows with input size. |
| Focuses on operations performed. | Focuses on memory required. |
| Example: scanning a list takes O(n) time. | Example: creating a copy of an n-element list takes O(n) extra space. |

An algorithm may use more memory to save time, or use less memory while performing more work. This is called a **time–space trade-off**.

### 5. Explain Big O, Big Omega, and Big Theta.

- **Big O — O(g(n)):** Describes an asymptotic upper bound on growth.
- **Big Omega — Ω(g(n)):** Describes an asymptotic lower bound on growth.
- **Big Theta — Θ(g(n)):** Describes a tight asymptotic bound when upper and lower bounds match.

Example: For `f(n) = 3n² + 5n + 2`, the dominant term is `n²`. Therefore, `f(n) = Θ(n²)` and also belongs to `O(n²)` and `Ω(n²)`.

These notations describe growth for large inputs and ignore constant factors and lower-order terms.

### 6. Classify arrays, stacks, queues, linked lists, trees, and graphs.

**Linear data structures** arrange elements in a sequence:
- **Array:** Stores elements in indexed positions.
- **Stack:** Follows LIFO order.
- **Queue:** Follows FIFO order.
- **Linked list:** Stores nodes connected by links.

**Nonlinear data structures** represent hierarchical or network-like relationships:
- **Tree:** Organizes nodes hierarchically, such as parent and child nodes.
- **Graph:** Represents vertices connected by edges.

This is the common introductory classification.

### 7. What is LIFO? Give a real-world example.

**LIFO** means **Last In, First Out**. The last item added is the first item removed.

Example: A stack of plates. The last plate placed on top is normally the first plate taken off.

A stack data structure follows LIFO.

### 8. What is FIFO? Give a real-world example.

**FIFO** means **First In, First Out**. The first item added is the first item removed.

Example: People waiting in a normal queue at a ticket counter. The person who arrives first is generally served first.

A queue data structure follows FIFO.

### 9. Why is a hash table useful? What is a collision?

A **hash table** stores data as key–value pairs and uses a hash function to map a key to a location. It is useful for fast lookup, insertion, and deletion; these operations are often **O(1) on average**.

A **collision** occurs when two different keys map to the same location or bucket. Implementations handle collisions using techniques such as chaining or open addressing. In the worst case, operations can take O(n).

### 10. Is hash table classification identical in every textbook? Explain.

No. Classification can vary by textbook and context. Many introductory explanations group arrays, stacks, queues, and linked lists as linear structures, and trees and graphs as nonlinear structures. A hash table is commonly described more specifically as an **associative key–value data structure**. Some sources group it under nonlinear structures, but there is no single classification convention used by every textbook.

The most important point is to understand how a hash table stores and retrieves key–value pairs using hashing.

### 11. Give examples of DSA collections in Python and C++.

| Concept | Python | C++ |
|---|---|---|
| Dynamic array / sequence | `list` | `vector` |
| Stack | `list` or `collections.deque` | `stack` |
| Queue | `collections.deque` | `queue` |
| Set | `set` | `set` or `unordered_set` |
| Key–value map / hash table | `dict` | `unordered_map` |
| Ordered key–value map | No direct built-in equivalent with the same guarantees; use a suitable library | `map` |
| Linked list | Usually implemented manually or through a library | `list` or `forward_list` |
| Tree / graph | Often implemented with classes, dictionaries, or lists | Often implemented with classes, vectors, maps, or adjacency lists |

The available operations and performance depend on the exact language feature or library. A Python `dict` and C++ `unordered_map`, for example, both provide hash-based key–value lookup.

### 12. Find the time complexity of a loop that visits each of n elements once.

The time complexity is **O(n)**, also commonly described as **Θ(n)** when each element is processed with constant work.

Example:

```python
for i in range(n):
    print(i)
```

The loop runs `n` times. If each iteration takes constant time, the total work grows linearly with `n`.
