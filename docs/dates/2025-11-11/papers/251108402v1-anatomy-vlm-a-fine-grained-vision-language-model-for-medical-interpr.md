---
layout: default
title: Anatomy-VLM: A Fine-grained Vision-Language Model for Medical Interpretation
---

# Anatomy-VLM: A Fine-grained Vision-Language Model for Medical Interpretation
**arXiv**：[2511.08402v1](https://arxiv.org/abs/2511.08402) · [PDF](https://arxiv.org/pdf/2511.08402.pdf)  
**作者**：Difei Gu, Yunhe Gao, Mu Zhou, Dimitris Metaxas  

**一句话要点**：提出Anatomy-VLM以解决医学影像中细粒度特征忽略导致的疾病诊断挑战

**关键词**：细粒度视觉语言模型, 医学影像诊断, 多尺度信息对齐, 解剖结构定位, 零样本解释

## 3 点简述
- 核心问题：医学影像异质性使疾病诊断困难，现有视觉语言模型忽略关键细粒度图像细节
- 方法要点：设计模型定位关键解剖结构，结合结构化知识进行多尺度信息对齐
- 实验或效果：在分布内外数据集表现优异，支持零样本解剖解释和下游分割任务

## 摘要（原文）

> Accurate disease interpretation from radiology remains challenging due to imaging heterogeneity. Achieving expert-level diagnostic decisions requires integration of subtle image features with clinical knowledge. Yet major vision-language models (VLMs) treat images as holistic entities and overlook fine-grained image details that are vital for disease diagnosis. Clinicians analyze images by utilizing their prior medical knowledge and identify anatomical structures as important region of interests (ROIs). Inspired from this human-centric workflow, we introduce Anatomy-VLM, a fine-grained, vision-language model that incorporates multi-scale information. First, we design a model encoder to localize key anatomical features from entire medical images. Second, these regions are enriched with structured knowledge for contextually-aware interpretation. Finally, the model encoder aligns multi-scale medical information to generate clinically-interpretable disease prediction. Anatomy-VLM achieves outstanding performance on both in- and out-of-distribution datasets. We also validate the performance of Anatomy-VLM on downstream image segmentation tasks, suggesting that its fine-grained alignment captures anatomical and pathology-related knowledge. Furthermore, the Anatomy-VLM's encoder facilitates zero-shot anatomy-wise interpretation, providing its strong expert-level clinical interpretation capabilities.

