---
layout: default
title: The Invisible Gorilla Effect in Out-of-distribution Detection
---

# The Invisible Gorilla Effect in Out-of-distribution Detection
**arXiv**：[2602.20068v1](https://arxiv.org/abs/2602.20068) · [PDF](https://arxiv.org/pdf/2602.20068.pdf)  
**作者**：Harry Anthony, Ziyun Liang, Hermione Warr, Konstantinos Kamnitsas  

**一句话要点**：揭示OOD检测中的隐形大猩猩效应：当伪影与模型感兴趣区域视觉相似时检测性能提升

**关键词**：OOD检测, 视觉相似性, 模型偏差, 伪影分析, 鲁棒性评估

## 3 点简述
- 核心问题：OOD检测性能受伪影与模型感兴趣区域视觉相似性影响，导致检测偏差。
- 方法要点：通过颜色标注伪影和生成颜色交换反事实，系统评估40种OOD方法。
- 实验或效果：在皮肤病变分类器中，红色墨水伪影检测AUROC比黑色墨水高31.5%。

## 摘要（原文）

> Deep Neural Networks achieve high performance in vision tasks by learning features from regions of interest (ROI) within images, but their performance degrades when deployed on out-of-distribution (OOD) data that differs from training data. This challenge has led to OOD detection methods that aim to identify and reject unreliable predictions. Although prior work shows that OOD detection performance varies by artefact type, the underlying causes remain underexplored. To this end, we identify a previously unreported bias in OOD detection: for hard-to-detect artefacts (near-OOD), detection performance typically improves when the artefact shares visual similarity (e.g. colour) with the model's ROI and drops when it does not - a phenomenon we term the Invisible Gorilla Effect. For example, in a skin lesion classifier with red lesion ROI, we show the method Mahalanobis Score achieves a 31.5% higher AUROC when detecting OOD red ink (similar to ROI) compared to black ink (dissimilar) annotations. We annotated artefacts by colour in 11,355 images from three public datasets (e.g. ISIC) and generated colour-swapped counterfactuals to rule out dataset bias. We then evaluated 40 OOD methods across 7 benchmarks and found significant performance drops for most methods when artefacts differed from the ROI. Our findings highlight an overlooked failure mode in OOD detection and provide guidance for more robust detectors. Code and annotations are available at: https://github.com/HarryAnthony/Invisible_Gorilla_Effect.

