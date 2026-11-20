import re, sys, pathlib
full, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
text = full.read_text(encoding="utf-8")
parts = re.split(r"^<!-- source: (website/docs/[^ ]+) -->\n", text, flags=re.M)
n = 0
for i in range(1, len(parts), 2):
    rel = parts[i].removeprefix("website/docs/")
    rel = re.sub(r"\.mdx?$", ".md", rel)
    url = "https://hermes-agent.nousresearch.com/docs/" + re.sub(r"(/?index)?\.md$", "", rel)
    body = parts[i + 1].rstrip().removesuffix("---").rstrip() + "\n"
    dest = out / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(f"<!-- url: {url} -->\n{body}", encoding="utf-8")
    n += 1
print(n, "pages")
