# 🏆 Oscar — Exercícios MongoDB

> Gerado automaticamente em 28/05/2026 00:25

---


## Nível 1 — Primeiros Passos

### 1.1 — Quantos registros existem na coleção de indicados ao Oscar?

**Comando MongoDB**

```js
db.indicados.countDocuments({})
```

**Resultado**

`10793`

---

### 1.2 — Quais são as diferentes categorias de premiação que existem no banco de dados?

**Comando MongoDB**

```js
db.indicados.distinct("categoria")
```

**Resultado**

- `ACTOR`
- `ACTOR IN A LEADING ROLE`
- `ACTOR IN A SUPPORTING ROLE`
- `ACTRESS`
- `ACTRESS IN A LEADING ROLE`
- `ACTRESS IN A SUPPORTING ROLE`
- `ANIMATED FEATURE FILM`
- `ANIMATED SHORT FILM`
- `ART DIRECTION`
- `ART DIRECTION (Black-and-White)`
- `ART DIRECTION (Color)`
- `ASSISTANT DIRECTOR`
- `AWARD OF COMMENDATION`
- `BEST INTERNATIONAL FEATURE FILM`
- `BEST MOTION PICTURE`
- `BEST PICTURE`
- `CASTING`
- `CINEMATOGRAPHY`
- `CINEMATOGRAPHY (Black-and-White)`
- `CINEMATOGRAPHY (Color)`
- _... e mais 95 itens_

---

### 1.3 — Qual foi o primeiro ano de cerimônia do Oscar registrado na base?

**Comando MongoDB**

```js
db.indicados.find({ano_cerimonia: {$ne: null}}).sort({ano_cerimonia: 1}).limit(1)
```

**Resultado**

`1928`

---

### 1.4 — Qual foi o último ano de cerimônia registrado na base?

**Comando MongoDB**

```js
db.indicados.find({ano_cerimonia: {$ne: null}}).sort({ano_cerimonia: -1}).limit(1)
```

**Resultado**

`2026`

---

### 1.5 — Quantas cerimônias do Oscar estão registradas no total?

**Comando MongoDB**

```js
db.indicados.distinct("ano_cerimonia").length
```

**Resultado**

`98`

---


## Nível 2 — Explorando Categorias

### 2.1 — Quantas indicações existem para cada categoria? Ordene da mais frequente para a menos frequente.

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: "$categoria", total: {$sum: 1}}}, {$sort: {total: -1}}])
```

**Resultado**

| _id | total |
|---|---|
| DIRECTING | 479 |
| FILM EDITING | 460 |
| ACTOR IN A SUPPORTING ROLE | 445 |
| ACTRESS IN A SUPPORTING ROLE | 445 |
| BEST PICTURE | 394 |
| DOCUMENTARY (Short Subject) | 378 |
| CINEMATOGRAPHY | 348 |
| DOCUMENTARY (Feature) | 345 |
| FOREIGN LANGUAGE FILM | 315 |
| ART DIRECTION | 307 |
| COSTUME DESIGN | 305 |
| MUSIC (Original Score) | 270 |
| SOUND | 255 |
| ACTOR IN A LEADING ROLE | 245 |
| ACTRESS IN A LEADING ROLE | 245 |
| ACTRESS | 236 |
| MUSIC (Original Song) | 235 |
| ACTOR | 232 |
| SHORT FILM (Live Action) | 226 |
| SHORT FILM (Animated) | 215 |

_... e mais 95 registros_

---

### 2.2 — Qual categoria teve mais indicações ao longo da história do Oscar?

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: "$categoria", total: {$sum: 1}}}, {$sort: {total: -1}}, {$limit: 1}])
```

**Resultado**

| Campo | Valor |
|---|---|
| `_id` | `DIRECTING` |
| `total` | `479` |

---

### 2.3 — Qual categoria teve menos indicações ao longo da história?

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: "$categoria", total: {$sum: 1}}}, {$sort: {total: 1}}, {$limit: 1}])
```

**Resultado**

| Campo | Valor |
|---|---|
| `_id` | `WRITING (Title Writing)` |
| `total` | `1` |

---

### 2.4 — A partir de que ano a categoria "ACTRESS" deixou de existir?

**Comando MongoDB**

```js
db.indicados.find({categoria: "ACTRESS"}).sort({ano_cerimonia: -1}).limit(1)
```

**Resultado**

`1976`

---

### 2.5 — Quais categorias existiam na primeira cerimônia (1928) e não existem mais hoje?

**Comando MongoDB**

```js
db.indicados.distinct("categoria", {ano_cerimonia: 1928})
```

**Resultado**

- `WRITING (Title Writing)`
- `DIRECTING (Comedy Picture)`
- `ENGINEERING EFFECTS`
- `WRITING (Original Story)`
- `ACTOR`
- `DIRECTING (Dramatic Picture)`
- `WRITING (Adaptation)`
- `OUTSTANDING PICTURE`
- `ACTRESS`
- `UNIQUE AND ARTISTIC PICTURE`
- `ART DIRECTION`

---

### 2.6 — Liste todas as categorias que contêm a palavra "DIRECTING" no nome.

**Comando MongoDB**

```js
db.indicados.distinct("categoria", {categoria: {$regex: "DIRECTING"}})
```

**Resultado**

- `DIRECTING`
- `DIRECTING (Comedy Picture)`
- `DIRECTING (Dramatic Picture)`

---


## Nível 3 — Atores e Atrizes Famosos

### 3.1 — Quantas vezes Natalie Portman foi indicada ao Oscar?

**Comando MongoDB**

```js
db.indicados.countDocuments({nome_do_indicado: "Natalie Portman"})
```

**Resultado**

`3`

---

### 3.2 — Quantos Oscars Natalie Portman ganhou?

**Comando MongoDB**

```js
db.indicados.countDocuments({nome_do_indicado: "Natalie Portman", vencedor: true})
```

**Resultado**

`1`

---

### 3.3 — Em quais anos e por quais filmes Natalie Portman foi indicada?

**Comando MongoDB**

```js
db.indicados.find({nome_do_indicado: "Natalie Portman"}, {ano_cerimonia: 1, nome_do_filme: 1})
```

**Resultado**

| ano_cerimonia | nome_do_filme |
|---|---|
| 2005 | Closer |
| 2011 | Black Swan |
| 2017 | Jackie |

---

### 3.4 — Liste todas as indicações de Natalie Portman mostrando: ano, categoria, filme e se venceu.

**Comando MongoDB**

```js
db.indicados.find({nome_do_indicado: "Natalie Portman"}, {ano_cerimonia: 1, categoria: 1, nome_do_filme: 1, vencedor: 1})
```

**Resultado**

| ano_cerimonia | categoria | nome_do_filme | vencedor |
|---|---|---|---|
| 2005 | ACTRESS IN A SUPPORTING ROLE | Closer | False |
| 2011 | ACTRESS IN A LEADING ROLE | Black Swan | True |
| 2017 | ACTRESS IN A LEADING ROLE | Jackie | False |

---

### 3.5 — Quantas vezes Viola Davis foi indicada ao Oscar?

**Comando MongoDB**

```js
db.indicados.countDocuments({nome_do_indicado: "Viola Davis"})
```

**Resultado**

`4`

---

### 3.6 — Quantos Oscars Viola Davis ganhou?

**Comando MongoDB**

```js
db.indicados.countDocuments({nome_do_indicado: "Viola Davis", vencedor: true})
```

**Resultado**

`1`

---

### 3.7 — Por quais filmes Viola Davis foi indicada?

**Comando MongoDB**

```js
db.indicados.distinct("nome_do_filme", {nome_do_indicado: "Viola Davis"})
```

**Resultado**

- `Doubt`
- `Fences`
- `Ma Rainey's Black Bottom`
- `The Help`

---

### 3.8 — Amy Adams já ganhou algum Oscar?

**Comando MongoDB**

```js
db.indicados.countDocuments({nome_do_indicado: "Amy Adams", vencedor: true})
```

**Resultado**

`Não`

---

### 3.9 — Quantas vezes Amy Adams foi indicada sem ganhar?

**Comando MongoDB**

```js
db.indicados.countDocuments({nome_do_indicado: "Amy Adams", vencedor: false})
```

**Resultado**

`6`

---

### 3.10 — Denzel Washington já ganhou algum Oscar?

**Comando MongoDB**

```js
db.indicados.countDocuments({nome_do_indicado: "Denzel Washington", vencedor: true})
```

