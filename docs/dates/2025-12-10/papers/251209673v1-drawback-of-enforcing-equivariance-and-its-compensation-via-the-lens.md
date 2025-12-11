---
layout: default
title: Drawback of Enforcing Equivariance and its Compensation via the Lens of Expressive Power
---

# Drawback of Enforcing Equivariance and its Compensation via the Lens of Expressive Power
**arXiv**：[2512.09673v1](https://arxiv.org/abs/2512.09673) · [PDF](https://arxiv.org/pdf/2512.09673.pdf)  
**作者**：Yuzhu Chen, Tian Qin, Xinmei Tian, Fengxiang He, Dacheng Tao  

**一句话要点**：揭示等变网络表达力受限及其通过扩大模型规模补偿的机制

**关键词**：等变神经网络, 表达力分析, 模型规模补偿, 泛化能力, ReLU网络, 对称性编码

## 3 点简述
- 核心问题：等变约束可能严格限制神经网络的表达力，影响其性能。
- 方法要点：通过分析ReLU网络的边界超平面和通道向量，构建示例证明表达力受限。
- 实验或效果：展示扩大模型规模可补偿此缺点，且等变网络仍具较低复杂度，提升泛化能力。

## 摘要（原文）

> Equivariant neural networks encode symmetry as an inductive bias and have achieved strong empirical performance in wide domains. However, their expressive power remains not well understood. Focusing on 2-layer ReLU networks, this paper investigates the impact of equivariance constraints on the expressivity of equivariant and layer-wise equivariant networks. By examining the boundary hyperplanes and the channel vectors of ReLU networks, we construct an example showing that equivariance constraints could strictly limit expressive power. However, we demonstrate that this drawback can be compensated via enlarging the model size. Furthermore, we show that despite a larger model size, the resulting architecture could still correspond to a hypothesis space with lower complexity, implying superior generalizability for equivariant networks.

