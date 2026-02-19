---
layout: default
title: Optimal training-conditional regret for online conformal prediction
---

# Optimal training-conditional regret for online conformal prediction
**arXiv**：[2602.16537v1](https://arxiv.org/abs/2602.16537) · [PDF](https://arxiv.org/pdf/2602.16537.pdf)  
**作者**：Jiadong Liang, Zhimei Ren, Yuxin Chen  

**一句话要点**：提出基于训练条件遗憾的在线共形预测算法，以处理非平稳数据流中的分布漂移。

**关键词**：在线共形预测, 分布漂移, 训练条件遗憾, 漂移检测, 极小极大最优, 非平稳数据流

## 3 点简述
- 研究在线共形预测在非平稳数据流中的性能评估，聚焦训练条件累积遗憾而非传统边际覆盖差距。
- 针对预训练和在线训练的非共形分数，分别提出结合漂移检测的自适应校准算法，实现极小极大最优遗憾。
- 通过数值实验验证理论结果，支持算法在突变点和平滑漂移场景下的有效性。

## 摘要（原文）

> We study online conformal prediction for non-stationary data streams subject to unknown distribution drift. While most prior work studied this problem under adversarial settings and/or assessed performance in terms of gaps of time-averaged marginal coverage, we instead evaluate performance through training-conditional cumulative regret. We specifically focus on independently generated data with two types of distribution shift: abrupt change points and smooth drift.
>   When non-conformity score functions are pretrained on an independent dataset, we propose a split-conformal style algorithm that leverages drift detection to adaptively update calibration sets, which provably achieves minimax-optimal regret. When non-conformity scores are instead trained online, we develop a full-conformal style algorithm that again incorporates drift detection to handle non-stationarity; this approach relies on stability - rather than permutation symmetry - of the model-fitting algorithm, which is often better suited to online learning under evolving environments. We establish non-asymptotic regret guarantees for our online full conformal algorithm, which match the minimax lower bound under appropriate restrictions on the prediction sets. Numerical experiments corroborate our theoretical findings.