**Resultado**

`Sim`

---

### 3.11 — Quantas vezes Denzel Washington foi indicado ao Oscar?

**Comando MongoDB**

```js
db.indicados.countDocuments({nome_do_indicado: "Denzel Washington"})
```

**Resultado**

`9`

---

### 3.12 — Liste todos os Oscars que Denzel Washington ganhou (ano, categoria, filme).

**Comando MongoDB**

```js
db.indicados.find({nome_do_indicado: "Denzel Washington", vencedor: true}, {ano_cerimonia: 1, categoria: 1, nome_do_filme: 1})
```

**Resultado**

| ano_cerimonia | categoria | nome_do_filme |
|---|---|---|
| 1990 | ACTOR IN A SUPPORTING ROLE | Glory |
| 2002 | ACTOR IN A LEADING ROLE | Training Day |

---


## Nível 4 — Vencedores Históricos

### 4.1 — Quem ganhou o primeiro Oscar para Melhor Atriz (ACTRESS)? Em que ano e por qual filme?

**Comando MongoDB**

```js
db.indicados.find({categoria: "ACTRESS", vencedor: true}).sort({ano_cerimonia: 1}).limit(1)
```

**Resultado**

| Campo | Valor |
|---|---|
| `nome` | `Janet Gaynor` |
| `ano` | `1928` |
| `filme` | `7th Heaven` |

---

### 4.2 — Quem ganhou o primeiro Oscar para Melhor Ator (ACTOR)? Em que ano e por qual filme?

**Comando MongoDB**

```js
db.indicados.find({categoria: "ACTOR", vencedor: true}).sort({ano_cerimonia: 1}).limit(1)
```

**Resultado**

| Campo | Valor |
|---|---|
| `nome` | `Emil Jannings` |
| `ano` | `1928` |
| `filme` | `The Last Command` |

---

### 4.3 — Quantos vencedores existem ao todo na base de dados?

**Comando MongoDB**

```js
db.indicados.countDocuments({vencedor: true})
```

**Resultado**

`2219`

---

### 4.4 — Liste todos os filmes que ganharam o Oscar de Melhor Filme.

**Comando MongoDB**

```js
db.indicados.distinct("nome_do_filme", {categoria: {$in: ["OUTSTANDING PICTURE", "BEST PICTURE"]}, vencedor: true})
```

**Resultado**

- `12 Years a Slave`
- `A Beautiful Mind`
- `A Man for All Seasons`
- `Amadeus`
- `American Beauty`
- `Annie Hall`
- `Anora`
- `Argo`
- `Birdman or (The Unexpected Virtue of Ignorance)`
- `Braveheart`
- `CODA`
- `Chariots of Fire`
- `Chicago`
- `Crash`
- `Dances With Wolves`
- `Driving Miss Daisy`
- `Everything Everywhere All at Once`
- `Forrest Gump`
- `Gandhi`
- `Gladiator`
- _... e mais 46 itens_

---

### 4.5 — Quantos filmes diferentes já ganharam o Oscar?

**Comando MongoDB**

```js
db.indicados.distinct("nome_do_filme", {vencedor: true}).length
```

**Resultado**

`1353`

---


## Nível 5 — Análise de Indicações

### 5.1 — Quais atores/atrizes foram indicados mais de uma vez?

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: "$nome_do_indicado", indicacoes: {$sum: 1}}}, {$match: {indicacoes: {$gt: 1}}}, {$sort: {indicacoes: -1}}])
```

**Resultado**

| _id | indicacoes |
|---|---|
| Metro-Goldwyn-Mayer | 64 |
| Walt Disney, Producer | 59 |
| John Williams | 46 |
| Warner Bros. | 43 |
| France | 38 |
| Alfred Newman | 34 |
| Italy | 29 |
| Paramount | 25 |
| Edith Head | 22 |
| Spain | 22 |
| Gordon Hollingshead, Producer | 22 |
| RKO Radio | 22 |
| Meryl Streep | 21 |
| 20th Century-Fox | 20 |
| Victor Young | 19 |
| Woody Allen | 18 |
| Leon Shamroy | 17 |
| Pete Smith, Producer | 16 |
| Sweden | 16 |
| Max Steiner | 16 |

_... e mais 1410 registros_

---

### 5.2 — Qual ator ou atriz tem o maior número de indicações na história do Oscar?

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: "$nome_do_indicado", indicacoes: {$sum: 1}}}, {$sort: {indicacoes: -1}}, {$limit: 1}])
```

**Resultado**

| Campo | Valor |
|---|---|
| `_id` | `Metro-Goldwyn-Mayer` |
| `indicacoes` | `64` |

---

### 5.3 — Quais atores foram indicados mais de 3 vezes, mas nunca ganharam?

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: "$nome_do_indicado", indicacoes: {$sum: 1}, vitorias: {$sum: {$cond: ["$vencedor", 1, 0]}}}}, {$match: {indicacoes: {$gt: 3}, vitorias: 0}}])
```

**Resultado**

| _id | indicacoes | vitorias |
|---|---|---|
| Thomas Newman | 14 | 0 |
| Alex North | 14 | 0 |
| George Folsey | 12 | 0 |
| Music and Lyric by Diane Warren | 11 | 0 |
| Israel | 10 | 0 |
| Walter Lantz, Producer | 10 | 0 |
| Paramount Studio Sound Department, Loren L. Ryder, Sound Director | 10 | 0 |
| Randy Newman | 9 | 0 |
| Ingmar Bergman | 8 | 0 |
| Belgium | 8 | 0 |
| Peter O'Toole | 8 | 0 |
| Glenn Close | 8 | 0 |
| Robert Emmett Dolan | 8 | 0 |
| Richard Burton | 7 | 0 |
| James Newton Howard | 7 | 0 |
| Bill Thomas | 7 | 0 |
| George Pal, Producer | 7 | 0 |
| Amy Adams | 6 | 0 |
| Samuel Goldwyn Studio Sound Department, Thomas T. Moulton, Sound Director | 6 | 0 |
| Ernest Haller | 6 | 0 |

_... e mais 104 registros_

---

### 5.4 — Encontre todos os artistas que foram indicados em categorias diferentes.

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: "$nome_do_indicado", categorias: {$addToSet: "$categoria"}}}, {$match: {$expr: {$gt: [{$size: "$categorias"}, 1]}}}])
```

**Resultado**

| _id | categorias |
|---|---|
| 20th Century-Fox | ['SHORT SUBJECT (One-reel)', 'OUTSTANDING PRODUCTION', 'SHORT SUBJECT (Cartoon)', 'OUTSTANDING MOTION PICTURE', 'BEST MOTION PICTURE'] |
| 20th Century-Fox Studio Sound Department, Carl Faulkner, Sound Director | ['SOUND RECORDING', 'SOUND'] |
| Aaron Copland | ['MUSIC (Music Score of a Dramatic or Comedy Picture)', 'MUSIC (Original Score)', 'MUSIC (Scoring)'] |
| Adam Driver | ['ACTOR IN A LEADING ROLE', 'ACTOR IN A SUPPORTING ROLE'] |
| Adaptation Score by Leonard Rosenman | ['MUSIC (Scoring: Original Song Score and Adaptation -or- Scoring: Adaptation)', 'MUSIC (Original Song Score and Its Adaptation or Adaptation Score)'] |
| Adaptation Score by Ralph Burns | ['MUSIC (Scoring: Adaptation and Original Song Score)', 'MUSIC (Original Song Score and Its Adaptation -or- Adaptation Score)'] |
| Al Pacino | ['ACTOR IN A LEADING ROLE', 'ACTOR', 'ACTOR IN A SUPPORTING ROLE'] |
| Alan Arkin | ['ACTOR', 'ACTOR IN A SUPPORTING ROLE'] |
| Alan J. Pakula | ['WRITING (Screenplay Based on Material from Another Medium)', 'DIRECTING'] |
| Alan Jay Lerner | ['WRITING (Story and Screenplay)', 'WRITING (Screenplay--based on material from another medium)'] |
| Alan Robert Murray, Bub Asman | ['SOUND EDITING', 'SOUND EFFECTS EDITING'] |
| Albert Finney | ['ACTOR IN A LEADING ROLE', 'ACTOR IN A SUPPORTING ROLE', 'ACTOR'] |
| Alec Guinness | ['ACTOR', 'ACTOR IN A SUPPORTING ROLE', 'WRITING (Screenplay--based on material from another medium)'] |
| Alex North | ['MUSIC (Original Dramatic Score)', 'MUSIC (Original Score)', 'MUSIC (Original Score--for a motion picture [not a musical])', 'MUSIC (Music Score--substantially original)', 'MUSIC (Music Score of a Dramatic or Comedy Picture)', 'MUSIC (Original Music Score)'] |
| Alexandre Desplat | ['MUSIC (Original Score)', 'MUSIC (ORIGINAL SCORE)'] |
| Alfonso Cuarón | ['CINEMATOGRAPHY', 'DIRECTING'] |
| Alfred Newman | ['MUSIC (Scoring)', 'MUSIC (Scoring of a Musical Picture)', 'MUSIC (Music Score of a Dramatic or Comedy Picture)', 'MUSIC (Music Score of a Dramatic Picture)', 'MUSIC (Music Score--substantially original)', 'MUSIC (Original Score)'] |
| Alfred Newman, Ken Darby | ['MUSIC (Music Score--substantially original)', 'MUSIC (Scoring of a Musical Picture)', 'MUSIC (Scoring of Music--adaptation or treatment)'] |
| Alvin Sargent | ['WRITING (Screenplay Based on Material from Another Medium)', 'WRITING (Screenplay--based on material from another medium)'] |
| Amy Adams | ['ACTRESS IN A SUPPORTING ROLE', 'ACTRESS IN A LEADING ROLE'] |

