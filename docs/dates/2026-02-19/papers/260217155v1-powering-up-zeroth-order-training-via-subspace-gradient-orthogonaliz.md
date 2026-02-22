---
layout: default
title: Powering Up Zeroth-Order Training via Subspace Gradient Orthogonalization
---

# Powering Up Zeroth-Order Training via Subspace Gradient Orthogonalization
**arXiv**：[2602.17155v1](https://arxiv.org/abs/2602.17155) · [PDF](https://arxiv.org/pdf/2602.17155.pdf)  
**作者**：Yicheng Lang, Changsheng Wang, Yihua Zhang, Mingyi Hong, Zheng Zhang, Wotao Yin, Sijia Liu  

**一句话要点**：提出ZO-Muon方法，通过子空间梯度正交化提升零阶优化的准确性与查询效率

**关键词**：零阶优化, 梯度估计, 子空间方法, 梯度正交化, 大模型微调, 查询效率

## 3 点简述
- 零阶优化在梯度估计中存在准确性与查询效率的权衡问题
- 结合子空间投影与梯度正交化，降低估计方差并提取谱结构
- 实验显示在LLM和ViT微调中显著加速收敛并提升性能

## 摘要（原文）

> Zeroth-order (ZO) optimization provides a gradient-free alternative to first-order (FO) methods by estimating gradients via finite differences of function evaluations, and has recently emerged as a memory-efficient paradigm for fine-tuning large-scale models by avoiding backpropagation. However, ZO optimization has a fundamental tension between accuracy and query efficiency. In this work, we show that ZO optimization can be substantially improved by unifying two complementary principles: (i) a projection-based subspace view that reduces gradient estimation variance by exploiting the intrinsic low-rank structure of model updates, and (ii) Muon-style spectral optimization that applies gradient orthogonalization to extract informative spectral structure from noisy ZO gradients. These findings form a unified framework of subspace gradient orthogonalization, which we instantiate in a new method, ZO-Muon, admitting a natural interpretation as a low-rank Muon optimizer in the ZO setting. Extensive experiments on large language models (LLMs) and vision transformers (ViTs) demonstrate that ZO-Muon significantly accelerates convergence and achieves a win-win improvement in accuracy and query/runtime efficiency. Notably, compared to the popular MeZO baseline, ZO-Muon requires only 24.7% of the queries to reach the same SST-2 performance for LLM fine-tuning, and improves accuracy by 25.1% on ViT-B fine-tuning on CIFAR-100.

