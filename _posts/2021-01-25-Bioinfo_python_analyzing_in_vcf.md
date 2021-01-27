---
layout: post
title: Python分析VCF数据
tags: Python
---

在完成变异检测后，会得到VCF文件，其中记录了样本的基因组基因组变异。Python模块`PyVCF`可以用来分析VCF 文件。

## 安装

> pip install pyvcf

## 数据准备

```{bash}
tabix -fh ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/release/20130502/supporting/vcf_with_sample_level_annotation/ALL.chr22.phase3_shapeit2_mvncall_integrated_v5_extra_anno.20130502.genotypes.vcf.gz 22:1-17000000 | bgzip -c > genotypes.vcf.gz

tabix -p vcf genotypes.vcf.gz
```

下载的是1000 Genomes Project 的22号染色体的VCF文件， 并压缩。

之后对其创建index。

## 分析步骤

```{python}
import vcf
v = vcf.Reader(filename='genotypes.vcf.gz')
print('Variant Level information')
infos = v.infos
for info in infos:
print(info)
print('Sample Level information')
fmts = v.formats
for fmt in fmts:
print(fmt)
```

我们首先查看了每条记录的一些可用注释信息

在变异水平上， 也就是对每一条变异记录而言：

-   AC: the total number of alleles in called genotypes

-   AF: the estimated ALT allele frequency

-   NS: the number of samples with data

-   AN: the total number of alleles in called genotypes

-   DP: the total read depth

等等， 其他的数据集可能会有其他的注释信息。

在样本水平上：

只有两个注释信息

-   GT： genotype

-   DP: the per sample read depth

接下来探究的是每个VCF变异记录的详细信息

```{python}
>>> rec = next(v)
>>> rec
<vcf.model._Record object at 0x7f197cafeac0>
>>> print(rec.CHROM, rec.POS, rec.ID, rec.REF, rec.ALT, rec.QUAL, rec.FILTER)
>>> print(rec.INFO)
>>> print(rec.FORMAT)
```

```{python}
22 16050319 None C [T] 100 []

{'AC': [1], 'AF': [0.000199681], 'AN': 5008, 'NS': 2504, 'DP': [22609], 'ASN_AF': [0.0], 'AMR_AF': [0.0014], 'SAS_AF': [''], 'EUR_AF': [0.0], 'EAS_AF': [''], 'AFR_AF': [0.0], 'SAN_AF': [0.0]}

GT:DP
```

```{python}
samples = rec.samples
print(len(samples))
sample = samples[0]
print(sample.called, sample.gt_alleles, sample.is_het,sample.phased)
print(int(sample['DP']))
```

```{python}
2504

True ['0', '0'] False True

10
```

首先从检索最基本的位置信息开始：

-   chromosome

-   position

-   identifier

-   reference base(typically just one)

-   alternative bases

-   quality

-   filter status

接下来检索的是变异水平的信息(AC, DP等)， 以及sample水平的format(DP & GT)。

最后我们计算了samples的数量， 并且提取出一个sample来检测, 它是否有这个位置的突变， 以及reported alleles, 还有杂合性。