_... e mais 593 registros_

---

### 5.5 — Quantos indicados têm exatamente 1 indicação na história?

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: "$nome_do_indicado", indicacoes: {$sum: 1}}}, {$match: {indicacoes: 1}}, {$count: "total"}])
```

**Resultado**

`5515`

---

### 5.6 — Qual o maior número de indicados em um único ano?

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: "$ano_cerimonia", total: {$sum: 1}}}, {$sort: {total: -1}}, {$limit: 1}])
```

**Resultado**

| Campo | Valor |
|---|---|
| `_id` | `1943` |
| `total` | `182` |

---


## Nível 6 — Análise de Filmes

### 6.1 — A série de filmes Toy Story ganhou Oscars em quais anos?

**Comando MongoDB**

```js
db.indicados.distinct("ano_cerimonia", {nome_do_filme: {$regex: "Toy Story", $options: "i"}, vencedor: true})
```

**Resultado**

- `2011`
- `2020`

---

### 6.2 — Quantas indicações a franquia Toy Story recebeu no total?

**Comando MongoDB**

```js
db.indicados.countDocuments({nome_do_filme: {$regex: "Toy Story", $options: "i"}})
```

**Resultado**

`11`

---

### 6.3 — Em quais categorias os filmes Toy Story foram indicados?

**Comando MongoDB**

```js
db.indicados.distinct("categoria", {nome_do_filme: {$regex: "Toy Story", $options: "i"}})
```

**Resultado**

- `ANIMATED FEATURE FILM`
- `BEST PICTURE`
- `MUSIC (Original Musical or Comedy Score)`
- `MUSIC (Original Song)`
- `SOUND EDITING`
- `WRITING (Adapted Screenplay)`
- `WRITING (Screenplay Written Directly for the Screen)`

---

### 6.4 — Em qual edição do Oscar o filme "Crash" concorreu?

**Comando MongoDB**

```js
db.indicados.distinct("ano_cerimonia", {nome_do_filme: "Crash"})
```

**Resultado**

- `2006`

---

### 6.5 — Quantas indicações o filme "Crash" recebeu?

**Comando MongoDB**

```js
db.indicados.countDocuments({nome_do_filme: "Crash"})
```

**Resultado**

`6`

---

### 6.6 — "Crash" ganhou o Oscar de Melhor Filme?

**Comando MongoDB**

```js
db.indicados.countDocuments({nome_do_filme: "Crash", categoria: {$in: ["OUTSTANDING PICTURE", "BEST PICTURE"]}, vencedor: true})
```

**Resultado**

`Sim`

---

### 6.7 — O filme "Central do Brasil" aparece no banco de dados?

**Comando MongoDB**

```js
db.indicados.findOne({nome_do_filme: {$regex: "Central do Brasil", $options: "i"}})
```

**Resultado**

`Não`

---

### 6.8 — Quantas indicações "Central do Brasil" recebeu?

**Comando MongoDB**

```js
db.indicados.countDocuments({nome_do_filme: {$regex: "Central do Brasil", $options: "i"}})
```

**Resultado**

`0`

---


## Nível 7 — Operações de Atualização

### 7.1 — No campo "vencedor", altere todos os valores "true" (string) para true (booleano) e "false" (string) para false (booleano).

**Comando MongoDB**

```js
db.indicados.updateMany({vencedor: "true"}, {$set: {vencedor: true}})
db.indicados.updateMany({vencedor: "false"}, {$set: {vencedor: false}})
```

**Resultado**

`0 documentos atualizados`

---

### 7.2 — Inclua no banco 3 filmes que nunca foram nomeados ao Oscar, mas que você acha que merecem.

**Comando MongoDB**

```js
db.indicados.insertMany([...])
```

**Resultado**

`3 filmes inseridos: The Shawshank Redemption, Mulholland Drive, Eternal Sunshine of the Spotless Mind`

---

### 7.3 — Adicione uma nova categoria chamada "BEST INTERNATIONAL FEATURE FILM" com alguns vencedores recentes (2020-2024).

**Comando MongoDB**

```js
db.indicados.insertMany([...])
```

**Resultado**

`5 vencedores inseridos na categoria BEST INTERNATIONAL FEATURE FILM (2020-2024)`

---

### 7.4 — Corrija possíveis erros de digitação nos nomes dos filmes (espaços extras, caracteres especiais).

**Comando MongoDB**

```js
db.indicados.updateMany(
  {nome_do_filme: {$regex: ";$"}},
  [{$set: {nome_do_filme: {$rtrim: {input: "$nome_do_filme", chars: ";"}}}}]
)
```

**Resultado**

`0 documentos corrigidos`

---

### 7.5 — Remova todos os registros com valor NULL no campo nome_do_filme.

**Comando MongoDB**

```js
db.indicados.deleteMany({nome_do_filme: null})
```

**Resultado**

`319 documentos removidos`

---


## Nível 8 — Análise Temporal

### 8.1 — Quantas indicações aconteceram por década?

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: {$multiply: [{$floor: {$divide: ["$ano_cerimonia", 10]}}, 10]}, total: {$sum: 1}}}, {$sort: {_id: 1}}])
```

**Resultado**

| _id | total |
|---|---|
| 1920.0 | 67 |
| 1930.0 | 662 |
| 1940.0 | 1459 |
| 1950.0 | 1146 |
| 1960.0 | 1167 |
| 1970.0 | 1026 |
| 1980.0 | 1036 |
| 1990.0 | 1091 |
| 2000.0 | 1105 |
| 2010.0 | 1211 |
| 2020.0 | 823 |

---

### 8.2 — Em qual década houve o maior número de indicações?

**Comando MongoDB**

```js
db.indicados.aggregate([..., {$sort: {total: -1}}, {$limit: 1}])
```

**Resultado**

| Campo | Valor |
|---|---|
| `_id` | `1940.0` |
| `total` | `1459` |

---

### 8.3 — Como o número de categorias evoluiu ao longo dos anos?

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: decada, categorias: {$addToSet: "$categoria"}}}, {$project: {total_categorias: {$size: "$categorias"}}}])
```

**Resultado**

| _id | decada | total_categorias |
|---|---|---|
| 1920.0 | 1920.0 | 14 |
| 1930.0 | 1930.0 | 25 |
| 1940.0 | 1940.0 | 35 |
| 1950.0 | 1950.0 | 37 |
| 1960.0 | 1960.0 | 37 |
| 1970.0 | 1970.0 | 46 |
| 1980.0 | 1980.0 | 30 |
| 1990.0 | 1990.0 | 27 |
| 2000.0 | 2000.0 | 28 |
| 2010.0 | 2010.0 | 26 |
| 2020.0 | 2020.0 | 36 |

---

