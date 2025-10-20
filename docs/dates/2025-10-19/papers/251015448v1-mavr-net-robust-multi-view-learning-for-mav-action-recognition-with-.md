---
layout: default
title: MAVR-Net: Robust Multi-View Learning for MAV Action Recognition with Cross-View Attention
---

# MAVR-Net: Robust Multi-View Learning for MAV Action Recognition with Cross-View Attention
**arXiv**：[2510.15448v1](https://arxiv.org/abs/2510.15448) · [PDF](https://arxiv.org/pdf/2510.15448.pdf)  
**作者**：Nengbo Zhang, Hann Woei Ho  

**一句话要点**：提出MAVR-Net多视图学习框架以解决MAV动作识别中RGB数据不足的问题

**关键词**：多视图学习, MAV动作识别, 跨视图注意力, 时空特征提取, 多模态融合

## 3 点简述
- 核心问题：仅依赖RGB数据难以捕捉MAV复杂时空运动特征，导致动作识别精度受限
- 方法要点：融合RGB、光流和分割掩码，采用跨视图注意力模块增强多模态交互
- 实验效果：在基准数据集上准确率高达97.8%、96.5%和92.8%，优于现有方法

## 摘要（原文）

> Recognizing the motion of Micro Aerial Vehicles (MAVs) is crucial for
> enabling cooperative perception and control in autonomous aerial swarms. Yet,
> vision-based recognition models relying only on RGB data often fail to capture
> the complex spatial temporal characteristics of MAV motion, which limits their
> ability to distinguish different actions. To overcome this problem, this paper
> presents MAVR-Net, a multi-view learning-based MAV action recognition
> framework. Unlike traditional single-view methods, the proposed approach
> combines three complementary types of data, including raw RGB frames, optical
> flow, and segmentation masks, to improve the robustness and accuracy of MAV
> motion recognition. Specifically, ResNet-based encoders are used to extract
> discriminative features from each view, and a multi-scale feature pyramid is
> adopted to preserve the spatiotemporal details of MAV motion patterns. To
> enhance the interaction between different views, a cross-view attention module
> is introduced to model the dependencies among various modalities and feature
> scales. In addition, a multi-view alignment loss is designed to ensure semantic
> consistency and strengthen cross-view feature representations. Experimental
> results on benchmark MAV action datasets show that our method clearly
> outperforms existing approaches, achieving 97.8\%, 96.5\%, and 92.8\% accuracy
> on the Short MAV, Medium MAV, and Long MAV datasets, respectively.

