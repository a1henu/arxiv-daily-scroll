---
layout: default
title: Breaking Symmetry Bottlenecks in GNN Readouts
---

# Breaking Symmetry Bottlenecks in GNN Readouts
**arXiv**：[2602.05950v1](https://arxiv.org/abs/2602.05950) · [PDF](https://arxiv.org/pdf/2602.05950.pdf)  
**作者**：Mouad Talhi, Arne Wolf, Anthea Monod  

**一句话要点**：提出投影器不变读出以解决图神经网络中线性不变读出的对称性瓶颈问题

**关键词**：图神经网络, 对称性瓶颈, 读出设计, 置换不变性, 表示理论, 图分类

## 3 点简述
- 核心问题：线性置换不变读出（如求和池化）会擦除非平凡对称感知信息，限制GNN表达能力
- 方法要点：基于有限维表示理论，设计投影器不变读出，分解节点表示并保留对称感知通道
- 实验或效果：仅替换读出即可分离WL难图对，提升多个基准测试性能

## 摘要（原文）

> Graph neural networks (GNNs) are widely used for learning on structured data, yet their ability to distinguish non-isomorphic graphs is fundamentally limited. These limitations are usually attributed to message passing; in this work we show that an independent bottleneck arises at the readout stage. Using finite-dimensional representation theory, we prove that all linear permutation-invariant readouts, including sum and mean pooling, factor through the Reynolds (group-averaging) operator and therefore project node embeddings onto the fixed subspace of the permutation action, erasing all non-trivial symmetry-aware components regardless of encoder expressivity. This yields both a new expressivity barrier and an interpretable characterization of what global pooling preserves or destroys. To overcome this collapse, we introduce projector-based invariant readouts that decompose node representations into symmetry-aware channels and summarize them with nonlinear invariant statistics, preserving permutation invariance while retaining information provably invisible to averaging. Empirically, swapping only the readout enables fixed encoders to separate WL-hard graph pairs and improves performance across multiple benchmarks, demonstrating that readout design is a decisive and under-appreciated factor in GNN expressivity.

