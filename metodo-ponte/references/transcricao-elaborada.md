# Transcrição elaborada de reuniões

Transforma uma transcrição bruta (do Teams, Meet, Zoom, gravador do celular), um áudio já transcrito ou anotações soltas num registro limpo e útil, lido pela lente do PONTE. Cada pessoa configura do seu jeito pelo **Perfil de transcrição**.

## Índice

1. Quando oferecer
2. Como começar
3. Perfil de transcrição (as opções)
4. Modelos de saída
5. Regras de fidelidade
6. Como obter a transcrição

---

## 1. Quando oferecer

- A pessoa cola uma transcrição bruta, longa ou confusa.
- Ela pede "organiza essa reunião", "faz a ata", "limpa essa transcrição", "resume a reunião".
- Depois de uma Reflexão, para gerar um registro que vá para a outra margem no formato dela.

## 2. Como começar

Junte, numa mesma mensagem curta, o pedido de percepção (veja SKILL.md) e a configuração:

> Recebi a transcrição. Antes de elaborar, duas coisas rápidas:
> 1. **Sua percepção** da reunião, em áudio ou por escrito: como você saiu dela e o que achou mais importante.
> 2. **Como você quer a transcrição.** Se já tem um Perfil de transcrição, cole aqui. Se não, eu uso o padrão (**ata PONTE**, pessoas pelo papel, com marcações, sem marcas de tempo) ou você me diz o que mudar.

Se a pessoa disser "só quero a transcrição, sem análise", respeite: elabore no formato pedido e, no fim, ofereça a leitura PONTE em uma linha. Mesmo assim, pergunte a percepção, porque ela ajuda a destacar o que importa.

Quando a configuração for nova, devolva no fim o bloco do Perfil preenchido e sugira que a pessoa o guarde (veja "Guardar o perfil").

## 3. Perfil de transcrição

Opções, com o padrão em **negrito**:

| Opção | Escolhas | Para que serve |
|---|---|---|
| Formato | limpa · **ata PONTE** · resumo · completa | O tipo de registro (veja os modelos) |
| Pessoas | **papéis** · iniciais · nomes | Privacidade. Nomes só com o consentimento de todos |
| Marcações PONTE | **sim** · não | Destaca no texto desejo comum, acordos, lacunas, termos ambíguos e Correntes |
| Detalhe | enxuto · **padrão** · detalhado | Tamanho do registro |
| Marcas de tempo | manter · **remover** | Útil para voltar à gravação |
| Idioma | **o da reunião** · outro | Tradução do registro |
| Saída | **texto formatado** · texto simples para colar (e-mail, Teams, WhatsApp) · tabela | Onde o registro vai ser usado |
| Versão para a outra margem | **não** · sim, no formato: ___ | Dupla tradução: o mesmo registro no canal e no estilo da outra margem (por exemplo, mensagem curta de WhatsApp para o Comercial e e-mail formal para o PMO) |
| Foco | **reunião toda** · só decisões · só um tema: ___ | Recorte |

### Bloco para copiar

```
PERFIL DE TRANSCRIÇÃO PONTE
formato: ata PONTE
pessoas: papéis
marcações PONTE: sim
detalhe: padrão
marcas de tempo: remover
idioma: o da reunião
saída: texto formatado
versão para a outra margem: não
foco: reunião toda
```

### Guardar o perfil

Sugira o jeito que existir na IA da pessoa:

- **Claude:** colar o bloco nas instruções de um Projeto, ou pedir "lembre do meu perfil de transcrição PONTE" se a memória estiver ativa.
- **Claude Code:** colar o bloco no `CLAUDE.md` do usuário ou do projeto.
- **ChatGPT / Gemini:** colar o bloco nas instruções do GPT ou do Gem, ou nas instruções personalizadas.
- **Qualquer IA:** guardar o bloco num arquivo de notas e colá-lo junto com a transcrição.

Quando o bloco aparecer na conversa ou nas instruções, siga-o sem perguntar de novo. Se a pessoa mudar uma opção só para aquela vez, use a mudança sem alterar o perfil.

## 4. Modelos de saída

