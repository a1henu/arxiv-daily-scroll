---
layout: default
title: Time2Vec-Integrated Transformer for Robust Gesture Recognition from Low-Density sEMG
---

# Time2Vec-Integrated Transformer for Robust Gesture Recognition from Low-Density sEMG
**arXiv**：[2602.01855v1](https://arxiv.org/abs/2602.01855) · [PDF](https://arxiv.org/pdf/2602.01855.pdf)  
**作者**：Blagoj Hristov, Hristijan Gjoreski, Vesna Ojleska Latkoska, Gorjan Nadzinski  

**一句话要点**：提出集成Time2Vec的Transformer框架，用于稀疏双通道sEMG的鲁棒手势识别。

**关键词**：手势识别, 表面肌电信号, Transformer, 时间嵌入, 数据高效学习, 假肢控制

## 3 点简述
- 核心问题：高密度传感器阵列限制肌电假肢控制的可及性，需数据高效方法。
- 方法要点：集成Time2Vec学习时间嵌入，采用归一化加性融合策略对齐时空特征分布。
- 实验或效果：在10类手势集上达到95.7% F1分数，快速校准协议提升未见受试者性能至96.9%。

## 摘要（原文）

> Accurate and responsive myoelectric prosthesis control typically relies on complex, dense multi-sensor arrays, which limits consumer accessibility. This paper presents a novel, data-efficient deep learning framework designed to achieve precise and accurate control using minimal sensor hardware. Leveraging an external dataset of 8 subjects, our approach implements a hybrid Transformer optimized for sparse, two-channel surface electromyography (sEMG). Unlike standard architectures that use fixed positional encodings, we integrate Time2Vec learnable temporal embeddings to capture the stochastic temporal warping inherent in biological signals. Furthermore, we employ a normalized additive fusion strategy that aligns the latent distributions of spatial and temporal features, preventing the destructive interference common in standard implementations. A two-stage curriculum learning protocol is utilized to ensure robust feature extraction despite data scarcity. The proposed architecture achieves a state-of-the-art multi-subject F1-score of 95.7% $\pm$ 0.20% for a 10-class movement set, statistically outperforming both a standard Transformer with fixed encodings and a recurrent CNN-LSTM model. Architectural optimization reveals that a balanced allocation of model capacity between spatial and temporal dimensions yields the highest stability. Furthermore, while direct transfer to a new unseen subject led to poor accuracy due to domain shifts, a rapid calibration protocol utilizing only two trials per gesture recovered performance from 21.0% $\pm$ 2.98% to 96.9% $\pm$ 0.52%. By validating that high-fidelity temporal embeddings can compensate for low spatial resolution, this work challenges the necessity of high-density sensing. The proposed framework offers a robust, cost-effective blueprint for next-generation prosthetic interfaces capable of rapid personalization.

