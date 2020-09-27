### Dependency Inversion Principle 
**In short:** High-level modules should not depend directly on low-level modules. They both should depend on abstraction.

Note: interfaces in Python - abstract base classes.

**[Full Explanation:](https://learning.oreilly.com/library/view/clean-code-in/9781788835831/33e93b2a-121f-4c68-9580-df663164f554.xhtml)**

The dependency inversion principle (DIP) proposes an interesting design principle by which we protect our code by making it independent of things that are fragile, volatile, or out of our control. 

The idea of inverting dependencies is that our code should not adapt to details or concrete implementations, but rather the other way around: we want to force whatever implementation or detail to adapt to our code via a sort of API.

Abstractions have to be organized in such a way that they do not depend on details, but rather the other way around—the details (concrete implementations) should depend on abstractions.
