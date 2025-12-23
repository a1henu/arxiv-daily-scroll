---
layout: default
title: Real-Time Machine Learning for Embedded Anomaly Detection
---

# Real-Time Machine Learning for Embedded Anomaly Detection
**arXiv**：[2512.19383v1](https://arxiv.org/abs/2512.19383) · [PDF](https://arxiv.org/pdf/2512.19383.pdf)  
**作者**：Abdelmadjid Benmachiche, Khadija Rais, Hamda Slimi  

**一句话要点**：综述嵌入式实时异常检测的机器学习方法，权衡精度与计算效率以应对资源受限边缘环境。

**关键词**：嵌入式异常检测, 实时机器学习, 轻量级算法, 资源约束优化, TinyML, 边缘计算

## 3 点简述
- 核心问题：资源受限的物联网边缘环境需实时异常检测，面临延迟、内存和功耗的严格约束。
- 方法要点：比较轻量级算法如孤立森林、单类SVM、循环架构和统计技术，分析嵌入式实现的现实挑战。
- 实验或效果：提供基于设备配置的算法选择建议和TinyML新趋势，以缩小检测能力与嵌入式现实间的差距。

## 摘要（原文）

> The spread of a resource-constrained Internet of Things (IoT) environment and embedded devices has put pressure on the real-time detection of anomalies occurring at the edge. This survey presents an overview of machine-learning methods aimed specifically at on-device anomaly detection with extremely strict constraints for latency, memory, and power consumption. Lightweight algorithms such as Isolation Forest, One-Class SVM, recurrent architectures, and statistical techniques are compared here according to the realities of embedded implementation. Our survey brings out significant trade-offs of accuracy and computational efficiency of detection, as well as how hardware constraints end up fundamentally redefining algorithm choice. The survey is completed with a set of practical recommendations on the choice of the algorithm depending on the equipment profiles and new trends in TinyML, which can help close the gap between detection capabilities and embedded reality. The paper serves as a strategic roadmap for engineers deploying anomaly detection in edge environments that are constrained by bandwidth and may be safety-critical.

