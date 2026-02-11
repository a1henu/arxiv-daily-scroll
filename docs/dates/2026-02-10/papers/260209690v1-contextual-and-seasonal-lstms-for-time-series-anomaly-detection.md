---
layout: default
title: Contextual and Seasonal LSTMs for Time Series Anomaly Detection
---

# Contextual and Seasonal LSTMs for Time Series Anomaly Detection
**arXiv**：[2602.09690v1](https://arxiv.org/abs/2602.09690) · [PDF](https://arxiv.org/pdf/2602.09690.pdf)  
**作者**：Lingpei Zhang, Qingming Li, Yong Yang, Jiahao Chen, Rui Zeng, Chenyang Lyu, Shouling Ji  

**一句话要点**：提出CS-LSTMs框架，结合上下文依赖和季节模式以增强单变量时间序列中细微异常的检测能力。

**关键词**：时间序列异常检测, 长短期记忆网络, 噪声分解, 上下文依赖, 季节模式, 频域表示

## 3 点简述
- 核心问题：现有基于重构和预测的方法难以捕捉单变量时间序列中的细微异常，如小点异常和缓慢上升异常。
- 方法要点：基于噪声分解策略，联合利用上下文依赖和季节模式，整合时域和频域表示以更准确建模周期趋势和异常定位。
- 实验或效果：在公共基准数据集上广泛评估，CS-LSTMs一致优于现有先进方法，显示出在鲁棒时间序列异常检测中的有效性和实用价值。

## 摘要（原文）

> Univariate time series (UTS), where each timestamp records a single variable, serve as crucial indicators in web systems and cloud servers. Anomaly detection in UTS plays an essential role in both data mining and system reliability management. However, existing reconstruction-based and prediction-based methods struggle to capture certain subtle anomalies, particularly small point anomalies and slowly rising anomalies. To address these challenges, we propose a novel prediction-based framework named Contextual and Seasonal LSTMs (CS-LSTMs). CS-LSTMs are built upon a noise decomposition strategy and jointly leverage contextual dependencies and seasonal patterns, thereby strengthening the detection of subtle anomalies. By integrating both time-domain and frequency-domain representations, CS-LSTMs achieve more accurate modeling of periodic trends and anomaly localization. Extensive evaluations on public benchmark datasets demonstrate that CS-LSTMs consistently outperform state-of-the-art methods, highlighting their effectiveness and practical value in robust time series anomaly detection.

