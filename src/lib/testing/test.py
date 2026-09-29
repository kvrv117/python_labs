import traceback

def test(func, cases):
    for c in cases:
        out = ''
        try:
            out = func(c)
        except Exception as e:
            out = traceback.format_exception(e)[-1].strip()
        print(f'{c} -> {out}')
