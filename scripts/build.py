"""Gera os pacotes de distribuição da skill PONTE.

Saídas em dist/:
- metodo-ponte.zip: a pasta da skill, pronta para enviar ao Claude (claude.ai,
  app desktop) ou copiar para ~/.claude/skills no Claude Code.
- PONTE-instrucoes-completas.md: tudo em um arquivo só, para colar nas
  instruções de outras IAs (ChatGPT, Gemini, Copilot...).

Uso: python scripts/build.py
"""
import pathlib
import re
import zipfile

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SKILL = RAIZ / "metodo-ponte"
DIST = RAIZ / "dist"

ORDEM_REFERENCIAS = [
    "guia-de-percepcao.md",
    "comportamentos.md",
    "leitura-de-transcricao.md",
    "inteligencia-do-grupo.md",
    "transcricao-elaborada.md",
    "cenarios.md",
    "metodo.md",
]


def gerar_zip() -> pathlib.Path:
    destino = DIST / "metodo-ponte.zip"
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for arquivo in sorted(SKILL.rglob("*")):
            if arquivo.is_file():
                z.write(arquivo, arquivo.relative_to(RAIZ).as_posix())
    return destino


def gerar_arquivo_unico() -> pathlib.Path:
    skill = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    corpo = re.sub(r"\A---\n.*?\n---\n", "", skill, flags=re.S).strip()
    partes = [
        "# Instruções completas: Método PONTE\n\n"
        "Cole este arquivo inteiro nas instruções de um assistente de IA "
        "(GPT personalizado, Gem, agente) ou no início de uma conversa. "
        "Quando o texto citar `references/<arquivo>.md`, use a seção de "
        "mesmo nome mais abaixo neste arquivo.",
        corpo,
    ]
    for nome in ORDEM_REFERENCIAS:
        texto = (SKILL / "references" / nome).read_text(encoding="utf-8").strip()
        texto = re.sub(r"(?m)^#", "##", texto)  # rebaixa os títulos um nível
        partes.append(f"---\n\n# references/{nome}\n\n{texto}")
    destino = DIST / "PONTE-instrucoes-completas.md"
    destino.write_text("\n\n".join(partes) + "\n", encoding="utf-8")
    return destino


if __name__ == "__main__":
    DIST.mkdir(exist_ok=True)
    for caminho in (gerar_zip(), gerar_arquivo_unico()):
        print("gerado:", caminho.relative_to(RAIZ))
