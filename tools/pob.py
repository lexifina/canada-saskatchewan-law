"""Parse the Assembly's 'Progress of Bills' PDFs (grid layout): bill number, title, Royal Assent date. Facts only."""
import fitz, re, sys, json, warnings
from pathlib import Path
warnings.simplefilter('ignore')
MON = {m: i + 1 for i, m in enumerate('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split())}
def parse(path):
    out = []
    d = fitz.open(path)
    for pg in d:
        ws = pg.get_text('words')
        hdr = [w for w in ws if w[4] == 'Assent']
        if hdr and not [w for w in ws if w[4] == 'Reading']: continue
        if not hdr: continue
        ra_x = (hdr[0][0] + hdr[0][2]) / 2
        tl = [w for w in ws if w[4] == 'Title']; mb = [w for w in ws if w[4] == 'Member']
        tx0 = 84; tx1 = mb[0][0] - 12 if mb else 226
        bills = sorted([w for w in ws if w[0] < 45 and re.fullmatch(r'\d{1,3}', w[4]) and w[1] > hdr[0][3]], key=lambda w: w[1])
        dates = []
        for w in ws:
            if re.fullmatch(r'\d{4}-\d\d-\d\d', w[4]): dates.append(((w[0] + w[2]) / 2, w[1], w[4]))
        MN = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
        for w in ws:
            m = re.fullmatch(r'(\d{1,2})/(\d\d)', w[4])
            if m:
                c = [v for v in ws if re.fullmatch(r'(Jan|Feb|Mar|Apr|May|June?|July?|Aug|Sept?|Oct|Nov|Dec)\.?', v[4]) and -3 <= w[1] - v[1] < 14 and abs(v[0] - w[0]) < 30]
                if c:
                    v = min(c, key=lambda v: abs(w[1] - v[1]) + abs(v[0] - w[0]))
                    yy = int(m.group(2)); y = (2000 if yy < 50 else 1900) + yy
                    dates.append(((min(v[0], w[0]) + max(v[2], w[2])) / 2, v[1], f'{y}-{MN[v[4][:3].lower()]:02d}-{int(m.group(1)):02d}'))
        for i, w in enumerate(ws):
            if w[4] in MON and i + 2 < len(ws):
                a, b = ws[i + 1], ws[i + 2]
                m = re.fullmatch(r'(\d{1,2}),?', a[4])
                if m and abs(a[1] - w[1]) < 3:
                    if re.fullmatch(r'\d{4}', b[4]) and abs(b[1] - w[1]) < 3: y = b; 
                    else:
                        y = next((c for c in ws if re.fullmatch(r'\d{4}', c[4]) and 0 < c[1] - w[1] < 14 and abs(c[0] - w[0]) < 40), None)
                    if y: dates.append((w[0] + 14, w[1], f'{y[4]}-{MON[w[4]]:02d}-{int(m.group(1)):02d}'))
        for i, b in enumerate(bills):
            y0 = b[1] - 4; y1 = bills[i + 1][1] - 4 if i + 1 < len(bills) else 1e9
            tw = sorted([w for w in ws if tx0 <= w[0] < tx1 and y0 <= w[1] < y1 and w[4] not in ('EN', '*')], key=lambda w: (round(w[1] / 4), w[0]))
            title = ' '.join(w[4] for w in tw); title = re.split(r' / ', title)[0].strip().rstrip(','); title = re.sub(r' Public Bills Title$| Private Members.*$', '', title).replace('(No.1)', '(No. 1)')
            ra = [dt for (x, y, dt) in dates if y0 <= y < y1 and abs(x - ra_x) < 28]
            out.append({'num': int(b[4]), 'title': title, 'ra': ra[0] if ra else None})
    return out
if __name__ == '__main__':
    for r in parse(sys.argv[1]): print(r)
