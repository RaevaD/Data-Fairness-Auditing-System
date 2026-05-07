import streamlit as st


def _inject_styles():
    st.markdown("""
<style>
.fa-card {
    background: linear-gradient(145deg,#0e0c1e 0%,#13102a 100%);
    border: 1px solid #22204a;
    border-radius: 14px;
    padding: 22px 24px 18px;
    margin-bottom: 8px;
    position: relative;
}
.fa-card::after {
    content:'';
    position:absolute;
    top:0;left:0;right:0;
    height:1px;
    background:linear-gradient(90deg,transparent,#3d3880 50%,transparent);
    border-radius:14px 14px 0 0;
}
.fa-header {
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:16px;
}
.fa-attr {
    font-family:'Syne',sans-serif !important;
    font-size:18px !important;
    font-weight:700 !important;
    color:#e8e0ff !important;
    letter-spacing:-0.3px;
}
.fa-pill-fair {
    font-family:'DM Mono',monospace !important;
    font-size:11px !important;
    font-weight:600 !important;
    letter-spacing:0.5px;
    color:#3dd68c !important;
    background:rgba(29,158,117,0.13) !important;
    border:1px solid rgba(29,158,117,0.4) !important;
    border-radius:999px !important;
    padding:5px 15px !important;
    box-shadow:0 0 10px rgba(29,158,117,0.18);
    white-space:nowrap;
}
.fa-pill-unfair {
    font-family:'DM Mono',monospace !important;
    font-size:11px !important;
    font-weight:600 !important;
    letter-spacing:0.5px;
    color:#ff8080 !important;
    background:rgba(255,107,107,0.11) !important;
    border:1px solid rgba(255,107,107,0.35) !important;
    border-radius:999px !important;
    padding:5px 15px !important;
    box-shadow:0 0 10px rgba(255,107,107,0.14);
    white-space:nowrap;
}
.fa-metrics {
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:10px;
    margin-bottom:18px;
}
.fa-metric {
    background:#09071a;
    border:1px solid #1b1940;
    border-radius:10px;
    padding:14px 8px;
    text-align:center;
}
.fa-mval {
    font-family:'DM Mono',monospace !important;
    font-size:22px !important;
    font-weight:600 !important;
    color:#5dcaa5 !important;
    line-height:1.1;
    margin-bottom:5px;
}
.fa-mlbl {
    font-family:'DM Mono',monospace !important;
    font-size:11px !important;
    color:#5dcaa5 !important;
    text-transform:uppercase;
    letter-spacing:0.5px;
    opacity:0.6;
}
.fa-bar-row { margin-bottom:22px; }
.fa-bar-lbl {
    display:flex;
    justify-content:space-between;
    align-items:baseline;
    gap:16px;
    font-family:'DM Mono',monospace !important;
    font-size:15px !important;
    color:#8e8bc0 !important;
    margin-bottom:10px;
}
.fa-algo-name {
    font-family:'Syne',sans-serif !important;
    font-size:19px !important;
    font-weight:700 !important;
    color:#f5c842 !important;
    text-shadow: 0 0 12px rgba(245,200,66,0.5), 0 0 24px rgba(245,200,66,0.25);
    letter-spacing:-0.2px;
}
.fa-algo-threshold {
    font-family:'DM Mono',monospace !important;
    font-size:14px !important;
    color:#5a5890 !important;
    margin-left:10px;
}
.fa-track {
    height:10px;
    background:#09071a;
    border-radius:5px;
    position:relative;
    overflow:visible;
}
.fa-fill {
    height:10px;
    border-radius:5px;
    position:absolute;
    top:0;
    transition:width .6s cubic-bezier(.4,0,.2,1);
}
.fa-marker {
    position:absolute;
    top:-4px;
    width:2px;
    height:18px;
    border-radius:1px;
}
.fa-axis {
    display:flex;
    justify-content:space-between;
    font-family:'DM Mono',monospace !important;
    font-size:13px !important;
    color:#5a5890 !important;
    margin-top:6px;
}
.fa-caption {
    font-family:'DM Mono',monospace !important;
    font-size:15px !important;
    font-weight:500 !important;
    margin-top:8px;
}
.fa-page-title {
    font-family:'Syne',sans-serif !important;
    font-size:26px !important;
    font-weight:700 !important;
    color:#f0ecff !important;
    letter-spacing:-0.5px;
    margin-bottom:2px;
}
.fa-page-sub {
    font-family:'DM Mono',monospace !important;
    font-size:11px !important;
    color:#38366a !important;
    letter-spacing:0.3px;
    margin-bottom:24px;
}
.fa-summary {
    display:flex;
    gap:12px;
    margin-bottom:20px;
}
.fa-sum-box {
    flex:1;
    background:#09071a;
    border:1px solid #1b1940;
    border-radius:10px;
    padding:12px;
    text-align:center;
}
.fa-sum-val {
    font-family:'DM Mono',monospace !important;
    font-size:26px !important;
    font-weight:600 !important;
    line-height:1;
    margin-bottom:4px;
}
.fa-sum-lbl {
    font-family:'DM Mono',monospace !important;
    font-size:10px !important;
    color:#38366a !important;
    text-transform:uppercase;
    letter-spacing:0.5px;
}
.fa-err {
    background:#120613;
    border:1px solid #340e25;
    border-radius:10px;
    padding:14px 18px;
    margin-bottom:14px;
}
.fa-err-title {
    font-family:'Syne',sans-serif !important;
    font-size:14px !important;
    font-weight:600 !important;
    color:#afa9ec !important;
    margin-bottom:4px;
}
.fa-err-msg {
    font-family:'DM Mono',monospace !important;
    font-size:11px !important;
    color:#e07090 !important;
}

/* ── AI explanation boxes ── */
.ai-box {
    background: linear-gradient(145deg,#0e0c1e 0%,#13102a 100%);
    border: 1px solid #22204a;
    border-radius: 14px;
    padding: 22px 26px;
    margin-bottom: 14px;
}
.ai-section-title {
    font-family:'Syne',sans-serif !important;
    font-size:18px !important;
    font-weight:700 !important;
    color:#f5c842 !important;
    letter-spacing:-0.2px;
    margin-bottom:14px;
    padding-bottom:10px;
    border-bottom:1px solid #22204a;
}
.ai-subtitle {
    font-family:'Syne',sans-serif !important;
    font-size:14px !important;
    font-weight:700 !important;
    color:#f5c842 !important;
    margin-top:14px;
    margin-bottom:4px;
}
.ai-body {
    font-family:'DM Mono',monospace !important;
    font-size:13px !important;
    color:#b0a8e0 !important;
    line-height:1.75 !important;
}
.ai-bullet {
    font-family:'DM Mono',monospace !important;
    font-size:13px !important;
    color:#b0a8e0 !important;
    line-height:1.75 !important;
    padding-left:12px;
    border-left:2px solid #2a2560;
    margin-bottom:6px;
}
.rem-priority-title {
    font-family:'Syne',sans-serif !important;
    font-size:18px !important;
    font-weight:700 !important;
    color:#f5c842 !important;
    margin-bottom:12px;
    padding-bottom:10px;
    border-bottom:1px solid #22204a;
}
.rem-sub {
    font-family:'Syne',sans-serif !important;
    font-size:14px !important;
    font-weight:700 !important;
    color:#f5c842 !important;
    margin-bottom:10px;
    margin-top:4px;
}
.rem-item {
    background: linear-gradient(145deg,#0e0c1e 0%,#13102a 100%);
    border:1px solid #22204a;
    border-radius:10px;
    padding:16px 20px;
    margin-bottom:10px;
}
.rem-label {
    font-family:'DM Mono',monospace !important;
    font-size:11px !important;
    color:#f5c842 !important;
    text-transform:uppercase;
    letter-spacing:0.6px;
    margin-bottom:3px;
}
.rem-text {
    font-family:'DM Mono',monospace !important;
    font-size:13px !important;
    color:#b0a8e0 !important;
    line-height:1.75 !important;
}
.rem-caption {
    font-family:'DM Mono',monospace !important;
    font-size:11px !important;
    color:#38366a !important;
    margin-top:5px;
}
</style>
""", unsafe_allow_html=True)


