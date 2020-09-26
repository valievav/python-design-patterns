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
            print(f'Finished writing data into {file.name}.')


if __name__ == "__main__":
    j = Journal()
    j.add_entry("I flied today.")
    j.add_entry("Today was a chill day.")
    j.add_entry("What a surprise!")
    j.save_to_file(os.getcwd(), "Journal_file.txt")
