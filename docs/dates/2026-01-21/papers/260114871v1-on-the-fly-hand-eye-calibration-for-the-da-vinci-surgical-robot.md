---
layout: default
title: On-the-fly hand-eye calibration for the da Vinci surgical robot
---

# On-the-fly hand-eye calibration for the da Vinci surgical robot
**arXiv**：[2601.14871v1](https://arxiv.org/abs/2601.14871) · [PDF](https://arxiv.org/pdf/2601.14871.pdf)  
**作者**：Zejian Cui, Ferdinando Rodriguez y Baena  

**一句话要点**：提出在线手眼标定框架以提升达芬奇手术机器人工具定位精度

**关键词**：手眼标定, 机器人辅助手术, 工具定位, 达芬奇机器人, 在线校准

## 3 点简述
- 核心问题：达芬奇机器人因编码器误差导致工具定位不准确，影响手术安全
- 方法要点：通过特征关联和手眼标定算法，无需预训练，适应多种手术场景
- 实验或效果：在公开视频数据集上测试，显著降低定位误差，精度媲美先进方法且更高效

## 摘要（原文）

> In Robot-Assisted Minimally Invasive Surgery (RMIS), accurate tool localization is crucial to ensure patient safety and successful task execution. However, this remains challenging for cable-driven robots, such as the da Vinci robot, because erroneous encoder readings lead to pose estimation errors. In this study, we propose a calibration framework to produce accurate tool localization results through computing the hand-eye transformation matrix on-the-fly. The framework consists of two interrelated algorithms: the feature association block and the hand-eye calibration block, which provide robust correspondences for key points detected on monocular images without pre-training, and offer the versatility to accommodate various surgical scenarios by adopting an array of filter approaches, respectively. To validate its efficacy, we test the framework extensively on publicly available video datasets that feature multiple surgical instruments conducting tasks in both in vitro and ex vivo scenarios, under varying illumination conditions and with different levels of key point measurement accuracy. The results show a significant reduction in tool localization errors under the proposed calibration framework, with accuracies comparable to other state-of-the-art methods while being more time-efficient.

