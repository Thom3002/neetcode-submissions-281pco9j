class TextEditor:
    def __init__(self) -> None:
        self.rows = []
        self.undo_stack = []
        self.redo_stack = []

        return

    def addText(self, row: int, column: int, text: str) -> None:
        cmd = AddCommand(self, row, column, text)
        cmd.execute()

        self.undo_stack.append(cmd)
        self.redo_stack.clear()
        return

    def deleteText(self, row: int, startColumn: int, length: int) -> None:
        cmd = DeleteCommand(self, row, startColumn, length)
        cmd.execute()

        self.undo_stack.append(cmd)
        self.redo_stack.clear()
        return

    def undo(self) -> None:
        if not self.undo_stack:
            return

        cmd = self.undo_stack.pop()
        cmd.undo()
        self.redo_stack.append(cmd)

        return

    def redo(self) -> None:
        if not self.redo_stack:
            return
        cmd = self.redo_stack.pop()
        cmd.execute()
        self.undo_stack.append(cmd)

        return

    def readLine(self, row: int) -> str:
        return self.rows[row]

    def _insert(self, row: int, column: int, text: str) -> None:
        if row == len(self.rows):
            self.rows.append('')

        line = self.rows[row]
        self.rows[row] = line[:column] + text + line[column:]
        return

    def _delete(self, row: int, startColumn: int, length: int) -> str:
        line = self.rows[row]
        deleted_text = line[startColumn: startColumn + length]
        self.rows[row] = line[:startColumn] + line[startColumn + length:]
        return deleted_text



class AddCommand:
    def __init__(self, editor: TextEditor, row: int, column: int, text: str) -> None:
        self.editor = editor
        self.row = row
        self.column = column
        self.text = text
        return

    def execute(self) -> None:
        self.editor._insert(self.row, self.column, self.text)
        return

    def undo(self) -> None:
        self.editor._delete(self.row, self.column, len(self.text))



class DeleteCommand:
    def __init__(self, editor: TextEditor, row: int, column: int, length: int) -> None:
        self.editor = editor
        self.row = row
        self.column = column
        self.length = length
        self.deleted_text = ''
        return

    def execute(self) -> None:
        self.deleted_text = self.editor._delete(self.row, self.column, self.length)
        return

    def undo(self) -> None:
        self.editor._insert(self.row, self.column, self.deleted_text)


if __name__ == "__main__":
    e = TextEditor()

    print("Example 1")
    e.addText(0, 0, "hello")
    print(e.readLine(0))  # hello

    e.addText(1, 0, "world")
    print(e.readLine(1))  # world

    print("\nExample 2")
    e.addText(0, 5, "-there")
    print(e.readLine(0))  # hello-there

    e.deleteText(0, 5, 6)
    print(e.readLine(0))  # hello

    e.undo()
    print(e.readLine(0))  # hello-there

    e.redo()
    print(e.readLine(0))  # hello

    print("\nExample 3")
    e.addText(1, 5, "-wide web")
    print(e.readLine(1))  # world-wide web

    e.deleteText(1, 5, 5)
    print(e.readLine(1))  # world web

    e.undo()
    print(e.readLine(1))  # world-wide web

    print("\nExample 4")
    e.addText(0, 5, "!")
    print(e.readLine(0))  # hello!

    e.addText(0, 6, "!")
    print(e.readLine(0))  # hello!!

    e.undo()
    print(e.readLine(0))  # hello!

    e.undo()
    print(e.readLine(0))  # hello

    e.redo()
    print(e.readLine(0))  # hello!

    e.addText(0, 6, "?")
    print(e.readLine(0))  # hello!?

    e.redo()
    print(e.readLine(0))  # hello!?

    print("\nExample 5")
    e2 = TextEditor()
    e2.addText(0, 0, "aa bb-cc")
    e2.deleteText(0, 0, 8)
    print("'" + e2.readLine(0) + "'")  # ''

    e2.undo()
    print(e2.readLine(0))  # aa bb-cc

    print("\nExample 6")
    e3 = TextEditor()
    e3.addText(0, 0, "world")
    e3.addText(0, 0, "hello-")
    print(e3.readLine(0))  # hello-world
