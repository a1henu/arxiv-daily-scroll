---
layout: default
title: Algorithmic Simplification of Neural Networks with Mosaic-of-Motifs
---

# Algorithmic Simplification of Neural Networks with Mosaic-of-Motifs
**arXiv**：[2602.14896v1](https://arxiv.org/abs/2602.14896) · [PDF](https://arxiv.org/pdf/2602.14896.pdf)  
**作者**：Pedram Bakhtiarifard, Tong Chen, Jonathan Wenshøj, Erik B Dam, Raghavendra Selvan  

**一句话要点**：提出Mosaic-of-Motifs方法以降低神经网络算法复杂度，实现模型压缩。

**关键词**：神经网络压缩, 算法复杂度, Mosaic-of-Motifs, Kolmogorov复杂度, 参数约束

## 3 点简述
- 核心问题：探究深度神经网络为何适合压缩，基于算法复杂度视角。
- 方法要点：通过分区参数为块并重用motifs，约束参数化以降低Kolmogorov复杂度。
- 实验或效果：实验显示训练后模型算法复杂度降低，性能与未约束模型相当。

## 摘要（原文）

> Large-scale deep learning models are well-suited for compression. Methods like pruning, quantization, and knowledge distillation have been used to achieve massive reductions in the number of model parameters, with marginal performance drops across a variety of architectures and tasks. This raises the central question: \emph{Why are deep neural networks suited for compression?} In this work, we take up the perspective of algorithmic complexity to explain this behavior. We hypothesize that the parameters of trained models have more structure and, hence, exhibit lower algorithmic complexity compared to the weights at (random) initialization. Furthermore, that model compression methods harness this reduced algorithmic complexity to compress models. Although an unconstrained parameterization of model weights, $\mathbf{w} \in \mathbb{R}^n$, can represent arbitrary weight assignments, the solutions found during training exhibit repeatability and structure, making them algorithmically simpler than a generic program. To this end, we formalize the Kolmogorov complexity of $\mathbf{w}$ by $\mathcal{K}(\mathbf{w})$. We introduce a constrained parameterization $\widehat{\mathbf{w}}$, that partitions parameters into blocks of size $s$, and restricts each block to be selected from a set of $k$ reusable motifs, specified by a reuse pattern (or mosaic). The resulting method, $\textit{Mosaic-of-Motifs}$ (MoMos), yields algorithmically simpler model parameterization compared to unconstrained models. Empirical evidence from multiple experiments shows that the algorithmic complexity of neural networks, measured using approximations to Kolmogorov complexity, can be reduced during training. This results in models that perform comparably with unconstrained models while being algorithmically simpler.

