---
layout: default
title: Persistent feature reconstruction of resident space objects (RSOs) within inverse synthetic aperture radar (ISAR) images
---

# Persistent feature reconstruction of resident space objects (RSOs) within inverse synthetic aperture radar (ISAR) images
**arXiv**：[2512.15618v1](https://arxiv.org/abs/2512.15618) · [PDF](https://arxiv.org/pdf/2512.15618.pdf)  
**作者**：Morgan Coe, Gruffudd Jones, Leah-Nani Alconcel, Marina Gashinova  

**一句话要点**：提出基于序列特征检测与跟踪的方法，在ISAR图像中实现RSO外部结构识别，以增强空间域感知能力。

**关键词**：逆合成孔径雷达, 空间域感知, 特征检测, Hough变换, 序列跟踪, 边缘检测

## 3 点简述
- 核心问题：近地空间RSO数量激增，需高精度识别其外部结构以支持空间域感知。
- 方法要点：使用Hough变换检测线性特征，通过序列跟踪和梯度比边缘检测提高特征识别准确性。
- 实验或效果：基于模拟ISAR图像验证，特征跟踪提升检测置信度，并展示阴影检测用例。

## 摘要（原文）

> With the rapidly growing population of resident space objects (RSOs) in the near-Earth space environment, detailed information about their condition and capabilities is needed to provide Space Domain Awareness (SDA). Space-based sensing will enable inspection of RSOs at shorter ranges, independent of atmospheric effects, and from all aspects. The use of a sub-THz inverse synthetic aperture radar (ISAR) imaging and sensing system for SDA has been proposed in previous work, demonstrating the achievement of sub-cm image resolution at ranges of up to 100 km. This work focuses on recognition of external structures by use of sequential feature detection and tracking throughout the aligned ISAR images of the satellites. The Hough transform is employed to detect linear features, which are tracked throughout the sequence. ISAR imagery is generated via a metaheuristic simulator capable of modelling encounters for a variety of deployment scenarios. Initial frame-to-frame alignment is achieved through a series of affine transformations to facilitate later association between image features. A gradient-by-ratio method is used for edge detection within individual ISAR images, and edge magnitude and direction are subsequently used to inform a double-weighted Hough transform to detect features with high accuracy. Feature evolution during sequences of frames is analysed. It is shown that the use of feature tracking within sequences with the proposed approach will increase confidence in feature detection and classification, and an example use-case of robust detection of shadowing as a feature is presented.

