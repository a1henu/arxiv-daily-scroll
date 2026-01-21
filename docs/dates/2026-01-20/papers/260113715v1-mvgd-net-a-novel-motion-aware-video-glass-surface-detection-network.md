---
layout: default
title: MVGD-Net: A Novel Motion-aware Video Glass Surface Detection Network
---

# MVGD-Net: A Novel Motion-aware Video Glass Surface Detection Network
**arXiv**：[2601.13715v1](https://arxiv.org/abs/2601.13715) · [PDF](https://arxiv.org/pdf/2601.13715.pdf)  
**作者**：Yiwei Lu, Hao Huang, Tao Yan  

**一句话要点**：提出MVGD-Net，利用运动不一致性检测视频中的玻璃表面，以提升机器人导航等系统的安全性。

**关键词**：视频玻璃表面检测, 运动不一致性, 时空特征融合, 光学流估计, 大规模数据集

## 3 点简述
- 核心问题：玻璃表面在视频中难以检测，可能威胁基于视觉的系统如机器人导航。
- 方法要点：基于运动不一致性，设计CMFM、HGAM、TCAM和TSD模块融合时空特征。
- 实验或效果：在自建大规模数据集上实验，MVGD-Net优于现有先进方法。

## 摘要（原文）

> Glass surface ubiquitous in both daily life and professional environments presents a potential threat to vision-based systems, such as robot and drone navigation. To solve this challenge, most recent studies have shown significant interest in Video Glass Surface Detection (VGSD). We observe that objects in the reflection (or transmission) layer appear farther from the glass surfaces. Consequently, in video motion scenarios, the notable reflected (or transmitted) objects on the glass surface move slower than objects in non-glass regions within the same spatial plane, and this motion inconsistency can effectively reveal the presence of glass surfaces. Based on this observation, we propose a novel network, named MVGD-Net, for detecting glass surfaces in videos by leveraging motion inconsistency cues. Our MVGD-Net features three novel modules: the Cross-scale Multimodal Fusion Module (CMFM) that integrates extracted spatial features and estimated optical flow maps, the History Guided Attention Module (HGAM) and Temporal Cross Attention Module (TCAM), both of which further enhances temporal features. A Temporal-Spatial Decoder (TSD) is also introduced to fuse the spatial and temporal features for generating the glass region mask. Furthermore, for learning our network, we also propose a large-scale dataset, which comprises 312 diverse glass scenarios with a total of 19,268 frames. Extensive experiments demonstrate that our MVGD-Net outperforms relevant state-of-the-art methods.

