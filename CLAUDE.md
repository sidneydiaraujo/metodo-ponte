# Método PONTE: skill de IA

Repositório **público** da skill que aplica o Método PONTE (alinhar culturas rumo a um
desejo comum), para qualquer pessoa baixar e instalar na própria IA.

## Contexto

- A fonte do conteúdo é o documento final do método (v2.3), que já incorpora o teste
  sintético (laboratório de IA em 4 passos) e as melhorias da versão 2.0.
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
- Inteligência do grupo na transcrição: % da fala e proposições por pessoa, culturas pelas
  palavras, dinâmica de grupo, sinais que a transcrição apaga, Pontoneiro provável como foco.
- Alerta de xenofobia, discriminação e falta de respeito, mesmo nas entrelinhas: descrever a
  fala, não rotular; sobre a pessoa, só "pode ser mais difícil, não é foco para acordos, evite
  pressioná-la". Não indicar o que fazer com ela.
- Entrega direta ao foco: sem análises gerais; só o que tem evidência; sem dado, perguntar e
  procurar na transcrição. Resumo no formato do usuário; sem pedido, direto e objetivo.
- Público amplo (qualquer pessoa, qualquer IA): linguagem simples, pt-BR, sem citar
  instituições, empresas ou cursos de origem.

## Publicar uma nova versão

1. Edite a skill em `metodo-ponte/`.
2. `python scripts/build.py` (atualiza `dist/`).
3. Commit + push e crie uma release com os dois arquivos de `dist/` como anexos
   (`gh release create vX.Y dist/metodo-ponte.zip dist/PONTE-instrucoes-completas.md`).
