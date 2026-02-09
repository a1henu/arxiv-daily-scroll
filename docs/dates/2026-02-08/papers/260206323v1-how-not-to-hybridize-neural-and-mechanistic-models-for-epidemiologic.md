---
layout: default
title: How (Not) to Hybridize Neural and Mechanistic Models for Epidemiological Forecasting
---

# How (Not) to Hybridize Neural and Mechanistic Models for Epidemiological Forecasting
**arXiv**：[2602.06323v1](https://arxiv.org/abs/2602.06323) · [PDF](https://arxiv.org/pdf/2602.06323.pdf)  
**作者**：Yiqi Su, Ray Lee, Jiaming Cui, Naren Ramakrishnan  

**一句话要点**：提出基于多尺度分解的受控神经ODE方法，以提升流行病学预测在非平稳动态下的鲁棒性。

**关键词**：流行病学预测, 混合模型, 神经ODE, 非平稳性, 多尺度分解, 时间序列分析

## 3 点简述
- 核心问题：传统混合模型在部分可观测和非平稳传播动态下易失效，需处理行为、免疫衰减等因素。
- 方法要点：从感染序列提取趋势、季节和残差分量，作为可解释控制信号驱动神经ODE与流行病学模型耦合。
- 实验或效果：在季节和非季节场景中，长期RMSE降低15-35%，峰值时间误差改善1-3周，峰值幅度偏差减少达30%。

## 摘要（原文）

> Epidemiological forecasting from surveillance data is a hard problem and hybridizing mechanistic compartmental models with neural models is a natural direction. The mechanistic structure helps keep trajectories epidemiologically plausible, while neural components can capture non-stationary, data-adaptive effects. In practice, however, many seemingly straightforward couplings fail under partial observability and continually shifting transmission dynamics driven by behavior, waning immunity, seasonality, and interventions. We catalog these failure modes and show that robust performance requires making non-stationarity explicit: we extract multi-scale structure from the observed infection series and use it as an interpretable control signal for a controlled neural ODE coupled to an epidemiological model. Concretely, we decompose infections into trend, seasonal, and residual components and use these signals to drive continuous-time latent dynamics while jointly forecasting and inferring time-varying transmission, recovery, and immunity-loss rates. Across seasonal and non-seasonal settings, including early outbreaks and multi-wave regimes, our approach reduces long-horizon RMSE by 15-35%, improves peak timing error by 1-3 weeks, and lowers peak magnitude bias by up to 30% relative to strong time-series, neural ODE, and hybrid baselines, without relying on auxiliary covariates.

