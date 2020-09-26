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

    # no more save method in class


# move save into separate manager that can work with any class
class FilesManager:
    @staticmethod
    def save_to_file(path: str, file_name: str, data: iter) -> None:
        if not os.path.exists(path):
            raise Exception("Such path does not exists")

        with open(os.path.join(path, file_name), "w") as file:
            file.write('Saved from File Manager.')
            file.writelines('\n' + line for line in data)


j = Journal()
j.add_entry("I flied today.")
j.add_entry("Today was a chill day.")
j.add_entry("What a surprise!")

fm = FilesManager()
fm.save_to_file(os.getcwd(), "Journal_file.txt", j.entries)
