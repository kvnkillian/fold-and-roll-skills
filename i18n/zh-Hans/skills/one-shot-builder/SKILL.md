---
name: one-shot-builder
description: "为一场 3–4 小时的团会写一则完整的龙与地下城 5e 一次性冒险：钩子、三幕结构、遭遇战、NPC，以及一个落地的收尾。当用户要求一场一次性冒险、单场冒险、展会游戏、新手入门冒险，或独立故事时使用。"
---

# 一次性冒险构建器

一次性冒险是一次坐下来就能讲完的完整故事：一个玩家无法忽视的钩子，一个让事情复杂起来的中间段，一个改变了什么的结局。它不是把战役章节的编号涂掉就成的东西。

## 动手之前——先问清关键信息

只问缺失的信息。方括号内为默认值。

1. **队伍等级** [3]
2. **队伍人数** [4]
3. **团时长** [3–4 小时]
4. **背景 / 钩子想法** [请用户用一句话描述，或自行编一个并说明]
5. **基调**——恐怖、喜剧、阴谋、地城探索 [先诡异、带冷幽默]
6. **有新手吗？** [没有——如果有，减轻规则负担，先把乐趣摆在前面]

## 规则

- **一个钩子、一个反派、一个收尾。** 一次性冒险装不下副线。凡是与钩子或结局无关的东西，全部删掉。
- **只用 SRD。** 怪物、法术与物品均出自 SRD 5.1 / 5.2.1。自创内容会标明为自创内容，并且只有在用户同意时才使用。
- **三幕结构，而且中间一幕必须让事情复杂起来。** 第一幕：钩子变得与个人相关。第二幕：问题比最初看起来更大或更古怪。第三幕：决定性的对峙与收尾。如果第二幕只是“更多第一幕”，重写它。
- **结局是一个后果，而非一个事件。** 用“结局之后什么必须不同”来定义结局——而不是它如何发生。十几个场景都能达成它；一个被提前破坏的事件就能毁了它。
- **预生成角色是可选项，不是必需品。** 如果用户想要预生成角色，可以作为后续补充提供——四名等级合适的角色，各自带一个欲望、一个秘密，以及与钩子的联系。不要在没人要求时就建好。
- **安全工具摆在前面。** Lines & Veils 与 X-card，在开玩之前就说明。如果这场一次性冒险触碰了常见的界线（身体恐怖、儿童身处险境、精神控制），要在推介里就标出来，而不是在游戏进行到一半时。
- **绝不替玩家一方行动。** 写世界呈现了什么。绝不要写玩家角色说了什么、想了什么、决定了什么。

## 工作流程

1. **钩子。** 一段话，再加一句地下城主可以直接读出来的台词。钩子必须打动*角色*想要的东西，而不只是“有个工作机会”。让队伍在最初十分钟内就有了在乎的理由。
2. **反派。** 一个队伍能够理解的目标、一个“队伍什么都不做时会发生什么”的计划，以及一个让他们没那么容易被直接杀掉的理由。反派就是引擎。
3. **第一幕——钩子变得与个人相关。** 导火索事件、一场遭遇战、一位重要的 NPC。
4. **第二幕——复杂化。** 问题比看起来更大或更古怪。一场探索或社交场景、一场战斗遭遇战、一次揭示。
5. **第三幕——对峙与收尾。** 决定性时刻，然后是收尾：世界与角色在之后有什么不同。
6. **演员表。** 3–4 名 NPC，每人一个怪癖、一个欲望、一个秘密（使用 `npc-generator` 的形式——不要在这里重述它的全部规则）。
7. **遭遇战。** 2–3 场遭遇战，每场包含经验值预算、地形与一个转折（使用 `encounter-builder` 的形式——不要在这里重述它的全部规则）。
8. **交付。** 按下面的格式。目标 2–3 页——地下城主读一遍就能开跑。

## 输出格式

```markdown
# <Title> — a one-shot for <n> level <x> characters, <3–4> hours

**Pitch:** <one line — the hook, as a sentence a DM could say to recruit players>
**Tone:** <tone> | **Lines & Veils:** <note the table's lines, or "confirm before play">

## The hook
<one paragraph. Then: **Read aloud:** "<one or two lines>">

## The villain: <name>
**Goal:** <one line> | **Plan if the party does nothing:** <one line> | **Why they are hard to kill:** <one line>

## Act 1 — <title>
<what happens, the NPC, the encounter>

## Act 2 — <title>
<the complication, the reveal, the encounter>

## Act 3 — <title>
<the confrontation, then the resolution — what is different after>

## Cast
- **<Name>** (<role>): <quirk> | Wants <want> | Hiding <secret>

## Encounters
- **<Name>** — <difficulty>, <monsters>, <terrain + twist in one line>

## If the party goes sideways
<one paragraph — the situation, not the plot: what moves, what surfaces elsewhere, what the villain does next>
```

## Fold&Roll 语气

先诡异，后幽默。黑色幽默里，笑话挨着令人不安的东西；恐怖里带着干巴巴的紧张笑意，绝不血腥。一座闹鬼的灯塔之所以吓人，是因为灯亮着、屋里却没人——而不是因为地窖里有什么。要敢于具体：一个名字、一种气味、一种戛然而止的声音。
