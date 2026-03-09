---
layout: default
title: Stochastic Event Prediction via Temporal Motif Transitions
---

# Stochastic Event Prediction via Temporal Motif Transitions
**arXiv**：[2603.05874v1](https://arxiv.org/abs/2603.05874) · [PDF](https://arxiv.org/pdf/2603.05874.pdf)  
**作者**：İbrahim Bahadır Altun, Ahmet Erdem Sarıyüce  

**一句话要点**：提出STEP框架，通过时序模体转换建模连续时间事件预测，提升社交网络等交互预测性能。

**关键词**：时序链接预测, 时序模体, 连续时间建模, 泊松过程, 事件预测, 图神经网络

## 3 点简述
- 核心问题：现有时序链接预测方法忽略交互的序列性和相关性，导致预测不准确。
- 方法要点：STEP将预测重构为连续时间序列问题，基于泊松过程建模时序模体转换，动态维护开放模体实例。
- 实验或效果：在五个真实数据集上，分类任务平均精度提升达21%，序列预测精度达0.99，运行时间更低。

## 摘要（原文）

> Networks of timestamped interactions arise across social, financial, and biological domains, where forecasting future events requires modeling both evolving topology and temporal ordering. Temporal link prediction methods typically frame the task as binary classification with negative sampling, discarding the sequential and correlated nature of real-world interactions. We introduce STEP (STochastic Event Predictor), a framework that reformulates temporal link prediction as a sequential forecasting problem in continuous time. STEP models event dynamics through discrete temporal motif transitions governed by Poisson processes, maintaining a set of open motif instances that evolve as new interactions arrive. At each step, the framework decides whether to initiate a new temporal motif or extend an existing one, selecting the most probable event via Bayesian scoring of temporal likelihoods and structural priors. STEP also produces compact, temporal motif-based feature vectors that can be concatenated with existing temporal graph neural network outputs, enriching their representations without architectural modifications. Experiments on five real-world datasets demonstrate up to 21% average precision gains over state-of-the-art baselines in classification and 0.99 precision in next $k$ sequential forecasting, with consistently lower runtime than competing motif-aware methods.