def _metric_color(val, threshold, above_good=True):
    if val is None:
        return '#5a5480'
    good = (float(val) >= threshold) if above_good else (abs(float(val)) <= threshold)
    return '#3dd68c' if good else '#ff8080'


def _di_bar(di):
    if di is None:
        return
    di_val = float(di)
    fill_pct = min(di_val / 1.2 * 100, 100)
    threshold_pct = round(0.8 / 1.2 * 100, 1)
    good = di_val >= 0.8
    fill_color = 'linear-gradient(90deg,#1d9e75,#3dd68c)' if good else 'linear-gradient(90deg,#b83030,#ff6b6b)'
    caption_color = '#1d9e75' if good else '#ff8080'
    caption = 'Within threshold' if good else 'Below threshold — bias detected'
    st.markdown(
        '<div class="fa-bar-row">'
        '<div class="fa-bar-lbl">'
        '<span>'
        '<span class="fa-algo-name">Disparate Impact</span>'
        '<span class="fa-algo-threshold">&middot;&nbsp; fair if &ge; 0.8</span>'
        '</span>'
        '<span style="color:' + caption_color + ';font-size:18px;font-weight:700;">' + str(round(di_val, 3)) + '</span>'
        '</div>'
        '<div class="fa-track">'
        '<div class="fa-fill" style="width:' + str(fill_pct) + '%;background:' + fill_color + ';"></div>'
        '<div class="fa-marker" style="left:' + str(threshold_pct) + '%;width:3px;background:rgba(175,169,236,0.85);box-shadow:0 0 6px rgba(175,169,236,0.5);"></div>'
        '</div>'
        '<div class="fa-caption" style="color:' + caption_color + ';">' + caption + '</div>'
        '</div>',
        unsafe_allow_html=True
    )


