---
layout: default
title: An Efficient Unsupervised Federated Learning Approach for Anomaly Detection in Heterogeneous IoT Networks
---

# An Efficient Unsupervised Federated Learning Approach for Anomaly Detection in Heterogeneous IoT Networks
**arXiv**：[2602.24209v1](https://arxiv.org/abs/2602.24209) · [PDF](https://arxiv.org/pdf/2602.24209.pdf)  
**作者**：Mohsen Tajgardan, Atena Shiranzaei, Mahdi Rabbani, Reza Khoshkangini, Mahtab Jamali  

**一句话要点**：提出一种高效无监督联邦学习框架，利用互补数据集共享特征优化异构物联网网络中的异常检测。

**关键词**：无监督联邦学习, 异常检测, 物联网网络, 特征异构性, 可解释人工智能

## 3 点简述
- 核心问题：物联网数据异构性（如设备能力、格式差异）挑战联邦学习的模型性能与隐私保护。
- 方法要点：结合异常检测与设备识别数据集，保留特定特征，并应用SHAP等可解释AI技术提升透明度。
- 实验或效果：在真实物联网数据集上验证，异常检测准确率显著优于传统联邦学习方法。

## 摘要（原文）

> Federated learning (FL) is an effective paradigm for distributed environments such as the Internet of Things (IoT), where data from diverse devices with varying functionalities remains localized while contributing to a shared global model. By eliminating the need to transmit raw data, FL inherently preserves privacy. However, the heterogeneous nature of IoT data, stemming from differences in device capabilities, data formats, and communication constraints, poses significant challenges to maintaining both global model performance and privacy. In the context of IoT-based anomaly detection, unsupervised FL offers a promising means to identify abnormal behavior without centralized data aggregation. Nevertheless, feature heterogeneity across devices complicates model training and optimization, hindering effective implementation. In this study we propose an efficient unsupervised FL framework that enhances anomaly detection by leveraging shared features from two distinct IoT datasets: one focused on anomaly detection and the other on device identification, while preserving dataset-specific features. To improve transparency and interpretability, we employ explainable AI techniques, such as SHAP, to identify key features influencing local model decisions. Experiments conducted on real-world IoT datasets demonstrate that the proposed method significantly outperforms conventional FL approaches in anomaly detection accuracy. This work underscores the potential of using shared features from complementary datasets to optimize unsupervised federated learning and achieve superior anomaly detection results in decentralized IoT environments.

