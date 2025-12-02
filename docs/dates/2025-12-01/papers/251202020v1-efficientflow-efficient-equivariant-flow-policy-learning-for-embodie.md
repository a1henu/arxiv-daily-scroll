---
layout: default
title: EfficientFlow: Efficient Equivariant Flow Policy Learning for Embodied AI
---

# EfficientFlow: Efficient Equivariant Flow Policy Learning for Embodied AI
**arXiv**：[2512.02020v1](https://arxiv.org/abs/2512.02020) · [PDF](https://arxiv.org/pdf/2512.02020.pdf)  
**作者**：Jianlei Chang, Ruofeng Mei, Wei Ke, Xiangyu Xu  

**一句话要点**：提出EfficientFlow框架，通过等变流匹配和加速正则化，提升具身AI策略学习的数据与采样效率。

**关键词**：具身AI, 流匹配, 等变性, 策略学习, 机器人操作, 高效推理

## 3 点简述
- 现有生成策略在数据效率和采样效率上不足，需大规模演示且推理慢。
- 引入等变流匹配提升泛化性，减少数据需求；提出加速正则化策略加速采样。
- 在机器人操作基准测试中，数据有限下性能优异，推理速度大幅提升。

## 摘要（原文）

> Generative modeling has recently shown remarkable promise for visuomotor policy learning, enabling flexible and expressive control across diverse embodied AI tasks. However, existing generative policies often struggle with data inefficiency, requiring large-scale demonstrations, and sampling inefficiency, incurring slow action generation during inference. We introduce EfficientFlow, a unified framework for efficient embodied AI with flow-based policy learning. To enhance data efficiency, we bring equivariance into flow matching. We theoretically prove that when using an isotropic Gaussian prior and an equivariant velocity prediction network, the resulting action distribution remains equivariant, leading to improved generalization and substantially reduced data demands. To accelerate sampling, we propose a novel acceleration regularization strategy. As direct computation of acceleration is intractable for marginal flow trajectories, we derive a novel surrogate loss that enables stable and scalable training using only conditional trajectories. Across a wide range of robotic manipulation benchmarks, the proposed algorithm achieves competitive or superior performance under limited data while offering dramatically faster inference. These results highlight EfficientFlow as a powerful and efficient paradigm for high-performance embodied AI.

