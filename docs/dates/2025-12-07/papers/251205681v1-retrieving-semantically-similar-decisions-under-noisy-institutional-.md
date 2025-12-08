---
layout: default
title: Retrieving Semantically Similar Decisions under Noisy Institutional Labels: Robust Comparison of Embedding Methods
---

# Retrieving Semantically Similar Decisions under Noisy Institutional Labels: Robust Comparison of Embedding Methods
**arXiv**：[2512.05681v1](https://arxiv.org/abs/2512.05681) · [PDF](https://arxiv.org/pdf/2512.05681.pdf)  
**作者**：Tereza Novotna, Jakub Harasta  

**一句话要点**：比较嵌入方法以在噪声标签下检索捷克宪法法院案例的语义相似决策

**关键词**：案例法检索, 嵌入方法比较, 噪声标签评估, 捷克宪法法院, 语义相似性, nDCG诊断

## 3 点简述
- 核心问题：在噪声机构标签下检索案例法，评估嵌入模型性能。
- 方法要点：比较通用嵌入器与领域特定BERT，采用噪声感知评估框架。
- 实验或效果：通用嵌入器显著优于领域BERT，差异统计显著，诊断显示低绝对性能源于标签漂移。

## 摘要（原文）

> Retrieving case law is a time-consuming task predominantly carried out by querying databases. We provide a comparison of two models in three different settings for Czech Constitutional Court decisions: (i) a large general-purpose embedder (OpenAI), (ii) a domain-specific BERT-trained from scratch on ~30,000 decisions using sliding windows and attention pooling. We propose a noise-aware evaluation including IDF-weighted keyword overlap as graded relevance, binarization via two thresholds (0.20 balanced, 0.28 strict), significance via paired bootstrap, and an nDCG diagnosis supported with qualitative analysis. Despite modest absolute nDCG (expected under noisy labels), the general OpenAI embedder decisively outperforms the domain pre-trained BERT in both settings at @10/@20/@100 across both thresholds; differences are statistically significant. Diagnostics attribute low absolutes to label drift and strong ideals rather than lack of utility. Additionally, our framework is robust enough to be used for evaluation under a noisy gold dataset, which is typical when handling data with heterogeneous labels stemming from legacy judicial databases.

