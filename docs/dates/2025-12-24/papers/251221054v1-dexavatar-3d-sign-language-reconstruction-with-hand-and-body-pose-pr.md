---
layout: default
title: DexAvatar: 3D Sign Language Reconstruction with Hand and Body Pose Priors
---

# DexAvatar: 3D Sign Language Reconstruction with Hand and Body Pose Priors
**arXiv**：[2512.21054v1](https://arxiv.org/abs/2512.21054) · [PDF](https://arxiv.org/pdf/2512.21054.pdf)  
**作者**：Kaustubh Kundu, Hrishav Bakul Barua, Lucy Robertson-Bell, Zhixi Cai, Kalin Stefanov  

**一句话要点**：提出DexAvatar框架，利用手部和身体姿态先验从单目手语视频重建精细3D姿态

**关键词**：3D手语重建, 姿态先验学习, 单目视频处理, 生物力学建模, 手部姿态估计

## 3 点简述
- 核心问题：手语视频缺乏准确3D数据，现有3D姿态估计方法易受遮挡和噪声影响。
- 方法要点：基于学习的手部和身体3D先验，重建生物力学准确的精细手部关节和身体运动。
- 实验或效果：在SGNify数据集上，身体和手部姿态估计比现有最佳方法提升35.11%。

## 摘要（原文）

> The trend in sign language generation is centered around data-driven generative methods that require vast amounts of precise 2D and 3D human pose data to achieve an acceptable generation quality. However, currently, most sign language datasets are video-based and limited to automatically reconstructed 2D human poses (i.e., keypoints) and lack accurate 3D information. Furthermore, existing state-of-the-art for automatic 3D human pose estimation from sign language videos is prone to self-occlusion, noise, and motion blur effects, resulting in poor reconstruction quality. In response to this, we introduce DexAvatar, a novel framework to reconstruct bio-mechanically accurate fine-grained hand articulations and body movements from in-the-wild monocular sign language videos, guided by learned 3D hand and body priors. DexAvatar achieves strong performance in the SGNify motion capture dataset, the only benchmark available for this task, reaching an improvement of 35.11% in the estimation of body and hand poses compared to the state-of-the-art. The official website of this work is: https://github.com/kaustesseract/DexAvatar.

