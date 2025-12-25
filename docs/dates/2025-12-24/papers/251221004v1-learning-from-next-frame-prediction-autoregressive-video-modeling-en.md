---
layout: default
title: Learning from Next-Frame Prediction: Autoregressive Video Modeling Encodes Effective Representations
---

# Learning from Next-Frame Prediction: Autoregressive Video Modeling Encodes Effective Representations
**arXiv**：[2512.21004v1](https://arxiv.org/abs/2512.21004) · [PDF](https://arxiv.org/pdf/2512.21004.pdf)  
**作者**：Jinghan Li, Yang Jin, Hao Jiang, Yadong Mu, Yang Song, Kun Xu  

**一句话要点**：提出NExT-Vid框架，通过掩码下一帧预测实现自回归视觉生成预训练，以提升视频表示学习效果。

**关键词**：自回归视觉生成, 下一帧预测, 视频表示学习, 条件流匹配, 上下文隔离预测, 生成预训练

## 3 点简述
- 核心问题：现有视觉生成预训练方法忽视时间信息或存在语义定位不准、生成质量差的问题。
- 方法要点：引入上下文隔离自回归预测器和条件流匹配解码器，联合建模图像与视频。
- 实验或效果：在大规模预训练模型上通过下游分类任务验证，性能优于先前生成预训练方法。

## 摘要（原文）

> Recent advances in pretraining general foundation models have significantly improved performance across diverse downstream tasks. While autoregressive (AR) generative models like GPT have revolutionized NLP, most visual generative pretraining methods still rely on BERT-style masked modeling, which often disregards the temporal information essential for video analysis. The few existing autoregressive visual pretraining methods suffer from issues such as inaccurate semantic localization and poor generation quality, leading to poor semantics. In this work, we propose NExT-Vid, a novel autoregressive visual generative pretraining framework that utilizes masked next-frame prediction to jointly model images and videos. NExT-Vid introduces a context-isolated autoregressive predictor to decouple semantic representation from target decoding, and a conditioned flow-matching decoder to enhance generation quality and diversity. Through context-isolated flow-matching pretraining, our approach achieves strong representations. Extensive experiments on large-scale pretrained models demonstrate that our proposed method consistently outperforms previous generative pretraining methods for visual representation learning via attentive probing in downstream classification.

