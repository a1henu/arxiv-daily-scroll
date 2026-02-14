---
layout: default
title: ArGEnT: Arbitrary Geometry-encoded Transformer for Operator Learning
---

# ArGEnT: Arbitrary Geometry-encoded Transformer for Operator Learning
**arXiv**：[2602.11626v1](https://arxiv.org/abs/2602.11626) · [PDF](https://arxiv.org/pdf/2602.11626.pdf)  
**作者**：Wenqian Chen, Yucheng Fu, Michael Penwarden, Pratanu Roy, Panos Stinis  

**一句话要点**：提出ArGEnT以解决复杂几何下算子学习的泛化与灵活评估问题

**关键词**：算子学习, 几何编码, Transformer注意力, 点云表示, 代理建模, 科学机器学习

## 3 点简述
- 核心问题：学习复杂几何和参数物理系统的解算子，需跨几何泛化并在任意空间位置评估
- 方法要点：基于Transformer注意力机制，通过点云表示编码几何信息，集成到DeepONet作为主干网络
- 实验或效果：在流体动力学、固体力学和电化学系统基准测试中，相比标准DeepONet和其他几何感知代理，预测精度和泛化性能显著提升

## 摘要（原文）

> Learning solution operators for systems with complex, varying geometries and parametric physical settings is a central challenge in scientific machine learning. In many-query regimes such as design optimization, control and inverse problems, surrogate modeling must generalize across geometries while allowing flexible evaluation at arbitrary spatial locations. In this work, we propose Arbitrary Geometry-encoded Transformer (ArGEnT), a geometry-aware attention-based architecture for operator learning on arbitrary domains. ArGEnT employs Transformer attention mechanisms to encode geometric information directly from point-cloud representations with three variants-self-attention, cross-attention, and hybrid-attention-that incorporates different strategies for incorporating geometric features. By integrating ArGEnT into DeepONet as the trunk network, we develop a surrogate modeling framework capable of learning operator mappings that depend on both geometric and non-geometric inputs without the need to explicitly parametrize geometry as a branch network input. Evaluation on benchmark problems spanning fluid dynamics, solid mechanics and electrochemical systems, we demonstrate significantly improved prediction accuracy and generalization performance compared with the standard DeepONet and other existing geometry-aware saurrogates. In particular, the cross-attention transformer variant enables accurate geometry-conditioned predictions with reduced reliance on signed distance functions. By combining flexible geometry encoding with operator-learning capabilities, ArGEnT provides a scalable surrogate modeling framework for optimization, uncertainty quantification, and data-driven modeling of complex physical systems.

