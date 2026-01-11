---
layout: default
title: AT$^2$PO: Agentic Turn-based Policy Optimization via Tree Search
---

# AT$^2$PO: Agentic Turn-based Policy Optimization via Tree Search
**arXiv**：[2601.04767v1](https://arxiv.org/abs/2601.04767) · [PDF](https://arxiv.org/pdf/2601.04767.pdf)  
**作者**：Zefang Zong, Dingwei Chen, Yang Li, Qi Yi, Bo Zhou, Chengming Li, Bo Qian, Peng Chen, Jie Jiang  

**一句话要点**：提出AT²PO框架，通过树搜索解决多轮智能体强化学习中的探索、信用分配和策略优化问题。

**关键词**：智能体强化学习, 树搜索, 多轮任务, 信用分配, 策略优化, 探索策略

## 3 点简述
- 核心问题：多轮智能体强化学习面临探索多样性不足、稀疏信用分配和策略优化不匹配的挑战。
- 方法要点：引入轮次级树结构，结合熵引导树扩展和轮次信用分配，并设计轮次级策略优化目标。
- 实验或效果：在七个基准测试中平均提升达1.84个百分点，消融研究验证了各组件有效性。

## 摘要（原文）

> LLM agents have emerged as powerful systems for tackling multi-turn tasks by interleaving internal reasoning and external tool interactions. Agentic Reinforcement Learning has recently drawn significant research attention as a critical post-training paradigm to further refine these capabilities. In this paper, we present AT$^2$PO (Agentic Turn-based Policy Optimization via Tree Search), a unified framework for multi-turn agentic RL that addresses three core challenges: limited exploration diversity, sparse credit assignment, and misaligned policy optimization. AT$^2$PO introduces a turn-level tree structure that jointly enables Entropy-Guided Tree Expansion for strategic exploration and Turn-wise Credit Assignment for fine-grained reward propagation from sparse outcomes. Complementing this, we propose Agentic Turn-based Policy Optimization, a turn-level learning objective that aligns policy updates with the natural decision granularity of agentic interactions. ATPO is orthogonal to tree search and can be readily integrated into any multi-turn RL pipeline. Experiments across seven benchmarks demonstrate consistent improvements over the state-of-the-art baseline by up to 1.84 percentage points in average, with ablation studies validating the effectiveness of each component. Our code is available at https://github.com/zzfoutofspace/ATPO.

