# Single Responsibility Principle (or Separation of Concerns)

# https://learning.oreilly.com/library/view/clean-code-in/9781788835831/2ae22d34-6460-426b-ba8c-5dac49eb829f.xhtml
# The single responsibility principle (SRP) states that a software component (in general, a class) must have only one responsibility.
# The fact that the class has a sole responsibility means that it is in charge of doing just one concrete thing,
# and as a consequence of that, we can conclude that it must have only one reason to change.

import os


class Journal:
    def __init__(self):
        self.entries = []

    def add_entry(self, text: str) -> None:
        self.entries.append(f"Entry {len(self.entries)+1}: {text}")

    def remove_entry(self, index: int) -> None:
        del self.entries[index]

    def __str__(self) -> str:
        return "\n".join(self.entries)

    # save method is withing the main obj class (this can lead to God objects - too many different responsibilities)
    def save_to_file(self, path: str, file_name: str) -> None:
        if not os.path.exists(path):
            raise Exception("Such path does not exists")

        with open(os.path.join(path, file_name), "w") as file:
            file.write('Saved from class.')
            file.writelines('\n' + line for line in self.entries)


j = Journal()
j.add_entry("I flied today.")
j.add_entry("Today was a chill day.")
j.add_entry("What a surprise!")
j.save_to_file(os.getcwd(), "Journal_file.txt")