def _spd_bar(spd):
    if spd is None:
        return
    spd_val = float(spd)
    abs_spd = abs(spd_val)
    good = abs_spd <= 0.1
    bar_color = 'linear-gradient(90deg,#1d9e75,#3dd68c)' if good else 'linear-gradient(90deg,#b83030,#ff6b6b)'
    caption_color = '#1d9e75' if good else '#ff8080'
    caption = 'Within &plusmn;0.1 threshold' if good else 'Exceeds &plusmn;0.1 threshold &mdash; bias detected'
    if spd_val >= 0:
        bar_left = 50
        bar_width = min(spd_val * 50, 50)
    else:
        bar_width = min(abs_spd * 50, 50)
        bar_left = 50 - bar_width
    st.markdown(
        '<div class="fa-bar-row">'
        '<div class="fa-bar-lbl">'
        '<span>'
        '<span class="fa-algo-name">Statistical Parity Difference</span>'
        '<span class="fa-algo-threshold">&middot;&nbsp; fair if within &plusmn;0.1</span>'
        '</span>'
        '<span style="color:' + caption_color + ';font-size:18px;font-weight:700;">' + str(round(spd_val, 3)) + '</span>'
        '</div>'
        '<div class="fa-track" style="background:#09071a;">'
        '<div class="fa-fill" style="left:' + str(bar_left) + '%;width:' + str(bar_width) + '%;background:' + bar_color + ';"></div>'
        '<div style="position:absolute;left:50%;top:-4px;width:3px;height:18px;background:rgba(175,169,236,0.85);transform:translateX(-50%);border-radius:1px;box-shadow:0 0 6px rgba(175,169,236,0.5);"></div>'
        '</div>'
        '<div class="fa-axis"><span>&minus;1</span><span>&minus;0.5</span><span>0</span><span>+0.5</span><span>+1</span></div>'
        '<div class="fa-caption" style="color:' + caption_color + ';">' + caption + '</div>'
        '</div>',
        unsafe_allow_html=True
    )


def _dp_bar(dp):
    if dp is None:
        return
    dp_val = float(dp)
    abs_dp = abs(dp_val)
    good = abs_dp <= 0.1
    bar_color = 'linear-gradient(90deg,#1d9e75,#3dd68c)' if good else 'linear-gradient(90deg,#b83030,#ff6b6b)'
    caption_color = '#1d9e75' if good else '#ff8080'
    caption = 'Within &plusmn;0.1 threshold' if good else 'Exceeds &plusmn;0.1 threshold &mdash; bias detected'
    if dp_val >= 0:
        bar_left = 50
        bar_width = min(dp_val * 50, 50)
    else:
        bar_width = min(abs_dp * 50, 50)
        bar_left = 50 - bar_width
    st.markdown(
        '<div class="fa-bar-row">'
        '<div class="fa-bar-lbl">'
        '<span>'
        '<span class="fa-algo-name">Demographic Parity</span>'
        '<span class="fa-algo-threshold">&middot;&nbsp; fair if within &plusmn;0.1</span>'
        '</span>'
        '<span style="color:' + caption_color + ';font-size:18px;font-weight:700;">' + str(round(dp_val, 3)) + '</span>'
        '</div>'
        '<div class="fa-track" style="background:#09071a;">'
        '<div class="fa-fill" style="left:' + str(bar_left) + '%;width:' + str(bar_width) + '%;background:' + bar_color + ';"></div>'
        '<div style="position:absolute;left:50%;top:-4px;width:3px;height:18px;background:rgba(175,169,236,0.85);transform:translateX(-50%);border-radius:1px;box-shadow:0 0 6px rgba(175,169,236,0.5);"></div>'
        '</div>'
        '<div class="fa-axis"><span>&minus;1</span><span>&minus;0.5</span><span>0</span><span>+0.5</span><span>+1</span></div>'
        '<div class="fa-caption" style="color:' + caption_color + ';">' + caption + '</div>'
        '</div>',
        unsafe_allow_html=True
    )


