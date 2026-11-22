> 註：本文件為機器翻譯，歡迎母語使用者協助校對與改進。

# Fold&Roll DM 技能

免費的 AI 代理技能，助你主持《龍與地下城》（Dungeons & Dragons）——出自 Fold&Roll 製作團隊。

將它們安裝到 Claude Code、Codex、Cursor，或任何支援 Agent Skills 開放標準的代理工具上，你的代理就不會再憑感覺即興拼湊 D&D 建議，而是像一位地下城主那樣備團：準備情境，而非劇情；準備後果，而非事件；先詭異，笑點晚一步跟上。

**桌邊人人有份。**

## 技能一覽

| 技能 | 功能 |
|---|---|
| `encounter-builder` | 依隊伍等級、人數與難度，打造平衡又令人難忘的 5e 遭遇戰——包含地形、戰術與一個轉折。 |
| `npc-generator` | 創造一位有怪癖、有渴望、有祕密的 NPC——再加上聲音、鉤子，以及隊伍若不理會他會發生什麼事。 |
| `session-prep` | 一頁的團前準備：情境、3–5 個節點、開場爆點、派系動向，以及收尾用的懸念。 |
| `one-shot-builder` | 一場完整的 3–4 小時單場冒險：鉤子、三幕、遭遇戰、NPC，以及一個收得住的結局。 |
| `solo-adventure` | 為一位玩家與一位代理地下城主準備的單人冒險——選擇、後果，以及一個真正的結局。 |
| `campaign-arc` | 三幕六節拍的戰役弧線，依「什麼改變了」來定義——而非依「發生了什麼」。 |
| `dice-roller` | 擲任何骰子——優勢、劣勢、重擊、傷害、團體擲骰——顯示骰面，而不只是總數。 |

## 安裝

### Claude Code

```sh
claude plugin install fold-and-roll-skills@kvnkillian
```

或將技能複製到你的個人技能資料夾：

```sh
git clone https://github.com/kvnkillian/fold-and-roll-skills.git
cp -r fold-and-roll-skills/skills/* ~/.claude/skills/
```

### Codex / Cursor / Copilot

```sh
npx skills@latest add kvnkillian/fold-and-roll-skills
```

或將技能複製到專案中的 `.agents/skills/`，個人使用則放進 `~/.agents/skills/`。

### 其他代理工具

將 `skills/<名稱>/` 資料夾複製到你的代理工具讀取技能的位置。每個技能就是一個 `SKILL.md` 檔案——無需建置步驟，沒有相依套件。`scripts/roll.py` 裡的擲骰小幫手只需要 Python 3。

## 使用方式

用平常的話問你的代理。技能描述會告訴它何時該啟動：

- 「為四名 5 級角色打造一場困難難度的遭遇戰，地點是一座淹水的神殿。」
- 「給我一個 NPC——一位知道太多的鐵匠。」
- 「準備今晚的團。上次隊伍跟公會燒斷了橋。」
- 「幫我寫一場鬧鬼燈塔的單場冒險。」
- 「為我 3 級的遊蕩者主持一場單人冒險。」
- 「規劃一條戰役弧線，主題是一座忘記自己名字的城市。」

代理會先問它真正需要的少數細節——隊伍等級與人數、氛圍、團的長度——然後交出可以直接上場的成品。

## Fold&Roll 之道

這些技能遵循 Fold&Roll 本身的設計原則：

- **備情境，不備劇情。** 情境經得起玩家接觸，劇情在玩家第一次做出意料之外舉動時就斷了。
- **玩家是共同作者。** 絕不替玩家角色說台詞、想心事、做決定。選擇永遠屬於他們。
- **先詭異，笑點晚一步跟上。** 黑色幽默裡，笑話就坐在令人不安的事物旁邊；恐怖帶著乾澀的神經質機智——絕不血腥，絕不為嚇人而嚇人。
- **僅用 SRD，除非你另有指示。** 怪物、法術與物品皆出自 SRD 5.1 / 5.2.1。自創內容會標示為自創，代理在自行發明之前會先問你。
- **安全優先。** 第零場、界線與帷幕（Lines & Veils）與 X 卡（X-card）是準備工作的一部分，不是事後補救。
- **桌邊人人有份。** 內容要讓每位玩家都能使用——語言清晰、沒有只能用看的資訊、沒有非得看見或聽見才懂的笑話。

## 想要整張桌子？

這些技能是備團。Fold&Roll 是桌子本身——角色卡、戰鬥地圖、先攻與骰子，為每人手中的手機與中間共用的桌子而造。

- **iOS：** https://apps.apple.com/app/fold-roll/id6822885522
- **Android 測試版：** https://play.google.com/apps/testing/com.kevin.rpgcompanion
- **網站：** https://kvnkillian.github.io/

從網站加入 Discord，分享你的桌邊故事、許願新技能，或回報一次糟糕的擲骰。

## 授權

MIT。自由使用這些技能、 fork、改作、在你的桌上使用。若你發布改作版本，附上回連連結會很受感謝，但不是必須。

這些技能中的 SRD 內容依據創用 CC 姓名標示 4.0 國際授權（SRD 5.2.1）與開放遊戲授權 v1.0a（SRD 5.1）使用。Wizards of the Coast、Dungeons & Dragons 與 D&D 皆為 Wizards of the Coast 的商標。本專案與 Wizards of the Coast 無關，亦未獲其背書。
