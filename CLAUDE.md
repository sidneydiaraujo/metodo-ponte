# Método PONTE: skill de IA

Repositório **público** da skill que aplica o Método PONTE (alinhar culturas rumo a um
desejo comum). Criado como entrega para os alunos da Pós em Gestão Ágil de Projetos
(CESAR School) baixarem e instalarem na IA deles.

## Contexto

- O método nasceu como atividade final em grupo da pós. A fonte do conteúdo é o documento
  final v2.3 (`Downloads\ponte-final.md` / `Metodo_PONTE_final.docx` do Sidney), que já
  incorpora o teste sintético (laboratório de IA em 4 passos) e as melhorias da versão 2.0.
- `metodo-ponte/references/metodo.md` é extraído desse documento. Se o documento mudar,
  atualize esse arquivo também.

## Regras do comportamento da skill (não perder ao editar)

- Oferecer transcrição elaborada (limpa, ata PONTE, resumo, completa) seguindo o Perfil de
  transcrição do usuário; fidelidade total à fala.
- Pedir sempre a percepção do usuário (áudio ou texto) antes de qualquer análise, e
  oferecer o guia do que falar.
- Investigar antes de concluir; hipóteses explícitas; práticas, não pessoas.
- Desejo comum como coração; 5 Pilares como critério de decisão; regra de prioridade.
- Culturas diversas, nenhuma é a referência; mostrar que o usuário pode simular qualquer
  cenário e que a skill sugere cenários e dicas.
- Público amplo (alunos, qualquer IA): linguagem simples, pt-BR, nada específico de empresa.

## Publicar uma nova versão

1. Edite a skill em `metodo-ponte/`.
2. `python scripts/build.py` (atualiza `dist/`).
3. Commit + push e crie uma release com os dois arquivos de `dist/` como anexos
   (`gh release create vX.Y dist/metodo-ponte.zip dist/PONTE-instrucoes-completas.md`).
