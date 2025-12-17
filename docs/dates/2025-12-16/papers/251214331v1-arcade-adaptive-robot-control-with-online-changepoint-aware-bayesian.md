---
layout: default
title: ARCADE: Adaptive Robot Control with Online Changepoint-Aware Bayesian Dynamics Learning
---

# ARCADE: Adaptive Robot Control with Online Changepoint-Aware Bayesian Dynamics Learning
**arXiv**：[2512.14331v1](https://arxiv.org/abs/2512.14331) · [PDF](https://arxiv.org/pdf/2512.14331.pdf)  
**作者**：Rishabh Dev Yadav, Avirup Das, Hongyu Song, Samuel Kaski, Wei Pan  

**一句话要点**：提出ARCADE框架，通过在线变化点感知贝叶斯动力学学习，实现机器人对动态变化的实时自适应控制。

**关键词**：机器人自适应控制, 在线贝叶斯学习, 变化点检测, 动力学建模, 实时更新, 不确定性校准

## 3 点简述
- 核心问题：现实机器人需应对动态变化，如漂移、波动或突变，要求实时适应且对短期变化鲁棒。
- 方法要点：离线学习潜在表示，在线进行闭式贝叶斯更新，引入变化点感知机制以区分连续性与变化。
- 实验或效果：在模拟和真实四旋翼飞行中验证，相比基线，预测精度更高、恢复更快、闭环跟踪更准确。

## 摘要（原文）

> Real-world robots must operate under evolving dynamics caused by changing operating conditions, external disturbances, and unmodeled effects. These may appear as gradual drifts, transient fluctuations, or abrupt shifts, demanding real-time adaptation that is robust to short-term variation yet responsive to lasting change. We propose a framework for modeling the nonlinear dynamics of robotic systems that can be updated in real time from streaming data. The method decouples representation learning from online adaptation, using latent representations learned offline to support online closed-form Bayesian updates. To handle evolving conditions, we introduce a changepoint-aware mechanism with a latent variable inferred from data likelihoods that indicates continuity or shift. When continuity is likely, evidence accumulates to refine predictions; when a shift is detected, past information is tempered to enable rapid re-learning. This maintains calibrated uncertainty and supports probabilistic reasoning about transient, gradual, or structural change. We prove that the adaptive regret of the framework grows only logarithmically in time and linearly with the number of shifts, competitive with an oracle that knows timings of shift. We validate on cartpole simulations and real quadrotor flights with swinging payloads and mid-flight drops, showing improved predictive accuracy, faster recovery, and more accurate closed-loop tracking than relevant baselines.

