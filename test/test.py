import clang.cindex

def print_function_names(node):
    if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
        print(f"Function: {node.spelling}")

    for child in node.get_children():
        print_function_names(child)

def main(source_file):
    # Initialize the index
    index = clang.cindex.Index.create()

    # Parse the source file
    translation_unit = index.parse(source_file)

    # Get the root cursor
    root_cursor = translation_unit.cursor

    # Print function names
    print_function_names(root_cursor)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <source-file>")
        sys.exit(1)

    source_file = sys.argv[1]
    main(source_file)
