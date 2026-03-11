---
layout: default
title: Improving 3D Foot Motion Reconstruction in Markerless Monocular Human Motion Capture
---

# Improving 3D Foot Motion Reconstruction in Markerless Monocular Human Motion Capture
**arXiv**：[2603.09681v1](https://arxiv.org/abs/2603.09681) · [PDF](https://arxiv.org/pdf/2603.09681.pdf)  
**作者**：Tom Wehrbein, Bodo Rosenhahn  

**一句话要点**：提出FootMR方法以提升无标记单目人体运动捕捉中的3D足部运动重建精度

**关键词**：3D足部运动重建, 无标记运动捕捉, 2D到3D提升, 残差预测, 数据增强, 足部数据集

## 3 点简述
- 现有方法在野外视频中恢复3D人体运动时，常因训练数据足部标注不准确和运动多样性不足，导致精细足部关节重建失败。
- FootMR通过将2D足部关键点序列提升至3D，避免直接图像输入，利用大规模运动捕捉数据，结合膝足运动上下文预测残差运动，改进足部运动。
- 在MOOF、MOYO和RICH数据集上实验显示，FootMR优于现有方法，在MOYO上踝关节角度误差降低达30%。

## 摘要（原文）

> State-of-the-art methods can recover accurate overall 3D human body motion from in-the-wild videos. However, they often fail to capture fine-grained articulations, especially in the feet, which are critical for applications such as gait analysis and animation. This limitation results from training datasets with inaccurate foot annotations and limited foot motion diversity. We address this gap with FootMR, a Foot Motion Refinement method that refines foot motion estimated by an existing human recovery model through lifting 2D foot keypoint sequences to 3D. By avoiding direct image input, FootMR circumvents inaccurate image-3D annotation pairs and can instead leverage large-scale motion capture data. To resolve ambiguities of 2D-to-3D lifting, FootMR incorporates knee and foot motion as context and predicts only residual foot motion. Generalization to extreme foot poses is further improved by representing joints in global rather than parent-relative rotations and applying extensive data augmentation. To support evaluation of foot motion reconstruction, we introduce MOOF, a 2D dataset of complex foot movements. Experiments on MOOF, MOYO, and RICH show that FootMR outperforms state-of-the-art methods, reducing ankle joint angle error on MOYO by up to 30% over the best video-based approach.

