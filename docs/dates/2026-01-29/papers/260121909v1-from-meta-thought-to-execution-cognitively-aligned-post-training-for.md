---
layout: default
title: From Meta-Thought to Execution: Cognitively Aligned Post-Training for Generalizable and Reliable LLM Reasoning
---

# From Meta-Thought to Execution: Cognitively Aligned Post-Training for Generalizable and Reliable LLM Reasoning
**arXiv**：[2601.21909v1](https://arxiv.org/abs/2601.21909) · [PDF](https://arxiv.org/pdf/2601.21909.pdf)  
**作者**：Shaojie Wang, Liang Zhang  

**一句话要点**：提出认知对齐后训练框架，通过两阶段方法提升LLM推理的泛化性与可靠性

**关键词**：LLM后训练, 认知对齐, 推理泛化, 强化学习, 训练效率, 抽象策略学习

## 3 点简述
- 核心问题：现有LLM后训练方法以完整推理轨迹为单元，未对齐人类认知的两阶段分解过程，导致抽象策略与具体执行纠缠。
- 方法要点：引入Chain-of-Meta-Thought（CoMT）专注于抽象推理模式学习，结合Confidence-Calibrated Reinforcement Learning（CCRL）优化任务适应，提升执行可靠性。
- 实验或效果：在四个模型和八个基准测试中，分布内和分布外性能分别提升2.19%和4.63%，训练时间减少65-70%，令牌消耗降低50%。

## 摘要（原文）

> Current LLM post-training methods optimize complete reasoning trajectories through Supervised Fine-Tuning (SFT) followed by outcome-based Reinforcement Learning (RL). While effective, a closer examination reveals a fundamental gap: this approach does not align with how humans actually solve problems. Human cognition naturally decomposes problem-solving into two distinct stages: first acquiring abstract strategies (i.e., meta-knowledge) that generalize across problems, then adapting them to specific instances. In contrast, by treating complete trajectories as basic units, current methods are inherently problem-centric, entangling abstract strategies with problem-specific execution. To address this misalignment, we propose a cognitively-inspired framework that explicitly mirrors the two-stage human cognitive process. Specifically, Chain-of-Meta-Thought (CoMT) focuses supervised learning on abstract reasoning patterns without specific executions, enabling acquisition of generalizable strategies. Confidence-Calibrated Reinforcement Learning (CCRL) then optimizes task adaptation via confidence-aware rewards on intermediate steps, preventing overconfident errors from cascading and improving execution reliability. Experiments across four models and eight benchmarks show 2.19\% and 4.63\% improvements in-distribution and out-of-distribution respectively over standard methods, while reducing training time by 65-70% and token consumption by 50%, demonstrating that aligning post-training with human cognitive principles yields not only superior generalization but also enhanced training efficiency.

