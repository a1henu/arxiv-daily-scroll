---
layout: default
title: High-accuracy and dimension-free sampling with diffusions
---

# High-accuracy and dimension-free sampling with diffusions
**arXiv**：[2601.10708v1](https://arxiv.org/abs/2601.10708) · [PDF](https://arxiv.org/pdf/2601.10708.pdf)  
**作者**：Khashayar Gatmiry, Sitan Chen, Adil Salim  

**一句话要点**：提出基于低度逼近与配置法的新求解器，实现扩散模型高精度且维度无关的采样。

**关键词**：扩散模型, 采样算法, 数值求解, 迭代复杂度, 维度无关性, 高精度保证

## 3 点简述
- 扩散模型采样依赖微分方程数值解，传统方法迭代复杂度随维度和精度呈多项式增长。
- 新方法结合低度逼近与配置法，证明迭代复杂度在精度上呈多对数缩放，不显式依赖环境维度。
- 仅需近似访问数据分布分数，首次为扩散采样器提供高精度保证，复杂度受目标分布有效半径影响。

## 摘要（原文）

> Diffusion models have shown remarkable empirical success in sampling from rich multi-modal distributions. Their inference relies on numerically solving a certain differential equation. This differential equation cannot be solved in closed form, and its resolution via discretization typically requires many small iterations to produce \emph{high-quality} samples.
>   More precisely, prior works have shown that the iteration complexity of discretization methods for diffusion models scales polynomially in the ambient dimension and the inverse accuracy $1/\varepsilon$. In this work, we propose a new solver for diffusion models relying on a subtle interplay between low-degree approximation and the collocation method (Lee, Song, Vempala 2018), and we prove that its iteration complexity scales \emph{polylogarithmically} in $1/\varepsilon$, yielding the first ``high-accuracy'' guarantee for a diffusion-based sampler that only uses (approximate) access to the scores of the data distribution. In addition, our bound does not depend explicitly on the ambient dimension; more precisely, the dimension affects the complexity of our solver through the \emph{effective radius} of the support of the target distribution only.

