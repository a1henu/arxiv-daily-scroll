---
layout: default
title: Convergence for Discrete Parameter Updates
---

# Convergence for Discrete Parameter Updates
**arXiv**：[2512.04051v1](https://arxiv.org/abs/2512.04051) · [PDF](https://arxiv.org/pdf/2512.04051.pdf)  
**作者**：Paul Wilson, Fabio Zanasi, George Constantinides  

**一句话要点**：提出离散参数更新方法以解决低精度训练中的量化问题

**关键词**：低精度训练, 离散参数更新, 收敛保证, 多项更新规则, 高效训练, 深度学习优化

## 3 点简述
- 核心问题：现代深度学习模型计算需求大，低精度训练依赖连续更新的量化，可能引入误差
- 方法要点：设计更新规则本身为离散，避免量化连续更新，提供收敛保证，并以多项更新为例
- 实验或效果：通过实证评估支持离散更新规则，为高效训练开辟新途径，尤其适用于离散结构模型

## 摘要（原文）

> Modern deep learning models require immense computational resources, motivating research into low-precision training. Quantised training addresses this by representing training components in low-bit integers, but typically relies on discretising real-valued updates. We introduce an alternative approach where the update rule itself is discrete, avoiding the quantisation of continuous updates by design. We establish convergence guarantees for a general class of such discrete schemes, and present a multinomial update rule as a concrete example, supported by empirical evaluation. This perspective opens new avenues for efficient training, particularly for models with inherently discrete structure.

