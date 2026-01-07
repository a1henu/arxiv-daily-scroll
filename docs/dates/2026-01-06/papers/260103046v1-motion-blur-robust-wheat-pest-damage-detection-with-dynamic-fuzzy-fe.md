---
layout: default
title: Motion Blur Robust Wheat Pest Damage Detection with Dynamic Fuzzy Feature Fusion
---

# Motion Blur Robust Wheat Pest Damage Detection with Dynamic Fuzzy Feature Fusion
**arXiv**：[2601.03046v1](https://arxiv.org/abs/2601.03046) · [PDF](https://arxiv.org/pdf/2601.03046.pdf)  
**作者**：Han Zhang, Yanwei Wang, Fang Li, Hongjun Wang  

**一句话要点**：提出动态模糊鲁棒卷积金字塔以解决运动模糊下小麦害虫损伤检测问题

**关键词**：运动模糊鲁棒检测, 动态模糊特征融合, 小麦害虫损伤检测, YOLOv11增强, CUDA并行优化, 边缘部署

## 3 点简述
- 核心问题：相机抖动导致运动模糊，降低边缘侧目标检测精度，现有方法或损失结构或增加延迟
- 方法要点：增强YOLOv11特征金字塔，结合多尺度特征并引入动态鲁棒开关单元自适应注入模糊特征
- 实验或效果：在私有数据集上训练，模糊测试集上准确率比基线提高约10.4%，部署速度提升超400倍

## 摘要（原文）

> Motion blur caused by camera shake produces ghosting artifacts that substantially degrade edge side object detection. Existing approaches either suppress blur as noise and lose discriminative structure, or apply full image restoration that increases latency and limits deployment on resource constrained devices. We propose DFRCP, a Dynamic Fuzzy Robust Convolutional Pyramid, as a plug in upgrade to YOLOv11 for blur robust detection. DFRCP enhances the YOLOv11 feature pyramid by combining large scale and medium scale features while preserving native representations, and by introducing Dynamic Robust Switch units that adaptively inject fuzzy features to strengthen global perception under jitter. Fuzzy features are synthesized by rotating and nonlinearly interpolating multiscale features, then merged through a transparency convolution that learns a content adaptive trade off between original and fuzzy cues. We further develop a CUDA parallel rotation and interpolation kernel that avoids boundary overflow and delivers more than 400 times speedup, making the design practical for edge deployment. We train with paired supervision on a private wheat pest damage dataset of about 3,500 images, augmented threefold using two blur regimes, uniform image wide motion blur and bounding box confined rotational blur. On blurred test sets, YOLOv11 with DFRCP achieves about 10.4 percent higher accuracy than the YOLOv11 baseline with only a modest training time overhead, reducing the need for manual filtering after data collection.

