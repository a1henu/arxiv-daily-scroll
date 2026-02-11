---
layout: default
title: Online Monitoring Framework for Automotive Time Series Data using JEPA Embeddings
---

# Online Monitoring Framework for Automotive Time Series Data using JEPA Embeddings
**arXiv**：[2602.09985v1](https://arxiv.org/abs/2602.09985) · [PDF](https://arxiv.org/pdf/2602.09985.pdf)  
**作者**：Alexander Fertig, Karthikeyan Chandra Sekaran, Lakshman Balasubramanian, Michael Botsch  

**一句话要点**：提出基于JEPA嵌入的在线监控框架，以无标签方式检测自动驾驶对象状态异常。

**关键词**：自动驾驶监控, 异常检测, 自监督学习, JEPA嵌入, 时间序列数据, 在线框架

## 3 点简述
- 核心问题：自动驾驶系统需在线监控未知异常，但缺乏异常标签难以训练。
- 方法要点：采用自监督JEPA预测任务生成对象嵌入，结合现有异常检测方法识别异常。
- 实验或效果：在nuScenes数据集上验证框架有效性，适用于真实环境未知异常检测。

## 摘要（原文）

> As autonomous vehicles are rolled out, measures must be taken to ensure their safe operation. In order to supervise a system that is already in operation, monitoring frameworks are frequently employed. These run continuously online in the background, supervising the system status and recording anomalies. This work proposes an online monitoring framework to detect anomalies in object state representations. Thereby, a key challenge is creating a framework for anomaly detection without anomaly labels, which are usually unavailable for unknown anomalies. To address this issue, this work applies a self-supervised embedding method to translate object data into a latent representation space. For this, a JEPA-based self-supervised prediction task is constructed, allowing training without anomaly labels and the creation of rich object embeddings. The resulting expressive JEPA embeddings serve as input for established anomaly detection methods, in order to identify anomalies within object state representations. This framework is particularly useful for applications in real-world environments, where new or unknown anomalies may occur during operation for which there are no labels available. Experiments performed on the publicly available, real-world nuScenes dataset illustrate the framework's capabilities.