### 8.4 — Qual foi o ano com o maior número de indicações registradas?

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: "$ano_cerimonia", total: {$sum: 1}}}, {$sort: {total: -1}}, {$limit: 1}])
```

**Resultado**

| Campo | Valor |
|---|---|
| `_id` | `1943` |
| `total` | `182` |

---

### 8.5 — Calcule a taxa de crescimento de indicações comparando a primeira década com a última.

**Comando MongoDB**

```js
duas aggregations separadas para primeira e última década
```

**Resultado**

| Campo | Valor |
|---|---|
| `primeira_decada` | | Campo | Valor |
|---|---|
| `_id` | `1920.0` |
| `total` | `67` | |
| `ultima_decada` | | Campo | Valor |
|---|---|
| `_id` | `2020.0` |
| `total` | `823` | |
| `crescimento_percentual` | `1128.36%` |

---


## Nível 9 — Questões Históricas e Sociais

### 9.1 — Sidney Poitier foi o primeiro ator negro a ser indicado ao Oscar. Em que ano ele foi indicado? Por qual filme?

**Comando MongoDB**

```js
db.indicados.find({nome_do_indicado: "Sidney Poitier"}).sort({ano_cerimonia: 1}).limit(1)
```

**Resultado**

| Campo | Valor |
|---|---|
| `ano` | `1959` |
| `filme` | `The Defiant Ones` |

---

### 9.2 — Sidney Poitier ganhou o Oscar nessa indicação?

**Comando MongoDB**

```js
db.indicados.find({nome_do_indicado: "Sidney Poitier"}).sort({ano_cerimonia: 1}).limit(1)
```

**Resultado**

`Não`

---

### 9.3 — Quantos atores/atrizes negros foram indicados na categoria ACTOR ou ACTRESS antes de 1970?

**Comando MongoDB**

```js
db.indicados.countDocuments({categoria: {$in: ["ACTOR", "ACTRESS"]}, ano_cerimonia: {$lt: 1970}})
```

**Resultado**

`398`

---

### 9.4 — Liste todos os filmes dirigidos por mulheres que ganharam algum Oscar.

**Comando MongoDB**

```js
db.indicados.distinct("nome_do_filme", {categoria: {$regex: "DIRECTING"}, vencedor: true})
```

**Resultado**

- `7th Heaven`
- `A Beautiful Mind`
- `A Letter to Three Wives`
- `A Man for All Seasons`
- `A Place in the Sun`
- `All Quiet on the Western Front`
- `All about Eve`
- `Amadeus`
- `American Beauty`
- `Annie Hall`
- `Anora`
- `Bad Girl`
- `Ben-Hur`
- `Birdman or (The Unexpected Virtue of Ignorance)`
- `Born on the Fourth of July`
- `Braveheart`
- `Brokeback Mountain`
- `Cabaret`
- `Casablanca`
- `Cavalcade`
- _... e mais 79 itens_

---

### 9.5 — Denzel Washington e Jamie Foxx já concorreram ao Oscar no mesmo ano?

**Comando MongoDB**

```js
db.indicados.distinct("ano_cerimonia", {nome_do_indicado: "Denzel Washington"})
```

**Resultado**

`Não`

---

### 9.6 — Se sim, em qual ano e quem ganhou?

**Resultado**

`Eles não concorreram no mesmo ano`

---

### 9.7 — Encontre casos onde o mesmo filme ganhou Oscar em múltiplas categorias na mesma cerimônia.

**Comando MongoDB**

```js
db.indicados.aggregate([{$match: {vencedor: true}}, {$group: {_id: {filme: "$nome_do_filme", ano: "$ano_cerimonia"}, categorias_vencidas: {$sum: 1}}}, {$match: {categorias_vencidas: {$gt: 1}}}])
```

**Resultado**

| _id | categorias_vencidas |
|---|---|
| {'filme': 'The Lord of the Rings: The Return of the King', 'ano': 2004} | 11 |
| {'filme': 'Ben-Hur', 'ano': 1960} | 11 |
| {'filme': 'Titanic', 'ano': 1998} | 11 |
| {'filme': 'West Side Story', 'ano': 1962} | 10 |
| {'filme': 'The English Patient', 'ano': 1997} | 9 |
| {'filme': 'Gigi', 'ano': 1959} | 9 |
| {'filme': 'The Last Emperor', 'ano': 1988} | 9 |
| {'filme': 'From Here to Eternity', 'ano': 1954} | 8 |
| {'filme': 'Slumdog Millionaire', 'ano': 2009} | 8 |
| {'filme': 'Cabaret', 'ano': 1973} | 8 |
| {'filme': 'On the Waterfront', 'ano': 1955} | 8 |
| {'filme': 'Amadeus', 'ano': 1985} | 8 |
| {'filme': 'Gandhi', 'ano': 1983} | 8 |
| {'filme': 'My Fair Lady', 'ano': 1965} | 8 |
| {'filme': 'Gone with the Wind', 'ano': 1940} | 8 |
| {'filme': 'The Sting', 'ano': 1974} | 7 |
| {'filme': 'Everything Everywhere All at Once', 'ano': 2023} | 7 |
| {'filme': 'Shakespeare in Love', 'ano': 1999} | 7 |
| {'filme': 'Gravity', 'ano': 2014} | 7 |
| {'filme': 'Patton', 'ano': 1971} | 7 |

_... e mais 345 registros_

---


## Nível 10 — Análise Avançada

### 10.1 — Quais filmes ganharam o Oscar de Melhor Filme e Melhor Diretor na mesma cerimônia?

**Comando MongoDB**

```js
db.indicados.aggregate([{$match: {vencedor: true, categoria: {$in: [...]}}}, {$lookup: {...}}, ...])
```

**Resultado**

| ano_cerimonia | nome_do_filme |
|---|---|
| 1963 | Lawrence of Arabia |
| 1964 | Tom Jones |
| 1965 | My Fair Lady |
| 1966 | The Sound of Music |
| 1967 | A Man for All Seasons |
| 1969 | Oliver! |
| 1970 | Midnight Cowboy |
| 1971 | Patton |
| 1972 | The French Connection |
| 1974 | The Sting |
| 1975 | The Godfather Part II |
| 1976 | One Flew over the Cuckoo's Nest |
| 1977 | Rocky |
| 1978 | Annie Hall |
| 1979 | The Deer Hunter |
| 1980 | Kramer vs. Kramer |
| 1981 | Ordinary People |
| 1983 | Gandhi |
| 1984 | Terms of Endearment |
| 1985 | Amadeus |

_... e mais 30 registros_

---

### 10.2 — Qual filme recebeu o maior número de indicações em uma única cerimônia?

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: {filme: "$nome_do_filme", ano: "$ano_cerimonia"}, total: {$sum: 1}}}, {$sort: {total: -1}}, {$limit: 1}])
```

**Resultado**

| Campo | Valor |
|---|---|
| `_id` | | Campo | Valor |
|---|---|
| `filme` | `Titanic` |
| `ano` | `1998` | |
| `total` | `14` |

---

### 10.3 — Qual filme teve a maior taxa de conversão (% de indicações que viraram vitórias)?

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {...}}, {$project: {taxa: {$multiply: [{$divide: ['$vitorias', '$indicacoes']}, 100]}}}, {$sort: {taxa: -1}}])
```

**Resultado**

| _id | indicacoes | vitorias | filme | taxa |
|---|---|---|---|---|
| God of Love | 1 | 1 | God of Love | 100.0 |
| This Tiny World | 1 | 1 | This Tiny World | 100.0 |
| The Phone Call | 1 | 1 | The Phone Call | 100.0 |
| Speedy Gonzales | 1 | 1 | Speedy Gonzales | 100.0 |
| Paperman | 1 | 1 | Paperman | 100.0 |
| the accountant | 1 | 1 | the accountant | 100.0 |
| Interviews with My Lai Veterans | 1 | 1 | Interviews with My Lai Veterans | 100.0 |
| The Queen of Basketball | 1 | 1 | The Queen of Basketball | 100.0 |
| The Golden Fish | 1 | 1 | The Golden Fish | 100.0 |
| Captain Carey, U.S.A. | 1 | 1 | Captain Carey, U.S.A. | 100.0 |

---

### 10.4 — Encontre atores que foram indicados em anos consecutivos.

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: '$nome_do_indicado', anos: {$addToSet: '$ano_cerimonia'}}}])
```

**Resultado**