### Limpa

Fala a fala, sem vícios de linguagem ("é...", "tipo", repetições), mantendo o sentido e as hesitações que importam.

```
[Gestor de Tecnologia] Nosso objetivo é lançar o plano em março sem retrabalho. Faz sentido para vocês?
[Gestora Comercial] Faz. Só que o cliente cobra na hora, então às vezes a gente combina por telefone.
```

### Ata PONTE (padrão)

```
📝 ATA — <tema> · <data, se houver>
Participantes: <papéis, por margem>

Desejo comum: <frase, se foi dita; senão "não explicitado">

Principais pontos
- <ponto> — <quem trouxe>

Decisões e acordos
- <acordo> · dono: <papel> · prazo: <data> · confirmado pelos dois lados? <sim/não>

Termos com dois sentidos
- "<termo>": <como cada margem parece entender> → confirmar

Lacunas (o que ficou sem dono, sem prazo ou sem resposta)
- <lacuna>

Próximos passos
- <passo> · <dono> · <prazo>
```

### Resumo

De 5 a 10 linhas: o desejo comum, as decisões, os próximos passos e um alerta, se houver.

### Completa

A transcrição limpa, depois a ata PONTE, depois a leitura PONTE (Correntes afetadas com trechos, 6 Sinais, 1 ajuste). Siga `leitura-de-transcricao.md` para a leitura.

### Marcações PONTE (quando ativas)

Inseridas no texto, entre colchetes, sem mudar a fala:

- `[DESEJO COMUM]` quando alguém formula o objetivo compartilhado
- `[ACORDO]` acordo construído · `[ACORDO?]` acordo não confirmado pelos dois lados
- `[TERMO AMBÍGUO: sexta]` termo que pode ter dois sentidos
- `[LACUNA]` pergunta sem resposta, decisão sem dono ou sem prazo
- `[CORRENTE: Ritmo]` trecho em que uma Corrente gerou ruído
- `[TENSÃO: Atrito]` momento de tensão, com o nível

### Versão para a outra margem

Reescreva o mesmo conteúdo (decisões, acordos, próximos passos) no canal e no estilo da outra margem, sem mudar nenhum compromisso. Mostre as duas versões lado a lado para a pessoa revisar antes de enviar.

## 5. Regras de fidelidade

- **Nunca invente.** Se um trecho estiver inaudível ou confuso, marque `[inaudível]` ou `[?]` e pergunte.
- **Limpar não é reescrever.** Tire os vícios, mas preserve o que é sinal cultural: "acho que dá", "vou ver", "pode ser" e silêncios são pistas de Discordância e de Ritmo.
- **Cite literalmente os momentos-chave**: o desejo comum, os acordos e os pontos de tensão.
- **Separe fala de interpretação.** O que foi dito fica no texto; a sua leitura fica nas marcações e na análise.
- **Privacidade por padrão.** Pessoas pelo papel. Lembre que a transcrição deve ter o consentimento dos participantes.
- **Atribuição incerta.** Se não der para saber quem falou, escreva `[participante não identificado]` em vez de chutar.

## 6. Como obter a transcrição

Os nomes dos menus mudam com o tempo e dependem do plano contratado; oriente de forma geral:

- **Microsoft Teams:** durante a reunião, em "Mais ações", inicie gravação e transcrição. Depois, baixe a transcrição (.docx ou .vtt) no resumo da reunião.
- **Google Meet:** em "Atividades", ative a transcrição (disponível em algumas edições do Google Workspace). O documento vai para o Drive de quem organizou.
- **Zoom:** ative a transcrição de áudio na gravação em nuvem ou as legendas automáticas, e baixe o arquivo depois.
- **Reunião presencial:** use o gravador do celular, que em muitos aparelhos já transcreve, ou um app de transcrição. Avise e peça consentimento antes de gravar.
- **Áudio direto na IA:** se a sua IA aceita arquivos de áudio, envie o arquivo. Se não aceitar, use uma das opções acima.
- **Sem gravação:** anotações feitas durante ou logo depois da reunião também servem. Diga que são anotações, para a leitura considerar os limites.
