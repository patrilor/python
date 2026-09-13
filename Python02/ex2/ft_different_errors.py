def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 1
    else:
        return

def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    operation_number = 0
    while operation_number < 5:
        print(f"Testing operation {operation_number}...")
        try:
            garden_operations(operation_number)
            print("Operation completed successfully")
        except (
            ValueError,
            ZeroDivisionError,
            FileNotFoundError,
            TypeError,
        ) as error:
            error_name = error.__class__.__name__
            print(f"Caught {error_name}: {error}")
        operation_number += 1
        
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()