| nome | anos |
|---|---|
| 20th Century | [1935, 1936] |
| 20th Century-Fox | [1938, 1939, 1941, 1942, 1943, 1944, 1945, 1947, 1948, 1949, 1950, 1951] |
| 20th Century-Fox Studio | [1955, 1956] |
| 20th Century-Fox Studio Sound Department | [1968, 1969] |
| 20th Century-Fox Studio Sound Department, Carl Faulkner, Sound Director | [1957, 1959, 1960] |
| 20th Century-Fox Studio Sound Department, E. H. Hansen, Sound Director | [1936, 1937, 1938, 1940, 1941, 1942, 1943, 1944, 1945] |
| 20th Century-Fox Studio Sound Department, James P. Corcoran, Sound Director | [1966, 1967] |
| 20th Century-Fox Studio Sound Department, Thomas T. Moulton, Sound Director | [1946, 1949, 1950, 1951, 1953] |
| Aaron Copland | [1940, 1941, 1944, 1950] |
| Adam Driver | [2019, 2020] |
| Adaptation Score by Leonard Rosenman | [1976, 1977] |
| Al Pacino | [1973, 1974, 1975, 1976, 1980, 1991, 1993, 2020] |
| Alan Menken | [1990, 1992, 1993] |
| Albert Finney | [1964, 1975, 1984, 1985, 2001] |
| Albert Wolsky | [1980, 1983, 1986, 1992, 1993, 2008, 2009] |
| Alec Guinness | [1953, 1958, 1959, 1978, 1989] |
| Alejandro G. Iñárritu | [2015, 2016] |
| Alex North | [1952, 1953, 1956, 1957, 1961, 1964, 1966, 1967, 1969, 1975, 1976, 1982, 1985] |
| Alexander Toluboff | [1938, 1939, 1940] |
| Alexandre Desplat | [2007, 2009, 2010, 2011, 2013, 2014, 2015, 2018, 2019, 2020, 2026] |

_... e mais 486 registros_

---

### 10.5 — Qual a média de indicações por cerimônia ao longo da história?

**Comando MongoDB**

```js
db.indicados.countDocuments({}) / db.indicados.distinct('ano_cerimonia').length
```

**Resultado**

`110.13`

---

### 10.6 — Identifique "surpresas" - indicados em categorias principais cujo filme só teve uma indicação.

**Comando MongoDB**

```js
db.indicados.aggregate([{$match: {categoria: {$in: ['ACTOR', 'ACTRESS', 'BEST PICTURE']}}}, {$group: {_id: '$nome_do_filme', total: {$sum: 1}}}, {$match: {total: 1}}])
```

**Resultado**

| _id | total_indicacoes_filme | indicados |
|---|---|---|
| 12 Years a Slave | 1 | [{'indicado': 'Brad Pitt, Dede Gardner, Jeremy Kleiner, Steve McQueen and Anthony Katagas, Producers', 'categoria': 'BEST PICTURE'}] |
| 127 Hours | 1 | [{'indicado': 'Christian Colson, Danny Boyle and John Smithson, Producers', 'categoria': 'BEST PICTURE'}] |
| 1917 | 1 | [{'indicado': 'Sam Mendes, Pippa Harris, Jayne-Ann Tenggren and Callum McDougall, Producers', 'categoria': 'BEST PICTURE'}] |
| 7th Heaven | 1 | [{'indicado': 'Janet Gaynor', 'categoria': 'ACTRESS'}] |
| A Beautiful Mind | 1 | [{'indicado': 'Brian Grazer and Ron Howard, Producers', 'categoria': 'BEST PICTURE'}] |
| A Clockwork Orange | 1 | [{'indicado': 'Stanley Kubrick, Producer', 'categoria': 'BEST PICTURE'}] |
| A Complete Unknown | 1 | [{'indicado': 'Fred Berger, James Mangold and Alex Heineman', 'categoria': 'BEST PICTURE'}] |
| A Double Life | 1 | [{'indicado': 'Ronald Colman', 'categoria': 'ACTOR'}] |
| A Few Good Men | 1 | [{'indicado': 'David Brown, Rob Reiner and Andrew Scheinman, Producers', 'categoria': 'BEST PICTURE'}] |
| A Hatful of Rain | 1 | [{'indicado': 'Anthony Franciosa', 'categoria': 'ACTOR'}] |
| A Man and a Woman | 1 | [{'indicado': 'Anouk Aimee', 'categoria': 'ACTRESS'}] |
| A Passage to India | 1 | [{'indicado': 'John Brabourne and Richard Goodwin, Producers', 'categoria': 'BEST PICTURE'}] |
| A Patch of Blue | 1 | [{'indicado': 'Elizabeth Hartman', 'categoria': 'ACTRESS'}] |
| A Room with a View | 1 | [{'indicado': 'Ismail Merchant, Producer', 'categoria': 'BEST PICTURE'}] |
| A Serious Man | 1 | [{'indicado': 'Joel Coen and Ethan Coen, Producers', 'categoria': 'BEST PICTURE'}] |
| A Ship Comes In | 1 | [{'indicado': 'Louise Dresser', 'categoria': 'ACTRESS'}] |
| A Soldier's Story | 1 | [{'indicado': 'Norman Jewison, Ronald L. Schwary and Patrick Palmer, Producers', 'categoria': 'BEST PICTURE'}] |
| A Song to Remember | 1 | [{'indicado': 'Cornel Wilde', 'categoria': 'ACTOR'}] |
| A Thousand Clowns | 1 | [{'indicado': 'Fred Coe, Producer', 'categoria': 'BEST PICTURE'}] |
| A Woman under the Influence | 1 | [{'indicado': 'Gena Rowlands', 'categoria': 'ACTRESS'}] |

_... e mais 625 registros_

---


## Nível 11 — Desafios Complexos

### 11.1 — Crie um ranking dos 10 filmes mais premiados da história.

**Comando MongoDB**

```js
db.indicados.aggregate([{$match: {vencedor: true}}, {$group: {_id: "$nome_do_filme", oscars: {$sum: 1}}}, {$sort: {oscars: -1}}, {$limit: 10}])
```

**Resultado**

| _id | oscars |
|---|---|
| Titanic | 12 |
| Ben-Hur | 11 |
| The Lord of the Rings: The Return of the King | 11 |
| West Side Story | 11 |
| The Last Emperor | 9 |
| Gigi | 9 |
| The English Patient | 9 |
| Gone with the Wind | 8 |
| Cabaret | 8 |
| Amadeus | 8 |

---

### 11.2 — Crie um ranking dos 10 artistas mais indicados da história, independente da categoria.

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: "$nome_do_indicado", indicacoes: {$sum: 1}}}, {$sort: {indicacoes: -1}}, {$limit: 10}])
```

**Resultado**

| _id | indicacoes |
|---|---|
| Metro-Goldwyn-Mayer | 64 |
| Walt Disney, Producer | 59 |
| John Williams | 46 |
| Warner Bros. | 43 |
| France | 38 |
| Alfred Newman | 34 |
| Italy | 29 |
| Paramount | 25 |
| RKO Radio | 22 |
| Gordon Hollingshead, Producer | 22 |

---

### 11.3 — Encontre "azarões" - artistas com mais de 5 indicações e 0 vitórias.

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: "$nome_do_indicado", indicacoes: {$sum: 1}, vitorias: {$sum: {$cond: ["$vencedor", 1, 0]}}}}, {$match: {indicacoes: {$gt: 5}, vitorias: 0}}])
```

**Resultado**

| _id | indicacoes | vitorias |
|---|---|---|
| Alex North | 14 | 0 |
| Thomas Newman | 14 | 0 |
| George Folsey | 12 | 0 |
| Music and Lyric by Diane Warren | 11 | 0 |
| Israel | 10 | 0 |
| Walter Lantz, Producer | 10 | 0 |
| Paramount Studio Sound Department, Loren L. Ryder, Sound Director | 10 | 0 |
| Randy Newman | 9 | 0 |
| Ingmar Bergman | 8 | 0 |
| Belgium | 8 | 0 |
| Robert Emmett Dolan | 8 | 0 |
| Glenn Close | 8 | 0 |
| Peter O'Toole | 8 | 0 |
| Bill Thomas | 7 | 0 |
| George Pal, Producer | 7 | 0 |
| James Newton Howard | 7 | 0 |
| Richard Burton | 7 | 0 |
| Deborah Kerr | 6 | 0 |
| Leon Schlesinger, Producer | 6 | 0 |
| Gerry Hambling | 6 | 0 |

_... e mais 17 registros_

---

### 11.4 — Qual categoria tem a maior concentração de vitórias (menos vencedores diferentes)?

**Comando MongoDB**

```js
db.indicados.aggregate([{$match: {vencedor: true}}, {$group: {_id: "$categoria", vencedores_unicos: {$addToSet: "$nome_do_indicado"}}}, {$project: {total: {$size: "$vencedores_unicos"}}}, {$sort: {total: 1}}])
```

