---
layout: default
title: This Looks Distinctly Like That: Grounding Interpretable Recognition in Stiefel Geometry against Neural Collapse
---

# This Looks Distinctly Like That: Grounding Interpretable Recognition in Stiefel Geometry against Neural Collapse
**arXiv**：[2603.08374v1](https://arxiv.org/abs/2603.08374) · [PDF](https://arxiv.org/pdf/2603.08374.pdf)  
**作者**：Junhao Jia, Jiaqi Wang, Yunyou Liu, Haodong Jing, Yueyi Wu, Xian Wu, Yefeng Zheng  

**一句话要点**：提出自适应流形原型框架，在细粒度分类中通过Stiefel流形优化解决原型崩溃问题

**关键词**：原型网络, 神经崩溃, Stiefel流形, 可解释性, 细粒度分类, 黎曼优化

## 3 点简述
- 核心问题：原型网络因原型崩溃导致可解释性下降，源于神经崩溃的终端动态
- 方法要点：在Stiefel流形上使用黎曼优化表示原型为正交基，通过近端梯度学习类特定有效秩
- 实验或效果：在细粒度基准测试中实现最先进分类精度，显著提升因果忠实性

## 摘要（原文）

> Prototype networks provide an intrinsic case based explanation mechanism, but their interpretability is often undermined by prototype collapse, where multiple prototypes degenerate to highly redundant evidence. We attribute this failure mode to the terminal dynamics of Neural Collapse, where cross entropy optimization suppresses intra class variance and drives class conditional features toward a low dimensional limit. To mitigate this, we propose Adaptive Manifold Prototypes (AMP), a framework that leverages Riemannian optimization on the Stiefel manifold to represent class prototypes as orthonormal bases and make rank one prototype collapse infeasible by construction. AMP further learns class specific effective rank via a proximal gradient update on a nonnegative capacity vector, and introduces spatial regularizers that reduce rotational ambiguity and encourage localized, non overlapping part evidence. Extensive experiments on fine-grained benchmarks demonstrate that AMP achieves state-of-the-art classification accuracy while significantly improving causal faithfulness over prior interpretable models.

