---
layout: default
title: Quantum-Enhanced Neural Contextual Bandit Algorithms
---

# Quantum-Enhanced Neural Contextual Bandit Algorithms
**arXiv**：[2601.02870v1](https://arxiv.org/abs/2601.02870) · [PDF](https://arxiv.org/pdf/2601.02870.pdf)  
**作者**：Yuqi Huang, Vincent Y. F Tan, Sharu Theresa Jose  

**一句话要点**：提出QNTK-UCB算法，利用量子神经正切核解决量子神经网络在上下文赌博机中的过参数化和训练不稳定问题。

**关键词**：量子神经网络, 上下文赌博机, 量子神经正切核, 岭回归, 在线学习, 量子优势

## 3 点简述
- 核心问题：量子神经网络在上下文赌博机中面临过参数化、计算不稳定和贫瘠高原现象，导致经典算法扩展困难。
- 方法要点：通过冻结随机初始化的量子神经网络，使用静态量子神经正切核进行岭回归，避免不稳定训练并利用量子归纳偏置。
- 实验或效果：理论分析显示参数缩放显著改善至Ω((TK)^3)，实证在低数据量下表现出优越样本效率。

## 摘要（原文）

> Stochastic contextual bandits are fundamental for sequential decision-making but pose significant challenges for existing neural network-based algorithms, particularly when scaling to quantum neural networks (QNNs) due to issues such as massive over-parameterization, computational instability, and the barren plateau phenomenon. This paper introduces the Quantum Neural Tangent Kernel-Upper Confidence Bound (QNTK-UCB) algorithm, a novel algorithm that leverages the Quantum Neural Tangent Kernel (QNTK) to address these limitations.
>   By freezing the QNN at a random initialization and utilizing its static QNTK as a kernel for ridge regression, QNTK-UCB bypasses the unstable training dynamics inherent in explicit parameterized quantum circuit training while fully exploiting the unique quantum inductive bias. For a time horizon $T$ and $K$ actions, our theoretical analysis reveals a significantly improved parameter scaling of $Ω((TK)^3)$ for QNTK-UCB, a substantial reduction compared to $Ω((TK)^8)$ required by classical NeuralUCB algorithms for similar regret guarantees. Empirical evaluations on non-linear synthetic benchmarks and quantum-native variational quantum eigensolver tasks demonstrate QNTK-UCB's superior sample efficiency in low-data regimes. This work highlights how the inherent properties of QNTK provide implicit regularization and a sharper spectral decay, paving the way for achieving ``quantum advantage'' in online learning.

