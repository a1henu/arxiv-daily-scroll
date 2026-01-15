---
layout: default
title: Explainable Autoencoder-Based Anomaly Detection in IEC 61850 GOOSE Networks
---

# Explainable Autoencoder-Based Anomaly Detection in IEC 61850 GOOSE Networks
**arXiv**：[2601.09287v1](https://arxiv.org/abs/2601.09287) · [PDF](https://arxiv.org/pdf/2601.09287.pdf)  
**作者**：Dafne Lozano-Paredes, Luis Bote-Curiel, Juan Ramón Feijóo-Martínez, Ismael Gómez-Talal, José Luis Rojo-Álvarez  

**一句话要点**：提出可解释自编码器异常检测框架以解决IEC 61850 GOOSE网络中的协议合规攻击检测问题

**关键词**：异常检测, 自编码器, IEC 61850 GOOSE协议, 可解释性, 无监督学习, 网络安全

## 3 点简述
- 核心问题：IEC 61850 GOOSE协议缺乏原生安全机制，传统方法难以检测协议合规和零日攻击，面临类别不平衡和标记数据有限挑战。
- 方法要点：使用非对称自编码器，在真实GOOSE流量上训练，分离语义完整性和时间可用性，通过重建误差与统计阈值进行无监督异常检测。
- 实验或效果：在真实变电站流量和公开数据集上评估，攻击检测率超过99%，误报率低于5%，展示强泛化能力和可解释性。

## 摘要（原文）

> The IEC 61850 Generic Object-Oriented Substation Event (GOOSE) protocol plays a critical role in real-time protection and automation of digital substations, yet its lack of native security mechanisms can expose power systems to sophisticated cyberattacks. Traditional rule-based and supervised intrusion detection techniques struggle to detect protocol-compliant and zero-day attacks under significant class imbalance and limited availability of labeled data. This paper proposes an explainable, unsupervised multi-view anomaly detection framework for IEC 61850 GOOSE networks that explicitly separates semantic integrity and temporal availability. The approach employs asymmetric autoencoders trained only on real operational GOOSE traffic to learn distinct latent representations of sequence-based protocol semantics and timing-related transmission dynamics in normal traffic. Anomaly detection is implemented using reconstruction errors mixed with statistically grounded thresholds, enabling robust detection without specified attack types. Feature-level reconstruction analysis provides intrinsic explainability by directly linking detection outcomes to IEC 61850 protocol characteristics. The proposed framework is evaluated using real substation traffic for training and a public dataset containing normal traffic and message suppression, data manipulation, and denial-of-service attacks for testing. Experimental results show attack detection rates above 99% with false positives remaining below 5% of total traffic, demonstrating strong generalization across environments and effective operation under extreme class imbalance and interpretable anomaly attribution.

