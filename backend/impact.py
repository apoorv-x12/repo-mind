# backend/impact.py
def find_impacted(file, all_chunks):
    impacted = set()
    name = file.split("/")[-1].replace(".py", "")

    for c in all_chunks:
        if name in c["content"]:
            impacted.add(c["file"])

    return list(impacted)
