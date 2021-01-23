---
layout: post
title: 用HLA-HD进行HLA分型
tags: SoftWare
---



主页：[HLA-HD](https://www.genome.med.kyoto-u.ac.jp/HLA-HD/)

## 下载

在主页中申请下载，注册一下拿到链接即可下载。

```shell
tar -zxvf hlahd.version.tar.gz
```

进入解压出来的目录中

```
sh install.sh
```

即可完成安装

注意`HLA-HD`需要`bowtie2`软件，并且需要将`bin`添加到`PATH`中。

## 使用

官方建议首先确认`open files`的值，最好大于1024

```shell
ulimit -Sa
```

如果小于1024

```
ulimit -n 1024
```

并且如果你的输入文件是压缩格式的，最好解压。

> If you have fastq.gz file, unzip gz file in advance. 

```shell
> hlahd.sh -t [thread_num] -m [minimum length of reads] -c [trimming rate] -f [path_to freq_data directory] fastq_1 fastq_2 gene_split_filt path_to_dictionary_directory IDNAME[any name] output_directory
```

主要是几个参数：

-m : A read whose length is shorter than this parameter is ignored. Default size is 100.

-t : Number of cores used to execute the program.

-c : Trimming option. If a match sequence is not found in the dictionary, trim the read until some sequence is matched to or reaches this ratio. Default is 1.0.

-f : Use information of allele frequencies. The default data exist in the installed directory (/hlahd.version/freq_data).



## 实例

```shell
> hlahd.sh -t 2 -m 100 -c 0.95 -f freq_data/ data/sample_1.fastq data/sample_2.fastq HLA_gene.split.txt dictionary/ sampleID estimation
```

其中`freq_data/`, `HLA_gene.split.txt`, `dictionary/`, 工具中都有提供