---
layout: default
title: Temperature Scaling Attack Disrupting Model Confidence in Federated Learning
---

# Temperature Scaling Attack Disrupting Model Confidence in Federated Learning
**arXiv**：[2602.06638v1](https://arxiv.org/abs/2602.06638) · [PDF](https://arxiv.org/pdf/2602.06638.pdf)  
**作者**：Kichang Lee, Jaeho Jin, JaeYeon Park, Songkuk Kim, JeongGil Ko  

**一句话要点**：提出温度缩放攻击以破坏联邦学习中模型置信度校准

**关键词**：联邦学习攻击, 置信度校准, 温度缩放, 非IID数据, 安全防御

## 3 点简述
- 核心问题：联邦学习攻击多针对准确性，但置信度校准作为关键攻击面被忽视。
- 方法要点：通过本地训练中注入温度缩放与学习率耦合，保持准确性但破坏校准。
- 实验或效果：在非IID设置下，攻击显著增加校准误差，对关键系统造成高风险影响。

## 摘要（原文）

> Predictive confidence serves as a foundational control signal in mission-critical systems, directly governing risk-aware logic such as escalation, abstention, and conservative fallback. While prior federated learning attacks predominantly target accuracy or implant backdoors, we identify confidence calibration as a distinct attack objective. We present the Temperature Scaling Attack (TSA), a training-time attack that degrades calibration while preserving accuracy. By injecting temperature scaling with learning rate-temperature coupling during local training, malicious updates maintain benign-like optimization behavior, evading accuracy-based monitoring and similarity-based detection. We provide a convergence analysis under non-IID settings, showing that this coupling preserves standard convergence bounds while systematically distorting confidence. Across three benchmarks, TSA substantially shifts calibration (e.g., 145% error increase on CIFAR-100) with <2 accuracy change, and remains effective under robust aggregation and post-hoc calibration defenses. Case studies further show that confidence manipulation can cause up to 7.2x increases in missed critical cases (healthcare) or false alarms (autonomous driving), even when accuracy is unchanged. Overall, our results establish calibration integrity as a critical attack surface in federated learning.

