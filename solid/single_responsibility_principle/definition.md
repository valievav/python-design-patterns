### Single Responsibility Principle 
**In short:** 1 class/method - 1 responsibility

**[Full Explanation:](https://learning.oreilly.com/library/view/clean-code-in/9781788835831/2ae22d34-6460-426b-ba8c-5dac49eb829f.xhtml)**

The single responsibility principle (SRP) states that a software component (in general, a class) must have only one responsibility.

The fact that the class has a sole responsibility means that it is in charge of doing just one concrete thing,
and as a consequence of that, we can conclude that it must have only one reason to change.

Only if one thing on the domain problem changes will the class have to be updated.

If we have to make modifications to a class, for different reasons, it means the abstraction is incorrect,
and that the class has too many responsibilities.
