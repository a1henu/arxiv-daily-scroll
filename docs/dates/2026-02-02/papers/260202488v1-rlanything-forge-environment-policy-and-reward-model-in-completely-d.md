---
layout: default
title: RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System
---

# RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System
**arXiv**：[2602.02488v1](https://arxiv.org/abs/2602.02488) · [PDF](https://arxiv.org/pdf/2602.02488.pdf)  
**作者**：Yinjie Wang, Tianbao Xie, Ke Shen, Mengdi Wang, Ling Yang  

**一句话要点**：提出RLAnything框架，通过闭环优化动态构建环境、策略和奖励模型，增强LLM或智能体场景的强化学习系统。

**关键词**：强化学习框架, 闭环优化, 动态环境适应, 奖励模型优化, LLM增强, 智能体场景

## 3 点简述
- 核心问题：强化学习系统在动态场景中环境、策略和奖励模型难以协同优化，影响学习效率和性能。
- 方法要点：采用闭环优化，策略训练集成步进和结果反馈，奖励模型通过一致性反馈联合优化，环境自动适应基于理论动机。
- 实验或效果：在OSWorld、AlfWorld和LiveBench等任务上显著提升模型性能，优化奖励信号优于依赖人工标签的结果。

## 摘要（原文）

> We propose RLAnything, a reinforcement learning framework that dynamically forges environment, policy, and reward models through closed-loop optimization, amplifying learning signals and strengthening the overall RL system for any LLM or agentic scenarios. Specifically, the policy is trained with integrated feedback from step-wise and outcome signals, while the reward model is jointly optimized via consistency feedback, which in turn further improves policy training. Moreover, our theory-motivated automatic environment adaptation improves training for both the reward and policy models by leveraging critic feedback from each, enabling learning from experience. Empirically, each added component consistently improves the overall system, and RLAnything yields substantial gains across various representative LLM and agentic tasks, boosting Qwen3-VL-8B-Thinking by 9.1% on OSWorld and Qwen2.5-7B-Instruct by 18.7% and 11.9% on AlfWorld and LiveBench, respectively. We also that optimized reward-model signals outperform outcomes that rely on human labels. Code: https://github.com/Gen-Verse/Open-AgentRL