**Resultado**

| _id | categoria | total_vencedores_unicos |
|---|---|---|
| ANIMATED SHORT FILM | ANIMATED SHORT FILM | 1 |
| WRITING (Screenplay--Adapted) | WRITING (Screenplay--Adapted) | 1 |
| WRITING (Screenplay--Original) | WRITING (Screenplay--Original) | 1 |
| MUSIC (Original Song Score or Adaptation Score) | MUSIC (Original Song Score or Adaptation Score) | 1 |
| WRITING (Story and Screenplay--based on material not previously published or produced) | WRITING (Story and Screenplay--based on material not previously published or produced) | 1 |

---

### 11.5 — Calcule a "competitividade" de cada categoria (média de indicados por cerimônia).

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: {categoria, ano}, indicados: {$sum: 1}}}, {$group: {_id: '$_id.categoria', media: {$avg: '$indicados'}}}])
```

**Resultado**

| _id | media_indicados |
|---|---|
| DOCUMENTARY | 25.0 |
| MUSIC (Music Score of a Dramatic Picture) | 20.0 |
| OUTSTANDING MOTION PICTURE | 10.0 |
| OUTSTANDING PRODUCTION | 9.272727272727273 |
| MUSIC (Scoring) | 8.0 |
| MUSIC (Music Score of a Dramatic or Comedy Picture) | 7.7894736842105265 |
| SOUND RECORDING | 7.1923076923076925 |
| DANCE DIRECTION | 7.0 |
| MUSIC (Scoring of a Musical Picture) | 6.35 |
| BEST PICTURE | 6.15625 |
| MUSIC (Song) | 5.972222222222222 |
| CINEMATOGRAPHY (Black-and-White) | 5.962962962962963 |
| ART DIRECTION (Black-and-White) | 5.52 |
| MUSIC (Original Score) | 5.510204081632653 |
| WRITING | 5.5 |
| ART DIRECTION | 5.203389830508475 |
| MUSIC (Original Dramatic Score) | 5.125 |
| MUSIC (ORIGINAL SCORE) | 5.0 |
| ACTOR IN A LEADING ROLE | 5.0 |
| ACTRESS IN A SUPPORTING ROLE | 5.0 |

_... e mais 95 registros_

---

### 11.6 — Encontre filmes que foram indicados em uma categoria em um ano e ganharam em outra categoria em outro ano.

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: '$nome_do_filme', anos: {$addToSet: '$ano_cerimonia'}, ...}}])
```

**Resultado**

| _id | anos | categorias_vencidas |
|---|---|---|
| Through a Glass Darkly | [1962, 1963] | [{'categoria': 'FOREIGN LANGUAGE FILM', 'ano': 1962}, None] |
| The Invisible Woman | [1942, 2014] | [None, None] |
| Marriage Italian Style | [1966, 1965] | [None, None] |
| The Emigrants | [1973, 1972] | [None, None, None, None, None] |
| Cyrano de Bergerac | [1991, 1951] | [{'categoria': 'ACTOR', 'ano': 1951}, None, None, {'categoria': 'COSTUME DESIGN', 'ano': 1991}, None, None] |
| Romeo and Juliet | [1937, 1969] | [None, None, None, None, {'categoria': 'CINEMATOGRAPHY', 'ano': 1969}, {'categoria': 'COSTUME DESIGN', 'ano': 1969}, None, None] |
| Goodbye, Mr. Chips | [1970, 1940] | [{'categoria': 'ACTOR', 'ano': 1940}, None, None, None, None, None, None, None, None] |
| Madame Bovary | [1992, 1950] | [None, None] |
| When Ladies Meet | [1942, 1933] | [None, None] |
| West Side Story | [2022, 1962] | [{'categoria': 'ACTOR IN A SUPPORTING ROLE', 'ano': 1962}, {'categoria': 'ACTRESS IN A SUPPORTING ROLE', 'ano': 1962}, {'categoria': 'ART DIRECTION (Color)', 'ano': 1962}, {'categoria': 'CINEMATOGRAPHY (Color)', 'ano': 1962}, {'categoria': 'COSTUME DESIGN (Color)', 'ano': 1962}, {'categoria': 'DIRECTING', 'ano': 1962}, {'categoria': 'FILM EDITING', 'ano': 1962}, {'categoria': 'MUSIC (Scoring of a Musical Picture)', 'ano': 1962}, {'categoria': 'BEST MOTION PICTURE', 'ano': 1962}, {'categoria': 'SOUND', 'ano': 1962}, None, {'categoria': 'ACTRESS IN A SUPPORTING ROLE', 'ano': 2022}, None, None, None, None, None, None] |
| The Color Purple | [2024, 1986] | [None, None, None, None, None, None, None, None, None, None, None, None] |
| Les Misérables | [2013, 2020] | [None, {'categoria': 'ACTRESS IN A SUPPORTING ROLE', 'ano': 2013}, None, {'categoria': 'MAKEUP AND HAIRSTYLING', 'ano': 2013}, None, None, None, {'categoria': 'SOUND MIXING', 'ano': 2013}, None] |
| Scent of a Woman | [1976, 1993] | [None, None, {'categoria': 'ACTOR IN A LEADING ROLE', 'ano': 1993}, None, None, None] |
| Titanic | [1998, 1954] | [None, {'categoria': 'WRITING (Story and Screenplay)', 'ano': 1954}, None, None, {'categoria': 'ART DIRECTION', 'ano': 1998}, {'categoria': 'CINEMATOGRAPHY', 'ano': 1998}, {'categoria': 'COSTUME DESIGN', 'ano': 1998}, {'categoria': 'DIRECTING', 'ano': 1998}, {'categoria': 'FILM EDITING', 'ano': 1998}, None, {'categoria': 'MUSIC (Original Dramatic Score)', 'ano': 1998}, {'categoria': 'MUSIC (Original Song)', 'ano': 1998}, {'categoria': 'BEST PICTURE', 'ano': 1998}, {'categoria': 'SOUND', 'ano': 1998}, {'categoria': 'SOUND EFFECTS EDITING', 'ano': 1998}, {'categoria': 'VISUAL EFFECTS', 'ano': 1998}] |
| Marie Antoinette | [2007, 1939] | [None, None, None, None, {'categoria': 'COSTUME DESIGN', 'ano': 2007}] |
| The Lion King | [1995, 2020] | [{'categoria': 'MUSIC (Original Score)', 'ano': 1995}, {'categoria': 'MUSIC (Original Song)', 'ano': 1995}, None, None, None] |
| King Kong | [1977, 2006] | [None, None, {'categoria': 'SPECIAL ACHIEVEMENT AWARD (Visual Effects)', 'ano': 1977}, None, {'categoria': 'SOUND EDITING', 'ano': 2006}, {'categoria': 'SOUND MIXING', 'ano': 2006}, {'categoria': 'VISUAL EFFECTS', 'ano': 2006}] |
| True Grit | [2011, 1970] | [{'categoria': 'ACTOR', 'ano': 1970}, None, None, None, None, None, None, None, None, None, None, None] |
| Contact | [1993, 1998] | [None, None] |
| All Quiet on the Western Front | [1930, 2023] | [None, {'categoria': 'DIRECTING', 'ano': 1930}, {'categoria': 'OUTSTANDING PRODUCTION', 'ano': 1930}, None, {'categoria': 'CINEMATOGRAPHY', 'ano': 2023}, {'categoria': 'INTERNATIONAL FEATURE FILM', 'ano': 2023}, None, {'categoria': 'MUSIC (Original Score)', 'ano': 2023}, None, {'categoria': 'PRODUCTION DESIGN', 'ano': 2023}, None, None, None, {'categoria': 'BEST INTERNATIONAL FEATURE FILM', 'ano': 2023}] |

---


## Nível 12 — Casos Práticos

### 12.1 — Liste os 20 filmes mais premiados do Oscar para sua mostra.

**Comando MongoDB**

```js
db.indicados.aggregate([{$match: {vencedor: true}}, {$group: {_id: "$nome_do_filme", oscars: {$sum: 1}}}, {$sort: {oscars: -1}}, {$limit: 20}])
```

**Resultado**

