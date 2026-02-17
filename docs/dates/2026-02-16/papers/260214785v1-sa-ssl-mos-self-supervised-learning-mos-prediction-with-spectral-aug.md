---
layout: default
title: SA-SSL-MOS: Self-supervised Learning MOS Prediction with Spectral Augmentation for Generalized Multi-Rate Speech Assessment
---

# SA-SSL-MOS: Self-supervised Learning MOS Prediction with Spectral Augmentation for Generalized Multi-Rate Speech Assessment
**arXiv**：[2602.14785v1](https://arxiv.org/abs/2602.14785) · [PDF](https://arxiv.org/pdf/2602.14785.pdf)  
**作者**：Fengyuan Cao, Xinyu Liang, Fredrik Cumlin, Victor Ungureanu, Chandan K. A. Reddy, Christian Schuldt, Saikat Chatterjee  

**一句话要点**：提出谱图增强自监督学习方法，通过并行分支架构整合高频特征以解决多速率语音质量评估中数据有限的问题。

**关键词**：语音质量评估, 自监督学习, 多速率语音, 谱图增强, 高频特征, 两阶段训练

## 3 点简述
- 核心问题：多速率语音质量评估因训练数据有限和自监督模型丢弃高频信息而面临挑战。
- 方法要点：采用谱图增强自监督学习，通过并行分支整合高达48 kHz的高频特征，并实施两阶段训练方案。
- 实验或效果：实验表明利用高频信息能提升评估准确性，两阶段训练在数据有限时增强泛化能力。

## 摘要（原文）

> Designing a speech quality assessment (SQA) system for estimating mean-opinion-score (MOS) of multi-rate speech with varying sampling frequency (16-48 kHz) is a challenging task. The challenge arises due to the limited availability of a MOS-labeled training dataset comprising multi-rate speech samples. While self-supervised learning (SSL) models have been widely adopted in SQA to boost performance, a key limitation is that they are pretrained on 16 kHz speech and therefore discard high-frequency information present in higher sampling rates. To address this issue, we propose a spectrogram-augmented SSL method that incorporates high-frequency features (up to 48 kHz sampling rate) through a parallel-branch architecture. We further introduce a two-step training scheme: the model is first pre-trained on a large 48 kHz dataset and then fine-tuned on a smaller multi-rate dataset. Experimental results show that leveraging high-frequency information overlooked by SSL features is crucial for accurate multi-rate SQA, and that the proposed two-step training substantially improves generalization when multi-rate data is limited.

