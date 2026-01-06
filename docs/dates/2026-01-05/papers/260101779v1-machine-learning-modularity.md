---
layout: default
title: Machine learning modularity
---

# Machine learning modularity
**arXiv**：[2601.01779v1](https://arxiv.org/abs/2601.01779) · [PDF](https://arxiv.org/pdf/2601.01779.pdf)  
**作者**：Yi Fan, Vishnu Jejjala, Yang Lei  

**一句话要点**：提出基于Transformer和动态批处理的机器学习框架，用于简化量子场论和弦理论中的椭圆Gamma函数表达式。

**关键词**：符号简化, 模变换, Transformer架构, 动态批处理, 量子场论计算, 弦理论工具

## 3 点简述
- 核心问题：自动简化涉及椭圆Gamma函数等特殊函数的复杂表达式，传统方法未知。
- 方法要点：结合Transformer序列到序列架构和动态批处理算法，学习应用SL(2,Z)和SL(3,Z)模变换代数恒等式。
- 实验或效果：模型在分布内测试准确率超99%，外推至更深加扰深度时保持超90%准确率，表明内化了模变换规则。

## 摘要（原文）

> Based on a transformer based sequence-to-sequence architecture combined with a dynamic batching algorithm, this work introduces a machine learning framework for automatically simplifying complex expressions involving multiple elliptic Gamma functions, including the $q$-$θ$ function and the elliptic Gamma function. The model learns to apply algebraic identities, particularly the SL$(2,\mathbb{Z})$ and SL$(3,\mathbb{Z})$ modular transformations, to reduce heavily scrambled expressions to their canonical forms. Experimental results show that the model achieves over 99\% accuracy on in-distribution tests and maintains robust performance (exceeding 90\% accuracy) under significant extrapolation, such as with deeper scrambling depths. This demonstrates that the model has internalized the underlying algebraic rules of modular transformations rather than merely memorizing training patterns. Our work presents the first successful application of machine learning to perform symbolic simplification using modular identities, offering a new automated tool for computations with special functions in quantum field theory and the string theory.

