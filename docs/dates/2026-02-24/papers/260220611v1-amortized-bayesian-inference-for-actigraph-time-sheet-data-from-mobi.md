---
layout: default
title: Amortized Bayesian inference for actigraph time sheet data from mobile devices
---

# Amortized Bayesian inference for actigraph time sheet data from mobile devices
**arXiv**：[2602.20611v1](https://arxiv.org/abs/2602.20611) · [PDF](https://arxiv.org/pdf/2602.20611.pdf)  
**作者**：Daniel Zhou, Sudipto Banerjee  

**一句话要点**：提出摊销贝叶斯推断方法，用于移动设备活动图时间表数据的概率插补与变量影响分析。

**关键词**：贝叶斯推断, 活动图数据, 摊销学习, 分层动态模型, 概率插补, 移动健康

## 3 点简述
- 核心问题：高分辨率活动图数据在AI框架下需适配迁移学习和摊销，以支持不确定性传播与量化。
- 方法要点：采用分层动态线性模型进行贝叶斯推断，实现摊销化处理，确保概率插补和变量影响学习。
- 实验或效果：基于PASTA-LA研究数据，成功插补活动图时间表，并统计学习解释变量对加速度幅值的时变影响。

## 摘要（原文）

> Mobile data technologies use ``actigraphs'' to furnish information on health variables as a function of a subject's movement. The advent of wearable devices and related technologies has propelled the creation of health databases consisting of human movement data to conduct research on mobility patterns and health outcomes. Statistical methods for analyzing high-resolution actigraph data depend on the specific inferential context, but the advent of Artificial Intelligence (AI) frameworks require that the methods be congruent to transfer learning and amortization. This article devises amortized Bayesian inference for actigraph time sheets. We pursue a Bayesian approach to ensure full propagation of uncertainty and its quantification using a hierarchical dynamic linear model. We build our analysis around actigraph data from the Physical Activity through Sustainable Transport Approaches in Los Angeles (PASTA-LA) study conducted by the Fielding School of Public Health in the University of California, Los Angeles. Apart from achieving probabilistic imputation of actigraph time sheets, we are also able to statistically learn about the time-varying impact of explanatory variables on the magnitude of acceleration (MAG) for a cohort of subjects.

