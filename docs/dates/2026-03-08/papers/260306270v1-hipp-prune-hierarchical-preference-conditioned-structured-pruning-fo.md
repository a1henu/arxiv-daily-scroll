---
layout: default
title: HiPP-Prune: Hierarchical Preference-Conditioned Structured Pruning for Vision-Language Models
---

# HiPP-Prune: Hierarchical Preference-Conditioned Structured Pruning for Vision-Language Models
**arXiv**：[2603.06270v1](https://arxiv.org/abs/2603.06270) · [PDF](https://arxiv.org/pdf/2603.06270.pdf)  
**作者**：Lincen Bai, Hedi Tabia, Raul Santos-Rodriguez  

**一句话要点**：提出HiPP-Prune框架，通过分层偏好条件结构化剪枝解决视觉语言模型压缩中的幻觉问题。

**关键词**：视觉语言模型剪枝, 结构化剪枝, 多目标优化, 幻觉抑制, 资源分配, 策略优化

## 3 点简述
- 核心问题：视觉语言模型剪枝易导致任务效用下降和视觉基础弱化，加剧对象幻觉。
- 方法要点：采用分层策略，基于用户偏好向量生成全局剪枝蓝图，整合视觉敏感信号优化层间资源分配。
- 实验或效果：在LLaVA模型上验证，实现可控的鲁棒性-效用权衡，发现多样非支配剪枝计划。

## 摘要（原文）

> Pruning vision-language models (VLMs) for efficient deployment is challenging because compression can affect not only task utility but also visual grounding, often amplifying object hallucinations even at the same sparsity level. We present HiPP-Prune, a hierarchical preference-conditioned structured pruning framework that treats pruning as conditional resource allocation under multiple objectives. HiPP-Prune makes plan-level decisions: a single policy invocation outputs a global pruning blueprint by factorizing decisions into an overall sparsity budget and a layer-wise allocation, enabling queryable trade-offs via a user-specified preference vector. To account for VLM-specific failure modes, our policy state integrates a visual sensitivity signal derived from attention flow between vision tokens and language hidden states, discouraging over-pruning of vision-critical layers that facilitate cross-modal fusion. We optimize pruning plans with plan-level Group Relative Policy Optimization (GRPO) under a multi-objective return that combines task utility, hallucination robustness (POPE), compression, and a synaptic-flow-inspired stability proxy to reduce unproductive exploration in high-sparsity regimes. Experiments on LLaVA with POPE and ScienceQA demonstrate that HiPP-Prune discovers diverse non-dominated pruning plans and provides controllable robustness--utility trade-offs under matched sparsity budgets.

