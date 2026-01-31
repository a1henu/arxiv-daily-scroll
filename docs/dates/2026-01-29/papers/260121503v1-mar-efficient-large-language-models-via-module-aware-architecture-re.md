---
layout: default
title: MAR: Efficient Large Language Models via Module-aware Architecture Refinement
---

# MAR: Efficient Large Language Models via Module-aware Architecture Refinement
**arXiv**：[2601.21503v1](https://arxiv.org/abs/2601.21503) · [PDF](https://arxiv.org/pdf/2601.21503.pdf)  
**作者**：Junhong Cai, Guiqin Wang, Kejie Zhao, Jianxiong Tang, Xiang Wang, Luziwei Leng, Ran Cheng, Yuxin Ma, Qinghai Guo  

**一句话要点**：提出模块感知架构精炼以降低大语言模型能耗，集成状态空间模型与激活稀疏化。

**关键词**：大语言模型, 状态空间模型, 激活稀疏化, 尖峰神经网络, 能量效率, 架构优化

## 3 点简述
- 核心问题：大语言模型因二次注意力与密集前馈网络导致高能耗。
- 方法要点：两阶段框架集成状态空间模型实现线性序列建模，并应用激活稀疏化减少前馈网络成本。
- 实验或效果：在受限资源下有效恢复密集模型性能，显著降低推理能耗，优于可比规模高效模型。

## 摘要（原文）

> Large Language Models (LLMs) excel across diverse domains but suffer from high energy costs due to quadratic attention and dense Feed-Forward Network (FFN) operations. To address these issues, we propose Module-aware Architecture Refinement (MAR), a two-stage framework that integrates State Space Models (SSMs) for linear-time sequence modeling and applies activation sparsification to reduce FFN costs. In addition, to mitigate low information density and temporal mismatch in integrating Spiking Neural Networks (SNNs) with SSMs, we design the Adaptive Ternary Multi-step Neuron (ATMN) and the Spike-aware Bidirectional Distillation Strategy (SBDS). Extensive experiments demonstrate that MAR effectively restores the performance of its dense counterpart under constrained resources while substantially reducing inference energy consumption. Furthermore, it outperforms efficient models of comparable or even larger scale, underscoring its potential for building efficient and practical LLMs.

