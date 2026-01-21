---
layout: default
title: Glance-or-Gaze: Incentivizing LMMs to Adaptively Focus Search via Reinforcement Learning
---

# Glance-or-Gaze: Incentivizing LMMs to Adaptively Focus Search via Reinforcement Learning
**arXiv**：[2601.13942v1](https://arxiv.org/abs/2601.13942) · [PDF](https://arxiv.org/pdf/2601.13942.pdf)  
**作者**：Hongbo Bai, Yujin Zhou, Yile Wu, Chi-Min Chan, Pengcheng Wen, Kunhao Pan, Sirui Han, Yike Guo  

**一句话要点**：提出Glance-or-Gaze框架，通过强化学习激励LMMs自适应聚焦搜索以解决复杂视觉查询问题。

**关键词**：大型多模态模型, 视觉搜索, 强化学习, 选择性凝视, 迭代推理, 知识密集型查询

## 3 点简述
- 核心问题：LMMs在知识密集型查询中因静态参数知识而表现不佳，现有搜索增强方法存在视觉冗余和缺乏深度迭代反思。
- 方法要点：引入选择性凝视机制动态选择全局或局部关注，结合双阶段训练策略，包括监督微调和复杂度自适应强化学习。
- 实验或效果：在六个基准测试中实现最先进性能，消融研究确认选择性凝视和复杂度自适应RL对有效视觉搜索至关重要。

## 摘要（原文）

> Large Multimodal Models (LMMs) have achieved remarkable success in visual understanding, yet they struggle with knowledge-intensive queries involving long-tail entities or evolving information due to static parametric knowledge. Recent search-augmented approaches attempt to address this limitation, but existing methods rely on indiscriminate whole-image retrieval that introduces substantial visual redundancy and noise, and lack deep iterative reflection, limiting their effectiveness on complex visual queries. To overcome these challenges, we propose Glance-or-Gaze (GoG), a fully autonomous framework that shifts from passive perception to active visual planning. GoG introduces a Selective Gaze mechanism that dynamically chooses whether to glance at global context or gaze into high-value regions, filtering irrelevant information before retrieval. We design a dual-stage training strategy: Reflective GoG Behavior Alignment via supervised fine-tuning instills the fundamental GoG paradigm, while Complexity-Adaptive Reinforcement Learning further enhances the model's capability to handle complex queries through iterative reasoning. Experiments across six benchmarks demonstrate state-of-the-art performance. Ablation studies confirm that both Selective Gaze and complexity-adaptive RL are essential for effective visual search. We will release our data and models for further exploration soon.

