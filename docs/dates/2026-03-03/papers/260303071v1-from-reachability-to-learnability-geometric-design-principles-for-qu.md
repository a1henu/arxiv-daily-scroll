---
layout: default
title: From Reachability to Learnability: Geometric Design Principles for Quantum Neural Networks
---

# From Reachability to Learnability: Geometric Design Principles for Quantum Neural Networks
**arXiv**：[2603.03071v1](https://arxiv.org/abs/2603.03071) · [PDF](https://arxiv.org/pdf/2603.03071.pdf)  
**作者**：Vishal S. Ngairangbam, Michael Spannowsky  

**一句话要点**：提出几何设计原则以解决量子神经网络特征学习能力不足的问题。

**关键词**：量子神经网络, 几何设计, 特征学习, 数据重上传, 可控几何

## 3 点简述
- 核心问题：量子神经网络中深度或状态可达性不足以保证特征学习能力。
- 方法要点：引入CLA映射和aCLS准则，分析数据与可训练权重的联合依赖性。
- 实验或效果：数值验证CLS满足的数据重上传模型优于非可调方案，减少门操作。

## 摘要（原文）

> Classical deep networks are effective because depth enables adaptive geometric deformation of data representations. In quantum neural networks (QNNs), however, depth or state reachability alone does not guarantee this feature-learning capability. We study this question in the pure-state setting by viewing encoded data as an embedded manifold in $\mathbb{C}P^{2^n-1}$ and analysing infinitesimal unitary actions through Lie-algebra directions. We introduce Classical-to-Lie-algebra (CLA) maps and the criterion of almost Complete Local Selectivity (aCLS), which combines directional completeness with data-dependent local selectivity. Within this framework, we show that data-independent trainable unitaries are complete but non-selective, i.e. learnable rigid reorientations, whereas pure data encodings are selective but non-tunable, i.e. fixed deformations. Hence, geometric flexibility requires a non-trivial joint dependence on data and trainable weights. We further show that accessing high-dimensional deformations of many-qubit state manifolds requires parametrised entangling directions; fixed entanglers such as CNOT alone do not provide adaptive geometric control. Numerical examples validate that CLS-satisfying data re-uploading models outperform non-tunable schemes while requiring only a quarter of the gate operations. Thus, the resulting picture reframes QNN design from state reachability to controllable geometry of hidden quantum representations.

