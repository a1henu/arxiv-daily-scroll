---
layout: default
title: Hybrid SIFT-SNN for Efficient Anomaly Detection of Traffic Flow-Control Infrastructure
---

# Hybrid SIFT-SNN for Efficient Anomaly Detection of Traffic Flow-Control Infrastructure
**arXiv**：[2511.21337v1](https://arxiv.org/abs/2511.21337) · [PDF](https://arxiv.org/pdf/2511.21337.pdf)  
**作者**：Munish Rathee, Boris Bačić, Maryam Doborjeh  

**一句话要点**：提出SIFT-SNN混合框架以实时检测交通基础设施结构异常

**关键词**：异常检测, 脉冲神经网络, 空间特征编码, 实时处理, 交通基础设施, 低功耗部署

## 3 点简述
- 核心问题：实时检测交通流控基础设施的结构异常，需低延迟和高能效。
- 方法要点：结合SIFT空间特征编码与LIF脉冲神经网络，实现稀疏处理和可解释性。
- 实验或效果：在奥克兰海港大桥数据集上达到92.3%准确率，每帧推理时间9.5毫秒。

## 摘要（原文）

> This paper presents the SIFT-SNN framework, a low-latency neuromorphic signal-processing pipeline for real-time detection of structural anomalies in transport infrastructure. The proposed approach integrates Scale-Invariant Feature Transform (SIFT) for spatial feature encoding with a latency-driven spike conversion layer and a Leaky Integrate-and-Fire (LIF) Spiking Neural Network (SNN) for classification. The Auckland Harbour Bridge dataset is recorded under various weather and lighting conditions, comprising 6,000 labelled frames that include both real and synthetically augmented unsafe cases. The presented system achieves a classification accuracy of 92.3% (+- 0.8%) with a per-frame inference time of 9.5 ms. Achieved sub-10 millisecond latency, combined with sparse spike activity (8.1%), enables real-time, low-power edge deployment. Unlike conventional CNN-based approaches, the hybrid SIFT-SNN pipeline explicitly preserves spatial feature grounding, enhances interpretability, supports transparent decision-making, and operates efficiently on embedded hardware. Although synthetic augmentation improved robustness, generalisation to unseen field conditions remains to be validated. The SIFT-SNN framework is validated through a working prototype deployed on a consumer-grade system and framed as a generalisable case study in structural safety monitoring for movable concrete barriers, which, as a traffic flow-control infrastructure, is deployed in over 20 cities worldwide.

