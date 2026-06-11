# hwconvert
a tool for converting files between formats(useful for gradescope submission). currently works for text formats and image to pdfs(the most common conversions needed for homeworks) only

supports: txt/md conversions, image to pdf, multiple image to pdf conversions

# usage and installation

install:

   
```bash
uv add "https://github.com/8kevin24/hwconvert/hwconvert.git"
```

usage: 

make sure the files you want to convert are in the same directory as the one you are running uv in
```bash
uv venv
uv run hwconvert img1.jpg img2.jpg --to pdf
```

you should see 
```bash
Created PDF: submission.pdf and the file in your directory
```

for txt/md conversions:
```bash
uv run hwconvert notes.txt --to md
uv run hwconvert notes.md --to txt
```


# known bugs
-for some reason txt to pdf generates output but it just strips the file of whitespace, doesn't actually generate pdf
