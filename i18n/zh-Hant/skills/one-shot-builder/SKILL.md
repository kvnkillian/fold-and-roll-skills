---
name: one-shot-builder
description: "為 3–4 小時的團撰寫一場完整的 D&D 5e 單場冒險：鉤子、三幕、遭遇戰、NPC，以及一個收得住的結局。適用於使用者要求單場冒險、單次團、展會團、新手入門冒險，或獨立故事時。"
---

# 單場冒險建構器

單場冒險是一次坐下來就能說完的完整故事：一個玩家無法忽視的鉤子、一個讓事情複雜化的中段，以及一個帶來改變的結局。它不是把序號磨掉的戰役章節。

## 開始建造前——先問真正重要的事

只問缺少的部分。預設值在方括號內。

1. **隊伍等級** [3]
2. **隊伍人數** [4]
3. **團的長度** [3–4 小時]
4. **背景 / 鉤子點子** [請對方用一句話描述，或自行編一個並明說]
5. **氛圍** —— 恐怖、喜劇、陰謀、地城探索 [先詭異、帶著乾澀幽默]
6. **有新手嗎？** [沒有——若有，減輕規則負擔，把樂趣往前放]

## 規則

- **一個鉤子、一個反派、一個結局。** 單場冒險裝不下副線。所有不服務鉤子或結局的東西，全部刪掉。
- **僅用 SRD。** 怪物、法術與物品皆出自 SRD 5.1 / 5.2.1。自創內容須標示為自創，且須經使用者同意。
- **三幕，而且中段必須複雜化。** 第一幕：鉤子變得與個人有關。第二幕：問題比最初看起來更大或更詭異。第三幕：決定性的對峙與收尾。如果第二幕只是「第一幕再多一點」，重寫它。
- **結局是後果，不是事件。** 用「結局之後什麼必須不同」來定義結局——而不是用「它如何發生」。十幾場戲都能抵達它；一個被先搶走的事件就能毀了它。
- **預設角色是選配，不是必需。** 若使用者想要預設角色，事後再提供——四名符合等級的角色，各有一個渴望、一個祕密，以及與鉤子的連結。不要沒人問就先建好。
- **安全工具先行。** 界線與帷幕（Lines & Veils）與 X 卡（X-card），開玩前就說清楚。若這場單場冒險會碰到常見界線（身體恐怖、孩童遇險、心智控制），在推銷時就標示出來，不要等到遊戲中段。
- **絕不替玩家行動。** 寫世界呈現了什麼。絕不寫玩家角色說了什麼、想了什麼、決定了什麼。

## 工作流程

1. **鉤子。** 一段文字，再加一句地下城主可以直接唸出的台詞。鉤子必須打動*角色*想要的東西，而不只是「有個工作機會」。讓隊伍在前十分鐘就有在乎的理由。
2. **反派。** 一個隊伍能理解的目標、一個「隊伍若什麼都不做會發生什麼」的計畫，以及一個讓他難以被直接殺掉的理由。反派就是引擎。
3. **第一幕——鉤子變得與個人有關。** 導火事件、一場遭遇戰、一位重要的 NPC。
4. **第二幕——複雜化。** 問題比看起來更大或更詭異。一場探索或社交戲、一場戰鬥遭遇戰、一個揭露。
5. **第三幕——對峙與結局。** 決定性的時刻，然後收尾：世界與角色在事後有什麼不同。
6. **角色陣容。** 3–4 位 NPC，每位各有一個怪癖、一個渴望、一個祕密（使用 `npc-generator` 的形式——不要在這裡重述它的完整規則）。
7. **遭遇戰。** 2–3 場遭遇戰，每場各有經驗值預算、地形與轉折（使用 `encounter-builder` 的形式——不要在這裡重述它的完整規則）。
8. **交付。** 依下方格式。目標 2–3 頁——地下城主讀過一次就應該能上場。

## 輸出格式

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

## Fold&Roll 語氣

先詭異，笑點晚一步跟上。黑色幽默裡，笑話就坐在令人不安的事物旁邊；恐怖帶著乾澀的神經質機智，絕不血腥。一座鬧鬼燈塔之所以可怕，是因為燈亮著，裡面卻沒有人——而不是因為地窖裡有什麼。堅持具體：一個名字、一股氣味、一個戛然而止的聲音。
