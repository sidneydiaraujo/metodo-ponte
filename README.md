# 🌉 Método PONTE: skill de IA

**Alinhar culturas sem apagar nenhuma.**

O PONTE é um método para levar duas ou mais culturas (áreas, empresas, cliente e fornecedor, gerações, regiões, países) a um **desejo comum**, sem que uma cultura se imponha à outra. Uma pessoa aplica sozinha, dentro de uma reunião comum, e o outro lado não precisa conhecer o método.

Esta skill transforma a sua IA num facilitador do método. Ela:

- **pede a sua percepção primeiro**, por áudio ou por escrito, e te guia sobre o que falar se você não souber por onde começar;
- **investiga** a situação: quem são as margens, qual é o desejo comum, o que ninguém disse;
- **lê transcrições e conversas** pelas 7 Correntes e encontra **lacunas, ruídos, atritos e rupturas**;
- reconhece **comportamentos do outro lado da ponte** e mostra como desviar deles sem impor o seu jeito;
- **lê o grupo na transcrição**: quem pesa na reunião (% da fala e propostas feitas), que culturas aparecem nas palavras, a dinâmica do grupo, quem é o **foco** para construir acordos (o Pontoneiro provável) e sinais que a transcrição costuma apagar, como interrupções e perguntas ignoradas;
- **sinaliza xenofobia, discriminação e falta de respeito**, mesmo nas entrelinhas, indicando só que aquela pessoa pode ser mais difícil e não é o foco para tirar acordos;
- vai **direto ao foco**: sem análises longas, sem inventar o que não está no texto, e pergunta quando falta dado;
- dá **direção guiada pelos 5 Pilares**, com frases prontas, plano B e quando escalar;
- **elabora transcrições de reuniões**: transforma a transcrição bruta em transcrição limpa, ata PONTE, resumo ou versão completa, do jeito que **você configurar**, inclusive com uma versão no formato da outra margem;
- **simula e valida qualquer cenário** que você imaginar, encena a outra margem para você ensaiar e sugere cenários e dicas.

---

## ⬇️ Baixar

Vá em **[Releases](../../releases/latest)** e baixe:

| Arquivo | Para quem |
|---|---|
| `metodo-ponte.zip` | Quem usa **Claude** (site, app ou Claude Code) |
| `PONTE-instrucoes-completas.md` | Quem usa **ChatGPT, Gemini, Copilot** ou outra IA |

Os mesmos arquivos também estão na pasta [`dist/`](dist/).

## 🛠️ Instalar

### Claude (site claude.ai ou app desktop)

1. Baixe o `metodo-ponte.zip` e **não descompacte**.
2. No Claude, abra **Configurações → Capacidades (Capabilities)** e procure a seção **Skills**. O nome do menu pode variar um pouco entre versões.
3. Se for preciso, ative **execução de código e criação de arquivos**, que é o recurso que permite usar skills.
4. Clique em **Enviar skill (Upload skill)** e escolha o zip.
5. Pronto: em qualquer conversa, fale de uma reunião difícil ou peça "aplica o método PONTE", e a skill entra em ação.

### Claude Code (terminal)

Descompacte o zip dentro da pasta de skills do seu usuário:

```bash
# macOS / Linux
unzip metodo-ponte.zip -d ~/.claude/skills/

# Windows (PowerShell)
Expand-Archive metodo-ponte.zip -DestinationPath "$HOME\.claude\skills\"
```

O resultado deve ser `~/.claude/skills/metodo-ponte/SKILL.md`.

### ChatGPT, Gemini, Copilot e outras IAs

Essas IAs não leem a pasta da skill, mas funcionam com as instruções em um arquivo só:

- **ChatGPT:** crie um GPT personalizado (Explorar GPTs → Criar), cole o conteúdo de `PONTE-instrucoes-completas.md` em **Instruções** ou envie o arquivo em **Conhecimento** com uma instrução curta, como "Siga o arquivo PONTE-instrucoes-completas.md".
- **Gemini:** crie um **Gem** e cole o conteúdo nas instruções.
- **Qualquer IA:** anexe o arquivo no início da conversa e escreva "Siga estas instruções a partir de agora".

## 💬 Como usar

Fale normalmente. Alguns exemplos:

