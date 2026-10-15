# boji-skill (薄拉图体系与薄肌生活方式 AI Skill 工具箱)

简体中文 | [English](README.en.md)

> **面向现代年轻人的身体机能、性张力、精力管理与生活掌控 AI Skills 工具箱。**  
> 把你的身材烦恼、饮食卡点、两性困境与自律内耗交给 Agent，刺破借口，获得清晰诊断与立刻可执行的下一步动作。

[![GitHub Repo](https://img.shields.io/badge/GitHub-FizzEat%2Fboji--skill-181717?style=flat-square&logo=github)](https://github.com/FizzEat/boji-skill)
[![GitHub Stars](https://img.shields.io/github/stars/FizzEat/boji-skill?style=flat-square&logo=github&color=EAB308)](https://github.com/FizzEat/boji-skill/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/FizzEat/boji-skill?style=flat-square&color=3B82F6)](https://github.com/FizzEat/boji-skill/network/members)
[![Release](https://img.shields.io/badge/release-v1.1.0-10B981.svg?style=flat-square)](https://github.com/FizzEat/boji-skill/releases)
[![Codex](https://img.shields.io/badge/Codex-supported-10B981?style=flat-square)](https://developers.openai.com/codex/skills)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-16A34A.svg?style=flat-square)](LICENSE)
[![Author](https://img.shields.io/badge/author-FizzEat-181717.svg?style=flat-square&logo=github)](https://github.com/FizzEat)
[![X/Twitter](https://img.shields.io/badge/X-@boniusex-000000.svg?style=flat-square&logo=x)](https://x.com/boniusex)
[![Share on X](https://img.shields.io/badge/Share%20on-X-000000.svg?style=flat-square&logo=x)](https://twitter.com/intent/tweet?text=%E6%90%9E%E9%92%B1%E5%85%88%E6%90%9E%E8%BA%AB%E4%BD%93%EF%BC%81%E5%AF%B9%E6%A0%87+dbskill%EF%BC%8C%E6%88%91%E6%8A%8A%E8%96%84%E8%82%8C%E7%90%86%E8%AE%BA%E5%81%9A%E6%88%90%E4%BA%86+AI+Agent+%E5%B7%A5%E5%85%B7%E7%AE%B1%EF%BC%9Ahttps%3A%2F%2Fgithub.com%2FFizzEat%2Fboji-skill+%40boniusex+%40AlanShao111)

---

## ⚡ 为什么做 boji-skill？

如果说优秀的商业 Skill（如 `dbskill`）解决的是**“搞钱与业务诊断”**的外部课题；  
那么 `boji-skill` 解决的则是每个人最核心的内部底层系统：**“身体硬件、原生吸引力、精力守恒与心智掌控”**。

### 🌟 核心基座：“孙学 - 薄肌 - 黄毛” 三位一体人生操作系统
基于博主 **[邵艾伦 (Alan Shao)](https://x.com/AlanShao111)** 与波场 TRON 创始人 **[孙宇晨 (Justin Sun)](https://x.com/justinsuntron)** 的深度思想碰撞，本工具箱将年轻人在 AI 时代的破局路径工程化为三位一体闭环：
- **【硬件层 · 薄肌 (Hardware)】**：身体是唯一原生硬件。肌肉是寿命储备与身体的美金现金存量，拒绝药物减重，死磕自然做功与 15 个正手引体阶梯。
- **【固件层 · 黄毛 (Firmware)】**：“我压根不跟你玩这个游戏”。屏蔽一切世俗评价体系与做题家单向供养陷阱，建立不可侵犯的雄性框架与极度自信。
- **【软件层 · 孙学 (Software)】**：认知升维、Small Ego（极致小自我与无面子哲学）、数学参照系大数遍历与全 AI 托管，实现零资源破局与轻资产全球套利。

---

## 🧭 能力一览与 Skill 全目录 (共 14 大专属技能)

**已适配 OpenAI Codex**（CLI / IDE 扩展 / 桌面端）。下表保留 Claude Code / Antigravity 的 `/` 写法；Codex 使用 `$` 前缀。独立安装时为 `$boji`；在本插件仓库中，Codex 会加上 `boji-skill:` 命名空间，例如 `$boji-skill:boji`。以技能列表显示的名称为准。

| 指令 | 对应底层理论 | 适用情境 | 核心产出 |
| :--- | :--- | :--- | :--- |
| **`/boji`** | 薄拉图总览 | 任何模糊问题、不知道从何开始 | 智能意图路由，编排 1 个主技能 + 辅助方案 |
| **`/boji-sunxue`** | 孙学 | 怕被嘲笑不敢尝试、死要面子、缺乏商业套利嗅觉 | Small Ego（小自我）、数学大数遍历、全 AI 托管与轻资产套利 |
| **`/boji-diagnosis`** | 薄肌分型 | 评估自身体质、判断该增还是该减 | 4 象限身材与代谢诊断、隐形致胖真因定性 |
| **`/boji-pullup`** | 薄士学位 | 引体向上 0 基础突破或瓶颈冲刺 | 0 到 15 个连续标准引体阶梯路线图、神经润滑法 |
| **`/boji-workout`** | 视觉廓形 | 没时间去健身房，追求肩腰比 | 专攻倒三角廓形的 30-40 分钟低心智课表（居家/器械） |
| **`/boji-nutrition`** | 牛肉面理论 | 外卖党、不想做饭备餐、戒不掉碳水 | 外卖红绿灯替换公式、掌心法则、低压热量缺口 |
| **`/boji-attraction`**| 黄毛理论 | 陷入两性讨好、缺乏性张力、老实人自卑规训 | 规则脱钩、拒绝当供养者、建立个人雄性铁框架 |
| **`/boji-aesthetic`** | 视觉穿搭 | 穿衣服显土、圆肩驼背猥琐颈假体态 | 60 秒即刻挺拔复位动作、重磅版型与下颌线修饰 |
| **`/boji-energy`** | 飞机杯理论 | 欲望内耗、深夜空虚、被荷尔蒙绑架 | 生理降噪阻断机制、注意力强制回收至核心资产 |
| **`/boji-listen`** | 听劝理论 | 平台期找借口、嘴硬死磕、认知傲慢 | 听劝差评估、刺破借口、交付唯一强制纠偏动作 |
| **`/boji-unblock`** | 破罐破摔 | 暴饮暴食之后极度自责、断练几天想摆烂 | 生理真相除颤、2 分钟极简微重启协议 |
| **`/boji-creator`** | 自媒体实战 | 想把真实蜕变过程做成个人 IP 账号 | 爆款黄金开头 Hook、前后反差叙事与流量杠杆 |
| **`/boji-version`** | 版本更新论 | 面对就业做题家困境、大环境与社会催婚买房规训 | 识别过期代码、收回人生主权、输出新时代版本答案 |
| **`/boji-speech`**  | 语言第一性原理 | 开口恐惧症、哑巴英语、人际社交尴尬畏缩 | 国际尬聊心理脱敏法则、口腔肌肉记忆高频语块 |

---

## 🚀 快速开始

### 方式 1：主入口智能导航
安装后，在 Codex 中输入 `$` 选择技能，在 Claude Code / Antigravity 中使用 `/boji`。以下示例使用本仓库内的 Codex 调用名；安装到普通项目或用户技能目录时去掉 `boji-skill:`：

```text
$boji-skill:boji 我身高176cm，体重75kg，平时只吃外卖，引体向上一个都拉不上去，
天天熬夜刷手机很内耗，想改变自己，该怎么开始？
```

Agent 会自动分析并给出诊断、推荐的主攻技能，以及一个**今天就能完成的最小动作**。

### 方式 2：单项指令直达
明确目标时，直接调用专属工具：

```text
$boji-skill:boji-nutrition 我今天中午想点沙县小吃，帮我选一套薄肌高蛋白搭配。
$boji-skill:boji-pullup 我现在最多拉 3 个引体，怎么最快突破到 8 个？
$boji-skill:boji-unblock 昨晚和朋友吃火锅暴饮暴食了，今早体重重了3斤，心态很崩，怎么办？
```

---

## 🛠️ 安装与集成

### 在 Codex CLI / IDE 扩展 / 桌面端中使用

在本仓库根目录执行（需要 Python 3，无第三方依赖）：

```bash
# 将全部 14 个技能安装到本仓库的 .agents/skills/
python3 tools/install_codex.py
```

也可以安装到另一个项目，或安装到用户目录供多个项目使用：

```bash
# 指定项目
python3 tools/install_codex.py --dest /path/to/your-project/.agents/skills

# 当前用户的所有项目
python3 tools/install_codex.py --dest "$HOME/.agents/skills"
```

安装器会完整复制各技能的 `SKILL.md`、参考资料及所需脚本，安装后不依赖原仓库。遇到同名目录会在复制前停止，避免覆盖；重新安装前请先移走需要替换的旧技能目录。

在目标项目打开 Codex，输入 `$` 选择 `boji`，然后输入 `新手入门`。本仓库内的完整调用名为 `$boji-skill:boji`；安装到普通项目或用户目录时为 `$boji`。子技能同理，例如 `$boji-skill:boji-diagnosis` 或 `$boji-diagnosis`。Codex 会自动发现技能；若列表尚未刷新，重启 Codex。该方式不需要安装 Claude Code 插件。参见 [Codex 官方技能文档](https://developers.openai.com/codex/skills)。

### 在 Claude Code 中使用
本项目原生包含 `.claude-plugin/plugin.json`，可直接作为插件载入：
```bash
claude plugin add /path/to/boji-skill
```

### 在 Antigravity 中使用
将本目录复制或软链接至你的 Workspace Customization 目录：
```bash
# 复制到当前项目下的 .agents/skills/
mkdir -p .agents/skills
cp -R skills/. .agents/skills/
```

### 运行本地速算工具
```bash
python3 tools/calc_metrics.py --height 175 --weight 75 --pullups 4
```

安装后的 `boji-diagnosis` 也自带 `scripts/calc_metrics.py`，可由 Codex 按技能目录定位运行。

### 开发验证

```bash
python3 -m unittest discover -s tests -v
```

---

## 📚 延伸阅读
- [完整使用指南](docs/新手入门.md)
- [薄拉图哲学与底层逻辑图解](docs/理论体系图.md)

---

## 🙏 致敬与灵感来源 (Acknowledgements)

本项目核心思想框架与认知模因源自知名博主 **[邵艾伦 (Alan Shao)](https://x.com/AlanShao111)** 提出的“薄肌理论”与“薄拉图（Boplato）全套学说”，以及波场 TRON 创始人 **[孙宇晨 (Justin Sun)](https://x.com/justinsuntron)** 带来的“孙学”财富与认知套利模型。

特别致敬 2026 年 10 月邵艾伦与孙宇晨的长达 4 小时深度思想对谈，直接促成了本项目**“孙学 - 薄肌 - 黄毛”三位一体人生操作系统**的体系化定型与落地。

感谢艾伦与孙哥在全网带来的先锋认知碰撞，本项目由 **[@FizzEat](https://github.com/FizzEat)** ([X: @boniusex](https://x.com/boniusex)) 基于 Antigravity / Claude Code 开源生态进行了系统的 AI Agent 技能工程化重构。

---

## 🤝 引用与推荐 (Cite & Share)

如果您在文章、播客、视频或开源项目中引用了 **boji-skill**，欢迎使用以下标准格式：

### Markdown
```markdown
[boji-skill](https://github.com/FizzEat/boji-skill) - 基于“孙学-薄肌-黄毛”三位一体的开源 AI Agent 工具箱 (@FizzEat).
```

### BibTeX
```bibtex
@software{fizzeat_boji_skill_2026,
  author = {FizzEat},
  title = {boji-skill: Open-Source Sunism, Thin Muscle & Huangmao AI Agent Toolkit},
  url = {https://github.com/FizzEat/boji-skill},
  version = {1.1.0},
  year = {2026}
}
```

---

## 📄 许可证
本项目采用 [CC BY-NC 4.0 (知识共享署名-非商业性使用 4.0 国际许可协议)](LICENSE)。
欢迎个人自用与社群学习，未经授权请勿用于商业闭门课程售卖。
