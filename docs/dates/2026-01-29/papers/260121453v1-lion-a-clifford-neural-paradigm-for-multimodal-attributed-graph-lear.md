---
layout: default
title: LION: A Clifford Neural Paradigm for Multimodal-Attributed Graph Learning
---

# LION: A Clifford Neural Paradigm for Multimodal-Attributed Graph Learning
**arXiv**：[2601.21453v1](https://arxiv.org/abs/2601.21453) · [PDF](https://arxiv.org/pdf/2601.21453.pdf)  
**作者**：Xunkai Li, Zhengyu Wu, Zekai Chen, Henan Sun, Daohan Su, Guang Zeng, Hongchao Qin, Rong-Hua Li, Guoren Wang  

**一句话要点**：提出基于Clifford代数的LION范式，以解决多模态属性图中的模态对齐与融合问题。

**关键词**：多模态属性图, Clifford代数, 模态对齐, 模态融合, 图神经网络, 下游任务

## 3 点简述
- 核心问题：现有方法在模态对齐中忽视图上下文，在模态融合中缺乏适应性，导致性能受限。
- 方法要点：利用Clifford代数构建几何流形进行高阶图传播，实现模态对齐；基于几何等级属性设计自适应全息聚合，优化模态融合。
- 实验或效果：在9个数据集上验证，LION在3种图和3种模态下游任务中显著优于现有方法。

## 摘要（原文）

> Recently, the rapid advancement of multimodal domains has driven a data-centric paradigm shift in graph ML, transitioning from text-attributed to multimodal-attributed graphs. This advancement significantly enhances data representation and expands the scope of graph downstream tasks, such as modality-oriented tasks, thereby improving the practical utility of graph ML. Despite its promise, limitations exist in the current neural paradigms: (1) Neglect Context in Modality Alignment: Most existing methods adopt topology-constrained or modality-specific operators as tokenizers. These aligners inevitably neglect graph context and inhibit modality interaction, resulting in suboptimal alignment. (2) Lack of Adaptation in Modality Fusion: Most existing methods are simple adaptations for 2-modality graphs and fail to adequately exploit aligned tokens equipped with topology priors during fusion, leading to poor generalizability and performance degradation. To address the above issues, we propose LION (c\underline{LI}ff\underline{O}rd \underline{N}eural paradigm) based on the Clifford algebra and decoupled graph neural paradigm (i.e., propagation-then-aggregation) to implement alignment-then-fusion in multimodal-attributed graphs. Specifically, we first construct a modality-aware geometric manifold grounded in Clifford algebra. This geometric-induced high-order graph propagation efficiently achieves modality interaction, facilitating modality alignment. Then, based on the geometric grade properties of aligned tokens, we propose adaptive holographic aggregation. This module integrates the energy and scale of geometric grades with learnable parameters to improve modality fusion. Extensive experiments on 9 datasets demonstrate that LION significantly outperforms SOTA baselines across 3 graph and 3 modality downstream tasks.

