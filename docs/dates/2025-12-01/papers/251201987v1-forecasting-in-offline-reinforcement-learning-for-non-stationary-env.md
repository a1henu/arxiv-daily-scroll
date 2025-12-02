---
layout: default
title: Forecasting in Offline Reinforcement Learning for Non-stationary Environments
---

# Forecasting in Offline Reinforcement Learning for Non-stationary Environments
**arXiv**：[2512.01987v1](https://arxiv.org/abs/2512.01987) · [PDF](https://arxiv.org/pdf/2512.01987.pdf)  
**作者**：Suzan Ece Ada, Georg Martius, Emre Ugur, Erhan Oztop  

**一句话要点**：提出FORL框架以解决非平稳环境中离线强化学习的性能下降问题

**关键词**：离线强化学习, 非平稳环境, 条件扩散模型, 零样本预测, 时间序列分析, 部分可观测性

## 3 点简述
- 核心问题：离线强化学习在非平稳环境中因偏移导致部分可观测性和性能下降
- 方法要点：结合条件扩散候选状态生成和零样本时间序列基础模型进行预测
- 实验或效果：在模拟真实非平稳性的基准测试中，FORL相比基线方法性能提升

## 摘要（原文）

> Offline Reinforcement Learning (RL) provides a promising avenue for training policies from pre-collected datasets when gathering additional interaction data is infeasible. However, existing offline RL methods often assume stationarity or only consider synthetic perturbations at test time, assumptions that often fail in real-world scenarios characterized by abrupt, time-varying offsets. These offsets can lead to partial observability, causing agents to misperceive their true state and degrade performance. To overcome this challenge, we introduce Forecasting in Non-stationary Offline RL (FORL), a framework that unifies (i) conditional diffusion-based candidate state generation, trained without presupposing any specific pattern of future non-stationarity, and (ii) zero-shot time-series foundation models. FORL targets environments prone to unexpected, potentially non-Markovian offsets, requiring robust agent performance from the onset of each episode. Empirical evaluations on offline RL benchmarks, augmented with real-world time-series data to simulate realistic non-stationarity, demonstrate that FORL consistently improves performance compared to competitive baselines. By integrating zero-shot forecasting with the agent's experience, we aim to bridge the gap between offline RL and the complexities of real-world, non-stationary environments.

