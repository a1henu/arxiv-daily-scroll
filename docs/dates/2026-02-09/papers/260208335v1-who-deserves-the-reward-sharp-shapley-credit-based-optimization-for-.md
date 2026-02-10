---
layout: default
title: Who Deserves the Reward? SHARP: Shapley Credit-based Optimization for Multi-Agent System
---

# Who Deserves the Reward? SHARP: Shapley Credit-based Optimization for Multi-Agent System
**arXiv**：[2602.08335v1](https://arxiv.org/abs/2602.08335) · [PDF](https://arxiv.org/pdf/2602.08335.pdf)  
**作者**：Yanming Li, Xuelin Zhang, WenJie Lu, Ziye Tang, Maodong Wu, Haotian Luo, Tongtong Wu, Zijie Peng, Hongze Mi, Yibo Feng, Naiqiang Tan, Chao Huang, Hong Chen, Li Shen  

**一句话要点**：提出SHARP框架，通过Shapley信用分配优化多智能体系统，解决信用分配难题。

**关键词**：多智能体系统, 信用分配, Shapley值, 强化学习, 大语言模型集成

## 3 点简述
- 核心问题：多智能体系统中信用分配困难，导致训练不稳定和效率低下。
- 方法要点：结合全局奖励、Shapley边际信用奖励和工具过程奖励，实现精确信用归因。
- 实验或效果：在多个基准测试中显著优于现有方法，平均匹配提升达23.66%和14.05%。

## 摘要（原文）

> Integrating Large Language Models (LLMs) with external tools via multi-agent systems offers a promising new paradigm for decomposing and solving complex problems. However, training these systems remains notoriously difficult due to the credit assignment challenge, as it is often unclear which specific functional agent is responsible for the success or failure of decision trajectories. Existing methods typically rely on sparse or globally broadcast rewards, failing to capture individual contributions and leading to inefficient reinforcement learning. To address these limitations, we introduce the Shapley-based Hierarchical Attribution for Reinforcement Policy (SHARP), a novel framework for optimizing multi-agent reinforcement learning via precise credit attribution. SHARP effectively stabilizes training by normalizing agent-specific advantages across trajectory groups, primarily through a decomposed reward mechanism comprising a global broadcast-accuracy reward, a Shapley-based marginal-credit reward for each agent, and a tool-process reward to improve execution efficiency. Extensive experiments across various real-world benchmarks demonstrate that SHARP significantly outperforms recent state-of-the-art baselines, achieving average match improvements of 23.66% and 14.05% over single-agent and multi-agent approaches, respectively.

