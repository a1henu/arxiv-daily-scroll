---
layout: default
title: Expectation and Acoustic Neural Network Representations Enhance Music Identification from Brain Activity
---

# Expectation and Acoustic Neural Network Representations Enhance Music Identification from Brain Activity
**arXiv**：[2603.03190v1](https://arxiv.org/abs/2603.03190) · [PDF](https://arxiv.org/pdf/2603.03190.pdf)  
**作者**：Shogo Noguchi, Taketo Akama, Tai Nakamura, Shun Minamikawa, Natalia Polouliakh  

**一句话要点**：提出区分声学与期望相关ANN表示作为教师目标，以提升基于EEG的音乐识别性能

**关键词**：音乐识别, 脑电图解码, 表示学习, 神经网络表示, 预测编码, 教师目标

## 3 点简述
- 核心问题：音乐聆听时脑皮层活动编码声学与期望信息，如何利用ANN表示增强EEG识别
- 方法要点：将ANN表示区分为声学与期望相关两类作为教师目标，用于预训练EEG模型
- 实验或效果：预训练模型优于基线，结合两类表示获得互补增益，超越随机初始化集成

## 摘要（原文）

> During music listening, cortical activity encodes both acoustic and expectation-related information. Prior work has shown that ANN representations resemble cortical representations and can serve as supervisory signals for EEG recognition. Here we show that distinguishing acoustic and expectation-related ANN representations as teacher targets improves EEG-based music identification. Models pretrained to predict either representation outperform non-pretrained baselines, and combining them yields complementary gains that exceed strong seed ensembles formed by varying random initializations. These findings show that teacher representation type shapes downstream performance and that representation learning can be guided by neural encoding. This work points toward advances in predictive music cognition and neural decoding. Our expectation representation, computed directly from raw signals without manual labels, reflects predictive structure beyond onset or pitch, enabling investigation of multilayer predictive encoding across diverse stimuli. Its scalability to large, diverse datasets further suggests potential for developing general-purpose EEG models grounded in cortical encoding principles.

