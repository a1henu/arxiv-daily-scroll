---
layout: default
title: SeeUPO: Sequence-Level Agentic-RL with Convergence Guarantees
---

# SeeUPO: Sequence-Level Agentic-RL with Convergence Guarantees
**arXiv**：[2602.06554v1](https://arxiv.org/abs/2602.06554) · [PDF](https://arxiv.org/pdf/2602.06554.pdf)  
**作者**：Tianyi Hu, Qingxu Fu, Yanxi Chen, Zhaoyang Liu, Bolin Ding  

**一句话要点**：提出SeeUPO以解决多轮交互中强化学习算法缺乏收敛保证的问题

**关键词**：强化学习, 多轮交互, 收敛保证, 策略优化, AI智能体, 序列级优化

## 3 点简述
- 分析现有RL算法在单/多轮场景中收敛性不足，指出PPO与GRAE组合破坏单调改进
- 提出SeeUPO，将多轮交互建模为顺序多臂赌博机问题，通过反向顺序更新确保收敛
- 在AppWorld和BFCL v4上实验，SeeUPO相比基线算法提升显著，训练稳定性优越

## 摘要（原文）

> Reinforcement learning (RL) has emerged as the predominant paradigm for training large language model (LLM)-based AI agents. However, existing backbone RL algorithms lack verified convergence guarantees in agentic scenarios, especially in multi-turn settings, which can lead to training instability and failure to converge to optimal policies.
>   In this paper, we systematically analyze how different combinations of policy update mechanisms and advantage estimation methods affect convergence properties in single/multi-turn scenarios. We find that REINFORCE with Group Relative Advantage Estimation (GRAE) can converge to the globally optimal under undiscounted conditions, but the combination of PPO & GRAE breaks PPO's original monotonic improvement property. Furthermore, we demonstrate that mainstream backbone RL algorithms cannot simultaneously achieve both critic-free and convergence guarantees in multi-turn scenarios.
>   To address this, we propose SeeUPO (Sequence-level Sequential Update Policy Optimization), a critic-free approach with convergence guarantees for multi-turn interactions. SeeUPO models multi-turn interaction as sequentially executed multi-agent bandit problems. Through turn-by-turn sequential policy updates in reverse execution order, it ensures monotonic improvement and convergence to global optimal solution via backward induction.
>   Experiments on AppWorld and BFCL v4 demonstrate SeeUPO's substantial improvements over existing backbone algorithms: relative gains of 43.3%-54.6% on Qwen3-14B and 24.1%-41.9% on Qwen2.5-14B (averaged across benchmarks), along with superior training stability.

