---
layout: default
title: MULTIAQUA: A multimodal maritime dataset and robust training strategies for multimodal semantic segmentation
---

# MULTIAQUA: A multimodal maritime dataset and robust training strategies for multimodal semantic segmentation
**arXiv**：[2512.17450v1](https://arxiv.org/abs/2512.17450) · [PDF](https://arxiv.org/pdf/2512.17450.pdf)  
**作者**：Jon Muhovič, Janez Perš  

**一句话要点**：提出MULTIAQUA数据集与鲁棒训练策略，以提升无人水面船在恶劣视觉条件下的多模态语义分割性能。

**关键词**：多模态语义分割, 海事数据集, 鲁棒训练策略, 无人水面船, 恶劣视觉条件

## 3 点简述
- 核心问题：无人水面船在复杂天气和光照条件下视觉感知困难，需多模态数据增强场景理解。
- 方法要点：构建同步校准的多模态海事数据集，包含RGB、热成像、红外和激光雷达等传感器数据。
- 实验或效果：在夜间测试集上评估多模态方法，提出仅用白天图像训练鲁棒深度网络，简化数据获取与训练过程。

## 摘要（原文）

> Unmanned surface vehicles can encounter a number of varied visual circumstances during operation, some of which can be very difficult to interpret. While most cases can be solved only using color camera images, some weather and lighting conditions require additional information. To expand the available maritime data, we present a novel multimodal maritime dataset MULTIAQUA (Multimodal Aquatic Dataset). Our dataset contains synchronized, calibrated and annotated data captured by sensors of different modalities, such as RGB, thermal, IR, LIDAR, etc. The dataset is aimed at developing supervised methods that can extract useful information from these modalities in order to provide a high quality of scene interpretation regardless of potentially poor visibility conditions. To illustrate the benefits of the proposed dataset, we evaluate several multimodal methods on our difficult nighttime test set. We present training approaches that enable multimodal methods to be trained in a more robust way, thus enabling them to retain reliable performance even in near-complete darkness. Our approach allows for training a robust deep neural network only using daytime images, thus significantly simplifying data acquisition, annotation, and the training process.

