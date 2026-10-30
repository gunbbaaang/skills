# Editable PowerPoint in terminal Codex

This skill is the Apache-2.0 slides workflow maintained in `JetBrains/skills`, with upstream OpenAI attribution retained. It uses ordinary PptxGenJS and included rendering/inspection scripts, not a proprietary desktop artifact runtime or an Anthropic account.

## Prepare the environment

- Use Node.js and an existing local `pptxgenjs` package if available. Otherwise create a deck working directory and run `npm install --save-exact pptxgenjs@4.0.1` there. Use `npm.cmd` on Windows when needed. This is the version smoke-tested for this bundle.
- Authoring `.pptx` needs Node and PptxGenJS. The included Python QA scripts additionally use Pillow, pdf2image, python-pptx and NumPy; install missing packages in a project virtual environment rather than altering system Python.
- Rendering needs LibreOffice (`soffice`) and Poppler (`pdfinfo`, `pdftoppm`). Font inspection can also require `fc-list`; availability differs on Windows. Check tools before promising PNG/PDF output or completed visual validation.
- If rendering is unavailable, preserve the `.pptx` and source `.js`, perform the available structural/content checks, and clearly label visual QA as not performed. Do not claim the slides fit merely because the file was generated. If that is insufficient for the user's submission, report the concrete missing tool.

## Korean hackathon decks

- Use the user's actual template when provided. Otherwise 16:9, readable Korean fonts available on the target machine, and native text/shapes/charts are suitable. Typical font candidates are Malgun Gothic or Noto Sans CJK KR, but inspect availability rather than assuming it.
- Keep editable text as text and simple charts as native charts. Screenshots of the working product may be images; do not flatten every slide into an image.
- Start from the actual interview notes, agreed problem, implementation, and test evidence. A useful outline for a short demo is: problem and user → evidence and constraints → chosen solution → working flow → verification → limitations and next step. Adapt the length to the official presentation time.
- Separate measured results, synthetic test data, proposed targets, and expected business impact. Do not invent employee quotes, measured savings, test outcomes, or production adoption.
- Deliver the `.pptx`, reproducible authoring source/assets, and a brief record of completed and incomplete checks. Public uploading is a separate requested action.
