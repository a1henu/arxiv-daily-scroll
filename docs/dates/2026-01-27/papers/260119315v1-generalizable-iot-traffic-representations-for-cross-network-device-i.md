---
layout: default
title: Generalizable IoT Traffic Representations for Cross-Network Device Identification
---

# Generalizable IoT Traffic Representations for Cross-Network Device Identification
**arXiv**：[2601.19315v1](https://arxiv.org/abs/2601.19315) · [PDF](https://arxiv.org/pdf/2601.19315.pdf)  
**作者**：Arunan Sivanathan, David Warren, Deepak Mishra, Sushmita Ruj, Natasha Fernandes, Quan Z. Sheng, Minh Tran, Ben Luo, Daniel Coscia, Gustavo Batista, Hassan Habibi Gharakaheili  

**一句话要点**：提出无监督编码器学习通用IoT流量表示，用于跨网络设备识别

**关键词**：物联网设备识别, 无监督表示学习, 流量编码器, 跨网络泛化, 设备分类

## 3 点简述
- 核心问题：现有IoT设备识别方法依赖标注数据，泛化性受限，难以跨环境部署。
- 方法要点：设计紧凑编码器，从无标注流量学习嵌入，通过冻结编码器协议评估表示质量。
- 实验或效果：基于1800万真实流量，设备类型分类宏F1超0.9，展示跨环境鲁棒性。

## 摘要（原文）

> Machine learning models have demonstrated strong performance in classifying network traffic and identifying Internet-of-Things (IoT) devices, enabling operators to discover and manage IoT assets at scale. However, many existing approaches rely on end-to-end supervised pipelines or task-specific fine-tuning, resulting in traffic representations that are tightly coupled to labeled datasets and deployment environments, which can limit generalizability. In this paper, we study the problem of learning generalizable traffic representations for IoT device identification. We design compact encoder architectures that learn per-flow embeddings from unlabeled IoT traffic and evaluate them using a frozen-encoder protocol with a simple supervised classifier. Our specific contributions are threefold. (1) We develop unsupervised encoder--decoder models that learn compact traffic representations from unlabeled IoT network flows and assess their quality through reconstruction-based analysis. (2) We show that these learned representations can be used effectively for IoT device-type classification using simple, lightweight classifiers trained on frozen embeddings. (3) We provide a systematic benchmarking study against the state-of-the-art pretrained traffic encoders, showing that larger models do not necessarily yield more robust representations for IoT traffic. Using more than 18 million real IoT traffic flows collected across multiple years and deployment environments, we learn traffic representations from unlabeled data and evaluate device-type classification on disjoint labeled subsets, achieving macro F1-scores exceeding 0.9 for device-type classification and demonstrating robustness under cross-environment deployment.

