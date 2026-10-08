import traceback

def test(func, cases, raw_output = False):
    for c in cases:
        out = ''
        try:
            out = func(c)
        except Exception as e:
            out = traceback.format_exception(e)[-1].strip()
        if raw_output:
            print(f'{repr(str(c))} -> {repr(str(out))}')
        else:
            print(f'{c} -> {out}')
