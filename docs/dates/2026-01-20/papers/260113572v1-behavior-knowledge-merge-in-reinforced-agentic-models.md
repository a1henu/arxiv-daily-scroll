---
layout: default
title: Behavior Knowledge Merge in Reinforced Agentic Models
---

# Behavior Knowledge Merge in Reinforced Agentic Models
**arXiv**：[2601.13572v1](https://arxiv.org/abs/2601.13572) · [PDF](https://arxiv.org/pdf/2601.13572.pdf)  
**作者**：Xiangchi Yuan, Dachuan Shi, Chunhui Zhang, Zheyuan Liu, Shenglong Yao, Soroush Vosoughi, Wenke Lee  

**一句话要点**：提出强化代理合并以解决RL训练代理模型合并中的任务向量不匹配问题

**关键词**：强化学习, 模型合并, 代理模型, 任务向量, 参数更新, 分布感知

## 3 点简述
- 核心问题：RL与SFT任务向量不匹配导致标准合并方法稀释关键任务特定行为
- 方法要点：RAM框架解耦共享与独特参数更新，选择性保留并重缩放独特更新
- 实验或效果：RAM在多个代理领域超越基线，实现优于专业代理的性能

## 摘要（原文）

> Reinforcement learning (RL) is central to post-training, particularly for agentic models that require specialized reasoning behaviors. In this setting, model merging offers a practical mechanism for integrating multiple RL-trained agents from different tasks into a single generalist model. However, existing merging methods are designed for supervised fine-tuning (SFT), and they are suboptimal to preserve task-specific capabilities on RL-trained agentic models. The root is a task-vector mismatch between RL and SFT: on-policy RL induces task vectors that are highly sparse and heterogeneous, whereas SFT-style merging implicitly assumes dense and globally comparable task vectors. When standard global averaging is applied under this mismatch, RL's non-overlapping task vectors that encode critical task-specific behaviors are reduced and parameter updates are diluted. To address this issue, we propose Reinforced Agent Merging (RAM), a distribution-aware merging framework explicitly designed for RL-trained agentic models. RAM disentangles shared and task-specific unique parameter updates, averaging shared components while selectively preserving and rescaling unique ones to counteract parameter update dilution. Experiments across multiple agent domains and model architectures demonstrate that RAM not only surpasses merging baselines, but also unlocks synergistic potential among agents to achieve performance superior to that of specialized agents in their domains.

