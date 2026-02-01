---
layout: default
title: Mixed-Precision Training and Compilation for RRAM-based Computing-in-Memory Accelerators
---

# Mixed-Precision Training and Compilation for RRAM-based Computing-in-Memory Accelerators
**arXiv**：[2601.21737v1](https://arxiv.org/abs/2601.21737) · [PDF](https://arxiv.org/pdf/2601.21737.pdf)  
**作者**：Rebecca Pelke, Joel Klein, Jose Cubero-Cascante, Nils Bosbach, Jan Moritz Joseph, Rainer Leupers  

**一句话要点**：提出混合精度训练与编译框架以解决RRAM存内计算加速器量化效率问题

**关键词**：存内计算, 混合精度训练, 强化学习, 量化优化, RRAM加速器, 编译框架

## 3 点简述
- 核心问题：存内计算加速器因量化位宽受限，导致矩阵向量乘法计算周期多且权重存储效率低。
- 方法要点：采用强化学习策略搜索量化配置，平衡延迟与精度，优化混合精度训练与编译。
- 实验或效果：在最佳情况下，相比现有方案实现2.48倍加速，精度损失仅0.086%。

## 摘要（原文）

> Computing-in-Memory (CIM) accelerators are a promising solution for accelerating Machine Learning (ML) workloads, as they perform Matrix-Vector Multiplications (MVMs) on crossbar arrays directly in memory. Although the bit widths of the crossbar inputs and cells are very limited, most CIM compilers do not support quantization below 8 bit. As a result, a single MVM requires many compute cycles, and weights cannot be efficiently stored in a single crossbar cell. To address this problem, we propose a mixed-precision training and compilation framework for CIM architectures. The biggest challenge is the massive search space, that makes it difficult to find good quantization parameters. This is why we introduce a reinforcement learning-based strategy to find suitable quantization configurations that balance latency and accuracy. In the best case, our approach achieves up to a 2.48x speedup over existing state-of-the-art solutions, with an accuracy loss of only 0.086 %.

