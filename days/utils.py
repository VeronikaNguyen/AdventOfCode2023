class FileReader:
    filename: str

    def __init__(self, filename):
        self.filename = filename

    def read_lines(self) -> list[str]:
        with open(self.filename) as file:
            lines = [line.rstrip() for line in file]
        return lines
