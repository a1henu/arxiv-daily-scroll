---
layout: default
title: Real-Time Aligned Reward Model beyond Semantics
---

# Real-Time Aligned Reward Model beyond Semantics
**arXiv**：[2601.22664v1](https://arxiv.org/abs/2601.22664) · [PDF](https://arxiv.org/pdf/2601.22664.pdf)  
**作者**：Zixuan Huang, Xin Xia, Yuxi Ren, Jianbin Zheng, Xuefeng Xiao, Hongyan Xie, Li Huaqiu, Songshi Liang, Zhongxiang Dai, Fuzhen Zhuang, Jianxin Li, Yikun Ban, Deqing Wang  

**一句话要点**：提出R2M框架，利用策略反馈实时对齐奖励模型以缓解RLHF中的奖励过优化问题

**关键词**：强化学习人类反馈, 奖励过优化, 实时对齐, 策略反馈, 轻量级框架

## 3 点简述
- 核心问题：RLHF中奖励模型易过优化，策略模型过度拟合奖励模式而非人类意图，导致奖励差异增大
- 方法要点：R2M超越语义依赖，通过策略隐藏状态实时对齐策略分布偏移，实现轻量级RLHF框架
- 实验或效果：未知，但论文指出为奖励模型性能提升提供了新方向

## 摘要（原文）

> Reinforcement Learning from Human Feedback (RLHF) is a pivotal technique for aligning large language models (LLMs) with human preferences, yet it is susceptible to reward overoptimization, in which policy models overfit to the reward model, exploit spurious reward patterns instead of faithfully capturing human intent. Prior mitigations primarily relies on surface semantic information and fails to efficiently address the misalignment between the reward model (RM) and the policy model caused by continuous policy distribution shifts. This inevitably leads to an increasing reward discrepancy, exacerbating reward overoptimization. To address these limitations, we introduce R2M (Real-Time Aligned Reward Model), a novel lightweight RLHF framework. R2M goes beyond vanilla reward models that solely depend on the semantic representations of a pretrained LLM. Instead, it leverages the evolving hidden states of the policy (namely policy feedback) to align with the real-time distribution shift of the policy during the RL process. This work points to a promising new direction for improving the performance of reward models through real-time utilization of feedback from policy models.

