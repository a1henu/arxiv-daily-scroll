---
layout: default
title: HiFi-Mesh: High-Fidelity Efficient 3D Mesh Generation via Compact Autoregressive Dependence
---

# HiFi-Mesh: High-Fidelity Efficient 3D Mesh Generation via Compact Autoregressive Dependence
**arXiv**：[2601.21314v1](https://arxiv.org/abs/2601.21314) · [PDF](https://arxiv.org/pdf/2601.21314.pdf)  
**作者**：Yanfeng Li, Tao Tan, Qingquan Gao, Zhiwen Cao, Xiaohong liu, Yue Sun  

**一句话要点**：提出LANE和AdaGraph以高效生成高保真3D网格，解决现有方法序列长度受限和推理慢的问题。

**关键词**：3D网格生成, 自回归模型, 高效推理, 序列建模, 几何一致性

## 3 点简述
- 核心问题：现有自回归方法资源利用不足，序列长度受限且推理慢，影响3D网格细节表达。
- 方法要点：引入LANE通过紧凑自回归依赖扩展序列长度，AdaGraph通过时空解耦加速推理。
- 实验或效果：LANE序列长度提升6倍，AdaGraph优化效率，实验验证在速度、细节和几何一致性上表现优越。

## 摘要（原文）

> High-fidelity 3D meshes can be tokenized into one-dimension (1D) sequences and directly modeled using autoregressive approaches for faces and vertices. However, existing methods suffer from insufficient resource utilization, resulting in slow inference and the ability to handle only small-scale sequences, which severely constrains the expressible structural details. We introduce the Latent Autoregressive Network (LANE), which incorporates compact autoregressive dependencies in the generation process, achieving a $6\times$ improvement in maximum generatable sequence length compared to existing methods. To further accelerate inference, we propose the Adaptive Computation Graph Reconfiguration (AdaGraph) strategy, which effectively overcomes the efficiency bottleneck of traditional serial inference through spatiotemporal decoupling in the generation process. Experimental validation demonstrates that LANE achieves superior performance across generation speed, structural detail, and geometric consistency, providing an effective solution for high-quality 3D mesh generation.

