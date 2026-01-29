---
layout: default
title: Loss Landscape Geometry and the Learning of Symmetries: Or, What Influence Functions Reveal About Robust Generalization
---

# Loss Landscape Geometry and the Learning of Symmetries: Or, What Influence Functions Reveal About Robust Generalization
**arXiv**：[2601.20172v1](https://arxiv.org/abs/2601.20172) · [PDF](https://arxiv.org/pdf/2601.20172.pdf)  
**作者**：James Amarel, Robyn Miller, Nicolas Hengartner, Benjamin Migliori, Emily Casleton, Alexei Skurikhin, Earl Lawrence, Gerd J. Kunde  

**一句话要点**：提出基于影响函数的诊断方法，评估偏微分方程神经模拟器对物理对称性的学习机制。

**关键词**：对称性学习, 损失景观几何, 影响函数, 偏微分方程模拟器, 泛化机制, 神经网络诊断

## 3 点简述
- 核心问题：研究神经网络如何内化偏微分方程解算子的物理对称性，超越前向传递等变性测试。
- 方法要点：引入影响诊断，通过度量对称相关状态间参数更新的传播，探测损失景观的局部几何结构。
- 实验或效果：应用于自回归流体流动模拟器，证明轨道梯度相干性促进对称变换的泛化，并指示训练是否选择对称兼容盆地。

## 摘要（原文）

> We study how neural emulators of partial differential equation solution operators internalize physical symmetries by introducing an influence-based diagnostic that measures the propagation of parameter updates between symmetry-related states, defined as the metric-weighted overlap of loss gradients evaluated along group orbits. This quantity probes the local geometry of the learned loss landscape and goes beyond forward-pass equivariance tests by directly assessing whether learning dynamics couple physically equivalent configurations. Applying our diagnostic to autoregressive fluid flow emulators, we show that orbit-wise gradient coherence provides the mechanism for learning to generalize over symmetry transformations and indicates when training selects a symmetry compatible basin. The result is a novel technique for evaluating if surrogate models have internalized symmetry properties of the known solution operator.

