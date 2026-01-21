---
layout: default
title: A universal linearized subspace refinement framework for neural networks
---

# A universal linearized subspace refinement framework for neural networks
**arXiv**：[2601.13989v1](https://arxiv.org/abs/2601.13989) · [PDF](https://arxiv.org/pdf/2601.13989.pdf)  
**作者**：Wenbo Cao, Weiwei Zhang  

**一句话要点**：提出线性化子空间精炼框架，提升神经网络在监督学习和算子学习中的预测精度。

**关键词**：线性化子空间精炼, 神经网络优化, 雅可比残差模型, 监督学习, 算子学习, 数值病态性

## 3 点简述
- 核心问题：梯度训练常无法达到模型表达能力内的最佳精度，数值病态性是主要瓶颈。
- 方法要点：利用固定网络状态的雅可比线性残差模型，通过子空间最小二乘求解优化预测。
- 实验或效果：在多个任务中实现误差数量级降低，无需修改网络架构或训练过程。

## 摘要（原文）

> Neural networks are predominantly trained using gradient-based methods, yet in many applications their final predictions remain far from the accuracy attainable within the model's expressive capacity. We introduce Linearized Subspace Refinement (LSR), a general and architecture-agnostic framework that exploits the Jacobian-induced linear residual model at a fixed trained network state. By solving a reduced direct least-squares problem within this subspace, LSR computes a subspace-optimal solution of the linearized residual model, yielding a refined linear predictor with substantially improved accuracy over standard gradient-trained solutions, without modifying network architectures, loss formulations, or training procedures. Across supervised function approximation, data-driven operator learning, and physics-informed operator fine-tuning, we show that gradient-based training often fails to access this attainable accuracy, even when local linearization yields a convex problem. This observation indicates that loss-induced numerical ill-conditioning, rather than nonconvexity or model expressivity, can constitute a dominant practical bottleneck. In contrast, one-shot LSR systematically exposes accuracy levels not fully exploited by gradient-based training, frequently achieving order-of-magnitude error reductions. For operator-constrained problems with composite loss structures, we further introduce Iterative LSR, which alternates one-shot LSR with supervised nonlinear alignment, transforming ill-conditioned residual minimization into numerically benign fitting steps and yielding accelerated convergence and improved accuracy. By bridging nonlinear neural representations with reduced-order linear solvers at fixed linearization points, LSR provides a numerically grounded and broadly applicable refinement framework for supervised learning, operator learning, and scientific computing.

