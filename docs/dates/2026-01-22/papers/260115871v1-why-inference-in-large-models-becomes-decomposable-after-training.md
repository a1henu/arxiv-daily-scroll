---
layout: default
title: Why Inference in Large Models Becomes Decomposable After Training
---

# Why Inference in Large Models Becomes Decomposable After Training
**arXiv**：[2601.15871v1](https://arxiv.org/abs/2601.15871) · [PDF](https://arxiv.org/pdf/2601.15871.pdf)  
**作者**：Jidong Jin  

**一句话要点**：提出后训练统计准则与结构退火方法，实现大模型推理的结构化并行化

**关键词**：大模型推理, 参数依赖分析, 结构分解, 后训练优化, 并行推理

## 3 点简述
- 核心问题：大模型推理依赖稠密参数矩阵，导致成本与复杂度随模型规模不可持续增长
- 方法要点：基于梯度更新局部性，移除未支持的参数依赖，揭示稳定独立子结构
- 实验或效果：未知，但方法旨在实现结构化并行推理，不改变模型功能或接口

## 摘要（原文）

> Inference in large-scale AI models is typically performed on dense parameter matrices, leading to inference cost and system complexity that scale unsustainably with model size. This limitation does not arise from insufficient model capacity, but from treating post-training inference systems as monolithic operators while ignoring internal structures formed during learning. We show that gradient update events in large models are highly localized and selective, leaving many parameter dependencies statistically indistinguishable from their initialization distribution after training. As a result, post-training inference systems are structurally non-uniform and inherently decomposable. Based on this observation, we introduce a post-training statistical criterion and a structural annealing procedure that removes unsupported dependencies and reveals stable, independent substructures. This work establishes a post-training, model-agnostic structural view of inference systems and enables structured, parallel inference without modifying model functionality or interfaces.

