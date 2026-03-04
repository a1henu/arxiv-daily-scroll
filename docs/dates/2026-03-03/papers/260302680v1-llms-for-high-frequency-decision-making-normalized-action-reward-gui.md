---
layout: default
title: LLMs for High-Frequency Decision-Making: Normalized Action Reward-Guided Consistency Policy Optimization
---

# LLMs for High-Frequency Decision-Making: Normalized Action Reward-Guided Consistency Policy Optimization
**arXiv**：[2603.02680v1](https://arxiv.org/abs/2603.02680) · [PDF](https://arxiv.org/pdf/2603.02680.pdf)  
**作者**：Yang Zhao, Zihao Li, Zhiyu Jiang, Dandan Ma, Ganchao Liu, Wenzhe Zhao  

**一句话要点**：提出归一化动作奖励引导的一致性策略优化方法，以解决大语言模型在高频决策任务中的性能限制问题。

**关键词**：高频决策, 大语言模型, 策略优化, 归一化奖励, 一致性损失, 无人机追捕

## 3 点简述
- 核心问题：大语言模型在高频决策任务中因状态信息频繁更新和策略不对齐而性能受限。
- 方法要点：通过归一化动作奖励优化策略，并利用一致性损失确保全局与子语义策略对齐。
- 实验或效果：在无人机追捕任务中验证了方法在独立和复合任务上的优越性能及泛化能力。

## 摘要（原文）

> While Large Language Models (LLMs) form the cornerstone of sequential decision-making agent development, they have inherent limitations in high-frequency decision tasks. Existing research mainly focuses on discrete embodied decision scenarios with low-frequency and significant semantic differences in state space (e.g., household planning). These methods suffer from limited performance in high-frequency decision-making tasks, since high-precision numerical state information in such tasks undergoes frequent updates with minimal fluctuations, and exhibiting policy misalignment between the learned sub-tasks and composite tasks. To address these issues, this paper proposes Normalized Action Reward guided Consistency Policy Optimization (NAR-CP). 1) Our method first acquires predefined dense rewards from environmental feedback of candidate actions via reward functions, then completes reward shaping through normalization, and theoretically verifies action reward normalization does not impair optimal policy. 2) To reduce policy misalignment in composite tasks, we use LLMs to infer sub-observation candidate actions and generate joint policies, with consistency loss ensuring precise alignment between global semantic policies and sub-semantic policies. Experiments on UAV pursuit, a typical high-frequency task, show our method delivers superior performance on independent and composite tasks with excellent generalization to unseen tasks.

