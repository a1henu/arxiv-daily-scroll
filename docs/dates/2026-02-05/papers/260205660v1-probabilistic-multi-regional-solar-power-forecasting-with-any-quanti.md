---
layout: default
title: Probabilistic Multi-Regional Solar Power Forecasting with Any-Quantile Recurrent Neural Networks
---

# Probabilistic Multi-Regional Solar Power Forecasting with Any-Quantile Recurrent Neural Networks
**arXiv**：[2602.05660v1](https://arxiv.org/abs/2602.05660) · [PDF](https://arxiv.org/pdf/2602.05660.pdf)  
**作者**：Slawek Smyl, Paweł Pełka, Grzegorz Dudek  

**一句话要点**：提出基于任意分位数循环神经网络的概率多区域太阳能功率预测框架，以应对光伏发电不确定性。

**关键词**：概率预测, 任意分位数, 循环神经网络, 多区域建模, 太阳能功率预测, 不确定性量化

## 3 点简述
- 核心问题：光伏发电渗透率增加导致电力系统不确定性，需超越确定性点预测的概率方法。
- 方法要点：结合任意分位数预测范式与双轨循环架构，处理序列特定和跨区域上下文信息。
- 实验或效果：使用259个欧洲区域30年小时数据评估，在准确性、校准和预测区间质量上优于基线。

## 摘要（原文）

> The increasing penetration of photovoltaic (PV) generation introduces significant uncertainty into power system operation, necessitating forecasting approaches that extend beyond deterministic point predictions. This paper proposes an any-quantile probabilistic forecasting framework for multi-regional PV power generation based on the Any-Quantile Recurrent Neural Network (AQ-RNN). The model integrates an any-quantile forecasting paradigm with a dual-track recurrent architecture that jointly processes series-specific and cross-regional contextual information, supported by dilated recurrent cells, patch-based temporal modeling, and a dynamic ensemble mechanism.
>   The proposed framework enables the estimation of calibrated conditional quantiles at arbitrary probability levels within a single trained model and effectively exploits spatial dependencies to enhance robustness at the system level. The approach is evaluated using 30 years of hourly PV generation data from 259 European regions and compared against established statistical and neural probabilistic baselines. The results demonstrate consistent improvements in forecast accuracy, calibration, and prediction interval quality, underscoring the suitability of the proposed method for uncertainty-aware energy management and operational decision-making in renewable-dominated power systems.

