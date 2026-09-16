
import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    n_arguments = len(sys.argv)
    if n_arguments == 1:
        print("No Arguments provided!")
    else:
        total = len(sys.argv) - 1
        print(f"Arguments received: {total}")
        i = 1
        while i < n_arguments:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {n_arguments}")


if __name__ == "__main__":
    main()
