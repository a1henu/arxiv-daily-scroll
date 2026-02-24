---
layout: default
title: HD-TTA: Hypothesis-Driven Test-Time Adaptation for Safer Brain Tumor Segmentation
---

# HD-TTA: Hypothesis-Driven Test-Time Adaptation for Safer Brain Tumor Segmentation
**arXiv**：[2602.19454v1](https://arxiv.org/abs/2602.19454) · [PDF](https://arxiv.org/pdf/2602.19454.pdf)  
**作者**：Kartik Jhawar, Lipo Wang  

**一句话要点**：提出假设驱动测试时适应以提升脑肿瘤分割安全性

**关键词**：测试时适应, 脑肿瘤分割, 安全关键应用, 几何假设, 跨域适应, 医学图像分析

## 3 点简述
- 标准测试时适应方法在医学分割中缺乏选择性，易导致肿瘤掩码溢出或预测退化。
- HD-TTA通过生成压缩与膨胀的几何假设，并基于纹理一致性选择最安全结果。
- 在跨域脑肿瘤分割任务中，HD-TTA显著降低Hausdorff距离并提高精度，同时保持Dice分数。

## 摘要（原文）

> Standard Test-Time Adaptation (TTA) methods typically treat inference as a blind optimization task, applying generic objectives to all or filtered test samples. In safety-critical medical segmentation, this lack of selectivity often causes the tumor mask to spill into healthy brain tissue or degrades predictions that were already correct. We propose Hypothesis-Driven TTA, a novel framework that reformulates adaptation as a dynamic decision process. Rather than forcing a single optimization trajectory, our method generates intuitive competing geometric hypotheses: compaction (is the prediction noisy? trim artifacts) versus inflation (is the valid tumor under-segmented? safely inflate to recover). It then employs a representation-guided selector to autonomously identify the safest outcome based on intrinsic texture consistency. Additionally, a pre-screening Gatekeeper prevents negative transfer by skipping adaptation on confident cases. We validate this proof-of-concept on a cross-domain binary brain tumor segmentation task, applying a source model trained on adult BraTS gliomas to unseen pediatric and more challenging meningioma target domains. HD-TTA improves safety-oriented outcomes (Hausdorff Distance (HD95) and Precision) over several state-of-the-art representative baselines in the challenging safety regime, reducing the HD95 by approximately 6.4 mm and improving Precision by over 4%, while maintaining comparable Dice scores. These results demonstrate that resolving the safety-adaptation trade-off via explicit hypothesis selection is a viable, robust path for safe clinical model deployment. Code will be made publicly available upon acceptance.