def _attribute_card(attribute, results):
    is_fair = results.get('is_fair', False) or (
        results.get('is_fair_di', False) and results.get('is_fair_spd', True)
    )
    pill_class = 'fa-pill-fair' if is_fair else 'fa-pill-unfair'
    pill_text  = '&#10003; FAIR' if is_fair else '&#9679; UNFAIR'

    di  = results.get('disparate_impact')
    dp  = results.get('demographic_parity')
    spd = results.get('spd') or results.get('statistical_parity_difference')

    di_str  = str(round(float(di),  3)) if di  is not None else '&mdash;'
    dp_str  = str(round(float(dp),  3)) if dp  is not None else '&mdash;'
    spd_str = str(round(float(spd), 3)) if spd is not None else '&mdash;'

    priv   = results.get('privileged_group', '')
    unpriv = results.get('unprivileged_group', '')
    show_groups = priv and not (str(priv).startswith('(') and ',' in str(priv))
    group_hint = (
        '<div style="font-family:DM Mono,monospace;font-size:11px;color:#5dcaa5;opacity:0.5;'
        'margin-top:-10px;margin-bottom:14px;">'
        'Privileged: ' + str(priv) + ' &nbsp;&middot;&nbsp; Unprivileged: ' + str(unpriv) + '</div>'
    ) if show_groups else ''

    st.markdown(
        '<div class="fa-card">'
        '<div class="fa-header">'
        '<span class="fa-attr">' + attribute.capitalize() + '</span>'
        '<span class="' + pill_class + '">' + pill_text + '</span>'
        '</div>'
        + group_hint +
        '<div class="fa-metrics">'
        '<div class="fa-metric">'
        '<div class="fa-mval">' + di_str + '</div>'
        '<div class="fa-mlbl">Disparate Impact</div>'
        '</div>'
        '<div class="fa-metric">'
        '<div class="fa-mval">' + dp_str + '</div>'
        '<div class="fa-mlbl">Demographic Parity</div>'
        '</div>'
        '<div class="fa-metric">'
        '<div class="fa-mval">' + spd_str + '</div>'
        '<div class="fa-mlbl">SPD</div>'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    _di_bar(di)
    _dp_bar(dp)
    _spd_bar(spd)


def _clean_markdown(text):
    """
    Strip ALL markdown syntax from a string — no bold, no headings, no asterisks.
    Used for plain-text rendering where we want zero formatting artifacts.
    """
    import re
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)   # **bold** → plain text
    text = re.sub(r'\*(.+?)\*', r'\1', text)         # *italic* → plain text
    text = re.sub(r'`(.+?)`', r'\1', text)           # `code` → plain text
    text = re.sub(r'^#+\s*', '', text)               # leading # markers
    return text.strip()


# Section label patterns Gemini may output as plain-text headings (no ## markers)
_PLAIN_SECTION_LABELS = (
    'Summary:',
    'Key Issues:',
    'Recommended Actions:',
    'Real-World Impact:',
    'Fairness Summary:',
)


