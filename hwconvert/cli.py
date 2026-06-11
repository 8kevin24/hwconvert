import argparse
from hwconvert.core import convert_file, convert_files


def main():
    parser = argparse.ArgumentParser(
        description="HWConvert: file conversion tool (txt/md/images → pdf)"
    )

    parser.add_argument(
        "inputs",
        nargs="+",
        help="Input files (e.g. img1.jpg img2.jpg or notes.txt)"
    )

    parser.add_argument(
        "--to",
        required=True,
        help="Target format: txt, md, pdf"
    )

    args = parser.parse_args()

    # =========================
    # IMAGE MODE (multi-file → PDF)
    # =========================
    if args.to == "pdf" and any(
        f.lower().endswith((".jpg", ".jpeg", ".png")) for f in args.inputs
    ):
        output = convert_files(args.inputs, "pdf")
        print(f"Created PDF: {output}")
        return

    # =========================
    # SINGLE FILE MODE
    # =========================
    if len(args.inputs) == 1:
        input_file = args.inputs[0]
        result = convert_file(input_file, args.to)

        output_file = input_file.rsplit(".", 1)[0] + f"_converted.{args.to}"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result)

        print(f"Created: {output_file}")
        return

    raise ValueError("Unsupported input combination")