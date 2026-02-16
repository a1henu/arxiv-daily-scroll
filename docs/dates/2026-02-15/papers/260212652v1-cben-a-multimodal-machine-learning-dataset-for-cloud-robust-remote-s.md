---
layout: default
title: CBEN -- A Multimodal Machine Learning Dataset for Cloud Robust Remote Sensing Image Understanding
---

# CBEN -- A Multimodal Machine Learning Dataset for Cloud Robust Remote Sensing Image Understanding
**arXiv**：[2602.12652v1](https://arxiv.org/abs/2602.12652) · [PDF](https://arxiv.org/pdf/2602.12652.pdf)  
**作者**：Marco Stricker, Masakazu Iwamura, Koichi Kise  

**一句话要点**：提出CBEN数据集以解决遥感图像在云遮挡下的鲁棒性分析问题

**关键词**：遥感图像理解, 多模态机器学习, 云鲁棒性, 数据集构建, 光学雷达融合

## 3 点简述
- 核心问题：云遮挡导致光学卫星图像失真，现有方法常排除云图，限制时间敏感应用。
- 方法要点：构建配对光学与雷达图像数据集CBEN，支持云鲁棒方法训练与评估。
- 实验或效果：在云图测试中，适应云数据的方法相比原方法提升17.2-28.7个百分点。

## 摘要（原文）

> Clouds are a common phenomenon that distorts optical satellite imagery, which poses a challenge for remote sensing. However, in the literature cloudless analysis is often performed where cloudy images are excluded from machine learning datasets and methods. Such an approach cannot be applied to time sensitive applications, e.g., during natural disasters. A possible solution is to apply cloud removal as a preprocessing step to ensure that cloudfree solutions are not failing under such conditions. But cloud removal methods are still actively researched and suffer from drawbacks, such as generated visual artifacts. Therefore, it is desirable to develop cloud robust methods that are less affected by cloudy weather. Cloud robust methods can be achieved by combining optical data with radar, a modality unaffected by clouds. While many datasets for machine learning combine optical and radar data, most researchers exclude cloudy images. We identify this exclusion from machine learning training and evaluation as a limitation that reduces applicability to cloudy scenarios. To investigate this, we assembled a dataset, named CloudyBigEarthNet (CBEN), of paired optical and radar images with cloud occlusion for training and evaluation. Using average precision (AP) as the evaluation metric, we show that state-of-the-art methods trained on combined clear-sky optical and radar imagery suffer performance drops of 23-33 percentage points when evaluated on cloudy images. We then adapt these methods to cloudy optical data during training, achieving relative improvement of 17.2-28.7 percentage points on cloudy test cases compared with the original approaches. Code and dataset are publicly available at: https://github.com/mstricker13/CBEN

