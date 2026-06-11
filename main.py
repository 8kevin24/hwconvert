import argparse
from hwconvert.core import convert_files


def main():
    parser = argparse.ArgumentParser(description="HWConvert Multi Image → PDF")

    parser.add_argument("inputs", nargs="+", help="Input files (images)")
    parser.add_argument("--to", required=True, help="Target format (pdf)")

    args = parser.parse_args()

    output = convert_files(args.inputs, args.to)

    print(f"Created: {output}")


if __name__ == "__main__":
    main()