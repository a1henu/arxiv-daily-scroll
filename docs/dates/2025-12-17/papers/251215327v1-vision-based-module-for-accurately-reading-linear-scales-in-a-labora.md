---
layout: default
title: Vision-based module for accurately reading linear scales in a laboratory
---

# Vision-based module for accurately reading linear scales in a laboratory
**arXiv**：[2512.15327v1](https://arxiv.org/abs/2512.15327) · [PDF](https://arxiv.org/pdf/2512.15327.pdf)  
**作者**：Parvesh Saini, Soumyadipta Maiti, Beena Rai  

**一句话要点**：提出基于视觉的线性刻度读取模块，用于实验室环境中的注射器和量筒液位测量。

**关键词**：线性刻度读取, 视觉测量, 实验室自动化, 图像变换, 特征提取

## 3 点简述
- 核心问题：现有视觉模型难以从图像中准确读取定量测量值，如人类直观读取线性刻度。
- 方法要点：通过图像变换校正随机方向，提取刻度、数字和液位指示器特征以计算读数。
- 实验或效果：系统读数与人工读数对比显示准确对应，验证了方法的有效性。

## 摘要（原文）

> Capabilities and the number of vision-based models are increasing rapidly. And these vision models are now able to do more tasks like object detection, image classification, instance segmentation etc. with great accuracy. But models which can take accurate quantitative measurements form an image, as a human can do by just looking at it, are rare. For a robot to work with complete autonomy in a Laboratory environment, it needs to have some basic skills like navigation, handling objects, preparing samples etc. to match human-like capabilities in an unstructured environment. Another important capability is to read measurements from instruments and apparatus. Here, we tried to mimic a human inspired approach to read measurements from a linear scale. As a test case we have picked reading level from a syringe and a measuring cylinder. For a randomly oriented syringe we carry out transformations to correct the orientation. To make the system efficient and robust, the area of interest is reduced to just the linear scale containing part of the image. After that, a series of features were extracted like the major makers, the corresponding digits, and the level indicator location, from which the final reading was calculated. Readings obtained using this system were also compared against human read values of the same instances and an accurate correspondence was observed.

