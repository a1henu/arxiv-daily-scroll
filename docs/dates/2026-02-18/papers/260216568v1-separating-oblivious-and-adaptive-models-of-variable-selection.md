---
layout: default
title: Separating Oblivious and Adaptive Models of Variable Selection
---

# Separating Oblivious and Adaptive Models of Variable Selection
**arXiv**：[2602.16568v1](https://arxiv.org/abs/2602.16568) · [PDF](https://arxiv.org/pdf/2602.16568.pdf)  
**作者**：Ziyun Chen, Jerry Li, Kevin Tian, Yusong Zhu  

**一句话要点**：提出稀疏恢复中ℓ∞误差的遗忘与自适应模型分离，揭示变量选择任务中的样本复杂度差异。

**关键词**：稀疏恢复, ℓ∞误差, 变量选择, 遗忘模型, 自适应模型, 样本复杂度

## 3 点简述
- 研究稀疏恢复问题，聚焦ℓ∞误差保证，适用于变量选择任务以估计稀疏信号支持。
- 证明遗忘模型下，近线性时间与≈k log d样本可达最优ℓ∞误差；自适应模型需≳k²样本。
- 初步探索部分自适应模型，展示≈k log d测量下可实现非平凡变量选择保证。

## 摘要（原文）

> Sparse recovery is among the most well-studied problems in learning theory and high-dimensional statistics. In this work, we investigate the statistical and computational landscapes of sparse recovery with $\ell_\infty$ error guarantees. This variant of the problem is motivated by \emph{variable selection} tasks, where the goal is to estimate the support of a $k$-sparse signal in $\mathbb{R}^d$. Our main contribution is a provable separation between the \emph{oblivious} (``for each'') and \emph{adaptive} (``for all'') models of $\ell_\infty$ sparse recovery. We show that under an oblivious model, the optimal $\ell_\infty$ error is attainable in near-linear time with $\approx k\log d$ samples, whereas in an adaptive model, $\gtrsim k^2$ samples are necessary for any algorithm to achieve this bound. This establishes a surprising contrast with the standard $\ell_2$ setting, where $\approx k \log d$ samples suffice even for adaptive sparse recovery. We conclude with a preliminary examination of a \emph{partially-adaptive} model, where we show nontrivial variable selection guarantees are possible with $\approx k\log d$ measurements.

