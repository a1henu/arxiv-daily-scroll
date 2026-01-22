---
layout: default
title: Efficient and Minimax-optimal In-context Nonparametric Regression with Transformers
---

# Efficient and Minimax-optimal In-context Nonparametric Regression with Transformers
**arXiv**：[2601.15014v1](https://arxiv.org/abs/2601.15014) · [PDF](https://arxiv.org/pdf/2601.15014.pdf)  
**作者**：Michelle Ching, Ioana Popescu, Nico Smith, Tianyi Ma, William G. Underwood, Richard J. Samworth  

**一句话要点**：提出高效Transformer实现上下文非参数回归，达到极小极大最优收敛率。

**关键词**：上下文学习, 非参数回归, Transformer, 极小极大最优, 收敛率, 局部多项式估计

## 3 点简述
- 研究上下文学习，针对α-Hölder光滑回归函数的非参数回归问题。
- 证明预训练Transformer能以较少参数和序列实现极小极大最优收敛率。
- 通过近似局部多项式估计器，实现核加权多项式基和梯度下降。

## 摘要（原文）

> We study in-context learning for nonparametric regression with $α$-Hölder smooth regression functions, for some $α>0$. We prove that, with $n$ in-context examples and $d$-dimensional regression covariates, a pretrained transformer with $Θ(\log n)$ parameters and $Ω\bigl(n^{2α/(2α+d)}\log^3 n\bigr)$ pretraining sequences can achieve the minimax-optimal rate of convergence $O\bigl(n^{-2α/(2α+d)}\bigr)$ in mean squared error. Our result requires substantially fewer transformer parameters and pretraining sequences than previous results in the literature. This is achieved by showing that transformers are able to approximate local polynomial estimators efficiently by implementing a kernel-weighted polynomial basis and then running gradient descent.

