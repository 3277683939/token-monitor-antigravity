import os

base = r'D:\guangguoqing\Documents\antigrative-dashboard'
old_repo = 'YOU-SHOULD-KNOW-ME/antigrative-dashboard'
new_repo = '3277683939/token-monitor-antigravity'

targets = [
    'CHANGELOG.md',
    'GITHUB_RELEASE.md',
    'README.md',
    'README.zh-CN.md',
    os.path.join('compat', 'inline-widget.cjs'),
    os.path.join('compat', 'update-worker.py'),
    os.path.join('docs', 'CLI.md'),
    os.path.join('docs', 'UPDATES.md'),
    os.path.join('ide', 'package.json'),
    os.path.join('ide', 'README.md'),
    os.path.join('tools', 'check-collection-state-ui.mjs'),
]

for rel in targets:
    p = os.path.join(base, rel)
    if not os.path.exists(p):
        continue
    with open(p, 'r', encoding='utf-8') as f:
        txt = f.read()
    new_txt = txt.replace(old_repo, new_repo).replace('YOU-SHOULD-KNOW-ME', '3277683939')
    if new_txt != txt:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(new_txt)
        print('[OK] Updated repo refs in:', rel)

# 在 README.zh-CN.md 顶部增加 Token Monitor 内置改造版说明
p_readme_zh = os.path.join(base, 'README.zh-CN.md')
with open(p_readme_zh, 'r', encoding='utf-8') as f:
    r_zh = f.read()

banner_zh = """> **⚡ Token Monitor 内置改造版（for Antigravity 2.0）**
>
> 本仓库基于原 `antigrative-dashboard` 对话栏原生嵌入式架构与官方精准配额底层，深度融合 **Token Monitor** 视觉设计与实时监控体验，支持：
> - **对话栏正下方原生嵌入胶囊**：带 `⚡ TM` 紫色闪电标识、绿色实时呼吸脉冲灯、真实 `tok/s` 速率、Prompt 缓存命中率、上下文水位监控；
> - **毛玻璃现代化仪表盘**：紫蓝流光进度条、5h/周配额精准倒计时、TTFT 延迟、正文/思考 Token 分离统计；
> - **全自动定期检测与同步机制**：已配置 GitHub Actions 定期跟踪上游更新及自动化测试发布，支持内置自更新。

"""
if 'Token Monitor 内置改造版' not in r_zh:
    r_zh = banner_zh + r_zh
    with open(p_readme_zh, 'w', encoding='utf-8') as f:
        f.write(r_zh)
    print('[OK] Added banner to README.zh-CN.md')

# 更新 README.md
p_readme_en = os.path.join(base, 'README.md')
with open(p_readme_en, 'r', encoding='utf-8') as f:
    r_en = f.read()

banner_en = """> **⚡ Token Monitor Built-in Edition (for Antigravity 2.0)**
>
> Refactored and enhanced from the native inline-widget architecture with **Token Monitor** aesthetics, real-time streaming TPS, cache hit tracking, and official quota countdowns. Supports automated periodic upstream checks & self-updating.

"""
if 'Token Monitor Built-in Edition' not in r_en:
    r_en = banner_en + r_en
    with open(p_readme_en, 'w', encoding='utf-8') as f:
        f.write(r_en)
    print('[OK] Added banner to README.md')
