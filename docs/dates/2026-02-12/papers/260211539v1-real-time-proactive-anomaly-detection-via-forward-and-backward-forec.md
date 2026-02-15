---
layout: default
title: Real-Time Proactive Anomaly Detection via Forward and Backward Forecast Modeling
---

# Real-Time Proactive Anomaly Detection via Forward and Backward Forecast Modeling
**arXiv**：[2602.11539v1](https://arxiv.org/abs/2602.11539) · [PDF](https://arxiv.org/pdf/2602.11539.pdf)  
**作者**：Luis Olmos, Rashida Hasan  

**一句话要点**：提出前向预测与后向重构模型，实现实时主动异常检测，适用于工业监控和网络安全等场景。

**关键词**：主动异常检测, 时间序列预测, 多变量分析, 实时监控, 深度学习架构

## 3 点简述
- 核心问题：现有主动异常检测方法难以处理异构多变量数据，且在噪声条件下精度不足。
- 方法要点：结合TCN、GRU和Transformer编码器，通过前向预测和后向重构建模时间动态。
- 实验或效果：在MSL等基准数据集上优于现有方法，显著提升异常检测及时性。

## 摘要（原文）

> Reactive anomaly detection methods, which are commonly deployed to identify anomalies after they occur based on observed deviations, often fall short in applications that demand timely intervention, such as industrial monitoring, finance, and cybersecurity. Proactive anomaly detection, by contrast, aims to detect early warning signals before failures fully manifest, but existing methods struggle with handling heterogeneous multivariate data and maintaining precision under noisy or unpredictable conditions. In this work, we introduce two proactive anomaly detection frameworks: the Forward Forecasting Model (FFM) and the Backward Reconstruction Model (BRM). Both models leverage a hybrid architecture combining Temporal Convolutional Networks (TCNs), Gated Recurrent Units (GRUs), and Transformer encoders to model directional temporal dynamics. FFM forecasts future sequences to anticipate disruptions, while BRM reconstructs recent history from future context to uncover early precursors. Anomalies are flagged based on forecasting error magnitudes and directional embedding discrepancies. Our models support both continuous and discrete multivariate features, enabling robust performance in real-world settings. Extensive experiments on four benchmark datasets, MSL, SMAP, SMD, and PSM, demonstrate that FFM and BRM outperform state-of-the-art baselines across detection metrics and significantly improve the timeliness of anomaly anticipation. These properties make our approach well-suited for deployment in time-sensitive domains requiring proactive monitoring.

