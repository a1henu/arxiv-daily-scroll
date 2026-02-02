---
layout: default
title: From Self-Evolving Synthetic Data to Verifiable-Reward RL: Post-Training Multi-turn Interactive Tool-Using Agents
---

# From Self-Evolving Synthetic Data to Verifiable-Reward RL: Post-Training Multi-turn Interactive Tool-Using Agents
**arXiv**：[2601.22607v1](https://arxiv.org/abs/2601.22607) · [PDF](https://arxiv.org/pdf/2601.22607.pdf)  
**作者**：Jiaxuan Gao, Jiaao Chen, Chuyi He, Wei-Chen Wang, Shusheng Xu, Hanrui Wang, Di Jin, Yi Wu  

**一句话要点**：提出结合自演化合成数据与可验证奖励强化学习的框架，以提升多轮交互工具使用代理的训练效率与性能。

**关键词**：多轮交互代理, 工具使用, 合成数据生成, 强化学习, 自演化系统, 对话状态跟踪

## 3 点简述
- 核心问题：多轮交互工具使用代理训练面临高质量合成数据难以扩展和强化学习信号噪声大的挑战。
- 方法要点：开发EigenData系统，通过分层多代理引擎合成工具对话与可执行检查器，并采用自演化过程提升数据可靠性。
- 实验或效果：在tau^2-bench基准上，最佳模型在Airline和Telecom任务中达到73.0%和98.3%的pass^1分数，匹配或超越前沿模型。

## 摘要（原文）

> Interactive tool-using agents must solve real-world tasks via multi-turn interaction with both humans and external environments, requiring dialogue state tracking, multi-step tool execution, while following complex instructions. Post-training such agents is challenging because synthesis for high-quality multi-turn tool-use data is difficult to scale, and reinforcement learning (RL) could face noisy signals caused by user simulation, leading to degraded training efficiency. We propose a unified framework that combines a self-evolving data agent with verifier-based RL. Our system, EigenData, is a hierarchical multi-agent engine that synthesizes tool-grounded dialogues together with executable per-instance checkers, and improves generation reliability via closed-loop self-evolving process that updates prompts and workflow. Building on the synthetic data, we develop an RL recipe that first fine-tunes the user model and then applies GRPO-style training with trajectory-level group-relative advantages and dynamic filtering, yielding consistent improvements beyond SFT. Evaluated on tau^2-bench, our best model reaches 73.0% pass^1 on Airline and 98.3% pass^1 on Telecom, matching or exceeding frontier models. Overall, our results suggest a scalable pathway for bootstrapping complex tool-using behaviors without expensive human annotation.

