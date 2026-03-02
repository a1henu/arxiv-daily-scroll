---
layout: default
title: Exploring Robust Intrusion Detection: A Benchmark Study of Feature Transferability in IoT Botnet Attack Detection
---

# Exploring Robust Intrusion Detection: A Benchmark Study of Feature Transferability in IoT Botnet Attack Detection
**arXiv**：[2602.23874v1](https://arxiv.org/abs/2602.23874) · [PDF](https://arxiv.org/pdf/2602.23874.pdf)  
**作者**：Alejandro Guerra-Manzanares, Jialin Huang  

**一句话要点**：评估物联网僵尸网络攻击检测中基于流的特征可迁移性，提供特征工程指南以提升跨域鲁棒性。

**关键词**：物联网入侵检测, 特征可迁移性, 跨域鲁棒性, SHAP分析, 特征工程

## 3 点简述
- 核心问题：物联网入侵检测面临网络流量特征和分布跨域变异性，导致模型性能显著下降。
- 方法要点：评估三种基于流的特征集在异构物联网数据集上的可迁移性，使用SHAP分析特征重要性。
- 实验或效果：发现分类算法和特征表示对可迁移性影响显著，提出特征空间设计和自适应策略以增强鲁棒性。

## 摘要（原文）

> Cross-domain intrusion detection remains a critical challenge due to significant variability in network traffic characteristics and feature distributions across environments. This study evaluates the transferability of three widely used flow-based feature sets (Argus, Zeek and CICFlowMeter) across four widely used datasets representing heterogeneous IoT and Industrial IoT network conditions. Through extensive experiments, we evaluate in- and cross-domain performance across multiple classification models and analyze feature importance using SHapley Additive exPlanations (SHAP). Our results show that models trained on one domain suffer significant performance degradation when applied to a different target domain, reflecting the sensitivity of IoT intrusion detection systems to distribution shifts. Furthermore, the results evidence that the choice of classification algorithm and feature representations significantly impact transferability. Beyond reporting performance differences and thorough analysis of the transferability of features and feature spaces, we provide practical guidelines for feature engineering to improve robustness under domain variability. Our findings suggest that effective intrusion detection requires both high in-domain performance and resilience to cross-domain variability, achievable through careful feature space design, appropriate algorithm selection and adaptive strategies.