def _render_ai_text(text):
    """
    Convert Gemini output into consistently styled HTML.

    Handles two heading styles:
      A) Markdown: ## Summary  → yellow ai-subtitle
      B) Plain:    Summary:    → yellow ai-subtitle  (for quality summary plain-text format)

    Color rules — strict:
      - Headings (both styles) → yellow, heading text only
      - Numbered items         → yellow number + blue body text on its own line
      - Bullets / body         → always #b0a8e0 blue, never yellow
      - Inline **bold**        → stripped to plain text, weight 700, SAME blue color

    No yellow ever bleeds into body text.
    """
    if not text:
        return ''

    import re

    BODY_STYLE = (
        "font-family:'DM Mono',monospace;"
        "font-size:13px;color:#b0a8e0;line-height:1.75;"
    )

    def inline_bold(s):
        """Bold = same #b0a8e0 color, weight 700. Strips backtick spans."""
        s = re.sub(r'`(.+?)`', r'\1', s)
        s = re.sub(r'\*\*(.+?)\*\*',
                   r'<strong style="font-weight:700;color:#b0a8e0;">\1</strong>', s)
        return s

    lines = text.split('\n')
    # Pre-process: split section labels and sentences onto individual lines
    # even when Gemini concatenates everything into one long string.
    expanded = []
    for raw_line in lines:
        raw_line = raw_line.strip()
        if not raw_line:
            expanded.append('')
            continue
        # Insert newline before any section label that appears mid-line
        for lbl in _PLAIN_SECTION_LABELS:
            idx = raw_line.find(lbl)
            if idx > 0:
                raw_line = raw_line[:idx] + '\n' + raw_line[idx:]
        expanded.extend(raw_line.split('\n'))

    # Second pass: within list sections (Key Issues / Recommended Actions),
    # split plain body sentences onto individual lines so each renders as its own block.
    final = []
    in_list_section = False
    for raw_line in expanded:
        stripped = raw_line.strip()
        if any(stripped == lbl or stripped.startswith(lbl)
               for lbl in ('Key Issues:', 'Recommended Actions:', 'Real-World Impact:')):
            in_list_section = True
            label = next(lbl for lbl in _PLAIN_SECTION_LABELS
                         if stripped == lbl or stripped.startswith(lbl))
            final.append(label)
            remainder = stripped[len(label):].strip()
            if remainder:
                sentences = re.split(r'(?<=\.)\s+', remainder)
                final.extend(s.strip() for s in sentences if s.strip())
        elif stripped.startswith('Summary:') or stripped.startswith('Fairness Summary:'):
            in_list_section = False
            final.append(stripped)
        elif in_list_section and stripped and not re.match(r'^#+\s+', stripped) \
                and not re.match(r'^\d+\.\s', stripped) \
                and not stripped.startswith('- ') and not stripped.startswith('* '):
            # Split plain sentences into individual lines
            sentences = re.split(r'(?<=\.)\s+', stripped)
            final.extend(s.strip() for s in sentences if s.strip())
        else:
            in_list_section = False
            final.append(stripped)
    lines = final
    html = ''

    for line in lines:
        line = line.strip()

        # ── blank line ────────────────────────────────────────────────
        if not line:
            html += '<div style="height:6px;"></div>'

        # ── markdown heading: ## Heading ──────────────────────────────
        elif re.match(r'^#+\s+', line):
            heading_text = re.sub(r'^#+\s+', '', line)
            heading_text = _clean_markdown(heading_text)
            html += (
                '<div class="ai-subtitle" style="margin-top:16px;margin-bottom:4px;">'
                + heading_text + '</div>'
            )

        # ── plain-text section label: "Summary:", "Key Issues:", etc. ─
        elif any(line == lbl or line.startswith(lbl) for lbl in _PLAIN_SECTION_LABELS):
            # Extract just the label part (up to and including the colon)
            label = next(lbl for lbl in _PLAIN_SECTION_LABELS
                         if line == lbl or line.startswith(lbl))
            html += (
                '<div class="ai-subtitle" style="margin-top:16px;margin-bottom:4px;">'
                + label + '</div>'
            )
            # If there's text after the label on the same line, render it as body
            remainder = line[len(label):].strip()
            if remainder:
                html += (
                    f'<div style="display:block;margin-bottom:2px;{BODY_STYLE}">'
                    + inline_bold(remainder) + '</div>'
                )

        # ── numbered item: "1. text" ──────────────────────────────────
        elif re.match(r'^\d+\.\s', line):
            dot_pos = line.index('. ')
            num  = line[:dot_pos + 1]
            rest = inline_bold(line[dot_pos + 2:])
            html += (
                f'<div style="display:block;margin-top:6px;margin-bottom:6px;{BODY_STYLE}">'
                f'<span style="color:#f5c842;font-weight:700;margin-right:8px;">{num}</span>'
                f'<span style="color:#b0a8e0;">{rest}</span>'
                '</div>'
            )

        # ── bullet: "- item" or "* item" ─────────────────────────────
        elif line.startswith('- ') or line.startswith('* '):
            content = inline_bold(line[2:])
            html += (
                f'<div style="display:block;margin-top:4px;margin-bottom:4px;'
                f'padding-left:12px;border-left:2px solid #2a2560;{BODY_STYLE}">'
                + content + '</div>'
            )

        # ── plain body ────────────────────────────────────────────────
        else:
            content = inline_bold(line)
            html += (
                f'<div style="display:block;margin-bottom:2px;{BODY_STYLE}">'
                + content + '</div>'
            )

    return html


