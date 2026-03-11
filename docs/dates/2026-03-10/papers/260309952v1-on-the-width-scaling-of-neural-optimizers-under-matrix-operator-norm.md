---
layout: default
title: On the Width Scaling of Neural Optimizers Under Matrix Operator Norms I: Row/Column Normalization and Hyperparameter Transfer
---

# On the Width Scaling of Neural Optimizers Under Matrix Operator Norms I: Row/Column Normalization and Hyperparameter Transfer
**arXiv**：[2603.09952v1](https://arxiv.org/abs/2603.09952) · [PDF](https://arxiv.org/pdf/2603.09952.pdf)  
**作者**：Ruihan Xu, Jiajin Li, Yiping Lu  

**一句话要点**：提出基于矩阵算子范数的归一化优化器以解决宽度缩放中的稳定性问题

**关键词**：优化器设计, 宽度缩放, 矩阵算子范数, 归一化方法, 学习率转移, 深度学习理论

## 3 点简述
- 核心问题：神经网络宽度增加时优化器行为不稳定，需设计宽度无关的稳定优化器
- 方法要点：引入均值归一化算子范数，实现层间可组合性，推导出宽度无关的光滑性界
- 实验或效果：MOGA优化器在GPT-2和LLaMA预训练中与Muon竞争，在大令牌低损失场景更快

## 摘要（原文）

> A central question in modern deep learning is how to design optimizers whose behavior remains stable as the network width $w$ increases. We address this question by interpreting several widely used neural-network optimizers, including \textrm{AdamW} and \textrm{Muon}, as instances of steepest descent under matrix operator norms. This perspective links optimizer geometry with the Lipschitz structure of the network forward map, and enables width-independent control of both Lipschitz and smoothness constants. However, steepest-descent rules induced by standard $p \to q$ operator norms lack layerwise composability and therefore cannot provide width-independent bounds in deep architectures. We overcome this limitation by introducing a family of mean-normalized operator norms, denoted $\pmean \to \qmean$, that admit layerwise composability, yield width-independent smoothness bounds, and give rise to practical optimizers such as \emph{rescaled} \textrm{AdamW}, row normalization, and column normalization. The resulting learning rate width-aware scaling rules recover $μ$P scaling~\cite{yang2021tensor} as a special case and provide a principled mechanism for cross-width learning-rate transfer across a broad class of optimizers. We further show that \textrm{Muon} can suffer an $\mathcal{O}(\sqrt{w})$ worst-case growth in the smoothness constant, whereas a new family of row-normalized optimizers we propose achieves width-independent smoothness guarantees. Based on the observations, we propose MOGA (Matrix Operator Geometry Aware), a width-aware optimizer based only on row/column-wise normalization that enables stable learning-rate transfer across model widths. Large-scale pre-training on GPT-2 and LLaMA shows that MOGA, especially with row normalization, is competitive with Muon while being notably faster in large-token and low-loss regimes.

