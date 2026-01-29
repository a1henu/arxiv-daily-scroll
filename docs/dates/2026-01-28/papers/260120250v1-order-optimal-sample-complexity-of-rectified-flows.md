---
layout: default
title: Order-Optimal Sample Complexity of Rectified Flows
---

# Order-Optimal Sample Complexity of Rectified Flows
**arXiv**：[2601.20250v1](https://arxiv.org/abs/2601.20250) · [PDF](https://arxiv.org/pdf/2601.20250.pdf)  
**作者**：Hari Krishna Sahoo, Mudit Gaur, Vaneet Aggarwal  

**一句话要点**：提出整流流模型，在标准假设下实现样本复杂度最优阶O(ε^{-2})，加速生成过程。

**关键词**：整流流模型, 样本复杂度, 生成模型, 流匹配, Rademacher复杂度, 线性传输轨迹

## 3 点简述
- 研究整流流模型，其约束传输轨迹从基分布到数据分布为线性，以加速采样。
- 在神经网络参数化速度场和数据分布的标准假设下，证明样本复杂度为O(ε^{-2})，优于流匹配模型。
- 分析利用整流流结构，平方损失沿线性路径训练，假设类局部Rademacher复杂度受控，解释其强实证性能。

## 摘要（原文）

> Recently, flow-based generative models have shown superior efficiency compared to diffusion models. In this paper, we study rectified flow models, which constrain transport trajectories to be linear from the base distribution to the data distribution. This structural restriction greatly accelerates sampling, often enabling high-quality generation with a single Euler step. Under standard assumptions on the neural network classes used to parameterize the velocity field and data distribution, we prove that rectified flows achieve sample complexity $\tilde{O}(\varepsilon^{-2})$. This improves on the best known $O(\varepsilon^{-4})$ bounds for flow matching model and matches the optimal rate for mean estimation. Our analysis exploits the particular structure of rectified flows: because the model is trained with a squared loss along linear paths, the associated hypothesis class admits a sharply controlled localized Rademacher complexity. This yields the improved, order-optimal sample complexity and provides a theoretical explanation for the strong empirical performance of rectified flow models.