def _render_rem_text(text):
    """
    Render remediation field text (issue / fix / technique / verification).
    - Strips all ** bold markers — converts bold labels to plain bold weight
    - Splits inline numbered sub-points (1. 2. 3. embedded in one string) onto new lines
    - Strips backtick code spans to plain text
    - All text is the same #b0a8e0 blue as ai-body, same DM Mono font
    """
    import re

    if not text:
        return ''

    BODY_STYLE = (
        "font-family:'DM Mono',monospace;"
        "font-size:13px;color:#b0a8e0;line-height:1.75;"
    )

    # Strip backtick spans and convert **bold** to weight-only bold (same color)
    text = re.sub(r'`(.+?)`', r'\1', text)
    text = re.sub(
        r'\*\*(.+?)\*\*',
        r'<strong style="font-weight:700;color:#b0a8e0;">\1</strong>',
        text
    )

    # Split inline numbered sub-points onto separate lines
    # e.g. "Do X. 1. Step one 2. Step two" → ["Do X.", "1. Step one", "2. Step two"]
    parts = re.split(r'(?<!\d)(?=\d+\.\s)', text)

    html = ''
    for part in parts:
        part = part.strip()
        if not part:
            continue
        # Check if this part starts with a number like "1. "
        if re.match(r'^\d+\.\s', part):
            dot_pos = part.index('. ')
            num  = part[:dot_pos + 1]
            rest = part[dot_pos + 2:]
            html += (
                f'<div style="display:block;margin-top:6px;{BODY_STYLE}">'
                f'<span style="color:#f5c842;font-weight:700;margin-right:6px;">{num}</span>'
                f'<span style="color:#b0a8e0;">{rest}</span>'
                '</div>'
            )
        else:
            html += (
                f'<div style="display:block;margin-bottom:4px;{BODY_STYLE}">'
                + part +
                '</div>'
            )

    return html


