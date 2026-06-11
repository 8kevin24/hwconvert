from PIL import Image


# =========================
# TEXT CONVERTERS
# =========================

def txt_to_txt(content: str) -> str:
    return content.strip()


def txt_to_md(content: str) -> str:
    return content.strip() + "\n"


def md_to_txt(content: str) -> str:
    """
    Very simple markdown stripper (starter version).
    Removes '#' and trims whitespace.
    """
    lines = content.splitlines()
    cleaned = [line.replace("#", "").strip() for line in lines]
    return "\n".join(cleaned)


def txt_to_pdf_text(content: str) -> str:
    """
    Placeholder for PDF export (text preparation only).
    Real PDF generation is handled elsewhere (e.g. reportlab or Pillow).
    """
    return content.strip()


# =========================
# IMAGE → PDF CONVERTER
# =========================

def images_to_pdf(image_paths: list[str], output_path: str):
    """
    Combine multiple images into a single PDF.

    Example:
        images_to_pdf(["a.jpg", "b.png"], "submission.pdf")
    """

    if not image_paths:
        raise ValueError("No images provided for PDF conversion.")

    images = []

    try:
        # Load and convert images
        for path in image_paths:
            img = Image.open(path)

            # PDF requires RGB mode
            if img.mode != "RGB":
                img = img.convert("RGB")

            images.append(img)

        # Save as multi-page PDF
        first_img = images[0]
        rest = images[1:]

        first_img.save(
            output_path,
            save_all=True,
            append_images=rest
        )

    finally:
        # Always close files to avoid resource leaks
        for img in images:
            img.close()