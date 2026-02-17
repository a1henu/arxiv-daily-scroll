---
layout: default
title: Scale redundancy and soft gauge fixing in positively homogeneous neural networks
---

# Scale redundancy and soft gauge fixing in positively homogeneous neural networks
**arXiv**：[2602.14729v1](https://arxiv.org/abs/2602.14729) · [PDF](https://arxiv.org/pdf/2602.14729.pdf)  
**作者**：Rodrigo Carmo Terin  

**一句话要点**：提出软规范固定方法以优化正齐次神经网络的训练稳定性与效率

**关键词**：正齐次神经网络, 规范冗余, 软规范固定, 优化条件, 尺度平衡, 机器学习理论

## 3 点简述
- 正齐次激活神经网络存在连续重参数化对称性，导致参数空间冗余
- 引入规范适应坐标分离不变与尺度失衡方向，并设计软轨道选择功能
- 实验表明该方法扩展稳定学习率范围并抑制尺度漂移，不改变表达能力

## 摘要（原文）

> Neural networks with positively homogeneous activations exhibit an exact continuous reparametrization symmetry: neuron-wise rescalings generate parameter-space orbits along which the input--output function is invariant. We interpret this symmetry as a gauge redundancy and introduce gauge-adapted coordinates that separate invariant and scale-imbalance directions. Inspired by gauge fixing in field theory, we introduce a soft orbit-selection (norm-balancing) functional acting only on redundant scale coordinates. We show analytically that it induces dissipative relaxation of imbalance modes to preserve the realized function. In controlled experiments, this orbit-selection penalty expands the stable learning-rate regime and suppresses scale drift without changing expressivity. These results establish a structural link between gauge-orbit geometry and optimization conditioning, providing a concrete connection between gauge-theoretic concepts and machine learning.

