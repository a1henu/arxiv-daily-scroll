---
layout: default
title: PCA of probability measures: Sparse and Dense sampling regimes
---

# PCA of probability measures: Sparse and Dense sampling regimes
**arXiv**：[2602.02190v1](https://arxiv.org/abs/2602.02190) · [PDF](https://arxiv.org/pdf/2602.02190.pdf)  
**作者**：Gachon Erell, Jérémie Bigot, Elsa Cazelles  

**一句话要点**：提出概率测度PCA的双渐近分析，揭示稀疏与稠密采样机制下的收敛率。

**关键词**：概率测度PCA, 双渐近分析, 稀疏采样, 稠密采样, 收敛率, 经验协方差算子

## 3 点简述
- 研究多概率测度PCA问题，分析n个测度各含m样本的双渐近收敛行为。
- 推导经验协方差算子和PCA超额风险的收敛率，形式为n^{-1/2} + m^{-α}，α取决于嵌入选择。
- 数值实验验证理论率，显示适当子采样可保持PCA精度并降低计算成本。

## 摘要（原文）

> A common approach to perform PCA on probability measures is to embed them into a Hilbert space where standard functional PCA techniques apply. While convergence rates for estimating the embedding of a single measure from $m$ samples are well understood, the literature has not addressed the setting involving multiple measures. In this paper, we study PCA in a double asymptotic regime where $n$ probability measures are observed, each through $m$ samples. We derive convergence rates of the form $n^{-1/2} + m^{-α}$ for the empirical covariance operator and the PCA excess risk, where $α>0$ depends on the chosen embedding. This characterizes the relationship between the number $n$ of measures and the number $m$ of samples per measure, revealing a sparse (small $m$) to dense (large $m$) transition in the convergence behavior. Moreover, we prove that the dense-regime rate is minimax optimal for the empirical covariance error. Our numerical experiments validate these theoretical rates and demonstrate that appropriate subsampling preserves PCA accuracy while reducing computational cost.

