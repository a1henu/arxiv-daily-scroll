---
layout: default
title: Safe Urban Traffic Control via Uncertainty-Aware Conformal Prediction and World-Model Reinforcement Learning
---

# Safe Urban Traffic Control via Uncertainty-Aware Conformal Prediction and World-Model Reinforcement Learning
**arXiv**：[2602.04821v1](https://arxiv.org/abs/2602.04821) · [PDF](https://arxiv.org/pdf/2602.04821.pdf)  
**作者**：Joydeep Chandra, Satyam Kumar Navneet, Aleksandr Algazinov, Yong Zhang  

**一句话要点**：提出STREAM-RL框架，通过不确定性感知的保形预测与世界模型强化学习实现安全城市交通控制。

**关键词**：城市交通控制, 保形预测, 世界模型强化学习, 不确定性传播, 安全保证, 端到端框架

## 3 点简述
- 核心问题：城市交通管理需同时预测未来、检测异常并采取安全行动，且需可靠性保证。
- 方法要点：引入PU-GAT+、CRFN-BY和LyCon-WRL+三个算法，实现从预测到策略学习的端到端不确定性传播与理论保证。
- 实验或效果：在真实交通数据上，覆盖效率达91.4%，FDR控制在4.1%，安全率提升至95.2%，推理延迟23ms。

## 摘要（原文）

> Urban traffic management demands systems that simultaneously predict future conditions, detect anomalies, and take safe corrective actions -- all while providing reliability guarantees. We present STREAM-RL, a unified framework that introduces three novel algorithmic contributions: (1) PU-GAT+, an Uncertainty-Guided Adaptive Conformal Forecaster that uses prediction uncertainty to dynamically reweight graph attention via confidence-monotonic attention, achieving distribution-free coverage guarantees; (2) CRFN-BY, a Conformal Residual Flow Network that models uncertainty-normalized residuals via normalizing flows with Benjamini-Yekutieli FDR control under arbitrary dependence; and (3) LyCon-WRL+, an Uncertainty-Guided Safe World-Model RL agent with Lyapunov stability certificates, certified Lipschitz bounds, and uncertainty-propagated imagination rollouts. To our knowledge, this is the first framework to propagate calibrated uncertainty from forecasting through anomaly detection to safe policy learning with end-to-end theoretical guarantees. Experiments on multiple real-world traffic trajectory data demonstrate that STREAM-RL achieves 91.4\% coverage efficiency, controls FDR at 4.1\% under verified dependence, and improves safety rate to 95.2\% compared to 69\% for standard PPO while achieving higher reward, with 23ms end-to-end inference latency.

