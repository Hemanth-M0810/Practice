from __future__ import annotations

def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of two numbers."""
    return a + b

def cli() -> None:
    """Simple CLI entrypoint."""
    import argparse
    parser = argparse.ArgumentParser(description="Add two numbers")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    args = parser.parse_args()
    result = add(args.a, args.b)
    print(result)

if __name__ == "__main__":
    cli()