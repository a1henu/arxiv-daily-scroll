---
layout: default
title: WP-CrackNet: A Collaborative Adversarial Learning Framework for End-to-End Weakly-Supervised Road Crack Detection
---

# WP-CrackNet: A Collaborative Adversarial Learning Framework for End-to-End Weakly-Supervised Road Crack Detection
**arXiv**：[2510.17566v1](https://arxiv.org/abs/2510.17566) · [PDF](https://arxiv.org/pdf/2510.17566.pdf)  
**作者**：Nachuan Ma, Zhengfei Song, Qiang Hu, Xiaoyu Tang, Chengxi Zhang, Rui Fan, Lihua Xie  

**一句话要点**：提出WP-CrackNet以弱监督方式实现端到端道路裂缝检测

**关键词**：弱监督学习, 道路裂缝检测, 对抗学习, 类激活图, 端到端框架

## 3 点简述
- 核心问题：减少对像素级标注的依赖，仅使用图像级标签进行道路裂缝检测。
- 方法要点：集成分类器、重建器和检测器，通过对抗学习和伪标签优化检测结果。
- 实验或效果：在自建数据集上，性能接近监督方法，优于现有弱监督方法。

## 摘要（原文）

> Road crack detection is essential for intelligent infrastructure maintenance
> in smart cities. To reduce reliance on costly pixel-level annotations, we
> propose WP-CrackNet, an end-to-end weakly-supervised method that trains with
> only image-level labels for pixel-wise crack detection. WP-CrackNet integrates
> three components: a classifier generating class activation maps (CAMs), a
> reconstructor measuring feature inferability, and a detector producing
> pixel-wise road crack detection results. During training, the classifier and
> reconstructor alternate in adversarial learning to encourage crack CAMs to
> cover complete crack regions, while the detector learns from pseudo labels
> derived from post-processed crack CAMs. This mutual feedback among the three
> components improves learning stability and detection accuracy. To further boost
> detection performance, we design a path-aware attention module (PAAM) that
> fuses high-level semantics from the classifier with low-level structural cues
> from the reconstructor by modeling spatial and channel-wise dependencies.
> Additionally, a center-enhanced CAM consistency module (CECCM) is proposed to
> refine crack CAMs using center Gaussian weighting and consistency constraints,
> enabling better pseudo-label generation. We create three image-level datasets
> and extensive experiments show that WP-CrackNet achieves comparable results to
> supervised methods and outperforms existing weakly-supervised methods,
> significantly advancing scalable road inspection. The source code package and
> datasets are available at https://mias.group/WP-CrackNet/.

