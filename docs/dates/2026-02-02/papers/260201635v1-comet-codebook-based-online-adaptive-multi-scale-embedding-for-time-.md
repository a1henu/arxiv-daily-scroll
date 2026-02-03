---
layout: default
title: COMET: Codebook-based Online-adaptive Multi-scale Embedding for Time-series Anomaly Detection
---

# COMET: Codebook-based Online-adaptive Multi-scale Embedding for Time-series Anomaly Detection
**arXiv**：[2602.01635v1](https://arxiv.org/abs/2602.01635) · [PDF](https://arxiv.org/pdf/2602.01635.pdf)  
**作者**：Jinwoo Park, Hyeongwon Kang, Seung Hun Han, Pilsung Kang  

**一句话要点**：提出COMET方法，通过码本在线自适应多尺度嵌入解决时间序列异常检测中的分布偏移问题。

**关键词**：时间序列异常检测, 多尺度嵌入, 向量量化, 在线自适应, 码本学习, 对比学习

## 3 点简述
- 核心问题：时间序列异常检测中，补丁级表示学习未充分探索时间依赖性和多变量相关性，且单尺度模式限制检测范围，正常数据表示易受推理时分布偏移影响。
- 方法要点：COMET包含多尺度补丁编码、向量量化核心集学习和在线码本自适应，结合量化误差与记忆距离的双重评分检测异常。
- 实验或效果：在五个基准数据集上，COMET在45个评估指标中的36个取得最佳性能，验证了其跨环境有效性。

## 摘要（原文）

> Time series anomaly detection is a critical task across various industrial domains. However, capturing temporal dependencies and multivariate correlations within patch-level representation learning remains underexplored, and reliance on single-scale patterns limits the detection of anomalies across different temporal ranges. Furthermore, focusing on normal data representations makes models vulnerable to distribution shifts at inference time. To address these limitations, we propose Codebook-based Online-adaptive Multi-scale Embedding for Time-series anomaly detection (COMET), which consists of three key components: (1) Multi-scale Patch Encoding captures temporal dependencies and inter-variable correlations across multiple patch scales. (2) Vector-Quantized Coreset learns representative normal patterns via codebook and detects anomalies with a dual-score combining quantization error and memory distance. (3) Online Codebook Adaptation generates pseudo-labels based on codebook entries and dynamically adapts the model at inference through contrastive learning. Experiments on five benchmark datasets demonstrate that COMET achieves the best performance in 36 out of 45 evaluation metrics, validating its effectiveness across diverse environments.

