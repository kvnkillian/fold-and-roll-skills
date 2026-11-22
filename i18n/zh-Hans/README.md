> 本文件为机器翻译，欢迎母语者审校指正。

# Fold&Roll 地下城主技能

免费的 AI 智能体技能，用于主持龙与地下城（Dungeons & Dragons）游戏——出自 Fold&Roll 的制作者。

把它们装进 Claude Code、Codex、Cursor，或任何支持 Agent Skills 开放标准的智能体，你的智能体就不再凭感觉即兴拼凑龙与地下城建议，而是像一位地下城主那样备课：准备情境，而非剧情；准备后果，而非事件；先诡异，后幽默。

**人人皆可入席。**

## 技能一览

| 技能 | 功能 |
|---|---|
| `encounter-builder` | 根据队伍等级、人数与难度，生成平衡且令人难忘的 5e 遭遇战——包含地形、战术与一个转折。 |
| `npc-generator` | 生成带有怪癖、欲望与秘密的 NPC——还有声音、钩子，以及队伍无视他们时会发生什么。 |
| `session-prep` | 一页纸的团前准备：情境、3–5 个节点、开场爆点、派系行动，以及收尾的悬念。 |
| `one-shot-builder` | 一场完整的 3–4 小时一次性冒险：钩子、三幕结构、遭遇战、NPC 与一个落地的收尾。 |
| `solo-adventure` | 为一名玩家与一位智能体地下城主准备的单人冒险——选择、后果与一个真正的结局。 |
| `campaign-arc` | 由三幕六个节拍构成的战役弧线，以“什么改变了”来定义——而非“发生了什么”。 |
| `dice-roller` | 掷任意骰子——优势、劣势、重击、伤害、团体掷骰——亮出骰子，而不只报总数。 |

## 安装

### Claude Code

```sh
claude plugin install fold-and-roll-skills@kvnkillian
```

或者把技能复制到你的个人技能文件夹：

```sh
git clone https://github.com/kvnkillian/fold-and-roll-skills.git
cp -r fold-and-roll-skills/skills/* ~/.claude/skills/
```

### Codex / Cursor / Copilot

```sh
npx skills@latest add kvnkillian/fold-and-roll-skills
```

或者把技能复制到项目中的 `.agents/skills/`，个人使用则复制到 `~/.agents/skills/`。

### 其他智能体

把 `skills/<name>/` 文件夹复制到你的智能体读取技能的位置。每个技能就是一个 `SKILL.md` 文件——无需构建步骤，没有依赖。`scripts/roll.py` 中的掷骰助手只需要 Python 3。

## 使用方法

用平常的话向你的智能体提问。技能描述会告诉它何时触发：

- “为四名 5 级角色建一场困难难度的遭遇战，地点是一座被淹没的神庙。”
- “给我一个 NPC——一位知道得太多的铁匠。”
- “准备今晚的团。上次队伍烧掉了与公会的桥。”
- “为一座闹鬼的灯塔写一场一次性冒险。”
- “为我的 3 级游荡者跑一场单人冒险。”
- “围绕一座忘记了自己名字的城市，规划一条战役弧线。”

智能体只会问它真正需要的少数细节——队伍等级与人数、基调、团时长——然后交出可以直接开跑的成品。

## Fold&Roll 之道

这些技能遵循 Fold&Roll 立身的同一套规则：

- **准备情境，而非剧情。** 情境经得起与玩家的接触。剧情在玩家第一次做出计划外举动的瞬间就会崩塌。
- **玩家是共同作者。** 绝不要替玩家角色说台词、想心思、做决定。选择永远属于他们。
- **先诡异，后幽默。** 黑色幽默里，笑话挨着令人不安的东西；恐怖里带着干巴巴的紧张笑意——绝不血腥，绝不为血腥而血腥。
- **只用 SRD，除非你另有要求。** 怪物、法术与物品均出自 SRD 5.1 / 5.2.1。自创内容会标明为自创内容，智能体在编造之前会先征求你的同意。
- **安全第一。** 第零场（Session Zero）、Lines & Veils 与 X-card 是备课的一部分，而不是事后补救。
- **人人皆可入席。** 内容要让每位玩家都能使用——语言清晰，没有仅凭视觉才能获得的信息，没有必须靠看或靠听才能接住的笑话。

## 想要完整的牌桌？

这些技能是备课。Fold&Roll 是牌桌——角色卡、战斗地图、先攻与骰子，为每人手里一部手机、中间一张共享牌桌而生。

- **iOS：** https://apps.apple.com/app/fold-roll/id6822885522
- **Android 测试版：** https://play.google.com/apps/testing/com.kevin.rpgcompanion
- **网站：** https://kvnkillian.github.io/

从网站加入 Discord，分享你的牌桌故事、请求一个技能，或举报一次坏骰运。

## 许可证

MIT 许可证。自由使用这些技能、分叉、改编、在你的牌桌上运行。如果你发布改编作品，附上回链会很受感激，但不是必须的。

这些技能中的 SRD 内容依据知识共享署名 4.0 国际许可协议（SRD 5.2.1）与开放游戏许可协议 v1.0a（SRD 5.1）使用。Wizards of the Coast、Dungeons & Dragons 与 D&D 均为 Wizards of the Coast 的商标。本项目与 Wizards of the Coast 没有关联，也未获得其背书。
