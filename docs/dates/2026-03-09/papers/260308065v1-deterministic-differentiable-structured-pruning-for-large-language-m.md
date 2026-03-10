---
layout: default
title: Deterministic Differentiable Structured Pruning for Large Language Models
---

# Deterministic Differentiable Structured Pruning for Large Language Models
**arXiv**：[2603.08065v1](https://arxiv.org/abs/2603.08065) · [PDF](https://arxiv.org/pdf/2603.08065.pdf)  
**作者**：Weiyu Huang, Pengle Zhang, Xiaolu Zhang, Jun Zhou, Jun Zhu, Jianfei Chen  

**一句话要点**：提出确定性可微分剪枝方法以解决大语言模型结构化剪枝中的随机性问题

**关键词**：结构化剪枝, 大语言模型, 确定性优化, 可微分剪枝, 推理加速

## 3 点简述
- 核心问题：现有结构化剪枝方法使用随机松弛优化，导致训练-测试不匹配和表达受限
- 方法要点：直接优化离散l0目标的确定性软代理，消除随机性，提升表达能力和收敛速度
- 实验或效果：在Qwen3等模型上实现20%稀疏度下性能损失仅1%，优于先前方法，并展示端到端推理加速

## 摘要（原文）

> Structured pruning reduces LLM inference cost by removing low-importance architectural components. This can be viewed as learning a multiplicative gate for each component under an l0 sparsity constraint. Due to the discreteness of the l0 norm, prior work typically adopts stochastic hard-concrete relaxations to enable differentiable optimization; however, this stochasticity can introduce a train--test mismatch when sampled masks are discretized for deployment and restricts masks to a bounded, near-binary range. To address this, we propose Deterministic Differentiable Pruning (DDP), a mask-only optimization method that eliminates stochasticity by directly optimizing a deterministic soft surrogate of the discrete l0 objective. Compared with prior approaches, DDP offers greater expressiveness, reduced train--test mismatch, and faster convergence. We apply our method to several dense and MoE models, including Qwen3-32B and Qwen3-30B-A3B, achieving a performance loss as small as 1% on downstream tasks while outperforming previous methods at 20% sparsity. We further demonstrate end-to-end inference speedups in realistic deployment settings with vLLM.

