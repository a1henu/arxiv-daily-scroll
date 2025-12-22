---
layout: default
title: More Consistent Accuracy PINN via Alternating Easy-Hard Training
---

# More Consistent Accuracy PINN via Alternating Easy-Hard Training
**arXiv**：[2512.17607v1](https://arxiv.org/abs/2512.17607) · [PDF](https://arxiv.org/pdf/2512.17607.pdf)  
**作者**：Zhaoqian Gao, Min Yanga  

**一句话要点**：提出交替难易训练策略以提升PINN在复杂PDE求解中的一致性与准确性

**关键词**：物理信息神经网络, 偏微分方程求解, 交替训练, 混合策略, 训练优化

## 3 点简述
- 核心问题：PINN训练策略存在性能不一致性，难易优先方法各有优劣
- 方法要点：开发交替训练算法，结合难易优先优势，形成混合策略
- 实验或效果：在陡峭梯度、非线性、高维PDE上实现高精度，相对L2误差达O(10^-5)至O(10^-6)

## 摘要（原文）

> Physics-informed neural networks (PINNs) have recently emerged as a prominent paradigm for solving partial differential equations (PDEs), yet their training strategies remain underexplored. While hard prioritization methods inspired by finite element methods are widely adopted, recent research suggests that easy prioritization can also be effective. Nevertheless, we find that both approaches exhibit notable trade-offs and inconsistent performance across PDE types. To address this issue, we develop a hybrid strategy that combines the strengths of hard and easy prioritization through an alternating training algorithm. On PDEs with steep gradients, nonlinearity, and high dimensionality, the proposed method achieves consistently high accuracy, with relative L2 errors mostly in the range of O(10^-5) to O(10^-6), significantly surpassing baseline methods. Moreover, it offers greater reliability across diverse problems, whereas compared approaches often suffer from variable accuracy depending on the PDE. This work provides new insights into designing hybrid training strategies to enhance the performance and robustness of PINNs.

