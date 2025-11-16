---
layout: default
title: Enhancing the Outcome Reward-based RL Training of MLLMs with Self-Consistency Sampling
---

# Enhancing the Outcome Reward-based RL Training of MLLMs with Self-Consistency Sampling
**arXiv**：[2511.10648v1](https://arxiv.org/abs/2511.10648) · [PDF](https://arxiv.org/pdf/2511.10648.pdf)  
**作者**：Jiahao Wang, Weiye Xu, Aijun Yang, Wengang Zhou, Lewei Lu, Houqiang Li, Xiaohua Wang, Jinguo Zhu  

**一句话要点**：提出自一致性采样以解决多模态大模型中基于结果奖励强化学习的不可靠轨迹问题

**关键词**：多模态大语言模型, 强化学习, 自一致性采样, 结果奖励, 多模态推理, 轨迹可靠性

## 3 点简述
- 核心问题：多模态推理中，错误思维链但猜对选项的轨迹获得相同奖励，影响训练忠实性。
- 方法要点：通过视觉扰动和轨迹截断重采样，计算一致性分数，在策略更新中降低不可靠轨迹权重。
- 实验或效果：在多个基准上提升准确率高达7.7个百分点，计算开销可忽略，适用于不同模型。

## 摘要（原文）

> Outcome-reward reinforcement learning (RL) is a common and increasingly significant way to refine the step-by-step reasoning of multimodal large language models (MLLMs). In the multiple-choice setting - a dominant format for multimodal reasoning benchmarks - the paradigm faces a significant yet often overlooked obstacle: unfaithful trajectories that guess the correct option after a faulty chain of thought receive the same reward as genuine reasoning, which is a flaw that cannot be ignored. We propose Self-Consistency Sampling (SCS) to correct this issue. For each question, SCS (i) introduces small visual perturbations and (ii) performs repeated truncation and resampling of an initial trajectory; agreement among the resulting trajectories yields a differentiable consistency score that down-weights unreliable traces during policy updates. Based on Qwen2.5-VL-7B-Instruct, plugging SCS into RLOO, GRPO, and REINFORCE++ series improves accuracy by up to 7.7 percentage points on six multimodal benchmarks with negligible extra computation. SCS also yields notable gains on both Qwen2.5-VL-3B-Instruct and InternVL3-8B, offering a simple, general remedy for outcome-reward RL in MLLMs.

