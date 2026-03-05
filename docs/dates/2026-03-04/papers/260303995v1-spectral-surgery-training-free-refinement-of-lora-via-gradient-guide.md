---
layout: default
title: Spectral Surgery: Training-Free Refinement of LoRA via Gradient-Guided Singular Value Reweighting
---

# Spectral Surgery: Training-Free Refinement of LoRA via Gradient-Guided Singular Value Reweighting
**arXiv**：[2603.03995v1](https://arxiv.org/abs/2603.03995) · [PDF](https://arxiv.org/pdf/2603.03995.pdf)  
**作者**：Zailong Tian, Yanzhe Chen, Zhuoheng Han, Lizi Liao  

**一句话要点**：提出Spectral Surgery，通过梯度引导的奇异值重加权实现训练后LoRA的无训练精炼。

**关键词**：低秩适应, 奇异值分解, 参数编辑, 训练后优化, 梯度引导, 模型精炼

## 3 点简述
- 核心问题：训练后LoRA更新常呈现低效频谱，任务效应集中于少数奇异方向，其余成分可能中性或有害。
- 方法要点：基于SVD分解LoRA更新，利用小校准集梯度估计组件敏感性，在保持方向固定下重加权奇异值。
- 实验或效果：在Llama-3.1-8B和Qwen3-8B上，Spectral Surgery在多个基准测试中带来一致提升，如CommonsenseQA提高4.4分。

## 摘要（原文）

> Low-Rank Adaptation (LoRA) improves downstream performance by restricting task updates to a low-rank parameter subspace, yet how this limited capacity is allocated within a trained adapter remains unclear. Through a geometric and empirical study across multiple tasks and backbones, we find that trained LoRA updates often exhibit an inefficient spectrum: task effects concentrate in a small subset of singular directions, while many remaining components are neutral or detrimental, motivating post-hoc refinement within the learned subspace. We propose Spectral Surgery, a training-free refinement that decomposes a LoRA update with SVD, estimates per-component sensitivity using gradients on a small calibration set, and reweights singular values under a magnitude constraint while keeping the learned directions fixed. Across Llama-3.1-8B and Qwen3-8B on four benchmarks, Spectral Surgery yields consistent gains (up to +4.4 points on CommonsenseQA and +2.4 pass@1 on HumanEval) by adjusting only $\approx 1{,}000$ scalar coefficients. These results demonstrate that SVD-structured, low-cost parameter editing can serve as a practical route to improving trained LoRA adapters in a purely post-hoc manner.

