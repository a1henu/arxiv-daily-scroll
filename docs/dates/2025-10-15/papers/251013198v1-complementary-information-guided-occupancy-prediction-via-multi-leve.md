---
layout: default
title: Complementary Information Guided Occupancy Prediction via Multi-Level Representation Fusion
---

# Complementary Information Guided Occupancy Prediction via Multi-Level Representation Fusion
**arXiv**：[2510.13198v1](https://arxiv.org/abs/2510.13198) · [PDF](https://arxiv.org/pdf/2510.13198.pdf)  
**作者**：Rongtao Xu, Jinzhou Lin, Jialei Zhou, Jiahua Dong, Changwei Wang, Ruisheng Wang, Li Guo, Shibiao Xu, Xiaodan Liang  

**一句话要点**：提出CIGOcc框架，通过多级表示融合提升自动驾驶中基于相机的3D占用预测性能。

**关键词**：3D占用预测, 多级表示融合, 知识蒸馏, 自动驾驶感知, 相机视觉, 特征提取

## 3 点简述
- 核心问题：现有方法未充分利用2D图像中多样特征，导致3D占用预测性能受限。
- 方法要点：提取分割、图形和深度特征，并采用可变形多级融合机制进行融合。
- 实验或效果：在SemanticKITTI基准上实现SOTA性能，未增加训练成本。

## 摘要（原文）

> Camera-based occupancy prediction is a mainstream approach for 3D perception
> in autonomous driving, aiming to infer complete 3D scene geometry and semantics
> from 2D images. Almost existing methods focus on improving performance through
> structural modifications, such as lightweight backbones and complex cascaded
> frameworks, with good yet limited performance. Few studies explore from the
> perspective of representation fusion, leaving the rich diversity of features in
> 2D images underutilized. Motivated by this, we propose \textbf{CIGOcc, a
> two-stage occupancy prediction framework based on multi-level representation
> fusion. \textbf{CIGOcc extracts segmentation, graphics, and depth features from
> an input image and introduces a deformable multi-level fusion mechanism to fuse
> these three multi-level features. Additionally, CIGOcc incorporates knowledge
> distilled from SAM to further enhance prediction accuracy. Without increasing
> training costs, CIGOcc achieves state-of-the-art performance on the
> SemanticKITTI benchmark. The code is provided in the supplementary material and
> will be released https://github.com/VitaLemonTea1/CIGOcc

