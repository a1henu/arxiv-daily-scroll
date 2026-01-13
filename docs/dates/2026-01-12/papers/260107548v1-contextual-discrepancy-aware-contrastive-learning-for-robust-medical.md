---
layout: default
title: Contextual Discrepancy-Aware Contrastive Learning for Robust Medical Time Series Diagnosis in Small-Sample Scenarios
---

# Contextual Discrepancy-Aware Contrastive Learning for Robust Medical Time Series Diagnosis in Small-Sample Scenarios
**arXiv**：[2601.07548v1](https://arxiv.org/abs/2601.07548) · [PDF](https://arxiv.org/pdf/2601.07548.pdf)  
**作者**：Kaito Tanaka, Aya Nakayama, Masato Ito, Yuji Nishimura, Keisuke Matsuda  

**一句话要点**：提出CoDAC框架，通过上下文差异感知对比学习解决小样本医疗时间序列诊断问题。

**关键词**：医疗时间序列诊断, 小样本学习, 对比学习, 异常检测, Transformer自编码器, 动态多视图

## 3 点简述
- 核心问题：医疗时间序列数据标注成本高导致样本稀缺，传统对比学习难以捕捉复杂时序模式。
- 方法要点：引入上下文差异估计器量化异常信号，动态多视图对比框架自适应加权聚焦诊断相关区域。
- 实验或效果：在阿尔茨海默病、帕金森病EEG和心肌梗死ECG数据集上性能优于现有方法，尤其在低标签可用性下表现突出。

## 摘要（原文）

> Medical time series data, such as EEG and ECG, are vital for diagnosing neurological and cardiovascular diseases. However, their precise interpretation faces significant challenges due to high annotation costs, leading to data scarcity, and the limitations of traditional contrastive learning in capturing complex temporal patterns. To address these issues, we propose CoDAC (Contextual Discrepancy-Aware Contrastive learning), a novel framework that enhances diagnostic accuracy and generalization, particularly in small-sample settings. CoDAC leverages external healthy data and introduces a Contextual Discrepancy Estimator (CDE), built upon a Transformer-based Autoencoder, to precisely quantify abnormal signals through context-aware anomaly scores. These scores dynamically inform a Dynamic Multi-views Contrastive Framework (DMCF), which adaptively weights different temporal views to focus contrastive learning on diagnostically relevant, discrepant regions. Our encoder combines dilated convolutions with multi-head attention for robust feature extraction. Comprehensive experiments on Alzheimer's Disease EEG, Parkinson's Disease EEG, and Myocardial Infarction ECG datasets demonstrate CoDAC's superior performance across all metrics, consistently outperforming state-of-the-art baselines, especially under low label availability. Ablation studies further validate the critical contributions of CDE and DMCF. CoDAC offers a robust and interpretable solution for medical time series diagnosis, effectively mitigating data scarcity challenges.

