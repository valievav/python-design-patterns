### Interface Segregation Principle 
**In short:** Class should not have redundant methods that are not used.

Note: interfaces in Python - abstract base classes.

**[Full Explanation:](https://learning.oreilly.com/library/view/clean-code-in/9781788835831/30a232ad-7d65-4804-a1e9-52c5297e1de5.xhtml)**

In Python, interfaces are implicitly defined by a class according to its methods. This is because Python follows the so-called duck typing principle.

In abstract terms, this means that the ISP states that, when we define an interface that provides multiple methods, it is better to instead break it down into multiple ones, each one containing fewer methods (preferably just one), with a very specific and accurate scope. 

By separating interfaces into the smallest possible units, to favor code reusability, each class that wants to implement one of these interfaces will most likely be highly cohesive given that it has a quite definite behavior and set of responsibilities.
