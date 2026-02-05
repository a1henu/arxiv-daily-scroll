---
layout: default
title: LORE: Jointly Learning the Intrinsic Dimensionality and Relative Similarity Structure From Ordinal Data
---

# LORE: Jointly Learning the Intrinsic Dimensionality and Relative Similarity Structure From Ordinal Data
**arXiv**：[2602.04192v1](https://arxiv.org/abs/2602.04192) · [PDF](https://arxiv.org/pdf/2602.04192.pdf)  
**作者**：Vivek Anand, Alec Helbling, Mark Davenport, Gordon Berman, Sankar Alagapan, Christopher Rozell  

**一句话要点**：提出LORE框架，从序数数据中联合学习内在维度和相对相似性结构。

**关键词**：序数嵌入, 内在维度学习, 非凸正则化, 感知空间建模, 低维结构发现

## 3 点简述
- 核心问题：从主观感知空间的序数数据中学习内在维度是挑战。
- 方法要点：使用非凸Schatten-p拟范数正则化，自动恢复嵌入维度和序数嵌入。
- 实验或效果：在合成、模拟和真实数据上验证，学习紧凑、可解释的低维嵌入。

## 摘要（原文）

> Learning the intrinsic dimensionality of subjective perceptual spaces such as taste, smell, or aesthetics from ordinal data is a challenging problem. We introduce LORE (Low Rank Ordinal Embedding), a scalable framework that jointly learns both the intrinsic dimensionality and an ordinal embedding from noisy triplet comparisons of the form, "Is A more similar to B than C?". Unlike existing methods that require the embedding dimension to be set apriori, LORE regularizes the solution using the nonconvex Schatten-$p$ quasi norm, enabling automatic joint recovery of both the ordinal embedding and its dimensionality. We optimize this joint objective via an iteratively reweighted algorithm and establish convergence guarantees. Extensive experiments on synthetic datasets, simulated perceptual spaces, and real world crowdsourced ordinal judgements show that LORE learns compact, interpretable and highly accurate low dimensional embeddings that recover the latent geometry of subjective percepts. By simultaneously inferring both the intrinsic dimensionality and ordinal embeddings, LORE enables more interpretable and data efficient perceptual modeling in psychophysics and opens new directions for scalable discovery of low dimensional structure from ordinal data in machine learning.

