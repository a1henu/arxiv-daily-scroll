---
layout: default
title: Scaling Ambiguity: Augmenting Human Annotation in Speech Emotion Recognition with Audio-Language Models
---

# Scaling Ambiguity: Augmenting Human Annotation in Speech Emotion Recognition with Audio-Language Models
**arXiv**：[2601.14620v1](https://arxiv.org/abs/2601.14620) · [PDF](https://arxiv.org/pdf/2601.14620.pdf)  
**作者**：Wenda Zhang, Hongyu Jin, Siyi Wang, Zhiqiang Wei, Ting Dang  

**一句话要点**：提出利用音频-语言模型生成合成感知代理，以增强语音情感识别中的模糊情感标注。

**关键词**：语音情感识别, 模糊情感识别, 音频-语言模型, 合成标注, 分布增强, 多模态情感分析

## 3 点简述
- 核心问题：语音情感识别中，单类别标签忽略情感模糊性，而基于稀疏人工标注的真实分布不可靠。
- 方法要点：利用大型音频-语言模型生成合成标注，增强人工标注，并引入分布感知多模态情感增强策略。
- 实验或效果：在IEMOCAP和MSP-Podcast数据集上，合成标注改善情感分布，尤其在低模糊区域有效，但对高模糊情感效果有限。

## 摘要（原文）

> Speech Emotion Recognition models typically use single categorical labels, overlooking the inherent ambiguity of human emotions. Ambiguous Emotion Recognition addresses this by representing emotions as probability distributions, but progress is limited by unreliable ground-truth distributions inferred from sparse human annotations. This paper explores whether Large Audio-Language Models (ALMs) can mitigate the annotation bottleneck by generating high-quality synthetic annotations. We introduce a framework leveraging ALMs to create Synthetic Perceptual Proxies, augmenting human annotations to improve ground-truth distribution reliability. We validate these proxies through statistical analysis of their alignment with human distributions and evaluate their impact by fine-tuning ALMs with the augmented emotion distributions. Furthermore, to address class imbalance and enable unbiased evaluation, we propose DiME-Aug, a Distribution-aware Multimodal Emotion Augmentation strategy. Experiments on IEMOCAP and MSP-Podcast show that synthetic annotations enhance emotion distribution, especially in low-ambiguity regions where annotation agreement is high. However, benefits diminish for highly ambiguous emotions with greater human disagreement. This work provides the first evidence that ALMs could address annotation scarcity in ambiguous emotion recognition, but highlights the need for more advanced prompting or generation strategies to handle highly ambiguous cases.

