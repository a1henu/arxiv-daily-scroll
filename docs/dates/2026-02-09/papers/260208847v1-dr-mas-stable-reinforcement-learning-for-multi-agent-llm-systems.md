---
layout: default
title: Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems
---

# Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems
**arXiv**：[2602.08847v1](https://arxiv.org/abs/2602.08847) · [PDF](https://arxiv.org/pdf/2602.08847.pdf)  
**作者**：Lang Feng, Longtao Zheng, Shuo He, Fuxiang Zhang, Bo An  

**一句话要点**：提出Dr. MAS以稳定多智能体大语言模型系统的强化学习训练

**关键词**：多智能体系统, 强化学习, 大语言模型, 训练稳定性, 优势归一化

## 3 点简述
- 核心问题：多智能体LLM系统在GRPO式优化中，全局归一化基线导致梯度范数不稳定
- 方法要点：采用智能体级优势归一化，基于各智能体自身奖励统计校准梯度尺度
- 实验或效果：在数学推理和多轮搜索基准上显著提升性能，消除梯度尖峰

## 摘要（原文）

> Multi-agent LLM systems enable advanced reasoning and tool use via role specialization, yet reliable reinforcement learning (RL) post-training for such systems remains difficult. In this work, we theoretically pinpoint a key reason for training instability when extending group-based RL to multi-agent LLM systems. We show that under GRPO-style optimization, a global normalization baseline may deviate from diverse agents' reward distributions, which ultimately leads to gradient-norm instability. Based on this finding, we propose Dr. MAS, a simple and stable RL training recipe for multi-agent LLM systems. Dr. MAS uses an agent-wise remedy: normalizing advantages per agent using each agent's own reward statistics, which calibrates gradient scales and dramatically stabilizes training, both theoretically and empirically. Beyond the algorithm, Dr. MAS provides an end-to-end RL training framework for multi-agent LLM systems, supporting scalable orchestration, flexible per-agent LLM serving and optimization configs, and shared resource scheduling of LLM actor backends. We evaluate Dr. MAS on multi-agent math reasoning and multi-turn search benchmarks using Qwen2.5 and Qwen3 series models. Dr. MAS achieves clear gains over vanilla GRPO (e.g., +5.6\% avg@16 and +4.6\% pass@16 on math, and +15.2\% avg@16 and +13.1\% pass@16 on search) while largely eliminating gradient spikes. Moreover, it remains highly effective under heterogeneous agent-model assignments while improving efficiency.

