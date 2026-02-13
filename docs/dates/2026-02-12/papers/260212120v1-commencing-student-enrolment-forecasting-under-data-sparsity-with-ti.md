---
layout: default
title: Commencing-Student Enrolment Forecasting Under Data Sparsity with Time Series Foundation Models
---

# Commencing-Student Enrolment Forecasting Under Data Sparsity with Time Series Foundation Models
**arXiv**：[2602.12120v1](https://arxiv.org/abs/2602.12120) · [PDF](https://arxiv.org/pdf/2602.12120.pdf)  
**作者**：Jittarin Jetwiriyanon, Teo Susnjak, Surangika Ranathunga  

**一句话要点**：提出基于时间序列基础模型和泄漏安全协变量的零-shot预测方法，以解决高等教育新生入学数据稀疏问题。

**关键词**：时间序列预测, 数据稀疏, 零-shot学习, 协变量工程, 高等教育管理, 机构运营条件指数

## 3 点简述
- 核心问题：高等教育新生入学预测面临数据稀疏、样本短、结构断裂等挑战，传统方法不稳定。
- 方法要点：采用时间序列基础模型进行零-shot预测，引入泄漏安全协变量集和机构运营条件指数，结合Google Trends需求代理。
- 实验或效果：通过扩展窗口回溯测试，协变量条件化模型在无机构特定训练下表现与传统基准相当，性能因队列和模型而异。

## 摘要（原文）

> Many universities face increasing financial pressure and rely on accurate forecasts of commencing enrolments. However, enrolment forecasting in higher education is often data-sparse; annual series are short and affected by reporting changes and regime shifts. Popular classical approaches can be unreliable, as parameter estimation and model selection are unstable with short samples, and structural breaks degrade extrapolation. Recently, TSFMs have provided zero-shot priors, delivering strong gains in annual, data-sparse institutional forecasting under leakage-disciplined covariate construction. We benchmark multiple TSFM families in a zero-shot setting and test a compact, leakage-safe covariate set and introduce the Institutional Operating Conditions Index (IOCI), a transferable 0-100 regime covariate derived from time-stamped documentary evidence available at each forecast origin, alongside Google Trends demand proxies with stabilising feature engineering. Using an expanding-window backtest with strict vintage alignment, covariate-conditioned TSFMs perform on par with classical benchmarks without institution-specific training, with performance differences varying by cohort and model.

