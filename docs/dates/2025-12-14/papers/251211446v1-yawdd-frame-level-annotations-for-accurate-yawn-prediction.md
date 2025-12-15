---
layout: default
title: YawDD+: Frame-level Annotations for Accurate Yawn Prediction
---

# YawDD+: Frame-level Annotations for Accurate Yawn Prediction
**arXiv**：[2512.11446v1](https://arxiv.org/abs/2512.11446) · [PDF](https://arxiv.org/pdf/2512.11446.pdf)  
**作者**：Ahmed Mujtaba, Gleb Radchenko, Marc Masana, Radu Prodan  

**一句话要点**：提出YawDD+数据集以解决驾驶员疲劳监测中视频级标注噪声问题，提升打哈欠预测准确性。

**关键词**：驾驶员疲劳监测, 打哈欠预测, 帧级标注, 半自动标注, 边缘AI硬件, 视频分析

## 3 点简述
- 核心问题：驾驶员疲劳导致事故，现有视频级标注数据集引入系统噪声，影响模型训练准确性。
- 方法要点：开发半自动标注流程，结合人工验证，生成帧级标注的YawDD+数据集，用于改进模型训练。
- 实验或效果：在YawDD+上训练MNasNet和YOLOv11，帧准确率提升6%，mAP提升5%，达到99.34%分类准确率和95.69%检测mAP，边缘硬件实现59.8 FPS。

## 摘要（原文）

> Driver fatigue remains a leading cause of road accidents, with 24\% of crashes involving drowsy drivers. While yawning serves as an early behavioral indicator of fatigue, existing machine learning approaches face significant challenges due to video-annotated datasets that introduce systematic noise from coarse temporal annotations. We develop a semi-automated labeling pipeline with human-in-the-loop verification, which we apply to YawDD, enabling more accurate model training. Training the established MNasNet classifier and YOLOv11 detector architectures on YawDD+ improves frame accuracy by up to 6\% and mAP by 5\% over video-level supervision, achieving 99.34\% classification accuracy and 95.69\% detection mAP. The resulting approach deliver up to 59.8 FPS on edge AI hardware (NVIDIA Jetson Nano), confirming that enhanced data quality alone supports on-device yawning monitoring without server-side computation.

