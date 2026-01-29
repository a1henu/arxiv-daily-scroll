---
layout: default
title: Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis
---

# Do Whitepaper Claims Predict Market Behavior? Evidence from Cryptocurrency Factor Analysis
**arXiv**：[2601.20336v1](https://arxiv.org/abs/2601.20336) · [PDF](https://arxiv.org/pdf/2601.20336.pdf)  
**作者**：Murad Farzulla  

**一句话要点**：提出结合零样本NLP与张量分解的管道，评估加密货币白皮书声明与市场行为的对齐性。

**关键词**：加密货币分析, 零样本NLP, 张量分解, 叙事经济学, 市场行为对齐

## 3 点简述
- 核心问题：加密货币白皮书声明是否与市场行为对齐，以验证叙事经济学假设。
- 方法要点：使用BART-MNLI分类和张量分解构建声明、市场统计和潜在因子三个空间。
- 实验或效果：结果显示弱对齐，统计-因子关系显著，但声明-市场对齐不显著，排除比特币影响后结论一致。

## 摘要（原文）

> Cryptocurrency projects articulate value propositions through whitepapers, making claims about functionality and technical capabilities. This study investigates whether these narratives align with observed market behavior. We construct a pipeline combining zero-shot NLP classification (BART-MNLI) with CP tensor decomposition to compare three spaces: (1) a claims matrix from 24 whitepapers across 10 semantic categories, (2) market statistics for 49 assets over two years of hourly data, and (3) latent factors from tensor decomposition (rank 2, 92.45% variance explained). Using Procrustes rotation and Tucker's congruence coefficient, we test alignment across 23 common entities.
>   Results show weak alignment: claims-statistics (phi=0.341, p=0.332), claims-factors (phi=0.077, p=0.747), and statistics-factors (phi=0.197, p<0.001). The statistics-factors significance validates our methodology, confirming the pipeline detects relationships when present. Inter-model validation with DeBERTa-v3 yields 32% exact agreement but 67% top-3 agreement. Cross-sectional analysis reveals heterogeneous contributions: NEAR, MKR, ATOM show positive alignment while ENS, UNI, Bitcoin diverge most. Excluding Bitcoin confirms results are not driven by market dominance.
>   We interpret findings as weak alignment between whitepaper narratives and market factor structure. Limited power (n=23) precludes distinguishing weak from no alignment, but strong alignment (phi>=0.70) can be confidently rejected. Implications for narrative economics and investment analysis are discussed.