- "Tenho reunião amanhã com o Comercial e a última terminou em mal-estar. Me ajuda a preparar?"
- "Vou colar a transcrição da reunião com o cliente. O que deu ruído?"
- "O fornecedor copiou meu diretor num e-mail reclamando do prazo. E agora?"
- "Quero testar um cenário: meu time ágil vai começar a trabalhar com uma área que só aceita cronograma."
- "Faz o papel do gestor da filial para eu ensaiar a abertura da reunião."
- "Organiza essa transcrição do Teams numa ata e faz uma versão curta para mandar no WhatsApp do Comercial."
- "Nessa transcrição, quem dominou a reunião e com quem eu devo construir o próximo acordo?"
- "O que é o método PONTE?"

A skill sempre começa pedindo a sua percepção. Pode **gravar um áudio** (o microfone ou o ditado por voz da sua IA serve) ou escrever. Um minuto já basta.

### 📝 Configure sua transcrição

A skill elabora a transcrição da reunião no formato que você escolher. Copie o bloco abaixo, ajuste as opções e cole junto com a transcrição. Melhor ainda: guarde-o nas instruções de um Projeto do Claude, de um GPT ou de um Gem, ou no seu `CLAUDE.md`, e a skill passa a seguir sempre o seu perfil.

```
PERFIL DE TRANSCRIÇÃO PONTE
formato: ata PONTE            (limpa · ata PONTE · resumo · completa)
pessoas: papéis               (papéis · iniciais · nomes)
marcações PONTE: sim          (destaca desejo comum, acordos, lacunas, termos ambíguos)
detalhe: enxuto               (enxuto · padrão · detalhado)
marcas de tempo: remover      (manter · remover)
idioma: o da reunião
saída: texto formatado        (texto formatado · texto simples para colar · tabela)
versão para a outra margem: não   (ou: "sim, mensagem curta de WhatsApp")
foco: reunião toda            (reunião toda · só decisões · só o tema ___)
```

Ainda não tem a transcrição? A skill explica como gerá-la no Teams, no Meet, no Zoom ou no celular. Anotações feitas à mão também servem.

**Cuidados:** use transcrições só com o consentimento dos participantes e retire nomes e dados pessoais antes de enviar. A IA investiga e sugere; quem conversa e decide é você.

## 🧭 O método em um cartão

```
MÉTODO PONTE — alinhar culturas sem apagar nenhuma

P  Percepção ........ Como a outra margem trabalha?   → Releia pelas 7 Correntes
O  Objetivo comum ... O que só fazemos juntos?        → Desejo comum em 1 frase
N  Normas ........... Como vamos combinar as coisas?  → 1 ou 2 acordos construídos juntos
T  Tradução ......... O que eu disse foi entendido?   → Dupla tradução
E  Evolução ......... Estamos mais perto?             → 6 Sinais + 1 ajuste

Correntes:  Tom · Canal · Ritmo · Registro · Discordância · Autoridade · Vínculo
Tensão:     Ruído → Atrito → Ruptura
Prioridade: inegociáveis > desejo comum > jeito de cada margem
Sem acordo: tente outro caminho → escale ao solicitante do desejo
Regra de ouro: práticas, não pessoas. Nenhuma margem é a referência.
```

**5 Pilares:** (1) Entenda antes de corrigir · (2) Diga o que está implícito · (3) Desejo comum, caminhos respeitados · (4) Cada margem decide o que é seu · (5) Método é agnóstico.

## 📁 Estrutura

```
metodo-ponte/                  ← a skill (a pasta que vai para a IA)
  SKILL.md                     ← como a skill conduz a conversa
  references/
    metodo.md                  ← o método completo (v2.3)
    guia-de-percepcao.md       ← o que falar no áudio ou escrever
    comportamentos.md          ← comportamentos do outro lado e como desviar
    leitura-de-transcricao.md  ← como ler transcrições e conversas
    inteligencia-do-grupo.md   ← quem pesa, culturas pelas palavras, dinâmica, foco e alerta de respeito
    transcricao-elaborada.md   ← transcrição limpa, ata, resumo e o Perfil de transcrição
    cenarios.md                ← simulação, ensaio e sementes de cenário
dist/                          ← pacotes prontos para baixar
scripts/build.py               ← gera os pacotes de dist/
```

## 🔄 Para quem quiser melhorar

O PONTE é um método vivo: foi testado só em simulação, e a próxima etapa é a experimentação em reuniões reais. Sugestões e relatos de uso são bem-vindos nas [Issues](../../issues). Depois de editar a skill, rode `python scripts/build.py` para atualizar os pacotes.

## 📄 Licença

[CC BY 4.0](LICENSE.md): pode usar, adaptar e compartilhar para qualquer fim, desde que cite a origem.
