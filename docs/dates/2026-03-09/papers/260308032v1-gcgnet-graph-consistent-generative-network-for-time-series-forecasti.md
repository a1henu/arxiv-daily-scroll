---
layout: default
title: GCGNet: Graph-Consistent Generative Network for Time Series Forecasting with Exogenous Variables
---

# GCGNet: Graph-Consistent Generative Network for Time Series Forecasting with Exogenous Variables
**arXiv**：[2603.08032v1](https://arxiv.org/abs/2603.08032) · [PDF](https://arxiv.org/pdf/2603.08032.pdf)  
**作者**：Zhengyu Li, Xiangfei Qiu, Yuhan Zhu, Xingjian Wu, Jilin Hu, Chenjuan Guo, Bin Yang  

**一句话要点**：提出GCGNet以解决带外生变量的时间序列预测中联合相关性与鲁棒性问题

**关键词**：时间序列预测, 外生变量, 图神经网络, 变分生成, 鲁棒性建模, 联合相关性

## 3 点简述
- 核心问题：现有方法分步建模时间与通道相关性，难以捕获联合相关性且对噪声敏感
- 方法要点：使用变分生成器粗预测，图结构对齐器评估相关性一致性，图精炼器防止退化
- 实验或效果：在12个真实数据集上超越先进基线，验证了方法的有效性

## 摘要（原文）

> Exogenous variables offer valuable supplementary information for predicting future endogenous variables. Forecasting with exogenous variables needs to consider both past-to-future dependencies (i.e., temporal correlations) and the influence of exogenous variables on endogenous variables (i.e., channel correlations). This is pivotal when future exogenous variables are available, because they may directly affect the future endogenous variables. Many methods have been proposed for time series forecasting with exogenous variables, focusing on modeling temporal and channel correlations. However, most of them use a two-step strategy, modeling temporal and channel correlations separately, which limits their ability to capture joint correlations across time and channels. Furthermore, in real-world scenarios, time series are frequently affected by various forms of noises, underscoring the critical importance of robustness in such correlations modeling. To address these limitations, we propose GCGNet, a Graph-Consistent Generative Network for time series forecasting with exogenous variables. Specifically, GCGNet first employs a Variational Generator to produce coarse predictions. A Graph Structure Aligner then further guides it by evaluating the consistency between the generated and true correlations, where the correlations are represented as graphs, and are robust to noises. Finally, a Graph Refiner is proposed to refine the predictions to prevent degeneration and improve accuracy. Extensive experiments on 12 real-world datasets demonstrate that GCGNet outperforms state-of-the-art baselines.

