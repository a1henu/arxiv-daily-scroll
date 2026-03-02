---
layout: default
title: MI$^2$DAS: A Multi-Layer Intrusion Detection Framework with Incremental Learning for Securing Industrial IoT Networks
---

# MI$^2$DAS: A Multi-Layer Intrusion Detection Framework with Incremental Learning for Securing Industrial IoT Networks
**arXiv**：[2602.23846v1](https://arxiv.org/abs/2602.23846) · [PDF](https://arxiv.org/pdf/2602.23846.pdf)  
**作者**：Wei Lian, Alejandro Guerra-Manzanares  

**一句话要点**：提出MI²DAS多层入侵检测框架，通过增量学习增强工业物联网网络安全

**关键词**：工业物联网安全, 多层入侵检测, 开集识别, 增量学习, 异常检测, 网络流量分析

## 3 点简述
- 工业物联网系统面临异构设备和动态流量带来的安全挑战，传统入侵检测系统依赖大量标注数据且难以检测新威胁。
- MI²DAS集成异常检测、开集识别和增量学习，以分层方式区分正常流量、已知攻击和未知攻击，并适应新攻击类型。
- 在Edge-IIoTset数据集上，各层性能优异，如GMM在正常-攻击区分中准确率达0.953，增量学习模块在纳入新攻击类时宏F1为0.8995。

## 摘要（原文）

> The rapid expansion of Industrial IoT (IIoT) systems has amplified security challenges, as heterogeneous devices and dynamic traffic patterns increase exposure to sophisticated and previously unseen cyberattacks. Traditional intrusion detection systems often struggle in such environments due to their reliance on extensive labeled data and limited ability to detect new threats. To address these challenges, we propose MI$^2$DAS, a multi-layer intrusion detection framework that integrates anomaly-based hierarchical traffic pooling, open-set recognition to distinguish between known and unknown attacks and incremental learning for adapting to novel attack types with minimal labeling. Experiments conducted on the Edge-IIoTset dataset demonstrate strong performance across all layers. In the first layer, GMM achieves superior normal-attack discrimination (accuracy = 0.953, TPR = 1.000). In open-set recognition, GMM attains a recall of 0.813 for known attacks, while LOF achieves 0.882 recall for unknown attacks. For fine-grained classification of known attacks, Random Forest achieves a macro-F1 of 0.941. Finally, the incremental learning module maintains robust performance when incorporation novel attack classes, achieving a macro-F1 of 0.8995. These results showcase MI$^2$DAS as an effective, scalable and adaptive framework for enhancing IIoT security against evolving threats.

