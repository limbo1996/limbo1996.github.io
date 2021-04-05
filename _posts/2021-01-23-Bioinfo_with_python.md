---
layout: post
title: Bioinformatics with Python(NGS)
tags: Python
---

> 参考《Antao - Bioinformatics with Python Cookbook Second Edition》

# 处理基本的测序数据

## 准备

下载Biopython

## 过程

导入模块并验证邮箱

```{python}
from Bio import Entrez, SeqIO

Entrez.email = "your@email"
```

下载数据

```{python}
from Bio import Entrez, SeqIO
hdl = Entrez.efetch(db='nucleotide', id=['NM_002299'], rettype='fasta') # Lactase gene 
seq = SeqIO.read(hdl, 'fasta')
```

```{python}
print(seq.id)
```

这一步将这个sequence读入为了一个`Biopython sequence`对象。

### 数据保存

接下来将读入的数据保存为一个FASTA文件

```{python}
from Bio import SeqIO

>>> w_hdl = open("/home/limbo1996/example.fasta", "w")
>>> w_seq = seq[11:5795]
>>> SeqIO.write([w_seq], w_hdl, "fasta")
>>> w_hdl.close()
```

`SeqIO.write` 函数输入的是一个sequence的list(可以不只是一个sequence)，但是当你要一次写入很多个sequence的时候， 最好不要用list，因为会消耗大量的内存，最好使用一个迭代器或者多次运行`SeqIO.write` .

到这里我们下载并保存了一个一个`fasta`文件，接下来将其读取

```{python}
>>> recs = SeqIO.parse('example.fasta', 'fasta')
>>> for rec in recs:
...     seq = rec.seq
...     print(rec.description)
...     print(seq[:10])
...     print(seq.alphabet)


NM_002299.4 Homo sapiens lactase (LCT), mRNA
GAAAATGGAG
```

在这里我们得到了DNA序列， 同样我们可以直接使用函数将DNA序列转录为RNA序列

```{python}
>>> rna = seq.transcribe()
>>> rna
```

同样可以进行翻译

```{python}
>>> pr = seq.translate()
```
