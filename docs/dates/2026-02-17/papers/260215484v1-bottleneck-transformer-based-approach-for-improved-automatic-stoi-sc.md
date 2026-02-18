---
layout: default
title: Bottleneck Transformer-Based Approach for Improved Automatic STOI Score Prediction
---

# Bottleneck Transformer-Based Approach for Improved Automatic STOI Score Prediction
**arXiv**：[2602.15484v1](https://arxiv.org/abs/2602.15484) · [PDF](https://arxiv.org/pdf/2602.15484.pdf)  
**作者**：Amartyaveer, Murali Kadambi, Chandra Mohan Sharma, Anupam Mondal, Prasanta Kumar Ghosh  

**一句话要点**：提出瓶颈变换器方法以改进非侵入式STOI分数预测

**关键词**：语音质量评估, 非侵入式方法, 瓶颈变换器, 多头自注意力, 深度学习

## 3 点简述
- 核心问题：传统STOI计算依赖干净参考语音，限制实际应用。
- 方法要点：结合卷积块学习帧级特征，使用多头自注意力层聚合信息。
- 实验或效果：在已见和未见场景中，相比最先进模型，相关性更高、均方误差更低。

## 摘要（原文）

> In this study, we have presented a novel approach to predict the Short-Time Objective Intelligibility (STOI) metric using a bottleneck transformer architecture. Traditional methods for calculating STOI typically requires clean reference speech, which limits their applicability in the real world. To address this, numerous deep learning-based nonintrusive speech assessment models have garnered significant interest. Many studies have achieved commendable performance, but there is room for further improvement.
>   We propose the use of bottleneck transformer, incorporating convolution blocks for learning frame-level features and a multi-head self-attention (MHSA) layer to aggregate the information. These components enable the transformer to focus on the key aspects of the input data. Our model has shown higher correlation and lower mean squared error for both seen and unseen scenarios compared to the state-of-the-art model using self-supervised learning (SSL) and spectral features as inputs.