| _id | oscars |
|---|---|
| Titanic | 12 |
| Ben-Hur | 11 |
| The Lord of the Rings: The Return of the King | 11 |
| West Side Story | 11 |
| The Last Emperor | 9 |
| The English Patient | 9 |
| Gigi | 9 |
| On the Waterfront | 8 |
| Cabaret | 8 |
| My Fair Lady | 8 |
| From Here to Eternity | 8 |
| Amadeus | 8 |
| Gone with the Wind | 8 |
| Gandhi | 8 |
| Slumdog Millionaire | 8 |
| Oppenheimer | 7 |
| Patton | 7 |
| The Sting | 7 |
| Going My Way | 7 |
| Schindler's List | 7 |

---

### 12.2 — Selecione 5 filmes de cada década (1930s até 2020s) que ganharam pelo menos um Oscar.

**Comando MongoDB**

```js
múltiplas queries por década com $match no ano_cerimonia
```

**Resultado**

| Campo | Valor |
|---|---|
| `1930s` | | _id | oscars |
|---|---|
| It Happened One Night | 5 |
| Anthony Adverse | 4 |
| The Informer | 4 |
| Cavalcade | 3 |
| Cimarron | 3 | |
| `1940s` | | _id | oscars |
|---|---|
| Gone with the Wind | 8 |
| Going My Way | 7 |
| The Best Years of Our Lives | 7 |
| Mrs. Miniver | 6 |
| How Green Was My Valley | 5 | |
| `1950s` | | _id | oscars |
|---|---|
| Gigi | 9 |
| On the Waterfront | 8 |
| From Here to Eternity | 8 |
| The Bridge on the River Kwai | 7 |
| An American in Paris | 6 | |
| `1960s` | | _id | oscars |
|---|---|
| Ben-Hur | 11 |
| West Side Story | 10 |
| My Fair Lady | 8 |
| Lawrence of Arabia | 7 |
| A Man for All Seasons | 6 | |
| `1970s` | | _id | oscars |
|---|---|
| Cabaret | 8 |
| The Sting | 7 |
| Patton | 7 |
| The Godfather Part II | 6 |
| Star Wars | 6 | |
| `1980s` | | _id | oscars |
|---|---|
| The Last Emperor | 9 |
| Gandhi | 8 |
| Amadeus | 8 |
| Out of Africa | 7 |
| Raiders of the Lost Ark | 5 | |
| `1990s` | | _id | oscars |
|---|---|
| Titanic | 11 |
| The English Patient | 9 |
| Dances With Wolves | 7 |
| Shakespeare in Love | 7 |
| Schindler's List | 7 | |
| `2000s` | | _id | oscars |
|---|---|
| The Lord of the Rings: The Return of the King | 11 |
| Slumdog Millionaire | 8 |
| Chicago | 6 |
| Gladiator | 5 |
| American Beauty | 5 | |
| `2010s` | | _id | oscars |
|---|---|
| Gravity | 7 |
| Mad Max: Fury Road | 6 |
| The Hurt Locker | 6 |
| La La Land | 6 |
| Hugo | 5 | |
| `2020s` | | _id | oscars |
|---|---|
| Everything Everywhere All at Once | 7 |
| Oppenheimer | 7 |
| Dune | 6 |
| Parasite | 5 |
| One Battle after Another | 5 | |

---

### 12.3 — Crie uma lista de "clássicos esquecidos" - filmes que ganharam Oscars, mas são de mais de 50 anos atrás.

**Comando MongoDB**

```js
db.indicados.aggregate([{$match: {vencedor: true, ano_filmagem: {$lt: 1975}}}, {$group: {_id: "$nome_do_filme", ano: {$first: "$ano_filmagem"}}}, {$sort: {ano: 1}}])
```

**Resultado**

| _id | ano | oscars |
|---|---|---|
| The Dove | 1927 | 1 |
| Wings | 1927 | 2 |
| 7th Heaven | 1927 | 3 |
| The Last Command | 1927 | 1 |
| Two Arabian Knights | 1927 | 1 |
| Sunrise | 1927 | 3 |
| Underworld | 1927 | 1 |
| White Shadows in the South Seas | 1928 | 1 |
| The Broadway Melody | 1928 | 1 |
| The Bridge of San Luis Rey | 1928 | 1 |
| Coquette | 1928 | 1 |
| The Patriot | 1928 | 1 |
| In Old Arizona | 1928 | 1 |
| The Divine Lady | 1928 | 1 |
| All Quiet on the Western Front | 1929 | 2 |
| The Divorcee | 1929 | 1 |
| Disraeli | 1929 | 1 |
| With Byrd at the South Pole | 1929 | 1 |
| King of Jazz | 1929 | 1 |
| The Big House | 1929 | 2 |

_... e mais 627 registros_

---

### 12.4 — Identifique os 5 momentos mais importantes (cerimônias com mais premiações).

**Comando MongoDB**

```js
db.indicados.aggregate([{$match: {vencedor: true}}, {$group: {_id: "$ano_cerimonia", premiações: {$sum: 1}}}, {$sort: {premiações: -1}}, {$limit: 5}])
```

**Resultado**

| _id | premiações |
|---|---|
| 1957 | 27 |
| 1950 | 27 |
| 1966 | 26 |
| 1952 | 26 |
| 1967 | 26 |

---

### 12.5 — Liste todos os "primeiros" históricos.

**Comando MongoDB**

```js
múltiplas queries com sort por ano_cerimonia
```

**Resultado**

| Campo | Valor |
|---|---|
| `primeira_vitoria_direcao` | | Campo | Valor |
|---|---|
| `nome` | `Lewis Milestone` |
| `ano` | `1928` |
| `filme` | `Two Arabian Knights` | |
| `primeiro_ator_negro_indicado` | | Campo | Valor |
|---|---|
| `nome` | `Sidney Poitier` |
| `ano` | `1959` |
| `filme` | `The Defiant Ones` | |

---

### 12.6 — Encontre casos de "injustiça" - filmes/atores muito indicados, mas que nunca ganharam.

**Comando MongoDB**

```js
db.indicados.aggregate([{$group: {_id: "$nome_do_indicado", indicacoes: {$sum: 1}, vitorias: {$sum: {$cond: ["$vencedor", 1, 0]}}}}, {$match: {indicacoes: {$gte: 4}, vitorias: 0}}])
```

**Resultado**

| _id | indicacoes | vitorias |
|---|---|---|
| Thomas Newman | 14 | 0 |
| Alex North | 14 | 0 |
| George Folsey | 12 | 0 |
| Music and Lyric by Diane Warren | 11 | 0 |
| Israel | 10 | 0 |
| Paramount Studio Sound Department, Loren L. Ryder, Sound Director | 10 | 0 |
| Walter Lantz, Producer | 10 | 0 |
| Randy Newman | 9 | 0 |
| Belgium | 8 | 0 |
| Glenn Close | 8 | 0 |
| Peter O'Toole | 8 | 0 |
| Robert Emmett Dolan | 8 | 0 |
| Ingmar Bergman | 8 | 0 |
| George Pal, Producer | 7 | 0 |
| James Newton Howard | 7 | 0 |
| Richard Burton | 7 | 0 |
| Bill Thomas | 7 | 0 |
| Republic Studio Sound Department, Daniel J. Bloomberg, Sound Director | 6 | 0 |
| Samuel Goldwyn Studio Sound Department, Gordon E. Sawyer, Sound Director | 6 | 0 |
| Deborah Kerr | 6 | 0 |

---

### 12.7 — Qual a probabilidade histórica de um filme indicado em 10 categorias ganhar Melhor Filme?

**Comando MongoDB**

```js
múltiplas aggregations combinadas
```

**Resultado**

`67.35% (66 de 98 casos)`

---

### 12.8 — Atores que ganharam Melhor Ator tendem a ter quantas indicações antes da primeira vitória?

**Comando MongoDB**

```js
query por vencedor + contagem de indicações anteriores por ator
```

**Resultado**

`Média de 2.73 indicações antes da primeira vitória`

---

### 12.9 — Qual categoria tem os vencedores mais "previsíveis" (mesmo artista/filme ganha múltiplas vezes)?

**Comando MongoDB**

```js
db.indicados.aggregate([{$match: {vencedor: true}}, {$group: {..., vencedores_unicos: {$addToSet: ...}}}, {$project: {repeticao: {$divide: [total, unicos]}}}])
```

**Resultado**

