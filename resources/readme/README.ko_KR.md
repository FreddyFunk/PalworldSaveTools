<div align="center">

![PalworldSaveTools 로고](../resources/PalworldSaveTools_Blue.png)

# __테크_19__

**Palworld을 위한 포괄적인 저장 파일 편집 툴킷**

[![다운로드](https://img.shields.io/github/downloads/deafdudecomputers/PalworldSaveTools/total)](https://github.com/deafdudecomputers/PalworldTools/releases/latest)
[![라이선스](https://img.shields.io/github/license/deafdudecomputers/PalworldSaveTools)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Join_for_support-blue)](https://discord.gg/sYcZwcT4cT)
[![NexusMods](https://img.shields.io/badge/NexusMods-Download-orange)](https://www.nexusmods.com/palworld/mods/3190)

[영어](../resources/readme/README.en_US.md) | [简体中文](../resources/readme/README.zh_CN.md) | [독일어](../resources/readme/README.de_DE.md) | [스페인어](../resources/readme/README.es_ES.md) | [프랑스어](../resources/readme/README.fr_FR.md) | [Русский](자원/readme/README.ru_RU.md) | [일본어](../resources/readme/README.ja_JP.md) | [한국어](../resources/readme/README.ko_KR.md)

---

### **[GitHub 릴리스](https://github.com/deafdudecomputers/PalworldSaveTools/releases/latest)에서 독립형 버전을 다운로드하세요**

---

</div>

## __테크_10__

- [Features](#기능)
- [Installation](#설치)
- [Quick Start](#빠른 시작)
- [도구 개요](#tools-overview)
- [가이드](#guides)
- [Troubleshooting](#문제 해결)
- [Contributing](#기여)
- [라이센스](#license)

---

## Features

### 핵심 기능

| 특징 | 설명 |
| --------- | ------------- |
| **빠른 저장 구문 분석** | 사용 가능한 가장 빠른 저장 파일 리더 중 하나 |
| **플레이어 관리** | 보기, 편집, 이름 바꾸기, 레벨 변경, 기술 잠금 해제 및 플레이어 관리 |
| **길드 관리** | 플레이어 생성, 이름 변경, 이동, 실험실 연구 잠금 해제, 길드 관리 |
| **Pal 편집자** | 통계, 기술, IV, 순위, 영혼, 성별, 보스/행운 토글을 위한 전체 편집기 |
| **베이스캠프 도구** | 내보내기, 가져오기, 복제, 반경 조정 및 기지 관리 |
| **맵 뷰어** | 좌표와 세부정보가 포함된 대화형 기지 및 플레이어 지도 |
| **캐릭터 이전** | 다른 월드/서버 간 캐릭터 전송(교차 저장) |
| **전환 저장** | Steam 및 GamePass 형식 간 변환 |
| **월드 설정** | WorldOption 및 LevelMeta 설정 편집 |
| **타임스탬프 도구** | 음수 타임스탬프 수정 및 플레이어 시간 재설정 |

### 올인원 도구

**올인원 도구** 제품군은 포괄적인 저장 관리 기능을 제공합니다.

- **삭제 도구**
  - Players, 기지 또는 길드 삭제
  - 시간 임계값을 기준으로 비활성 플레이어 삭제
  - 중복 플레이어 및 빈 길드 제거
  - 참조되지 않거나 분리된 데이터 삭제

- **정리 도구**
  - 유효하지 않거나 수정된 ​​항목 제거
  - 유효하지 않은 친구 및 수동적 요소 제거
  - 불법 친구 수정(법적 최대 통계로 제한)
  - 잘못된 구조 제거
  - 대공 포탑 재설정
  - 개인 상자를 잠금 해제하세요

- **길드 도구**
  - 모든 길드 재건
  - 길드 간 플레이어 이동
  - 플레이어 길드장 만들기
  - 길드 이름 바꾸기
  - 최대 길드 레벨
  - 모든 연구실 연구 잠금 해제

- **플레이어 도구**
  - 플레이어 친구 통계 및 기술 편집
  - 모든 기술 잠금 해제
  - 관찰 케이지 잠금 해제
  - 레벨 업/다운 플레이어
  - 플레이어 이름 바꾸기

- **유틸리티 저장**
  - 임무 재설정
  - 던전 초기화
  - 타임스탬프 수정
  - 과도하게 채워진 재고 정리
  - PalDefender 명령 생성

### 추가 도구

| 도구 | 설명 |
| ------ | ------------- |
| **플레이어 친구 편집** | 통계, 기술, IV, 재능, 영혼, 순위 및 성별을 갖춘 완전한 친구 편집자 |
| **SteamID 변환기** | Steam ID를 Palworld UID로 변환 |
| **호스트 저장 수정** | 두 플레이어 간에 UID을 교환합니다(예: 호스트 교환의 경우). |
| **스왑 플레이어 UIDs** | 두 플레이어 간에 UID을 교환합니다. |
| **슬롯 인젝터** | 플레이어당 팔박스 슬롯 늘리기 |
| **지도 복원** | 모든 월드/서버에 잠금 해제된 지도 진행 상황 적용 |
| **세계 이름 바꾸기** | LevelMeta에서 세계 이름 변경 |
| **WorldOption 편집자** | 세계 설정 및 구성 편집 |
| **LevelMeta 편집자** | 월드 메타데이터 편집(이름, 호스트, 레벨) |
| **좌표 변환기** | 게임 내 좌표 변환 |

---

## Installation

### 전제 조건

**독립형(Windows)의 경우:**
- Windows 10/11
- [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-microsoft-visual-c-redistributable-version)(2015-2022)

**소스(Linux 또는 개발)에서 실행하는 경우:**
- Python 3.10 이상
- pip (Python 패키지 관리자)

### 독립형(Windows - 권장)

1. [GitHub 릴리스](https://github.com/deafdudecomputers/PalworldSaveTools/releases/latest)에서 최신 릴리스를 다운로드하세요.
2. zip 파일 추출
3. `PalworldSaveTools.exe`를 실행하세요.

### 소스에서(Linux 또는 개발용)

``배쉬
자식 복제 https://github.com/deafdudecomputers/PalworldSaveTools.git
CD PalworldSaveTools
pip 설치 -r 요구사항.txt
파이썬 start.py
````

---

## __테크_0__

1. **저장 파일 로드**
   - **파일 → 저장 로드**를 클릭하세요.
   - Palworld 저장 폴더로 이동하세요.
   - `Level.sav`를 선택하세요.

2. **데이터 탐색**
   - 탭을 사용하여 Players, 길드, 기지 또는 지도를 확인하세요.
   - 검색 및 필터링하여 특정 항목 찾기

3. **변경**
   - 편집, 삭제, 수정할 항목을 선택하세요.
   - 추가 옵션을 보려면 상황에 맞는 메뉴를 사용하세요.

4. **변경사항 저장**
   - **파일 → 변경 사항 저장**을 클릭합니다.
   - 백업이 자동으로 생성됩니다.

---

## 도구 개요

### 올인원 도구(AIO)

세 개의 탭이 있는 포괄적인 저장 관리를 위한 기본 인터페이스:

**Players 탭** - 서버의 모든 플레이어를 보고 관리합니다.
- 플레이어 이름, 레벨, 친구 수 편집
- 비활성 플레이어 삭제
- 플레이어 길드 및 마지막 온라인 시간 보기

**길드 탭** - 길드와 길드 기지를 관리합니다.
- 길드 이름 변경, 리더 변경
- 기본 위치 및 레벨 보기
- 비어 있거나 활동하지 않는 길드 삭제

**기지 탭** - 모든 베이스캠프 보기
- 기본 청사진 내보내기/가져오기
- 기지를 다른 길드에 복제
- 기본 반경 조정

### 맵 뷰어

세상의 대화형 시각화:
- 모든 기지 위치와 플레이어 위치 보기
- 길드 또는 플레이어 이름으로 필터링
- 자세한 정보를 보려면 마커를 클릭하세요.
- PalDefender에 대한 `killnearestbase` 명령 생성

### 캐릭터 이전

다른 세계/서버 간 캐릭터 전송(교차 저장):
- 단일 또는 모든 플레이어 전송
- 캐릭터, 친구, 인벤토리, 기술을 보존합니다.
- 협동조합과 dedicated server 사이의 마이그레이션에 유용합니다.

### 호스트 저장 수정

두 플레이어 간에 UID을 교환합니다.
- 한 플레이어에서 다른 플레이어로 진행 상황 전송
- host/co-op에서 서버로 이전하는 데 필수적입니다.
- 플레이어 간 호스트 역할을 교환하는 데 유용합니다.
- 플랫폼 교체에 유용합니다(Xbox ← Steam)
- 호스트/서버 UID 할당 문제 해결
- **메모:** Affected player must have a character created on the target save first

---

## 가이드

### 저장 파일 위치

**호스트/협동조합:**
````
%localappdata%\Pal\Saved\SaveGames\YOURID\RANDOMID\
````

**전용 서버:**
````
steamapps\common\Palworld\Pal\Saved\SaveGames\0\RANDOMSERVERID\
````

### 지도 잠금 해제

<상세>
<summary>지도 잠금 해제 지침을 펼치려면 클릭하세요.</summary>

1. `src\resources\`에서 `LocalData.sav` 복사
2. 서버/월드 저장 폴더 찾기
3. 기존 `LocalData.sav`를 복사된 파일로 교체하세요.
4. 완전히 잠금 해제된 지도로 게임을 시작하세요

> **참고:** 자동 백업을 통해 잠금 해제된 지도를 모든 월드/서버에 한 번에 적용하려면 PST의 **도구 → 지도 복원** 옵션을 사용하세요.

</세부사항>

### 호스트 → 서버 이전

<상세>
<summary>호스트에서 서버로의 전송 가이드를 펼치려면 클릭하세요</summary>

1. 호스트 저장에서 `Level.sav` 및 `Players` 폴더를 복사합니다.
2. dedicated server 저장 폴더에 붙여넣기
3. 서버를 시작하고 새로운 캐릭터를 생성하세요
4. 자동 저장을 기다린 후 닫습니다.
5. **Fix Host Save**를 사용하여 GUID을(를) 마이그레이션하세요
6. 파일을 다시 복사하고 실행하세요.

**수정 호스트 저장 사용:**
- 임시 폴더에서 `Level.sav`를 선택하세요.
- **이전 캐릭터**를 선택하세요(원본 저장에서)
- **새 캐릭터**(방금 생성한 캐릭터)를 선택하세요.
- **이전**을 클릭하세요.

</세부사항>

### 호스트 스왑(호스트 변경)

<상세>
<summary>호스트 스왑 가이드를 펼치려면 클릭</summary>

**배경:**
- 호스트는 항상 `0001.sav`를 사용합니다. 호스트가 누구이든 동일한 UID입니다.
- 각 클라이언트는 고유한 일반 UID 저장(예: `123xxx.sav`, `987xxx.sav`)을 사용합니다.

**전제조건:**
두 플레이어(이전 호스트와 새 호스트) 모두 일반 저장을 생성해야 합니다. 이는 호스트의 세계에 합류하고 새로운 캐릭터를 생성함으로써 발생합니다.

**단계:**

1. **정기 저장이 있는지 확인**
   - 플레이어 A(이전 호스트)는 일반 저장(예: `123xxx.sav`)을 가지고 있어야 합니다.
   - 플레이어 B(새 호스트)는 일반 저장(예: `987xxx.sav`)을 가지고 있어야 합니다.

2. **이전 호스트의 호스트 저장을 일반 저장으로 전환**
   - PalworldSaveTools **Fix Host Save**를 사용하여 교체합니다.
   - 이전 호스트의 `0001.sav` → `123xxx.sav`
   - (이렇게 하면 이전 호스트의 진행 상황이 호스트 슬롯에서 일반 플레이어 슬롯으로 이동됩니다.)

3. **새 호스트의 일반 저장을 호스트 저장으로 전환**
   - PalworldSaveTools **Fix Host Save**를 사용하여 교체합니다.
   - 새 호스트의 `987xxx.sav` → `0001.sav`
   - (이렇게 하면 새 호스트의 진행 상황이 호스트 슬롯으로 이동됩니다.)

**결과:**
- 플레이어 B는 이제 `0001.sav`에서 자신의 캐릭터와 친구들이 있는 호스트입니다.
- 플레이어 A는 `123xxx.sav`의 원래 진행 상황으로 클라이언트가 됩니다.

</세부사항>

### 기본 내보내기/가져오기

<상세>
<summary>기본 내보내기/가져오기 가이드를 확장하려면 클릭</summary>

**베이스 내보내기:**
1. PST에 저장 내용을 로드하세요.
2. 기지 탭으로 이동
3. 베이스 우클릭 → 베이스 내보내기
4. `.json` 파일로 저장

**베이스 가져오기:**
1. 기지 탭 또는 기본 지도 뷰어로 이동하세요.
2. 기지를 가져오려는 길드를 마우스 오른쪽 버튼으로 클릭하세요.
3. 가져오기 베이스 선택
4. 내보낸 `.json` 파일을 선택하세요.

**베이스 복제:**
1. 베이스를 마우스 오른쪽 버튼으로 클릭 → 베이스 복제
2. 대상 길드 선택
3. 베이스는 오프셋 위치 지정을 통해 복제됩니다.

**베이스 반경 조정:**
1. 베이스를 마우스 오른쪽 버튼으로 클릭 → 반경 조정
2. 새 반경을 입력하세요(50% - 1000%).
3. 구조를 재할당하려면 게임 내 저장 파일을 저장하고 로드하세요.

</세부사항>

---

## Troubleshooting

### "VCRUNTIME140.dll을 찾을 수 없습니다"

**해결책:** [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-microsoft-visual-c-redistributable-version) 설치

### 저장 구문 분석 시 `struct.error`

**원인:** 오래된 저장 파일 형식

**해결책:**
1. 게임에서 저장 파일을 로드합니다(Solo, Coop 또는 Dedicated Server 모드).
2. 그러면 자동 구조 업데이트가 트리거됩니다.
3. 최신 게임 패치나 그 이후에 저장 내용이 업데이트되었는지 확인하세요.

### GamePass 변환기가 작동하지 않습니다

**해결책:**
1. Palworld의 GamePass 버전을 닫습니다.
2. 몇 분만 기다려주세요
3. Steam → GamePass 변환기를 실행하세요.
4. GamePass에서 Palworld을 실행하여 확인하세요.

---

## 소스에서 빌드

``배쉬
# 저장소 복제
자식 복제 https://github.com/deafdudecomputers/PalworldSaveTools.git

# 종속성 설치
pip 설치 -r 요구사항.txt

# 애플리케이션 실행
파이썬 start.py
````

독립 실행형 실행 파일을 빌드하려면 빌드 스크립트를 사용하세요.
``배쉬
파이썬 스크립트/build.py
````

---

## __기술_3__

기여를 환영합니다! 언제든지 Pull Request를 제출해 주세요.

1. 저장소 포크
2. 기능 브랜치를 생성하세요(`git checkout -b feature/AmazingFeature`)
3. 변경 사항을 커밋합니다(`git commit -m 'Add some AmazingFeature'`)
4. 브랜치로 푸시(`git push Origin feature/AmazingFeature`)
5. 끌어오기 요청 열기

---

## 면책조항

**이 도구를 사용할 때 발생하는 위험은 사용자 본인의 책임입니다. 수정하기 전에 항상 저장 파일을 백업하십시오.**

이 도구를 사용함으로써 발생할 수 있는 저장 데이터의 손실이나 문제에 대해 개발자는 책임을 지지 않습니다.

---

## 지원하다

- **__기술_1__:** [Join us for support, base builds, and more!](https://discord.gg/sYcZwcT4cT)
- **GitHub 문제:** [Report a bug](https://github.com/deafdudecomputers/PalworldSaveTools/issues)
- **선적 서류 비치:** [Wiki](https://github.com/deafdudecomputers/PalworldSaveTools/wiki) *(Currently in development)*

---

## 라이센스

이 프로젝트는 MIT License에 따라 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

---

## 감사의 말씀

- **Palworld** developed by Pocketpair, Inc.
- 이 도구를 개선하는 데 도움을 준 모든 기여자와 커뮤니티 구성원에게 감사드립니다.

---

<div align="center">

**Palworld 커뮤니티를 위해 ❤️으로 제작됨**

[⬆ 맨 위로 이동](#palworldsavetools)

</div>
