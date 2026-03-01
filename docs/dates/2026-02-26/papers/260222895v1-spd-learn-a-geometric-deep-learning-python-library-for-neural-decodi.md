---
layout: default
title: SPD Learn: A Geometric Deep Learning Python Library for Neural Decoding Through Trivialization
---

# SPD Learn: A Geometric Deep Learning Python Library for Neural Decoding Through Trivialization
**arXiv**：[2602.22895v1](https://arxiv.org/abs/2602.22895) · [PDF](https://arxiv.org/pdf/2602.22895.pdf)  
**作者**：Bruno Aristimunha, Ce Ju, Antoine Collas, Florent Bouchard, Ammar Mian, Bertrand Thirion, Sylvain Chevallier, Reinmar Kobler  

**一句话要点**：提出SPD Learn库以解决SPD矩阵神经网络在神经解码中的碎片化问题

**关键词**：几何深度学习, SPD矩阵, 神经解码, 平凡化参数化, 脑机接口, Python库

## 3 点简述
- 核心问题：SPD矩阵神经网络实现分散，阻碍可重复性和集成到现代深度学习流程
- 方法要点：提供统一模块化库，基于平凡化参数化实现流形约束，支持标准反向传播
- 实验或效果：与脑机接口工具包集成，促进可重复基准测试和实际部署

## 摘要（原文）

> Implementations of symmetric positive definite (SPD) matrix-based neural networks for neural decoding remain fragmented across research codebases and Python packages. Existing implementations often employ ad hoc handling of manifold constraints and non-unified training setups, which hinders reproducibility and integration into modern deep-learning workflows. To address this gap, we introduce SPD Learn, a unified and modular Python package for geometric deep learning with SPD matrices. SPD Learn provides core SPD operators and neural-network layers, including numerically stable spectral operators, and enforces Stiefel/SPD constraints via trivialization-based parameterizations. This design enables standard backpropagation and optimization in unconstrained Euclidean spaces while producing manifold-constrained parameters by construction. The package also offers reference implementations of representative SPDNet-based models and interfaces with widely used brain computer interface/neuroimaging toolkits and modern machine-learning libraries (e.g., MOABB, Braindecode, Nilearn, and SKADA), facilitating reproducible benchmarking and practical deployment.

