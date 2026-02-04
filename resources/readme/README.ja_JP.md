<div align="center">

![PalworldSaveTools ロゴ](resources/PalworldSaveTools_Blue.png)

# Palworld保存ツール

**Palworld 用の包括的な保存ファイル編集ツールキット**

[![ダウンロード](https://img.shields.io/github/downloads/deafdudecomputers/PalworldSaveTools/total)](https://github.com/deafdudecomputers/PalworldTools/releases/latest)
[！[ライセンス](https://img.shields.io/github/license/deafdudecomputers/PalworldSaveTools)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Join_for_support-blue)](https://discord.gg/sYcZwcT4cT)
[![NexusMods](https://img.shields.io/badge/NexusMods-Download-orange)](https://www.nexusmods.com/palworld/mods/3190)

[英語](../resources/readme/README.en_US.md) | [简体中文](../resources/readme/README.zh_CN.md) | [Deutsch](../resources/readme/README.de_DE.md) | [Español](../resources/readme/README.es_ES.md) | [Français](../resources/readme/README.fr_FR.md) | [Русский](../resources/readme/README.ru_RU.md) | [日本語](../resources/readme/README.ja_JP.md) | [한국어](../resources/readme/README.ko_KR.md)

---

### **Download the standalone version from [GitHub リリース](https://github.com/deafdudecomputers/PalworldSaveTools/releases/latest)**

---

</div>

## Table of Contents

- [Features](#機能)
- [Installation](#インストール)
- [Quick Start](#クイックスタート)
- [ツールの概要](#tools-overview)
- [ガイド](#guides)
- [Troubleshooting](#トラブルシューティング)
- [Contributing](#貢献)
- [ライセンス](#ライセンス)

---

## Features

### コア機能

| 特徴 | 説明 |
| --------- | ------------- |
| **高速保存解析** | 利用可能な保存ファイル リーダーの中で最も速いものの 1 つ |
| **プレイヤー管理** | 表示、編集、名前変更、レベル変更、テクノロジーのロック解除、プレーヤーの管理 |
| **ギルド管理** | プレイヤーの作成、名前変更、移動、ラボ研究のロック解除、ギルドの管理 |
| **Pal 編集者** | ステータス、スキル、IV、ランク、ソウル、性別、ボス/ラッキー切り替えの完全エディター |
| **ベースキャンプツール** | エクスポート、インポート、クローン作成、半径の調整、およびベースの管理 |
| **マップビューア** | 座標と詳細を含むインタラクティブなベースとプレーヤーのマップ |
| **キャラクター転送** | 異なるワールド/サーバー間でキャラクターを転送 (クロスセーブ) |
| **変換を保存** | Steam 形式と GamePass 形式の間で変換します |
| **ワールド設定** | WorldOption および LevelMeta 設定を編集する |
| **タイムスタンプ ツール** | 負のタイムスタンプを修正し、プレーヤーの時間をリセットします |

### オールインワン ツール

**オールインワン ツール** スイートは、包括的な保存管理を提供します。

- **削除ツール**
  - Players、拠点、またはギルドを削除します
  - 時間のしきい値に基づいて非アクティブなプレーヤーを削除します
  - 重複したプレイヤーと空のギルドを削除する
  - 参照されていない/孤立したデータを削除する

- **クリーンアップツール**
  - 無効な/変更されたアイテムを削除する
  - 無効な仲間とパッシブを削除する
  - 違法な仲間を修正（合法的な最大ステータスに制限）
  - 無効な構造を削除する
  - 対空砲塔をリセットする
  - プライベートチェストのロックを解除する

- **ギルドツール**
  - すべてのギルドを再構築する
  - ギルド間でプレイヤーを移動する
  - プレイヤーのギルドリーダーを作る
  - ギルド名の変更
  - 最大ギルドレベル
  - すべての研究室の研究をロック解除する

- **プレーヤーツール**
  - プレイヤー仲間のステータスとスキルを編集する
  - すべてのテクノロジーのロックを解除する
  - 視聴ケージのロックを解除する
  - プレイヤーのレベルアップ/レベルダウン
  - プレイヤーの名前を変更する

- **ユーティリティの保存**
  - ミッションをリセットする
  - ダンジョンをリセットする
  - タイムスタンプを修正する
  - 過剰な在庫を削減する
  - PalDefender コマンドを生成する

### 追加ツール

| 道具 | 説明 |
| ------ | ------------- |
| **プレイヤー仲間を編集** | ステータス、スキル、個体値、タレント、ソウル、ランク、性別を備えた完全な仲間エディター |
| **SteamID コンバーター** | Steam ID を Palworld UID に変換します |
| **ホスト保存を修正** | 2 人のプレイヤー間で UID を交換します (ホスト交換など) |
| **プレーヤー UIDs を交換します** | 2 人のプレイヤー間で UID を交換します |
| **スロットインジェクター** | プレイヤーごとのパルボックススロットを増やす |
| **マップを復元** | ロック解除されたマップの進行状況をすべてのワールド/サーバーに適用します |
| **ワールドの名前を変更** | LevelMeta でワールド名を変更する |
| **WorldOption 編集者** | ワールドの設定と構成を編集する |
| **LevelMeta 編集者** | ワールドのメタデータ (名前、ホスト、レベル) を編集します |
| **座標コンバータ** | ゲーム内座標を変換する |

---

## Installation

### 前提条件

**スタンドアロン (Windows) の場合:**
- Windows 10/11
- [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-microsoft-visual-c-redistributable-version) (2015-2022)

**ソースから実行する場合 (Linux または開発):**
- Python 3.10 以降
- pip (Python パッケージ マネージャー)

### スタンドアロン (Windows - 推奨)

1. [GitHub リリース](https://github.com/deafdudecomputers/PalworldSaveTools/releases/latest) から最新リリースをダウンロードします。
2. zipファイルを解凍します
3. 「PalworldSaveTools.exe」を実行します。

### ソースから (Linux または開発用)

```bash
git clone https://github.com/deafdudecomputers/PalworldSaveTools.git
cd PalworldSaveTools
pip install -r requirements.txt
python start.py
```

---

## Quick Start

1. **セーブデータをロード**
   - **[ファイル] → [読み込み] [保存]** をクリックします。
   - Palworld 保存フォルダーに移動します
   - 「Level.sav」を選択します

2. **データを探索する**
   - タブを使用して、Players、ギルド、拠点、またはマップを表示します
   - 特定のエントリを見つけるための検索とフィルタリング

3. **変更を加える**
   - 編集、削除、または変更する項目を選択します
   - 追加オプションについてはコンテキスト メニューを使用する

4. **変更を保存**
   - **[ファイル] → [変更を保存]** をクリックします。
   - バックアップは自動的に作成されます

---

## ツールの概要

### オールインワン ツール (AIO)

包括的な保存管理のためのメイン インターフェイスには 3 つのタブがあります。

**Players タブ** - サーバー上のすべてのプレーヤーを表示および管理します
- プレイヤー名、レベル、仲間数を編集する
- 非アクティブなプレイヤーを削除する
- プレイヤーのギルドと前回のオンライン時間を表示

**ギルド タブ** - ギルドとその拠点を管理します
- ギルドの名前を変更し、リーダーを変更する
- 拠点の場所とレベルを表示する
- 空のギルドまたは非アクティブなギルドを削除する

**「ベース」タブ** - すべてのベースキャンプを表示
- ベースブループリントのエクスポート/インポート
- 他のギルドに基地のクローンを作成する
- ベース半径を調整する

### マップビューア

あなたの世界をインタラクティブに視覚化:
- すべての拠点の場所とプレーヤーの位置を表示する
- ギルド名またはプレイヤー名でフィルタリングする
- マーカーをクリックすると詳細情報が表示されます
- PalDefender の「killnearestbase」コマンドを生成する

### キャラクター転送

異なるワールド/サーバー間でキャラクターを転送する (クロスセーブ):
- 1 人のプレイヤーまたは全員のプレイヤーを転送する
- キャラクター、仲間、インベントリ、テクノロジーを保存します
- 協力プレイと dedicated server の間の移行に役立ちます

### ホスト保存を修正

2 人のプレイヤー間で UID を交換します:
- 進行状況をあるプレイヤーから別のプレイヤーに転送する
- host/co-op からサーバーへの転送に必須
- プレイヤー間でホストの役割を交換するのに役立ちます
- プラットフォームの交換に便利 (Xbox ↔ Steam)
- ホスト/サーバー UID 割り当ての問題を解決します
- **注記：** Affected player must have a character created on the target save first

---

## ガイド

### ファイルの保存場所

**ホスト/協力:**
```
%localappdata%\Pal\Saved\SaveGames\YOURID\RANDOMID\
```

**専用サーバー:**
```
steamapps\common\Palworld\Pal\Saved\SaveGames\0\RANDOMSERVERID\
```

### マップのロック解除

<詳細>
<summary>クリックしてマップのロック解除手順を展開します</summary>

1. `src\resources\` から `LocalData.sav` をコピーします
2. サーバー/ワールド保存フォルダーを見つけます
3. 既存の LocalData.sav をコピーしたファイルで置き換えます
4. 完全にロックが解除されたマップでゲームを起動します

> **注:** PST の **ツール → マップの復元** オプションを使用して、自動バックアップを使用してロック解除されたマップをすべてのワールド/サーバーに一度に適用します。

</詳細>

### ホスト→サーバー転送

<詳細>
<summary>クリックしてホストからサーバーへの転送ガイドを展開します</summary>

1. ホスト保存から `Level.sav` および `Players` フォルダーをコピーします
2. dedicated server 保存フォルダーに貼り付けます
3. サーバーを起動し、新しいキャラクターを作成します
4. 自動保存されるまで待ってから閉じます
5. **ホスト保存の修正** を使用して GUID を移行します
6. ファイルをコピーして戻して起動する

**修正ホスト保存の使用:**
- 一時フォルダーから「Level.sav」を選択します
- **古いキャラクター** (元のセーブから) を選択してください
- **新しいキャラクター** (先ほど作成したもの) を選択します
- [**移行**] をクリックします

</詳細>

### ホストスワップ (ホストの変更)

<詳細>
<summary>クリックしてホスト スワップ ガイドを展開します</summary>

**背景：**
- ホストは常に `0001.sav` を使用します - 誰がホストしても同じ UID
- 各クライアントは、固有の通常の UID セーブ (例: `123xxx.sav`、`987xxx.sav`) を使用します。

**前提条件:**
両方のプレーヤー (古いホストと新しいホスト) が通常のセーブを生成する必要があります。これは、ホストの世界に参加し、新しいキャラクターを作成することで発生します。

**手順:**

1. **定期的な保存が存在することを確認してください**
   - プレーヤー A (古いホスト) には通常のセーブ (例: `123xxx.sav`) が必要です。
   - プレーヤー B (新しいホスト) には通常のセーブ (例: `987xxx.sav`) が必要です。

2. **古いホストのホスト セーブを通常のセーブに交換**
   - PalworldSaveTools **ホスト セーブを修正** を使用して交換します。
   - 旧ホストの「0001.sav」→「123xxx.sav」
   - (これにより、古いホストの進行状況がホスト スロットから通常のプレイヤー スロットに移動します)

3. **新しいホストの通常の保存をホストの保存に交換**
   - PalworldSaveTools **ホスト セーブを修正** を使用して交換します。
   - 新しいホストの `987xxx.sav` → `0001.sav`
   - (これにより、新しいホストの進行状況がホスト スロットに移動されます)

**結果：**
- プレイヤー B はホストとなり、「0001.sav」内に自分のキャラクターと仲間がいます。
- プレイヤー A は、`123xxx.sav` にある元の進行状況を持つクライアントになります。

</詳細>

### 基本エクスポート/インポート

<詳細>
<summary>クリックして基本的なエクスポート/インポート ガイドを展開します</summary>

**ベースのエクスポート:**
1. セーブデータを PST にロードします
2. 「拠点」タブに移動します
3. ベースを右クリック → ベースのエクスポート
4. `.json` ファイルとして保存

**ベースのインポート:**
1. 「Bases」タブまたは「Base Map Viewer」に移動します。
2. 拠点をインポートしたいギルドを右クリックします
3. インポートベースの選択
4. エクスポートした「.json」ファイルを選択します

**ベースのクローン作成:**
1. ベースを右クリック→「ベースのクローン」
2. 対象ギルドを選択
3. ベースはオフセット配置で複製されます

**ベース半径の調整:**
1. ベースを右クリック → 半径を調整
2. 新しい半径を入力してください (50% - 1000%)
3. 再割り当てする構造物については、ゲーム内で保存してロードします。

</詳細>

---

## Troubleshooting

### 「VCRUNTIME140.dll が見つかりませんでした」

**Solution:** Install [マイクロソフト Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-microsoft-visual-c-redistributable-version)

### `struct.error` when parsing save

**原因:** 保存ファイル形式が古い

**解決：**
1. ゲームにセーブデータをロードします (ソロ、コープ、または専用サーバー モード)
2. これにより、構造の自動更新がトリガーされます
3. 最新のゲームパッチ以降にセーブデータが更新されていることを確認してください

### GamePass コンバータが動作しない

**解決：**
1. Palworld の GamePass バージョンを閉じます
2. 数分待ちます
3. Steam → GamePass コンバータを実行します
4. GamePass で Palworld を起動して確認してください

---

## ソースからのビルド

```bash
# Clone the repository
git clone https://github.com/deafdudecomputers/PalworldSaveTools.git

# Install dependencies
pip install -r requirements.txt

# Run the application
python start.py
```

スタンドアロンの実行可能ファイルをビルドするには、ビルド スクリプトを使用します。
```bash
python scripts/build.py
```

---

## Contributing

貢献は大歓迎です!お気軽にプルリクエストを送信してください。

1. リポジトリをフォークする
2. 機能ブランチを作成します (`git checkout -b feature/AmazingFeature`)
3. 変更をコミットします (`git commit -m 'Add some AmazingFeature'`)
4. ブランチにプッシュします (`git Push Origin feature/AmazingFeature`)
5. プルリクエストを開く

---

## 免責事項

**このツールはご自身の責任で使用してください。変更を加える前に、必ず保存ファイルをバックアップしてください。**

開発者は、このツールの使用によって発生する可能性のあるセーブデータの損失や問題について責任を負いません。

---

＃＃ サポート

- **Discord:** [Join us for support, base builds, and more!](https://discord.gg/sYcZwcT4cT)
- **GitHub 問題:** [Report a bug](https://github.com/deafdudecomputers/PalworldSaveTools/issues)
- **ドキュメント:** [Wiki](https://github.com/deafdudecomputers/PalworldSaveTools/wiki) *(Currently in development)*

---

## ライセンス

このプロジェクトは MIT License に基づいてライセンスされています。詳細については、[LICENSE](LICENSE) ファイルを参照してください。

---

## 謝辞

- **__技術_0__** developed by Pocketpair, Inc.
- このツールの改善に協力してくれたすべての貢献者とコミュニティ メンバーに感謝します

---

<div align="center">

**Palworld コミュニティのために ❤️ で作成されました**

[⬆ トップに戻る](#palworldsavetools)

</div>
