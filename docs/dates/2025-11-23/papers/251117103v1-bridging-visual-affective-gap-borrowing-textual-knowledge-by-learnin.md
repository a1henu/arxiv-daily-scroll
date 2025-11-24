---
layout: default
title: Bridging Visual Affective Gap: Borrowing Textual Knowledge by Learning from Noisy Image-Text Pairs
---

# Bridging Visual Affective Gap: Borrowing Textual Knowledge by Learning from Noisy Image-Text Pairs
**arXiv**：[2511.17103v1](https://arxiv.org/abs/2511.17103) · [PDF](https://arxiv.org/pdf/2511.17103.pdf)  
**作者**：Daiqing Wu, Dongbao Yang, Yu Zhou, Can Ma  

**一句话要点**：提出分区自适应对比学习以解决视觉情感识别中的情感鸿沟问题

**关键词**：视觉情感识别, 情感鸿沟, 对比学习, 图像-文本对, 预训练模型, 噪声数据

## 3 点简述
- 核心问题：视觉情感识别中预训练模型存在情感鸿沟，即事实特征与情感类别缺乏直接关联
- 方法要点：利用噪声图像-文本对，通过分区自适应对比学习动态构建正负样本对
- 实验或效果：在情感相关下游任务中显著提升多种预训练视觉模型的性能

## 摘要（原文）

> Visual emotion recognition (VER) is a longstanding field that has garnered increasing attention with the advancement of deep neural networks. Although recent studies have achieved notable improvements by leveraging the knowledge embedded within pre-trained visual models, the lack of direct association between factual-level features and emotional categories, called the "affective gap", limits the applicability of pre-training knowledge for VER tasks. On the contrary, the explicit emotional expression and high information density in textual modality eliminate the "affective gap". Therefore, we propose borrowing the knowledge from the pre-trained textual model to enhance the emotional perception of pre-trained visual models. We focus on the factual and emotional connections between images and texts in noisy social media data, and propose Partitioned Adaptive Contrastive Learning (PACL) to leverage these connections. Specifically, we manage to separate different types of samples and devise distinct contrastive learning strategies for each type. By dynamically constructing negative and positive pairs, we fully exploit the potential of noisy samples. Through comprehensive experiments, we demonstrate that bridging the "affective gap" significantly improves the performance of various pre-trained visual models in downstream emotion-related tasks. Our code is released on https://github.com/wdqqdw/PACL.

