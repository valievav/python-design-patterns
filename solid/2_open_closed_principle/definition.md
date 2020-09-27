### Opened-Closed Principle 
**In short:** Class/method should be opened for extension, closed for modification

**[Full Explanation:](https://learning.oreilly.com/library/view/clean-code-in/9781788835831/4e44acb4-51ce-4f65-b94e-08a86e54ef9f.xhtml)**

When designing a class, for instance, we should carefully encapsulate the logic so that it has good maintenance, 
meaning that we will want it to be open to extension but closed for modification.

What this means in simple terms is that, of course, we want our code to be extensible, to adapt to new requirements, or changes in the domain problem. 

This means that, when something new appears on the domain problem, we only want to add new things to our model, not change anything existing that is closed to modification.

If, for some reason, when something new has to be added, we found ourselves modifying the code, then that logic is probably poorly designed. 

Ideally, when requirements change, we want to just have to extend the module with the new required behavior in order to comply with the new requirements, but without having to modify the code.
