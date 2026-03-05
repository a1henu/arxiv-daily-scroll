---
layout: default
title: Small Object Detection in Complex Backgrounds with Multi-Scale Attention and Global Relation Modeling
---

# Small Object Detection in Complex Backgrounds with Multi-Scale Attention and Global Relation Modeling
**arXiv**：[2603.03788v1](https://arxiv.org/abs/2603.03788) · [PDF](https://arxiv.org/pdf/2603.03788.pdf)  
**作者**：Wenguang Tao, Xiaotian Wang, Tian Yan, Yi Wang, Jie Yan  

**一句话要点**：提出多尺度注意力与全局关系建模框架以解决复杂背景下小目标检测问题

**关键词**：小目标检测, 多尺度特征增强, 全局关系建模, 注意力机制, 复杂背景, 定位精度

## 3 点简述
- 核心问题：小目标检测因下采样和背景干扰导致特征退化、语义弱和定位不准。
- 方法要点：引入残差哈尔小波下采样、全局关系建模和跨尺度混合注意力模块增强特征。
- 实验或效果：在RGBT-Tiny基准上优于现有方法，验证了框架的有效性和鲁棒性。

## 摘要（原文）

> Small object detection under complex backgrounds remains a challenging task due to severe feature degradation, weak semantic representation, and inaccurate localization caused by downsampling operations and background interference. Existing detection frameworks are mainly designed for general objects and often fail to explicitly address the unique characteristics of small objects, such as limited structural cues and strong sensitivity to localization errors. In this paper, we propose a multi-level feature enhancement and global relation modeling framework tailored for small object detection. Specifically, a Residual Haar Wavelet Downsampling module is introduced to preserve fine-grained structural details by jointly exploiting spatial-domain convolutional features and frequency-domain representations. To enhance global semantic awareness and suppress background noise, a Global Relation Modeling module is employed to capture long-range dependencies at high-level feature stages. Furthermore, a Cross-Scale Hybrid Attention module is designed to establish sparse and aligned interactions across multi-scale features, enabling effective fusion of high-resolution details and high-level semantic information with reduced computational overhead. Finally, a Center-Assisted Loss is incorporated to stabilize training and improve localization accuracy for small objects. Extensive experiments conducted on the large-scale RGBT-Tiny benchmark demonstrate that the proposed method consistently outperforms existing state-of-the-art detectors under both IoU-based and scale-adaptive evaluation metrics. These results validate the effectiveness and robustness of the proposed framework for small object detection in complex environments.