| _id | total_vitorias | categoria | total_unicos | repeticao |
|---|---|---|---|---|
| FOREIGN LANGUAGE FILM | 63 | FOREIGN LANGUAGE FILM | 28 | 2.25 |
| SHORT SUBJECT (Cartoon) | 39 | SHORT SUBJECT (Cartoon) | 18 | 2.1666666666666665 |
| SHORT SUBJECT (Two-reel) | 21 | SHORT SUBJECT (Two-reel) | 10 | 2.1 |
| OUTSTANDING PRODUCTION | 11 | OUTSTANDING PRODUCTION | 7 | 1.5714285714285714 |
| SOUND RECORDING | 26 | SOUND RECORDING | 17 | 1.5294117647058822 |
| MUSIC (Music Score of a Dramatic or Comedy Picture) | 19 | MUSIC (Music Score of a Dramatic or Comedy Picture) | 13 | 1.4615384615384615 |
| COSTUME DESIGN | 61 | COSTUME DESIGN | 43 | 1.4186046511627908 |
| MUSIC (Music Score--substantially original) | 4 | MUSIC (Music Score--substantially original) | 3 | 1.3333333333333333 |
| COSTUME DESIGN (Black-and-White) | 17 | COSTUME DESIGN (Black-and-White) | 13 | 1.3076923076923077 |
| DIRECTING | 97 | DIRECTING | 75 | 1.2933333333333332 |

---


## Nível 13 — Queries Criativas

### 13.1 — Encontre todos os filmes cujo nome começa com "The" e ganharam pelo menos um Oscar.

**Comando MongoDB**

```js
db.indicados.distinct("nome_do_filme", {nome_do_filme: {$regex: "^The "}, vencedor: true})
```

**Resultado**

- `The Abyss`
- `The Accidental Tourist`
- `The Accused`
- `The Adventures of Don Juan`
- `The Adventures of Priscilla, Queen of the Desert`
- `The Adventures of Robin Hood`
- `The African Queen`
- `The Age of Innocence`
- `The Alamo`
- `The Alaskan Eskimo`
- `The Anderson Platoon`
- `The Apartment`
- `The Appointments of Dennis Jennings`
- `The Artist`
- `The Assault`
- `The Aviator`
- `The Awful Truth`
- `The Bachelor and the Bobby-Soxer`
- `The Bad and the Beautiful`
- `The Barbarian Invasions`
- _... e mais 307 itens_

---

### 13.2 — Liste todos os indicados cujo nome contém um sobrenome composto (ex: "Mary-Louise Parker").

**Comando MongoDB**

```js
db.indicados.distinct("nome_do_indicado", {nome_do_indicado: {$regex: "-"}})
```

**Resultado**

- `20th Century-Fox`
- `20th Century-Fox Studio`
- `20th Century-Fox Studio Music Department, Louis Silvers, head of department  (no composer credit)`
- `20th Century-Fox Studio Sound Department`
- `20th Century-Fox Studio Sound Department, Carl Faulkner, Sound Director`
- `20th Century-Fox Studio Sound Department, Carl W. Faulkner, Sound Director`
- `20th Century-Fox Studio Sound Department, E. H. Hansen, Sound Director`
- `20th Century-Fox Studio Sound Department, Edmund H. Hansen, Sound Director`
- `20th Century-Fox Studio Sound Department, James P. Corcoran, Sound Director`
- `20th Century-Fox Studio Sound Department, James P. Corcoran, Sound Director; and Todd-AO Sound Department, Fred Hynes, Sound Director`
- `20th Century-Fox Studio Sound Department, Thomas T. Moulton, Sound Director`
- `Ai-Ling Lee and Mildred Iatrou Morgan`
- `Alain Gagnol and Jean-Loup Felicioli`
- `Alain Robbe-Grillet`
- `Alison Nigh-Strelich, Producer`
- `Ana López-Puigcerver, David Martí and Montse Ribé`
- `Anders Østergaard and Lise Lense-Møller`
- `Andrew Coats and Lou Hamou-Lhadj`
- `Andy Nelson, Ai-Ling Lee and Steve A. Morrow`
- `Ann-Margret`
- _... e mais 140 itens_

---

### 13.3 — Encontre todas as cerimônias onde houve empate (múltiplos vencedores na mesma categoria no mesmo ano).

**Comando MongoDB**

```js
db.indicados.aggregate([{$match: {vencedor: true}}, {$group: {_id: {categoria, ano}, total: {$sum: 1}}}, {$match: {total: {$gt: 1}}}])
```

**Resultado**

| _id | vencedores | total |
|---|---|---|
| {'categoria': 'CINEMATOGRAPHY', 'ano': 1928} | ['Charles Rosher', 'Karl Struss'] | 2 |
| {'categoria': 'ACTOR', 'ano': 1932} | ['Wallace Beery', 'Fredric March'] | 2 |
| {'categoria': 'DOCUMENTARY', 'ano': 1943} | ['United States Navy', 'Australian News & Information Bureau', 'Artkino', 'United States Army Special Services'] | 4 |
| {'categoria': 'DOCUMENTARY (Short Subject)', 'ano': 1950} | ['Richard de Rochemont, Producer', 'Edward Selzer, Producer'] | 2 |
| {'categoria': 'ACTRESS', 'ano': 1969} | ['Katharine Hepburn', 'Barbra Streisand'] | 2 |
| {'categoria': 'SPECIAL ACHIEVEMENT AWARD (Visual Effects)', 'ano': 1977} | ['Carlo Rambaldi, Glen Robinson, Frank Van der Veer', 'L. B. Abbott, Glen Robinson, Matthew Yuricich'] | 2 |
| {'categoria': 'DOCUMENTARY (Feature)', 'ano': 1987} | ['Brigitte Berman, Producer', 'Joseph Feury and Milton Justice, Producers'] | 2 |
| {'categoria': 'SHORT FILM (Live Action)', 'ano': 1995} | ['Peter Capaldi, Ruth Kenley-Letts', 'Peggy Rajski, Randy Stone'] | 2 |
| {'categoria': 'SOUND EDITING', 'ano': 2013} | ['Per Hallberg and Karen Baker Landers', 'Paul N.J. Ottosson'] | 2 |
| {'categoria': 'LIVE ACTION SHORT FILM', 'ano': 2026} | ['Sam A. Davis and Jack Piatt', 'Alexandre Singh and Natalie Musteata'] | 2 |

---

### 13.4 — Crie uma query que simule uma "loteria" - selecione 5 filmes aleatórios que ganharam Melhor Filme.

**Comando MongoDB**

```js
db.indicados.aggregate([{$match: {categoria: {$in: [...]}, vencedor: true}}, {$sample: {size: 5}}])
```

**Resultado**

| ano_cerimonia | nome_do_filme |
|---|---|
| 1986 | Out of Africa |
| 2017 | Moonlight |
| 2006 | Crash |
| 2024 | Oppenheimer |
| 2016 | Spotlight |

---

### 13.5 — Encontre padrões nos nomes dos filmes vencedores (quantos têm uma palavra, duas palavras, etc.).

**Comando MongoDB**

```js
db.indicados.distinct('nome_do_filme', {categoria: {$in: [...]}, vencedor: true}) + análise em Python
```

**Resultado**

| Campo | Valor |
|---|---|
| `1 palavra(s)` | `21` |
| `2 palavra(s)` | `14` |
| `3 palavra(s)` | `18` |
| `4 palavra(s)` | `5` |
| `5 palavra(s)` | `4` |
| `6 palavra(s)` | `2` |
| `7 palavra(s)` | `1` |
| `10 palavra(s)` | `1` |

---


## Nível 14 — Dashboard Completo

### 14.1 — Dashboard executivo completo em uma única query.

**Comando MongoDB**

```js
db.indicados.aggregate([{$facet: { total_indicacoes: [{$count: 'total'}], total_cerimonias: [...], ... }}])
```

**Resultado**

| Campo | Valor |
|---|---|
| `total_indicacoes` | `10793` |
| `total_cerimonias` | `98` |
| `total_vencedores` | `2219` |
| `categoria_mais_indicada` | | Campo | Valor |
|---|---|
| `_id` | `DIRECTING` |
| `total` | `479` | |
| `filme_mais_premiado` | | Campo | Valor |
|---|---|
| `_id` | `Titanic` |
| `oscars` | `12` | |
| `artista_mais_indicado` | | Campo | Valor |
|---|---|
| `_id` | `Metro-Goldwyn-Mayer` |
| `indicacoes` | `64` | |
| `decada_mais_premiacoes` | | Campo | Valor |
|---|---|
| `_id` | `1950.0` |
| `total` | `253` | |
| `total_categorias_unicas` | `115` |

---
