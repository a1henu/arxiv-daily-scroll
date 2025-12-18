---
layout: default
title: Automated Motion Artifact Check for MRI (AutoMAC-MRI): An Interpretable Framework for Motion Artifact Detection and Severity Assessment
---

# Automated Motion Artifact Check for MRI (AutoMAC-MRI): An Interpretable Framework for Motion Artifact Detection and Severity Assessment
**arXiv**：[2512.15315v1](https://arxiv.org/abs/2512.15315) · [PDF](https://arxiv.org/pdf/2512.15315.pdf)  
**作者**：Antony Jerald, Dattesh Shanbhag, Sudhanya Chatterjee  

**一句话要点**：提出AutoMAC-MRI框架，用于MRI运动伪影检测与严重性评估，提升可解释性。

**关键词**：MRI运动伪影检测, 可解释性框架, 监督对比学习, 亲和力评分, 图像质量评估

## 3 点简述
- 核心问题：MRI运动伪影降低图像质量，现有方法多为二元决策且缺乏可解释性。
- 方法要点：使用监督对比学习学习运动严重性表示，通过亲和力评分实现透明分级。
- 实验或效果：在5000多张脑MRI切片上评估，亲和力评分与专家标注一致，支持在线质量控制。

## 摘要（原文）

> Motion artifacts degrade MRI image quality and increase patient recalls. Existing automated quality assessment methods are largely limited to binary decisions and provide little interpretability. We introduce AutoMAC-MRI, an explainable framework for grading motion artifacts across heterogeneous MR contrasts and orientations. The approach uses supervised contrastive learning to learn a discriminative representation of motion severity. Within this feature space, we compute grade-specific affinity scores that quantify an image's proximity to each motion grade, thereby making grade assignments transparent and interpretable. We evaluate AutoMAC-MRI on more than 5000 expert-annotated brain MRI slices spanning multiple contrasts and views. Experiments assessing affinity scores against expert labels show that the scores align well with expert judgment, supporting their use as an interpretable measure of motion severity. By coupling accurate grade detection with per-grade affinity scoring, AutoMAC-MRI enables inline MRI quality control, with the potential to reduce unnecessary rescans and improve workflow efficiency.

