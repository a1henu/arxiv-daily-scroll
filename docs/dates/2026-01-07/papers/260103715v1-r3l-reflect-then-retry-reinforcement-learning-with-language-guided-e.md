---
layout: default
title: R$^3$L: Reflect-then-Retry Reinforcement Learning with Language-Guided Exploration, Pivotal Credit, and Positive Amplification
---

# R$^3$L: Reflect-then-Retry Reinforcement Learning with Language-Guided Exploration, Pivotal Credit, and Positive Amplification
**arXiv**：[2601.03715v1](https://arxiv.org/abs/2601.03715) · [PDF](https://arxiv.org/pdf/2601.03715.pdf)  
**作者**：Weijie Shi, Yanxi Chen, Zexi Li, Xuchen Pan, Yuchang Sun, Jiajie Xu, Xiaofang Zhou, Yaliang Li  

**一句话要点**：提出R³L强化学习方法，通过语言引导探索、关键信用分配和正信号放大，解决探索与利用难题。

**关键词**：强化学习, 语言引导探索, 信用分配, 训练稳定性, 代理任务, 推理任务

## 3 点简述
- 核心问题：强化学习在探索中成功率低、成本高，利用中信用分配粗糙、训练不稳定。
- 方法要点：采用反思-重试机制合成高质量轨迹，语言反馈诊断错误，关键信用分配更新分歧后缀，正信号放大优化过程。
- 实验或效果：在代理和推理任务上相对基线提升5%至52%，保持训练稳定性。

## 摘要（原文）

> Reinforcement learning drives recent advances in LLM reasoning and agentic capabilities, yet current approaches struggle with both exploration and exploitation. Exploration suffers from low success rates on difficult tasks and high costs of repeated rollouts from scratch. Exploitation suffers from coarse credit assignment and training instability: Trajectory-level rewards penalize valid prefixes for later errors, and failure-dominated groups overwhelm the few positive signals, leaving optimization without constructive direction. To this end, we propose R$^3$L, Reflect-then-Retry Reinforcement Learning with Language-Guided Exploration, Pivotal Credit, and Positive Amplification. To synthesize high-quality trajectories, R$^3$L shifts from stochastic sampling to active synthesis via reflect-then-retry, leveraging language feedback to diagnose errors, transform failed attempts into successful ones, and reduce rollout costs by restarting from identified failure points. With errors diagnosed and localized, Pivotal Credit Assignment updates only the diverging suffix where contrastive signals exist, excluding the shared prefix from gradient update. Since failures dominate on difficult tasks and reflect-then-retry produces off-policy data, risking training instability, Positive Amplification upweights successful trajectories to ensure positive signals guide the optimization process. Experiments on agentic and reasoning tasks demonstrate 5\% to 52\% relative improvements over baselines while maintaining training stability. Our code is released at https://github.com/shiweijiezero/R3L.

