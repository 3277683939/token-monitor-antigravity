import os

base = r'D:\guangguoqing\Documents\antigrative-dashboard'

# 1. 美化升级 compat/inline-widget.cjs (输入框胶囊 + 悬浮卡片)
p_widget = os.path.join(base, 'compat', 'inline-widget.cjs')
with open(p_widget, 'r', encoding='utf-8') as f:
    widget_txt = f.read()

# 注入 Token Monitor 专属样式（放在 </style> 前）
tm_inline_css = """
    /* Token Monitor Edition Enhancements */
    .tm-brand{display:inline-flex;align-items:center;gap:4px;padding:2px 6px;border-radius:999px;background:rgba(139,92,246,0.13);border:1px solid rgba(139,92,246,0.3);color:#a78bfa;font-size:10px;font-weight:600;margin-right:2px;flex:none;letter-spacing:.2px}
    .tm-bolt{width:11px;height:11px;flex:none;color:#a78bfa}
    .dot{display:inline-block!important;width:5px;height:5px;border-radius:50%;flex:none;transition:all .2s ease}
    .dot.live{display:inline-block!important;background:#22c55e!important;box-shadow:0 0 6px rgba(34,197,94,0.85)}
    @keyframes tm-pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.45;transform:scale(.82)}}
    :host(.icons-only) .tm-brand,:host(.narrow) .tm-label{display:none}
    .chip{border-radius:7px!important;transition:background-color .16s ease,box-shadow .16s ease,color .16s ease!important}
    .chip:hover,.chip[aria-expanded=true]{background:rgba(139,92,246,0.12)!important;box-shadow:inset 0 0 0 1px rgba(139,92,246,0.28)}
    .card{backdrop-filter:blur(16px)!important;-webkit-backdrop-filter:blur(16px)!important;border-color:rgba(139,92,246,0.28)!important;box-shadow:0 12px 36px rgba(0,0,0,0.26)!important}
    .track i{background-image:linear-gradient(90deg,transparent,rgba(56,189,248,0.28));border-radius:3px}
    </style><div class="bar" data-i18n-aria="strip" aria-label="Dashboard statistics">
      <span class="tm-brand" title="Token Monitor • 实时监控"><svg class="tm-bolt" viewBox="0 0 16 16" aria-hidden="true"><path d="M9.5 1.5L3 9.5h4.5L6.5 14.5 13 6.5H8.5l1-5z" fill="currentColor" stroke="none"/></svg><span class="tm-label">TM</span><span class="dot" id="dot" title="Connecting"></span></span>"""

old_anchor = """    </style><div class="bar" data-i18n-aria="strip" aria-label="Dashboard statistics">
      <span class="dot" id="dot" title="Connecting"></span>"""

if 'tm-brand' not in widget_txt:
    if old_anchor in widget_txt:
        widget_txt = widget_txt.replace(old_anchor, tm_inline_css, 1)
        with open(p_widget, 'w', encoding='utf-8') as f:
            f.write(widget_txt)
        print('[OK] Upgraded inline-widget.cjs with Token Monitor capsule styling!')
    else:
        print('[WARN] Could not find anchor in inline-widget.cjs (checking line endings)')
        # Fallback with normalized line endings
        norm_anchor = old_anchor.replace('\n', '\r\n')
        if norm_anchor in widget_txt:
            widget_txt = widget_txt.replace(norm_anchor, tm_inline_css.replace('\n', '\r\n'), 1)
            with open(p_widget, 'w', encoding='utf-8') as f:
                f.write(widget_txt)
            print('[OK] Upgraded inline-widget.cjs (CRLF)!')
        else:
            print('[ERR] Anchor not found in inline-widget.cjs!')
else:
    print('[SKIP] inline-widget.cjs already has Token Monitor styling.')

# 2. 美化升级 sidecars/panel/index.html (闪电 SVG Logo)
p_idx = os.path.join(base, 'sidecars', 'panel', 'index.html')
with open(p_idx, 'r', encoding='utf-8') as f:
    idx_txt = f.read()

old_svg = '<symbol id="pulse" viewBox="0 0 16 16"><path d="M1 8h4l2-5 3 10 2-5h3"/></symbol>'
new_svg = '<symbol id="pulse" viewBox="0 0 16 16"><path d="M9.5 1.5L3 9.5h4.5L6.5 14.5 13 6.5H8.5l1-5z"/></symbol>'
if old_svg in idx_txt:
    idx_txt = idx_txt.replace(old_svg, new_svg)
    with open(p_idx, 'w', encoding='utf-8') as f:
        f.write(idx_txt)
    print('[OK] Updated index.html lightning SVG icon!')

# 3. 美化升级 sidecars/panel/styles.css (紫蓝流光渐变 + 毛玻璃动效)
p_css = os.path.join(base, 'sidecars', 'panel', 'styles.css')
with open(p_css, 'r', encoding='utf-8') as f:
    css_txt = f.read()

tm_panel_css = """
/* === Token Monitor Edition Visual Polish === */
.widget {
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border-color: rgba(139, 92, 246, 0.25);
  box-shadow: 0 10px 34px rgba(0, 0, 0, 0.22);
}
.brand .icon {
  color: #a78bfa !important;
  fill: rgba(139, 92, 246, 0.2);
}
.connection-dot.live {
  width: 6px;
  height: 6px;
  background: #22c55e !important;
  box-shadow: 0 0 8px rgba(34, 197, 94, 0.85);
  animation: tm-panel-pulse 2s infinite;
}
@keyframes tm-panel-pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.45; transform: scale(0.8); }
}
.version-tag {
  background: rgba(139, 92, 246, 0.14) !important;
  color: #c4b5fd !important;
  border-color: rgba(139, 92, 246, 0.32) !important;
  font-weight: 600 !important;
}
.metric-chip {
  transition: transform 150ms cubic-bezier(.23,1,.32,1), border-color 150ms ease, background-color 150ms ease, box-shadow 150ms ease !important;
}
.metric-chip:hover {
  transform: translateY(-1px);
  border-color: rgba(139, 92, 246, 0.35) !important;
  box-shadow: 0 4px 12px rgba(139, 92, 246, 0.08);
}
.metric-chip[aria-selected=true] {
  border-color: rgba(139, 92, 246, 0.45) !important;
}
.metric-chip[aria-selected=true]::after {
  background: linear-gradient(90deg, #8b5cf6, #6366f1, #38bdf8) !important;
  height: 2.5px !important;
}
.quota-track i {
  background-image: linear-gradient(90deg, transparent, rgba(56, 189, 248, 0.28));
}
.detail-card {
  border-color: rgba(139, 92, 246, 0.22) !important;
}
"""

if 'Token Monitor Edition Visual Polish' not in css_txt:
    css_txt += '\n' + tm_panel_css
    with open(p_css, 'w', encoding='utf-8') as f:
        f.write(css_txt)
    print('[OK] Upgraded styles.css with Token Monitor visual polish!')
else:
    print('[SKIP] styles.css already polished.')
