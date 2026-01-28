---
layout: default
title: Smoothing the Score Function for Generalization in Diffusion Models: An Optimization-based Explanation Framework
---

# Smoothing the Score Function for Generalization in Diffusion Models: An Optimization-based Explanation Framework
**arXiv**：[2601.19285v1](https://arxiv.org/abs/2601.19285) · [PDF](https://arxiv.org/pdf/2601.19285.pdf)  
**作者**：Xinyu Zhou, Jiawei Zhang, Stephen J. Wright  

**一句话要点**：提出噪声无条件化和温度平滑方法以解决扩散模型中的记忆化问题

**关键词**：扩散模型, 记忆化问题, 分数函数平滑, 泛化增强, 优化框架

## 3 点简述
- 核心问题：扩散模型存在记忆化现象，生成样本可能精确复制训练样本，源于经验分数函数的结构导致单点主导
- 方法要点：理论框架解释记忆化，并提出噪声无条件化和温度平滑来平滑分数函数，增强泛化
- 实验或效果：多数据集实验验证理论分析，新方法在保持高质量生成的同时有效改善泛化

## 摘要（原文）

> Diffusion models achieve remarkable generation quality, yet face a fundamental challenge known as memorization, where generated samples can replicate training samples exactly. We develop a theoretical framework to explain this phenomenon by showing that the empirical score function (the score function corresponding to the empirical distribution) is a weighted sum of the score functions of Gaussian distributions, in which the weights are sharp softmax functions. This structure causes individual training samples to dominate the score function, resulting in sampling collapse. In practice, approximating the empirical score function with a neural network can partially alleviate this issue and improve generalization. Our theoretical framework explains why: In training, the neural network learns a smoother approximation of the weighted sum, allowing the sampling process to be influenced by local manifolds rather than single points. Leveraging this insight, we propose two novel methods to further enhance generalization: (1) Noise Unconditioning enables each training sample to adaptively determine its score function weight to increase the effect of more training samples, thereby preventing single-point dominance and mitigating collapse. (2) Temperature Smoothing introduces an explicit parameter to control the smoothness. By increasing the temperature in the softmax weights, we naturally reduce the dominance of any single training sample and mitigate memorization. Experiments across multiple datasets validate our theoretical analysis and demonstrate the effectiveness of the proposed methods in improving generalization while maintaining high generation quality.

