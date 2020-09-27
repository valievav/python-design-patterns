### Liskov Substitution Principle 
**In short:** child class should be able to replace parent class w/o any impact to functionality.

**[Full Explanation:](https://learning.oreilly.com/library/view/clean-code-in/9781788835831/59d0a137-8f2d-4808-84df-e459e091df98.xhtml)**

The main idea behind LSP is that, for any class, a client should be able to use any of its subtypes indistinguishably, without even noticing, and therefore without compromising the expected behavior at runtime. 

This means that clients are completely isolated and unaware of changes in the class hierarchy.

More formally, this is the original definition (LISKOV 01) of Liskov's substitution principle: if S is a subtype of T, then objects of type T may be replaced by objects of type S, without breaking the program.
