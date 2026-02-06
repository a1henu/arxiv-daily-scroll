---
layout: default
title: Steering Large Reasoning Models towards Concise Reasoning via Flow Matching
---

# Steering Large Reasoning Models towards Concise Reasoning via Flow Matching
**arXiv**：[2602.05539v1](https://arxiv.org/abs/2602.05539) · [PDF](https://arxiv.org/pdf/2602.05539.pdf)  
**作者**：Yawei Li, Benjamin Bergner, Yinghan Zhao, Vihang Prakash Patil, Bei Chen, Cheng Wang  

**一句话要点**：提出FlowSteer方法，通过流匹配学习非线性变换，以引导大型推理模型生成简洁推理输出。

**关键词**：大型推理模型, 流匹配, 非线性引导, 推理效率, 分布对齐

## 3 点简述
- 核心问题：大型推理模型输出冗长，现有线性引导方法受限于线性表示假设，效率低下。
- 方法要点：引入FlowSteer，基于流匹配学习从冗长到简洁推理分布的完整非线性变换，实现输入依赖的精确控制。
- 实验或效果：在多样化推理基准测试中，FlowSteer相比领先推理时基线，展现出强任务性能和更高的标记效率。

## 摘要（原文）

> Large Reasoning Models (LRMs) excel at complex reasoning tasks, but their efficiency is often hampered by overly verbose outputs. Prior steering methods attempt to address this issue by applying a single, global vector to hidden representations -- an approach grounded in the restrictive linear representation hypothesis. In this work, we introduce FlowSteer, a nonlinear steering method that goes beyond uniform linear shifts by learning a complete transformation between the distributions associated with verbose and concise reasoning. This transformation is learned via Flow Matching as a velocity field, enabling precise, input-dependent control over the model's reasoning process. By aligning steered representations with the distribution of concise-reasoning activations, FlowSteer yields more compact reasoning than the linear shifts. Across diverse reasoning benchmarks, FlowSteer demonstrates strong task performance and token efficiency compared to leading inference-time baselines. Our work demonstrates that modeling the full distributional transport with generative techniques offers a more effective and principled foundation for controlling LRMs.