def show_fairness_page(BASE_URL):
    _inject_styles()

    st.markdown('<div class="fa-page-title">Fairness Audit</div>', unsafe_allow_html=True)
    st.markdown('<div class="fa-page-sub">Bias detection across protected demographic attributes</div>', unsafe_allow_html=True)

    if not st.session_state.fairness_result:
        st.warning('No fairness audit run yet. Go to Quality Report and click "Run Fairness Audit".')
        return

    result        = st.session_state.fairness_result
    fairness_data = result.get('fairness_audit') or result.get('fairness') or {}
    audit         = fairness_data.get('results') or fairness_data or {}
    audit         = {k: v for k, v in audit.items() if isinstance(v, dict)}

    if not audit:
        st.markdown(
            '<div class="ai-box">'
            '<div class="ai-section-title">No Protected Attributes</div>'
            '<div class="ai-body">No protected demographic columns were found. Fairness audit cannot be performed.</div>'
            '</div>',
            unsafe_allow_html=True
        )
        if st.toggle('Show AI Explanation'):
            _show_explanation(BASE_URL, show_fairness=False)
        return

    outcome_col = fairness_data.get('outcome_attribute')
    if outcome_col:
        st.caption('Outcome column: **' + outcome_col + '**')

    summary = fairness_data.get('summary', {})
    if summary:
        total  = summary.get('total_attributes_checked', len(audit))
        fair   = summary.get('fair_attributes', 0)
        unfair = summary.get('unfair_attributes', 0)
        st.markdown(
            '<div class="fa-summary">'
            '<div class="fa-sum-box">'
            '<div class="fa-sum-val" style="color:#7f77dd;">' + str(total) + '</div>'
            '<div class="fa-sum-lbl">Attributes checked</div>'
            '</div>'
            '<div class="fa-sum-box">'
            '<div class="fa-sum-val" style="color:#3dd68c;">' + str(fair) + '</div>'
            '<div class="fa-sum-lbl">Fair</div>'
            '</div>'
            '<div class="fa-sum-box">'
            '<div class="fa-sum-val" style="color:#ff8080;">' + str(unfair) + '</div>'
            '<div class="fa-sum-lbl">Unfair</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    for attribute, results in audit.items():
        if 'error' in results:
            st.markdown(
                '<div class="fa-err">'
                '<div class="fa-err-title">' + attribute.capitalize() + '</div>'
                '<div class="fa-err-msg">&#10007; Could not audit &mdash; ' + str(results['error']) + '</div>'
                '</div>',
                unsafe_allow_html=True
            )
            continue
        _attribute_card(attribute, results)

    st.divider()

    if st.toggle('Show AI Explanation & Remediation Plan'):
        _show_explanation(BASE_URL, show_fairness=True)


def _show_explanation(BASE_URL, show_fairness=True):
    if not st.session_state.explanation_result:
        with st.spinner('Generating AI explanation... this may take 10-20 seconds.'):
            headers = {}
            if st.session_state.get('token'):
                headers['Authorization'] = 'Bearer ' + st.session_state.token
            res = st.session_state.api_session.post(
                BASE_URL + '/api/explain',
                json={'dataset_id': st.session_state.dataset_id},
                headers=headers
            )
        if res.status_code == 200:
            st.session_state.explanation_result = res.json()
        else:
            st.error('Could not generate explanation. Check your API key in the .env file.')
            return

    exp_data    = st.session_state.explanation_result
    explanation = exp_data.get('explanation', {})
    remediation = exp_data.get('remediation_plan', {})

    quality_exp  = explanation.get('quality_summary', {})
    quality_text = quality_exp.get('explanation', '') if isinstance(quality_exp, dict) else str(quality_exp)

    if quality_text:
        st.markdown(
            '<div class="ai-box">'
            '<div class="ai-section-title">Quality Summary</div>'
            + _render_ai_text(quality_text) +
            '</div>',
            unsafe_allow_html=True
        )

    if show_fairness:
        fairness_exp  = explanation.get('fairness_summary', {})
        fairness_text = fairness_exp.get('explanation', '') if isinstance(fairness_exp, dict) else str(fairness_exp)
        if fairness_text:
            st.markdown(
                '<div class="ai-box">'
                '<div class="ai-section-title">Fairness Analysis &amp; Action Items</div>'
                + _render_ai_text(fairness_text) +
                '</div>',
                unsafe_allow_html=True
            )

    if remediation and remediation.get('source') != 'no_findings':
        st.markdown(
            '<div class="ai-box">'
            '<div class="rem-priority-title">Remediation Plan</div>',
            unsafe_allow_html=True
        )

        if remediation.get('source') == 'fallback':
            st.warning('Remediation plan generated with fallback (Gemini unavailable).')

        for priority, label, color in [
            ('critical_priority', 'Critical Priority', '#ff8080'),
            ('high_priority',     'High Priority',     '#f0c040'),
            ('medium_priority',   'Medium Priority',   '#3dd68c'),
        ]:
            items = remediation.get(priority, [])
            if not items:
                continue
            st.markdown(
                f'<div class="rem-sub" style="color:{color};">{label}</div>',
                unsafe_allow_html=True
            )
            for item in items:
                st.markdown(
                    '<div class="rem-item">'
                    '<div class="rem-label">Issue</div>'
                    '<div class="rem-text">' + _render_rem_text(item.get('issue', '')) + '</div>'
                    '<div class="rem-label" style="margin-top:10px;">Fix</div>'
                    '<div class="rem-text">' + _render_rem_text(item.get('fix', '')) + '</div>'
                    + (
                        '<div class="rem-label" style="margin-top:10px;">Technique</div>'
                        '<div class="rem-text">' + _render_rem_text(item['technique']) + '</div>'
                        if item.get('technique') else ''
                    )
                    + (
                        '<div class="rem-label" style="margin-top:10px;">Verification</div>'
                        '<div class="rem-text">' + _render_rem_text(item['verification']) + '</div>'
                        if item.get('verification') else ''
                    )
                    + '</div>',
                    unsafe_allow_html=True
                )

        st.markdown('</div>', unsafe_allow_html=True)