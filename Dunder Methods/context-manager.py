class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "r")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileHandler("example.txt") as f:
    print(f.read())  # Reads the content of example.txt