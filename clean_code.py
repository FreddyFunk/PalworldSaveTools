import tokenize, io, os
def clean_python_code(source_code):
    result = []
    tokens = tokenize.generate_tokens(io.StringIO(source_code).readline)
    prev_toktype = None
    for toktype, ttext, start, end, line in tokens:
        if toktype == tokenize.COMMENT:
            continue
        if toktype == tokenize.STRING:
            if ttext.strip().startswith(('"""', "'''")):
                if start[1] == 0 or prev_toktype in (tokenize.INDENT, tokenize.NEWLINE, tokenize.NL):
                    continue
        if toktype in (tokenize.NL, tokenize.NEWLINE):
            if prev_toktype in (tokenize.NL, tokenize.NEWLINE, None):
                continue
        result.append((toktype, ttext))
        prev_toktype = toktype
    return tokenize.untokenize(result)
def run_cleanup(root_dir):
    ignore_folders = {'pst_venv', 'venv', '.venv', '.git', '__pycache__', 'node_modules'}
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ignore_folders]
        for file in files:
            if file.endswith('.py') and file != 'clean_code.py':
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                cleaned = clean_python_code(content)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned)