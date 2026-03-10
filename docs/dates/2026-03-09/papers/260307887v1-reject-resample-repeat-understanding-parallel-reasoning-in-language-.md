---
layout: default
title: Reject, Resample, Repeat: Understanding Parallel Reasoning in Language Model Inference
---

# Reject, Resample, Repeat: Understanding Parallel Reasoning in Language Model Inference
**arXiv**：[2603.07887v1](https://arxiv.org/abs/2603.07887) · [PDF](https://arxiv.org/pdf/2603.07887.pdf)  
**作者**：Noah Golowich, Fan Chen, Dhruv Rohatgi, Raghav Singhal, Carles Domingo-Enrich, Dylan J. Foster, Akshay Krishnamurthy  

**一句话要点**：提出基于粒子滤波的框架以分析语言模型推理中的并行采样方法

**关键词**：语言模型推理, 粒子滤波, 序列蒙特卡洛, 采样误差, 过程奖励模型, 并行推理

## 3 点简述
- 核心问题：缺乏对语言模型推理时聚合与剪枝多样本方法的精度-成本权衡的理论理解
- 方法要点：使用序列蒙特卡洛等粒子滤波算法，研究在给定过程奖励模型下的采样准确性
- 实验或效果：理论标准有效控制采样误差，但最终精度需额外理论视角

## 摘要（原文）

> Inference-time methods that aggregate and prune multiple samples have emerged as a powerful paradigm for steering large language models, yet we lack any principled understanding of their accuracy-cost tradeoffs. In this paper, we introduce a route to rigorously study such approaches using the lens of *particle filtering* algorithms such as Sequential Monte Carlo (SMC). Given a base language model and a *process reward model* estimating expected terminal rewards, we ask: *how accurately can we sample from a target distribution given some number of process reward evaluations?* Theoretically, we identify (1) simple criteria enabling non-asymptotic guarantees for SMC; (2) algorithmic improvements to SMC; and (3) a fundamental limit faced by all particle filtering methods. Empirically, we demonstrate that our theoretical criteria effectively govern the *sampling error* of SMC, though not necessarily its final *accuracy*, suggesting that theoretical perspectives beyond sampling may be necessary.

