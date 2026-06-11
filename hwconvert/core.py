from pathlib import Path
from hwconvert.converters import (
    txt_to_md,
    md_to_txt,
    txt_to_txt,
    txt_to_pdf_text,
    images_to_pdf
)


# =========================
# TEXT FILE CONVERSION
# =========================

def read_text(file_path: str) -> str:
    return Path(file_path).read_text(encoding="utf-8")


def write_text(file_path: str, content: str):
    Path(file_path).write_text(content, encoding="utf-8")


def convert_file(input_path: str, target_format: str) -> str:
    """
    Convert SINGLE text-based files.
    Supported:
        .txt -> md/txt/pdf
        .md  -> txt
    """

    content = read_text(input_path)
    suffix = Path(input_path).suffix.lower()

    if suffix == ".txt" and target_format == "md":
        return txt_to_md(content)

    elif suffix == ".md" and target_format == "txt":
        return md_to_txt(content)

    elif suffix == ".txt" and target_format == "txt":
        return txt_to_txt(content)

    elif suffix == ".txt" and target_format == "pdf":
        return txt_to_pdf_text(content)

    else:
        raise ValueError(
            f"Unsupported conversion: {suffix} -> {target_format}"
        )


# =========================
# IMAGE → PDF CONVERSION
# =========================

def convert_files(input_paths: list[str], target_format: str) -> str:
    """
    Convert MULTIPLE image files into a single PDF.
    Supported:
        jpg/png/... -> pdf
    """

    if target_format != "pdf":
        raise ValueError("Currently only image → pdf conversion is supported for multi-file input.")

    if not input_paths:
        raise ValueError("No input files provided.")

    output_path = "submission.pdf"

    images_to_pdf(input_paths, output_path)

    return output_path