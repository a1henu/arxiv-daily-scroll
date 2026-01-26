---
layout: default
title: Boundary and Position Information Mining for Aerial Small Object Detection
---

# Boundary and Position Information Mining for Aerial Small Object Detection
**arXiv**：[2601.16617v1](https://arxiv.org/abs/2601.16617) · [PDF](https://arxiv.org/pdf/2601.16617.pdf)  
**作者**：Rongxin Huang, Guangfeng Lin, Wenbo Zhou, Zhirong Li, Wenhuan Wu  

**一句话要点**：提出边界与位置信息挖掘框架以解决无人机图像中小目标检测的尺度不平衡与边缘模糊问题。

**关键词**：小目标检测, 无人机图像, 边界信息挖掘, 位置信息引导, 跨尺度特征融合, 注意力机制

## 3 点简述
- 核心问题：无人机图像中小目标检测面临尺度不平衡和边缘模糊的挑战，导致目标难以准确捕获。
- 方法要点：设计BPIM框架，包括位置信息引导、边界信息引导、跨尺度融合等模块，通过注意力机制和特征融合整合边界、位置与尺度信息。
- 实验或效果：在VisDrone2021、DOTA1.0和WiderPerson数据集上优于基线Yolov5-P2，并在计算负载相当下达到先进性能。

## 摘要（原文）

> Unmanned Aerial Vehicle (UAV) applications have become increasingly prevalent in aerial photography and object recognition. However, there are major challenges to accurately capturing small targets in object detection due to the imbalanced scale and the blurred edges. To address these issues, boundary and position information mining (BPIM) framework is proposed for capturing object edge and location cues. The proposed BPIM includes position information guidance (PIG) module for obtaining location information, boundary information guidance (BIG) module for extracting object edge, cross scale fusion (CSF) module for gradually assembling the shallow layer image feature, three feature fusion (TFF) module for progressively combining position and boundary information, and adaptive weight fusion (AWF) module for flexibly merging the deep layer semantic feature. Therefore, BPIM can integrate boundary, position, and scale information in image for small object detection using attention mechanisms and cross-scale feature fusion strategies. Furthermore, BPIM not only improves the discrimination of the contextual feature by adaptive weight fusion with boundary, but also enhances small object perceptions by cross-scale position fusion. On the VisDrone2021, DOTA1.0, and WiderPerson datasets, experimental results show the better performances of BPIM compared to the baseline Yolov5-P2, and obtains the promising performance in the state-of-the-art methods with comparable computation load.

