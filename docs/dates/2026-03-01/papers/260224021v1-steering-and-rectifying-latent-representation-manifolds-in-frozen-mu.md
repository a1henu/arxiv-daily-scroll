---
layout: default
title: Steering and Rectifying Latent Representation Manifolds in Frozen Multi-modal LLMs for Video Anomaly Detection
---

# Steering and Rectifying Latent Representation Manifolds in Frozen Multi-modal LLMs for Video Anomaly Detection
**arXiv**：[2602.24021v1](https://arxiv.org/abs/2602.24021) · [PDF](https://arxiv.org/pdf/2602.24021.pdf)  
**作者**：Zhaolin Cai, Fan Li, Huiyu Duan, Lijun He, Guangtao Zhai  

**一句话要点**：提出SteerVAD框架，通过主动干预冻结多模态大语言模型的潜在表示流形，以提升视频异常检测性能。

**关键词**：视频异常检测, 多模态大语言模型, 表示流形干预, 无梯度分析, 分层元控制器, 调优免费方法

## 3 点简述
- 核心问题：冻结多模态大语言模型在视频异常检测中因预训练偏见和表示不适应，难以处理细微或模糊异常。
- 方法要点：利用无梯度表示可分性分析识别关键注意力头，并通过分层元控制器生成动态校正信号，对表示流形进行各向异性缩放。
- 实验或效果：在主流基准测试中，仅需1%训练数据即实现调优免费方法中的最先进性能。

## 摘要（原文）

> Video anomaly detection (VAD) aims to identify abnormal events in videos. Traditional VAD methods generally suffer from the high costs of labeled data and full training, thus some recent works have explored leveraging frozen multi-modal large language models (MLLMs) in a tuning-free manner to perform VAD. However, their performance is limited as they directly inherit pre-training biases and cannot adapt internal representations to specific video contexts, leading to difficulties in handling subtle or ambiguous anomalies. To address these limitations, we propose a novel intervention framework, termed SteerVAD, which advances MLLM-based VAD by shifting from passively reading to actively steering and rectifying internal representations. Our approach first leverages the gradient-free representational separability analysis (RSA) to identify top attention heads as latent anomaly experts (LAEs) which are most discriminative for VAD. Then a hierarchical meta-controller (HMC) generates dynamic rectification signals by jointly conditioning on global context and these LAE outputs. The signals execute targeted, anisotropic scaling directly upon the LAE representation manifolds, amplifying anomaly-relevant dimensions while suppressing inherent biases. Extensive experiments on mainstream benchmarks demonstrate our method achieves state-of-the-art performance among tuning-free approaches requiring only 1% of training data, establishing it as a powerful new direction for video anomaly detection. The code will be released upon the publication.

