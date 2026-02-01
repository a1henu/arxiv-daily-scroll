---
layout: default
title: From Meta-Thought to Execution: Cognitively Aligned Post-Training for Generalizable and Reliable LLM Reasoning
---

# From Meta-Thought to Execution: Cognitively Aligned Post-Training for Generalizable and Reliable LLM Reasoning
**arXiv**：[2601.21909v1](https://arxiv.org/abs/2601.21909) · [PDF](https://arxiv.org/pdf/2601.21909.pdf)  
**作者**：Shaojie Wang, Liang Zhang  

**一句话要点**：提出认知对齐后训练框架以提升LLM推理的泛化性与可靠性

**关键词**：大语言模型后训练, 认知对齐, 推理泛化, 强化学习, 训练效率

## 3 点简述
- 核心问题：现有后训练方法未对齐人类认知，将抽象策略与具体执行纠缠，限制泛化。
- 方法要点：引入Chain-of-Meta-Thought和Confidence-Calibrated Reinforcement Learning，分阶段学习抽象策略与任务适应。
- 实验或效果：在八个基准上提升泛化性能，同时减少训练时间和令牌消耗。

## 摘要（原文）

> Current LLM post-training methods optimize complete reasoning trajectories through Supervised Fine-Tuning (SFT) followed by outcome-based Reinforcement Learning (RL). While effective, a closer examination reveals a fundamental gap: this approach does not align with how humans actually solve problems. Human cognition naturally decomposes problem-solving into two distinct stages: first acquiring abstract strategies (i.e., meta-knowledge) that generalize across problems, then adapting them to specific instances. In contrast, by treating complete trajectories as basic units, current methods are inherently problem-centric, entangling abstract strategies with problem-specific execution. To address this misalignment, we propose a cognitively-inspired framework that explicitly mirrors the two-stage human cognitive process. Specifically, Chain-of-Meta-Thought (CoMT) focuses supervised learning on abstract reasoning patterns without specific executions, enabling acquisition of generalizable strategies. Confidence-Calibrated Reinforcement Learning (CCRL) then optimizes task adaptation via confidence-aware rewards on intermediate steps, preventing overconfident errors from cascading and improving execution reliability. Experiments across four models and eight benchmarks show 2.19\% and 4.63\% improvements in-distribution and out-of-distribution respectively over standard methods, while reducing training time by 65-70% and token consumption by 50%, demonstrating that aligning post-training with human cognitive principles yields not only superior generalization but also enhanced training efficiency.

