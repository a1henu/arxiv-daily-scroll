---
layout: default
title: AnomalyVFM -- Transforming Vision Foundation Models into Zero-Shot Anomaly Detectors
---

# AnomalyVFM -- Transforming Vision Foundation Models into Zero-Shot Anomaly Detectors
**arXiv**：[2601.20524v1](https://arxiv.org/abs/2601.20524) · [PDF](https://arxiv.org/pdf/2601.20524.pdf)  
**作者**：Matic Fučka, Vitjan Zavrtanik, Danijel Skočaj  

**一句话要点**：提出AnomalyVFM框架，将视觉基础模型转化为零样本异常检测器

**关键词**：零样本异常检测, 视觉基础模型, 合成数据集生成, 参数高效适应, 低秩特征适配器, 置信度加权损失

## 3 点简述
- 核心问题：现有视觉基础模型在零样本异常检测中性能落后，源于数据集多样性不足和适应策略浅层
- 方法要点：结合三阶段合成数据集生成与参数高效适应机制，使用低秩特征适配器和置信度加权像素损失
- 实验或效果：以RADIO为骨干，在9个数据集上平均图像级AUROC达94.1%，超越先前方法3.3个百分点

## 摘要（原文）

> Zero-shot anomaly detection aims to detect and localise abnormal regions in the image without access to any in-domain training images. While recent approaches leverage vision-language models (VLMs), such as CLIP, to transfer high-level concept knowledge, methods based on purely vision foundation models (VFMs), like DINOv2, have lagged behind in performance. We argue that this gap stems from two practical issues: (i) limited diversity in existing auxiliary anomaly detection datasets and (ii) overly shallow VFM adaptation strategies. To address both challenges, we propose AnomalyVFM, a general and effective framework that turns any pretrained VFM into a strong zero-shot anomaly detector. Our approach combines a robust three-stage synthetic dataset generation scheme with a parameter-efficient adaptation mechanism, utilising low-rank feature adapters and a confidence-weighted pixel loss. Together, these components enable modern VFMs to substantially outperform current state-of-the-art methods. More specifically, with RADIO as a backbone, AnomalyVFM achieves an average image-level AUROC of 94.1% across 9 diverse datasets, surpassing previous methods by significant 3.3 percentage points. Project Page: https://maticfuc.github.io/anomaly_vfm/

