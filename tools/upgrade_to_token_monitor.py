import os

base = r'D:\guangguoqing\Documents\antigrative-dashboard'

# 1. Update plugin.json
p_plugin = os.path.join(base, 'plugin.json')
with open(p_plugin, 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('"display_name": "Antigrative Dashboard"', '"display_name": "Token Monitor"')
text = text.replace('"version": "0.8.20"', '"version": "1.0.0"')
text = text.replace('"description": "Token throughput, cache hit, context window and quotas on Windows, Linux and macOS. English / Chinese switching."', '"description": "Token throughput, speed (tok/s), cache hit, context window and quotas. Token Monitor Edition for Antigravity."')
with open(p_plugin, 'w', encoding='utf-8') as f:
    f.write(text)
print('[OK] Updated plugin.json')

# 2. Update sidecar.json
p_sidecar = os.path.join(base, 'sidecars', 'panel', 'sidecar.json')
with open(p_sidecar, 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('"display_name": "Antigrative Dashboard"', '"display_name": "Token Monitor"')
text = text.replace('"title": "Antigrative Dashboard"', '"title": "Token Monitor"')
with open(p_sidecar, 'w', encoding='utf-8') as f:
    f.write(text)
print('[OK] Updated sidecar.json')

# 3. Update panel-source.mjs
p_ps = os.path.join(base, 'sidecars', 'panel', 'panel-source.mjs')
with open(p_ps, 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('Antigrative Dashboard', 'Token Monitor')
with open(p_ps, 'w', encoding='utf-8') as f:
    f.write(text)
print('[OK] Updated panel-source.mjs')

# 4. Update index.html
p_idx = os.path.join(base, 'sidecars', 'panel', 'index.html')
with open(p_idx, 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('<title>Antigrative Dashboard</title>', '<title>Token Monitor</title>')
text = text.replace('<span id="panel-name">Antigrative Dashboard</span>', '<span id="panel-name">⚡ Token Monitor</span>')
with open(p_idx, 'w', encoding='utf-8') as f:
    f.write(text)
print('[OK] Updated index.html')

# 5. Update i18n.cjs
p_i18n = os.path.join(base, 'compat', 'i18n.cjs')
with open(p_i18n, 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('Antigrative Dashboard statistics', '⚡ Token Monitor')
text = text.replace('Antigrative Dashboard 会话与额度状态条', '⚡ Token Monitor 状态条')
text = text.replace('已连接 Antigrative Dashboard', '已连接 Token Monitor')
text = text.replace('Connected to Antigrative Dashboard', 'Connected to Token Monitor')
text = text.replace('Antigrative Dashboard 暂未连接', 'Token Monitor 暂未连接')
text = text.replace('Antigrative Dashboard is offline', 'Token Monitor is offline')
with open(p_i18n, 'w', encoding='utf-8') as f:
    f.write(text)
print('[OK] Updated i18n.cjs')

# 6. Update inline-widget.cjs
p_widget = os.path.join(base, 'compat', 'inline-widget.cjs')
with open(p_widget, 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('Antigrative Dashboard', 'Token Monitor')
with open(p_widget, 'w', encoding='utf-8') as f:
    f.write(text)
print('[OK] Updated inline-widget.cjs')

print('\nAll files successfully upgraded to Token Monitor!')
