---
layout: default
title: ProAct: Agentic Lookahead in Interactive Environments
---

# ProAct: Agentic Lookahead in Interactive Environments
**arXiv**：[2602.05327v1](https://arxiv.org/abs/2602.05327) · [PDF](https://arxiv.org/pdf/2602.05327.pdf)  
**作者**：Yangbin Yu, Mingyu Yang, Junyou Li, Yiming Gao, Feiyu Liu, Yijun Yang, Zichuan Lin, Jiafei Lyu, Yicheng Liu, Zhicong Lu, Deheng Ye, Jie Jiang  

**一句话要点**：提出ProAct框架，通过两阶段训练解决交互环境中LLM代理的长时规划错误问题。

**关键词**：长时规划, 蒸馏训练, 值估计, 交互环境, 强化学习

## 3 点简述
- 现有LLM代理在交互环境中因未来状态模拟误差累积而规划困难。
- 采用GLAD蒸馏搜索轨迹和MC-Critic辅助值估计，提升规划准确性和稳定性。
- 在随机和确定性环境中实验显示，ProAct显著优于开源基线并媲美闭源模型。

## 摘要（原文）

> Existing Large Language Model (LLM) agents struggle in interactive environments requiring long-horizon planning, primarily due to compounding errors when simulating future states. To address this, we propose ProAct, a framework that enables agents to internalize accurate lookahead reasoning through a two-stage training paradigm. First, we introduce Grounded LookAhead Distillation (GLAD), where the agent undergoes supervised fine-tuning on trajectories derived from environment-based search. By compressing complex search trees into concise, causal reasoning chains, the agent learns the logic of foresight without the computational overhead of inference-time search. Second, to further refine decision accuracy, we propose the Monte-Carlo Critic (MC-Critic), a plug-and-play auxiliary value estimator designed to enhance policy-gradient algorithms like PPO and GRPO. By leveraging lightweight environment rollouts to calibrate value estimates, MC-Critic provides a low-variance signal that facilitates stable policy optimization without relying on expensive model-based value approximation. Experiments on both stochastic (e.g., 2048) and deterministic (e.g., Sokoban) environments demonstrate that ProAct significantly improves planning accuracy. Notably, a 4B parameter model trained with ProAct outperforms all open-source baselines and rivals state-of-the-art closed-source models, while demonstrating robust generalization to unseen environments. The codes and models are available at https://github.com/GreatX3/ProAct

