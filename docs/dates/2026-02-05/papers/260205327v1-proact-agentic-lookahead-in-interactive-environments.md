---
layout: default
title: ProAct: Agentic Lookahead in Interactive Environments
---

# ProAct: Agentic Lookahead in Interactive Environments
**arXiv**：[2602.05327v1](https://arxiv.org/abs/2602.05327) · [PDF](https://arxiv.org/pdf/2602.05327.pdf)  
**作者**：Yangbin Yu, Mingyu Yang, Junyou Li, Yiming Gao, Feiyu Liu, Yijun Yang, Zichuan Lin, Jiafei Lyu, Yicheng Liu, Zhicong Lu, Deheng Ye, Jie Jiang  

**一句话要点**：提出ProAct框架，通过两阶段训练解决LLM智能体在交互环境中长程规划的复合误差问题。

**关键词**：长程规划, 蒸馏训练, 价值估计, 交互环境, 策略优化, 泛化能力

## 3 点简述
- 现有LLM智能体在交互环境中因模拟未来状态时复合误差而难以进行长程规划。
- ProAct采用Grounded LookAhead Distillation和Monte-Carlo Critic两阶段训练，前者通过监督微调压缩搜索树为因果推理链，后者通过轻量环境模拟校准价值估计以稳定策略优化。
- 在随机和确定性环境实验中，ProAct显著提升规划准确性，4B参数模型超越开源基线并媲美闭源模型，展现强泛化能力。

## 摘要（原文）

> Existing Large Language Model (LLM) agents struggle in interactive environments requiring long-horizon planning, primarily due to compounding errors when simulating future states. To address this, we propose ProAct, a framework that enables agents to internalize accurate lookahead reasoning through a two-stage training paradigm. First, we introduce Grounded LookAhead Distillation (GLAD), where the agent undergoes supervised fine-tuning on trajectories derived from environment-based search. By compressing complex search trees into concise, causal reasoning chains, the agent learns the logic of foresight without the computational overhead of inference-time search. Second, to further refine decision accuracy, we propose the Monte-Carlo Critic (MC-Critic), a plug-and-play auxiliary value estimator designed to enhance policy-gradient algorithms like PPO and GRPO. By leveraging lightweight environment rollouts to calibrate value estimates, MC-Critic provides a low-variance signal that facilitates stable policy optimization without relying on expensive model-based value approximation. Experiments on both stochastic (e.g., 2048) and deterministic (e.g., Sokoban) environments demonstrate that ProAct significantly improves planning accuracy. Notably, a 4B parameter model trained with ProAct outperforms all open-source baselines and rivals state-of-the-art closed-source models, while demonstrating robust generalization to unseen environments. The codes and models are available at https://github.com/GreatX3/ProAct

