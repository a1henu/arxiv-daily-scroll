---
layout: default
title: ADNet: A Large-Scale and Extensible Multi-Domain Benchmark for Anomaly Detection Across 380 Real-World Categories
---

# ADNet: A Large-Scale and Extensible Multi-Domain Benchmark for Anomaly Detection Across 380 Real-World Categories
**arXiv**：[2511.20169v1](https://arxiv.org/abs/2511.20169) · [PDF](https://arxiv.org/pdf/2511.20169.pdf)  
**作者**：Hai Ling, Jia Guo, Zhulin Tao, Yunkang Cao, Donglin Di, Hongyan Xu, Xiu Su, Yang Song, Lei Fan  

**一句话要点**：提出ADNet基准和Dinomaly-m方法以解决大规模多领域异常检测的泛化挑战

**关键词**：异常检测基准, 多领域数据集, 混合专家模型, 像素级标注, 可扩展性评估

## 3 点简述
- 现有异常检测基准覆盖类别有限，限制跨上下文泛化与可扩展性评估
- 引入ADNet基准，含380类别和标准化多模态标注，支持大规模异常检测
- Dinomaly-m方法在扩展类别时提升性能，I-AUROC达83.2%，优于现有方法

## 摘要（原文）

> Anomaly detection (AD) aims to identify defects using normal-only training data. Existing anomaly detection benchmarks (e.g., MVTec-AD with 15 categories) cover only a narrow range of categories, limiting the evaluation of cross-context generalization and scalability. We introduce ADNet, a large-scale, multi-domain benchmark comprising 380 categories aggregated from 49 publicly available datasets across Electronics, Industry, Agrifood, Infrastructure, and Medical domains. The benchmark includes a total of 196,294 RGB images, consisting of 116,192 normal samples for training and 80,102 test images, of which 60,311 are anomalous. All images are standardized with MVTec-style pixel-level annotations and structured text descriptions spanning both spatial and visual attributes, enabling multimodal anomaly detection tasks. Extensive experiments reveal a clear scalability challenge: existing state-of-the-art methods achieve 90.6% I-AUROC in one-for-one settings but drop to 78.5% when scaling to all 380 categories in a multi-class setting. To address this, we propose Dinomaly-m, a context-guided Mixture-of-Experts extension of Dinomaly that expands decoder capacity without increasing inference cost. It achieves 83.2% I-AUROC and 93.1% P-AUROC, demonstrating superior performance over existing approaches. ADNet is designed as a standardized and extensible benchmark, supporting the community in expanding anomaly detection datasets across diverse domains and providing a scalable foundation for future anomaly detection foundation models. Dataset: https://grainnet.github.io/ADNet

