---
layout: default
title: Designing Time Series Experiments in A/B Testing with Transformer Reinforcement Learning
---

# Designing Time Series Experiments in A/B Testing with Transformer Reinforcement Learning
**arXiv**：[2602.01853v1](https://arxiv.org/abs/2602.01853) · [PDF](https://arxiv.org/pdf/2602.01853.pdf)  
**作者**：Xiangkun Wu, Qianglin Wen, Yingying Zhang, Hongtu Zhu, Ting Li, Chengchun Shi  

**一句话要点**：提出基于Transformer强化学习的方法，以优化时间序列A/B测试中的策略分配设计。

**关键词**：时间序列实验, A/B测试, Transformer, 强化学习, 策略分配优化

## 3 点简述
- 核心问题：时间序列A/B测试中，现有设计未充分利用历史数据且依赖强假设，导致策略分配次优。
- 方法要点：结合Transformer处理完整历史依赖，使用强化学习直接优化均方误差，避免假设限制。
- 实验或效果：在合成数据、公开模拟器和真实网约车数据集上验证，方法优于现有设计。

## 摘要（原文）

> A/B testing has become a gold standard for modern technological companies to conduct policy evaluation. Yet, its application to time series experiments, where policies are sequentially assigned over time, remains challenging. Existing designs suffer from two limitations: (i) they do not fully leverage the entire history for treatment allocation; (ii) they rely on strong assumptions to approximate the objective function (e.g., the mean squared error of the estimated treatment effect) for optimizing the design. We first establish an impossibility theorem showing that failure to condition on the full history leads to suboptimal designs, due to the dynamic dependencies in time series experiments. To address both limitations simultaneously, we next propose a transformer reinforcement learning (RL) approach which leverages transformers to condition allocation on the entire history and employs RL to directly optimize the MSE without relying on restrictive assumptions. Empirical evaluations on synthetic data, a publicly available dispatch simulator, and a real-world ridesharing dataset demonstrate that our proposal consistently outperforms existing designs.

