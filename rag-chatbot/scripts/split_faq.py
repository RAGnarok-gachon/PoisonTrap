"""
faq_source.md를 "## " 제목 단위로 쪼개서 rag-chatbot/data/normal/ 아래에
개별 문서 파일로 저장한다. 각 파일이 나중에 RAG 지식베이스에 들어갈
"정상 문서" 하나가 된다 (포이즈닝 문서와 같은 레벨에서 비교하기 위해
파일 단위를 맞춰두는 것).

사용법:
    python rag-chatbot/scripts/split_faq.py
"""

import re
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "data" / "faq_source.md"
OUT_DIR = Path(__file__).resolve().parent.parent / "data" / "normal"


def slugify(title: str) -> str:
    s = title.strip()
    s = re.sub(r"[^\w가-힣]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s.lower()


def main():
    text = SRC.read_text(encoding="utf-8")
    # 최상위 제목(# ...)과 안내문 한 줄은 건너뛰고, "## " 섹션만 추출
    sections = re.split(r"\n(?=## )", text)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    count = 0
    for section in sections:
        section = section.strip()
        if not section.startswith("## "):
            continue
        title_line, _, body = section.partition("\n")
        title = title_line[3:].strip()
        body = body.strip()

        count += 1
        slug = slugify(title)
        filename = f"{count:02d}_{slug}.md"
        out_path = OUT_DIR / filename

        content = f"# {title}\n\n{body}\n"
        out_path.write_text(content, encoding="utf-8")
        print(f"저장: {out_path.relative_to(OUT_DIR.parent.parent.parent)}")

    print(f"\n총 {count}개 정상 문서 생성 완료 → {OUT_DIR}")


if __name__ == "__main__":
    main()
