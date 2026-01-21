---
layout: default
title: ButterflyMoE: Sub-Linear Ternary Experts via Structured Butterfly Orbits
---

# ButterflyMoE: Sub-Linear Ternary Experts via Structured Butterfly Orbits
**arXiv**：[2601.13563v1](https://arxiv.org/abs/2601.13563) · [PDF](https://arxiv.org/pdf/2601.13563.pdf)  
**作者**：Aryan Karmore  

**一句话要点**：提出ButterflyMoE方法，通过结构化蝴蝶轨道实现子线性三元专家，以解决边缘设备上专家模型内存线性扩展问题。

**关键词**：专家混合模型, 内存压缩, 结构化参数化, 量化训练, 边缘计算, 子线性扩展

## 3 点简述
- 核心问题：线性内存扩展存储N个独立专家权重矩阵需O(N·d²)内存，超出边缘设备预算。
- 方法要点：将专家视为统一共享量化基质的几何重定向，通过学习的旋转实现子线性内存O(d² + N·d log d)。
- 实验或效果：在语言建模基准上，256专家时内存减少150倍，精度损失可忽略，使64专家适配4GB设备。

## 摘要（原文）

> Linear memory scaling stores $N$ independent expert weight matrices requiring $\mathcal{O}(N \cdot d^2)$ memory, which exceeds edge devices memory budget. Current compression methods like quantization, pruning and low-rank factorization reduce constant factors but leave the scaling bottleneck unresolved. We introduce ButterflyMoE, a method that treats experts not as independent weight matrices but as geometric reorientations of a unified shared quantized substrate. Diversity among experts arises from viewing different angles of shared capacity, not from redundant storage. By applying learned rotations to a shared ternary prototype, each expert yields $\mathcal{O}(d^2 + N \cdot d \log d)$ memory -- sub-linear in the number of experts. The key insight: training these rotations with quantization reduces activation outliers and stabilizes extreme low bit training, where static methods collapse. Across language modeling benchmarks, ButterflyMoE achieves 150 times memory reduction at 256 experts with negligible accuracy loss. This allows 64 experts to fit on 4GB devices compared to standard MoE's 8 experts, showing geometric parametrization breaks linear scaling.

