# boji-skill (薄拉图体系与薄肌生活方式 AI Skill 工具箱)

简体中文 | [English](README.en.md)

> **面向现代年轻人的身体机能、性张力、精力管理与生活掌控 AI Skills 工具箱。**  
> 把你的身材烦恼、饮食卡点、两性困境与自律内耗交给 Agent，刺破借口，获得清晰诊断与立刻可执行的下一步动作。

[![Version](https://img.shields.io/badge/version-1.0.0-2563EB.svg?style=flat-square)](VERSION)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-16A34A.svg?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/supported-Claude%20Code%20%7C%20Antigravity%20%7C%20Codex-8B5CF6.svg?style=flat-square)](.)

---

## ⚡ 为什么做 boji-skill？

如果说优秀的商业 Skill（如 `dbskill`）解决的是**“搞钱与业务诊断”**的外部课题；  
那么 `boji-skill` 解决的则是每个人最核心的内部底层系统：**“身体硬件、原生吸引力、精力守恒与心智掌控”**。

很多普通人听了网上的“薄肌理论”或“薄拉图概念”热血沸腾，但回到现实依然不知道今天外卖怎么吃、引体怎么练、心态崩了怎么办。  
**`boji-skill` 将抽象的网络模因升华为高度确定性的生理学与行为工程**，打造一个真正能够陪伴你完成蜕变的数字教练。

---

## 🧭 能力一览与 Skill 全目录

| 指令 | 对应底层理论 | 适用情境 | 核心产出 |
| :--- | :--- | :--- | :--- |
| **`/boji`** | 薄拉图总览 | 任何模糊问题、不知道从何开始 | 智能意图路由，编排 1 个主技能 + 辅助方案 |
| **`/boji-diagnosis`** | 薄肌分型 | 评估自身体质、判断该增还是该减 | 4 象限身材与代谢诊断、隐形致胖真因定性 |
| **`/boji-pullup`** | 薄士学位 | 引体向上 0 基础突破或瓶颈冲刺 | 0 到 15 个连续标准引体阶梯路线图、神经润滑法 |
| **`/boji-workout`** | 视觉廓形 | 没时间去健身房，追求肩腰比 | 专攻倒三角廓形的 30-40 分钟低心智课表（居家/器械） |
| **`/boji-nutrition`** | 牛肉面理论 | 外卖党、不想做饭备餐、戒不掉碳水 | 外卖红绿灯替换公式、掌心法则、低压热量缺口 |
| **`/boji-attraction`**| 黄毛理论 | 陷入两性讨好、缺乏性张力、老实人自卑 | 拒绝当供养者、建立个人框架、原生吸引力重塑 |
| **`/boji-aesthetic`** | 视觉穿搭 | 穿衣服显土、圆肩驼背猥琐颈假体态 | 60 秒即刻挺拔复位动作、重磅版型与下颌线修饰 |
| **`/boji-energy`** | 飞机杯理论 | 欲望内耗、深夜空虚、被荷尔蒙绑架 | 生理降噪阻断机制、注意力强制回收至核心资产 |
| **`/boji-listen`** | 听劝理论 | 平台期找借口、嘴硬死磕、认知傲慢 | 听劝差评估、刺破借口、交付唯一强制纠偏动作 |
| **`/boji-unblock`** | 破罐破摔 | 暴饮暴食之后极度自责、断练几天想摆烂 | 生理真相除颤、2 分钟极简微重启协议 |
| **`/boji-creator`** | 自媒体实战 | 想把真实蜕变过程做成个人 IP 账号 | 爆款黄金开头 Hook、前后反差叙事与分镜头脚本 |
| **`/boji-version`** | 版本更新论 | 面对就业做题家困境、大环境与社会催婚买房规训 | 识别过期代码、收回人生主权、输出新时代版本答案 |
| **`/boji-speech`**  | 语言第一性原理 | 开口恐惧症、哑巴英语、人际社交尴尬畏缩 | 国际尬聊心理脱敏法则、口腔肌肉记忆高频语块 |

---

## 🚀 快速开始

### 方式 1：主入口智能导航
在任何支持 Skill 的 Agent（如 Claude Code / Antigravity）中，直接输入当前处境：

```text
/boji 我身高176cm，体重75kg，平时只吃外卖，引体向上一个都拉不上去，
天天熬夜刷手机很内耗，想改变自己，该怎么开始？
```

Agent 会自动分析并给出诊断、推荐的主攻技能，以及一个**今天就能完成的最小动作**。

### 方式 2：单项指令直达
明确目标时，直接调用专属工具：

```text
/boji-nutrition 我今天中午想点沙县小吃，帮我选一套薄肌高蛋白搭配。
/boji-pullup 我现在最多拉 3 个引体，怎么最快突破到 8 个？
/boji-unblock 昨晚和朋友吃火锅暴饮暴食了，今早体重重了3斤，心态很崩，怎么办？
```

---

## 🛠️ 安装与集成

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
cp -r /Users/wuyanliu/.gemini/antigravity/scratch/boji-skill/skills/* .agents/skills/
```

### 运行本地速算工具
```bash
python3 tools/calc_metrics.py --height 175 --weight 75 --pullups 4
```

---

## 📚 延伸阅读
- [完整使用指南](docs/新手入门.md)
- [薄拉图哲学与底层逻辑图解](docs/理论体系图.md)

---

## 🙏 致敬与灵感来源 (Acknowledgements)

本项目核心思想框架与认知模因源自知名博主 **[邵艾伦 (Alan Shao)](https://x.com/AlanShao111)** 提出的“薄肌理论”与“薄拉图（Boplato）全套学说”（涵盖薄士学位、黄毛理论、牛肉面理论、飞机杯理论、听劝理论与版本更新论）。

感谢艾伦在全网带来的先锋认知碰撞与破圈模因，本项目由社区开发者基于 Antigravity / Claude Code 开源生态进行了系统的 AI Agent 技能工程化重构与闭环落地。

---

## 📄 许可证
本项目采用 [CC BY-NC 4.0 (知识共享署名-非商业性使用 4.0 国际许可协议)](LICENSE)。
欢迎个人自用与社群学习，未经授权请勿用于商业闭门课程售卖。
