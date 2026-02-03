---
layout: default
title: Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration
---

# Reliable Real-Time Value at Risk Estimation via Quantile Regression Forest with Conformal Calibration
**arXiv**：[2602.01912v1](https://arxiv.org/abs/2602.01912) · [PDF](https://arxiv.org/pdf/2602.01912.pdf)  
**作者**：Du-Yi Wang, Guo Liang, Kun Zhang, Qianwen Zhu  

**一句话要点**：提出基于分位数回归森林与保形校准的实时风险价值估计方法，以提升在线风险监控的可靠性。

**关键词**：风险价值估计, 分位数回归森林, 保形校准, 在线估计, 风险监控, 离线-模拟-在线框架

## 3 点简述
- 核心问题：实时市场条件下风险价值在线估计的准确性与可靠性挑战。
- 方法要点：离线训练分位数回归森林学习风险因素关系，在线结合保形校准确保估计可靠性。
- 实验或效果：理论分析证明一致性与覆盖有效性，数值实验验证方法在实际中的有效性。

## 摘要（原文）

> Rapidly evolving market conditions call for real-time risk monitoring, but its online estimation remains challenging. In this paper, we study the online estimation of one of the most widely used risk measures, Value at Risk (VaR). Its accurate and reliable estimation is essential for timely risk control and informed decision-making. We propose to use the quantile regression forest in the offline-simulation-online-estimation (OSOA) framework. Specifically, the quantile regression forest is trained offline to learn the relationship between the online VaR and risk factors, and real-time VaR estimates are then produced online by incorporating observed risk factors. To further ensure reliability, we develop a conformalized estimator that calibrates the online VaR estimates. To the best of our knowledge, we are the first to leverage conformal calibration to estimate real-time VaR reliably based on the OSOA formulation. Theoretical analysis establishes the consistency and coverage validity of the proposed estimators. Numerical experiments confirm the proposed method and demonstrate its effectiveness in practice.

