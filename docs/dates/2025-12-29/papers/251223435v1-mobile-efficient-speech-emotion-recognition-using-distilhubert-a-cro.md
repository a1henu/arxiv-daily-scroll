---
layout: default
title: Mobile-Efficient Speech Emotion Recognition Using DistilHuBERT: A Cross-Corpus Validation Study
---

# Mobile-Efficient Speech Emotion Recognition Using DistilHuBERT: A Cross-Corpus Validation Study
**arXiv**：[2512.23435v1](https://arxiv.org/abs/2512.23435) · [PDF](https://arxiv.org/pdf/2512.23435.pdf)  
**作者**：Saifelden M. Ismail  

**一句话要点**：提出基于DistilHuBERT的移动高效语音情感识别系统，实现模型压缩与跨语料泛化。

**关键词**：语音情感识别, 模型蒸馏, 量化压缩, 跨语料验证, 移动部署

## 3 点简述
- 核心问题：语音情感识别在移动部署中受限于Transformer架构的计算需求。
- 方法要点：采用蒸馏和8位量化技术压缩模型，结合跨语料训练提升泛化能力。
- 实验或效果：在IEMOCAP上实现61.4%未加权准确率，模型仅23MB，跨语料训练改善性能指标。

## 摘要（原文）

> Speech Emotion Recognition (SER) has significant potential for mobile applications, yet deployment remains constrained by the computational demands of state-of-the-art transformer architectures. This paper presents a mobile-efficient SER system based on DistilHuBERT, a distilled and 8-bit quantized transformer that achieves 92% parameter reduction compared to full-scale Wav2Vec 2.0 models while maintaining competitive accuracy. We conduct a rigorous 5-fold Leave-One-Session-Out (LOSO) cross-validation on the IEMOCAP dataset to ensure speaker independence, augmented with cross-corpus training on CREMA-D to enhance generalization. Cross-corpus training with CREMA-D yields a 1.2% improvement in Weighted Accuracy, a 1.4% gain in Macro F1-score, and a 32% reduction in cross-fold variance, with the Neutral class showing the most substantial benefit at 5.4% F1-score improvement. Our approach achieves an Unweighted Accuracy of 61.4% with a quantized model footprint of only 23 MB, representing approximately 91% of full-scale baseline performance. Cross-corpus evaluation on RAVDESS reveals that the theatrical nature of acted emotions causes predictions to cluster by arousal level rather than valence: happiness is systematically confused with anger due to acoustic saturation in high-energy expressions. Despite this theatricality effect reducing overall RAVDESS accuracy to 43.29%, the model maintains robust arousal detection with 97% recall for anger and 64% for sadness. These findings establish a Pareto-optimal tradeoff between model size and accuracy, enabling practical affect recognition on resource-constrained mobile devices.

