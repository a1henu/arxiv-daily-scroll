---
layout: default
title: Towards Principled Design of Mixture-of-Experts Language Models under Memory and Inference Constraints
---

# Towards Principled Design of Mixture-of-Experts Language Models under Memory and Inference Constraints
**arXiv**：[2601.08215v1](https://arxiv.org/abs/2601.08215) · [PDF](https://arxiv.org/pdf/2601.08215.pdf)  
**作者**：Seng Pei Liew, Kenta Shinzato, Yuyang Dong  

**一句话要点**：提出基于总参数与专家稀疏度的MoE设计原则，以解决内存与推理约束下的架构优化问题。

**关键词**：混合专家模型, 内存约束, 推理成本, 架构设计, 参数优化, 稀疏性

## 3 点简述
- 核心问题：现有MoE模型仅依赖总参数和激活参数，不足以描述最优架构。
- 方法要点：通过系统研究，发现性能主要由总参数和专家稀疏度决定，提出最大化总参数、最小化稀疏度的设计原则。
- 实验或效果：研究表明，专家数量增加会轻微损害性能，需在约束下平衡核心模型维度。

## 摘要（原文）

> Modern Mixture-of-Experts (MoE) language models are designed based on total parameters (memory footprint) and active parameters (inference cost). However, we find these two factors alone are insufficient to describe an optimal architecture. Through a systematic study, we demonstrate that MoE performance is primarily determined by total parameters ($N_{total}$) and expert sparsity ($s:=n_{exp}/n_{topk}$).
>   Moreover, $n_{exp}$ and $n_{topk}$ do not "cancel out" within the sparsity ratio; instead, a larger total number of experts slightly penalizes performance by forcing a reduction in core model dimensions (depth and width) to meet memory constraints. This motivates a simple principle for MoE design which maximizes $N_{total}$ while minimizing $s$ (maximizing $n_{topk}$) and $n_{exp}$ under the given constraints. Our findings provide a robust framework for resolving architectural ambiguity and guiding MoE design.

