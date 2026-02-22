---
layout: default
title: Forecasting Anomaly Precursors via Uncertainty-Aware Time-Series Ensembles
---

# Forecasting Anomaly Precursors via Uncertainty-Aware Time-Series Ensembles
**arXiv**：[2602.17028v1](https://arxiv.org/abs/2602.17028) · [PDF](https://arxiv.org/pdf/2602.17028.pdf)  
**作者**：Hyeongwon Kang, Jinwoo Park, Seunghun Han, Pilsung Kang  

**一句话要点**：提出FATE框架，通过不确定性感知的时间序列集成预测异常前兆，实现无监督早期预警。

**关键词**：时间序列预测, 异常检测, 不确定性量化, 集成学习, 无监督学习, 早期预警

## 3 点简述
- 核心问题：现有方法多为反应式，无法在异常发生前提供预警信号。
- 方法要点：利用时间序列预测模型的集成分歧量化预测不确定性，检测异常前兆。
- 实验或效果：在五个真实数据集上，PTaPR AUC平均提升19.9个百分点，无需异常标签。

## 摘要（原文）

> Detecting anomalies in time-series data is critical in domains such as industrial operations, finance, and cybersecurity, where early identification of abnormal patterns is essential for ensuring system reliability and enabling preventive maintenance. However, most existing methods are reactive: they detect anomalies only after they occur and lack the capability to provide proactive early warning signals. In this paper, we propose FATE (Forecasting Anomalies with Time-series Ensembles), a novel unsupervised framework for detecting Precursors-of-Anomaly (PoA) by quantifying predictive uncertainty from a diverse ensemble of time-series forecasting models. Unlike prior approaches that rely on reconstruction errors or require ground-truth labels, FATE anticipates future values and leverages ensemble disagreement to signal early signs of potential anomalies without access to target values at inference time. To rigorously evaluate PoA detection, we introduce Precursor Time-series Aware Precision and Recall (PTaPR), a new metric that extends the traditional Time-series Aware Precision and Recall (TaPR) by jointly assessing segment-level accuracy, within-segment coverage, and temporal promptness of early predictions. This enables a more holistic assessment of early warning capabilities that existing metrics overlook. Experiments on five real-world benchmark datasets show that FATE achieves an average improvement of 19.9 percentage points in PTaPR AUC and 20.02 percentage points in early detection F1 score, outperforming baselines while requiring no anomaly labels. These results demonstrate the effectiveness and practicality of FATE for real-time unsupervised early warning in complex time-series environments.

