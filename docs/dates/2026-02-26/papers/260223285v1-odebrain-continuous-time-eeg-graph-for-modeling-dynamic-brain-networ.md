---
layout: default
title: ODEBrain: Continuous-Time EEG Graph for Modeling Dynamic Brain Networks
---

# ODEBrain: Continuous-Time EEG Graph for Modeling Dynamic Brain Networks
**arXiv**：[2602.23285v1](https://arxiv.org/abs/2602.23285) · [PDF](https://arxiv.org/pdf/2602.23285.pdf)  
**作者**：Haohui Jia, Zheng Chen, Lingwei Zhu, Rikuto Kotoge, Jathurshan Pradeepkumar, Yasuko Matsubara, Jimeng Sun, Yasushi Sakurai, Takashi Matsubara  

**一句话要点**：提出ODEBRAIN框架，通过神经ODE建模连续脑电图动态以提升预测精度和鲁棒性。

**关键词**：脑电图动态建模, 神经ODE, 谱图节点, 连续时间建模, 预测精度提升

## 3 点简述
- 核心问题：传统方法离散化时间建模脑动态，导致累积误差和无法捕捉EEG瞬时非线性特征。
- 方法要点：整合时空频特征到谱图节点，用神经ODE建模连续潜在动态，捕获复杂脑状态的随机变化。
- 实验或效果：实验验证ODEBRAIN在EEG动态预测上显著优于现有方法，增强鲁棒性和泛化能力。

## 摘要（原文）

> Modeling neural population dynamics is crucial for foundational neuroscientific research and various clinical applications. Conventional latent variable methods typically model continuous brain dynamics through discretizing time with recurrent architecture, which necessarily results in compounded cumulative prediction errors and failure of capturing instantaneous, nonlinear characteristics of EEGs. We propose ODEBRAIN, a Neural ODE latent dynamic forecasting framework to overcome these challenges by integrating spatio-temporal-frequency features into spectral graph nodes, followed by a Neural ODE modeling the continuous latent dynamics. Our design ensures that latent representations can capture stochastic variations of complex brain states at any given time point. Extensive experiments verify that ODEBRAIN can improve significantly over existing methods in forecasting EEG dynamics with enhanced robustness and generalization capabilities.

