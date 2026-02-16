---
layout: default
title: Block-Sample MAC-Bayes Generalization Bounds
---

# Block-Sample MAC-Bayes Generalization Bounds
**arXiv**：[2602.12605v1](https://arxiv.org/abs/2602.12605) · [PDF](https://arxiv.org/pdf/2602.12605.pdf)  
**作者**：Matthias Frey, Jingge Zhu, Michael C. Gastpar  

**一句话要点**：提出块样本MAC-Bayes泛化界以改进传统PAC-Bayes和MAC-Bayes界的紧致性。

**关键词**：泛化界, MAC-Bayes, 块样本, PAC-Bayes, 机器学习理论, 期望误差

## 3 点简述
- 核心问题：传统PAC-Bayes界以高概率约束泛化误差，MAC-Bayes界约束期望泛化误差，但两者紧致性可能不足。
- 方法要点：提出块样本MAC-Bayes界，通过依赖训练数据子集（块）的散度项，泛化已知PAC-Bayes界的期望版本。
- 实验或效果：数值示例显示，传统PAC-Bayes界可能无效，而新界在适当块大小下有限，且探讨高概率版本的可能性未知。

## 摘要（原文）

> We present a family of novel block-sample MAC-Bayes bounds (mean approximately correct). While PAC-Bayes bounds (probably approximately correct) typically give bounds for the generalization error that hold with high probability, MAC-Bayes bounds have a similar form but bound the expected generalization error instead. The family of bounds we propose can be understood as a generalization of an expectation version of known PAC-Bayes bounds. Compared to standard PAC-Bayes bounds, the new bounds contain divergence terms that only depend on subsets (or \emph{blocks}) of the training data. The proposed MAC-Bayes bounds hold the promise of significantly improving upon the tightness of traditional PAC-Bayes and MAC-Bayes bounds. This is illustrated with a simple numerical example in which the original PAC-Bayes bound is vacuous regardless of the choice of prior, while the proposed family of bounds are finite for appropriate choices of the block size. We also explore the question whether high-probability versions of our MAC-Bayes bounds (i.e., PAC-Bayes bounds of a similar form) are possible. We answer this question in the negative with an example that shows that in general, it is not possible to establish a PAC-Bayes bound which (a) vanishes with a rate faster than $\mathcal{O}(1/\log n)$ whenever the proposed MAC-Bayes bound vanishes with rate $\mathcal{O}(n^{-1/2})$ and (b) exhibits a logarithmic dependence on the permitted error probability.

