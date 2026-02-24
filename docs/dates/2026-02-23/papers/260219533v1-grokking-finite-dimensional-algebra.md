---
layout: default
title: Grokking Finite-Dimensional Algebra
---

# Grokking Finite-Dimensional Algebra
**arXiv**：[2602.19533v1](https://arxiv.org/abs/2602.19533) · [PDF](https://arxiv.org/pdf/2602.19533.pdf)  
**作者**：Pascal Jr Tikeng Notsawo, Guillaume Dumas, Guillaume Rabusseau  

**一句话要点**：提出有限维代数学习框架，统一分析神经网络训练中的顿悟现象

**关键词**：顿悟现象, 有限维代数, 神经网络泛化, 结构张量, 矩阵分解, 离散表示学习

## 3 点简述
- 研究有限维代数乘法学习中的顿悟现象，扩展至非结合、非交换、非单位代数
- 将学习问题关联到矩阵分解与低秩偏置，或有限域上的离散表示学习
- 实验探究代数性质、结构张量特征与潜在嵌入对齐对顿悟的影响

## 摘要（原文）

> This paper investigates the grokking phenomenon, which refers to the sudden transition from a long memorization to generalization observed during neural networks training, in the context of learning multiplication in finite-dimensional algebras (FDA). While prior work on grokking has focused mainly on group operations, we extend the analysis to more general algebraic structures, including non-associative, non-commutative, and non-unital algebras. We show that learning group operations is a special case of learning FDA, and that learning multiplication in FDA amounts to learning a bilinear product specified by the algebra's structure tensor. For algebras over the reals, we connect the learning problem to matrix factorization with an implicit low-rank bias, and for algebras over finite fields, we show that grokking emerges naturally as models must learn discrete representations of algebraic elements. This leads us to experimentally investigate the following core questions: (i) how do algebraic properties such as commutativity, associativity, and unitality influence both the emergence and timing of grokking, (ii) how structural properties of the structure tensor of the FDA, such as sparsity and rank, influence generalization, and (iii) to what extent generalization correlates with the model learning latent embeddings aligned with the algebra's representation. Our work provides a unified framework for grokking across algebraic structures and new insights into how mathematical structure governs neural network generalization dynamics.

