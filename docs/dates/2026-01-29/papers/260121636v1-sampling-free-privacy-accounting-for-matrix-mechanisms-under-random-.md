---
layout: default
title: Sampling-Free Privacy Accounting for Matrix Mechanisms under Random Allocation
---

# Sampling-Free Privacy Accounting for Matrix Mechanisms under Random Allocation
**arXiv**：[2601.21636v1](https://arxiv.org/abs/2601.21636) · [PDF](https://arxiv.org/pdf/2601.21636.pdf)  
**作者**：Jan Schuchardt, Nikita Kalinin  

**一句话要点**：提出基于Rényi散度和条件组合的无采样隐私放大方法，用于随机分配下的矩阵机制隐私计算。

**关键词**：差分隐私, 隐私放大, 矩阵机制, Rényi散度, 随机分配, 动态规划

## 3 点简述
- 研究随机分配下差分隐私模型训练中矩阵机制的隐私放大问题，解决现有采样方法概率性保证或需随机弃权的问题。
- 开发基于Rényi散度的动态规划方法和条件组合方法，提供无采样隐私界限，适用于任意带状和非带状矩阵。
- 通过数值比较验证方法在多种矩阵机制中的有效性，优于现有采样方法，尤其在低ε时提供更强隐私保证。

## 摘要（原文）

> We study privacy amplification for differentially private model training with matrix factorization under random allocation (also known as the balls-in-bins model). Recent work by Choquette-Choo et al. (2025) proposes a sampling-based Monte Carlo approach to compute amplification parameters in this setting. However, their guarantees either only hold with some high probability or require random abstention by the mechanism. Furthermore, the required number of samples for ensuring $(ε,δ)$-DP is inversely proportional to $δ$. In contrast, we develop sampling-free bounds based on Rényi divergence and conditional composition. The former is facilitated by a dynamic programming formulation to efficiently compute the bounds. The latter complements it by offering stronger privacy guarantees for small $ε$, where Rényi divergence bounds inherently lead to an over-approximation. Our framework applies to arbitrary banded and non-banded matrices. Through numerical comparisons, we demonstrate the efficacy of our approach across a broad range of matrix mechanisms used in research and practice.

