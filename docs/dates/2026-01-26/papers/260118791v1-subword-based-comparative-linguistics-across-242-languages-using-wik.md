---
layout: default
title: Subword-Based Comparative Linguistics across 242 Languages Using Wikipedia Glottosets
---

# Subword-Based Comparative Linguistics across 242 Languages Using Wikipedia Glottosets
**arXiv**：[2601.18791v1](https://arxiv.org/abs/2601.18791) · [PDF](https://arxiv.org/pdf/2601.18791.pdf)  
**作者**：Iaroslav Chelombitko, Mika Hämäläinen, Aleksey Komissarov  

**一句话要点**：提出基于子词的维基百科语料集框架，用于242种拉丁和西里尔文字语言的比较语言学分析。

**关键词**：子词分析, 比较语言学, 字节对编码, 语言相似性, 词汇重叠, 跨语言研究

## 3 点简述
- 核心问题：大规模跨语言词汇比较，分析语言相似性和词汇差异。
- 方法要点：利用字节对编码构建子词向量，通过语料集进行统一分析。
- 实验或效果：BPE分割与语素边界对齐度提升95%，词汇相似性与语言亲缘性显著相关。

## 摘要（原文）

> We present a large-scale comparative study of 242 Latin and Cyrillic-script languages using subword-based methodologies. By constructing 'glottosets' from Wikipedia lexicons, we introduce a framework for simultaneous cross-linguistic comparison via Byte-Pair Encoding (BPE). Our approach utilizes rank-based subword vectors to analyze vocabulary overlap, lexical divergence, and language similarity at scale. Evaluations demonstrate that BPE segmentation aligns with morpheme boundaries 95% better than random baseline across 15 languages (F1 = 0.34 vs 0.15). BPE vocabulary similarity correlates significantly with genetic language relatedness (Mantel r = 0.329, p < 0.001), with Romance languages forming the tightest cluster (mean distance 0.51) and cross-family pairs showing clear separation (0.82). Analysis of 26,939 cross-linguistic homographs reveals that 48.7% receive different segmentations across related languages, with variation correlating to phylogenetic distance. Our results provide quantitative macro-linguistic insights into lexical patterns across typologically diverse languages within a unified analytical framework.

