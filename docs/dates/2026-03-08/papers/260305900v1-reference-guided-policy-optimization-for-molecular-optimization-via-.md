---
layout: default
title: Reference-guided Policy Optimization for Molecular Optimization via LLM Reasoning
---

# Reference-guided Policy Optimization for Molecular Optimization via LLM Reasoning
**arXiv**：[2603.05900v1](https://arxiv.org/abs/2603.05900) · [PDF](https://arxiv.org/pdf/2603.05900.pdf)  
**作者**：Xuan Li, Zhanke Zhou, Zongze Li, Jiangchao Yao, Yu Rong, Lu Zhang, Bo Han  

**一句话要点**：提出参考引导策略优化以解决基于指令的分子优化中参考分子利用与探索平衡问题

**关键词**：分子优化, 大语言模型, 强化学习, 参考引导, 策略优化, 推理任务

## 3 点简述
- 核心问题：基于指令的分子优化中，仅参考分子导致推理崩溃和奖励稀疏，限制优化效果
- 方法要点：结合强化学习探索新分子和监督学习利用参考分子，通过参考引导策略优化平衡两者
- 实验或效果：在分子优化基准上优于SFT和RLVR基线，提升优化指标和泛化能力

## 摘要（原文）

> Large language models (LLMs) benefit substantially from supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR) in reasoning tasks. However, these recipes perform poorly in instruction-based molecular optimization, where each data point typically provides only a single optimized reference molecule and no step-by-step optimization trajectory. We reveal that answer-only SFT on the reference molecules collapses reasoning, and RLVR provides sparse feedback under similarity constraints due to the model's lack of effective exploration, which slows learning and limits optimization. To encourage the exploration of new molecules while balancing the exploitation of the reference molecules, we introduce Reference-guided Policy Optimization (RePO), an optimization approach that learns from reference molecules without requiring trajectory data. At each update, RePO samples candidate molecules with their intermediate reasoning trajectories from the model and trains the model using verifiable rewards that measure property satisfaction under similarity constraints in an RL manner. Meanwhile, it applies reference guidance by keeping the policy's intermediate reasoning trajectory as context and training only the answer in a supervised manner. Together, the RL term promotes exploration, while the guidance term mitigates reward sparsity and stabilizes training by grounding outputs to references when many valid molecular edits exist. Across molecular optimization benchmarks, RePO consistently outperforms SFT and RLVR baselines (e.g., GRPO), achieving improvements on the optimization metric (Success Rate $\times$ Similarity), improving balance across competing objectives, and generalizing better to unseen instruction styles. Our code is publicly available at https://github.com/tmlr-group/RePO.

