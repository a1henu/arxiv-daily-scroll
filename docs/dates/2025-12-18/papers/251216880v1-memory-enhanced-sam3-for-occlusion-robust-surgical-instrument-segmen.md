---
layout: default
title: Memory-Enhanced SAM3 for Occlusion-Robust Surgical Instrument Segmentation
---

# Memory-Enhanced SAM3 for Occlusion-Robust Surgical Instrument Segmentation
**arXiv**：[2512.16880v1](https://arxiv.org/abs/2512.16880) · [PDF](https://arxiv.org/pdf/2512.16880.pdf)  
**作者**：Valay Bundele, Mehran Hosseinzadeh, Hendrik P. A. Lensch  

**一句话要点**：提出ReMeDI-SAM3以解决内窥镜视频中手术器械分割的遮挡问题

**关键词**：手术器械分割, 视频对象分割, 遮挡鲁棒性, 内存增强, 零样本学习, 内窥镜视频

## 3 点简述
- 核心问题：SAM3在手术场景中因内存更新不区分、容量固定和遮挡后身份恢复弱而性能受限
- 方法要点：通过相关性感知内存过滤、分段插值扩展容量和基于特征的再识别模块增强SAM3
- 实验或效果：在EndoVis17和EndoVis18上零样本评估，mcIoU分别提升约7%和16%，优于训练方法

## 摘要（原文）

> Accurate surgical instrument segmentation in endoscopic videos is crucial for computer-assisted interventions, yet remains challenging due to frequent occlusions, rapid motion, specular artefacts, and long-term instrument re-entry. While SAM3 provides a powerful spatio-temporal framework for video object segmentation, its performance in surgical scenes is limited by indiscriminate memory updates, fixed memory capacity, and weak identity recovery after occlusions. We propose ReMeDI-SAM3, a training-free memory-enhanced extension of SAM3, that addresses these limitations through three components: (i) relevance-aware memory filtering with a dedicated occlusion-aware memory for storing pre-occlusion frames, (ii) a piecewise interpolation scheme that expands the effective memory capacity, and (iii) a feature-based re-identification module with temporal voting for reliable post-occlusion identity disambiguation. Together, these components mitigate error accumulation and enable reliable recovery after occlusions. Evaluations on EndoVis17 and EndoVis18 under a zero-shot setting show absolute mcIoU improvements of around 7% and 16%, respectively, over vanilla SAM3, outperforming even prior training-based approaches. Project page: https://valaybundele.github.io/remedi-sam3/.

