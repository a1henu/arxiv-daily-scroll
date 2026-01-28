---
layout: default
title: GTFMN: Guided Texture and Feature Modulation Network for Low-Light Image Enhancement and Super-Resolution
---

# GTFMN: Guided Texture and Feature Modulation Network for Low-Light Image Enhancement and Super-Resolution
**arXiv**：[2601.19157v1](https://arxiv.org/abs/2601.19157) · [PDF](https://arxiv.org/pdf/2601.19157.pdf)  
**作者**：Yongsong Huang, Tzu-Hsuan Peng, Tomo Miyazaki, Xiaofeng Liu, Chun-Ting Chou, Ai-Chun Pang, Shinichiro Omachi  

**一句话要点**：提出GTFMN网络，通过解耦光照估计与纹理恢复，解决低光照图像超分辨率问题。

**关键词**：低光照图像增强, 图像超分辨率, 光照估计, 特征调制, 空间自适应恢复

## 3 点简述
- 核心问题：低光照图像超分辨率中，低分辨率与光照不足耦合导致恢复困难。
- 方法要点：使用光照流预测光照图，通过IGM块动态调制纹理流特征，实现空间自适应增强。
- 实验或效果：在OmniNormal5和OmniNormal15数据集上，定量指标与视觉质量均优于现有方法。

## 摘要（原文）

> Low-light image super-resolution (LLSR) is a challenging task due to the coupled degradation of low resolution and poor illumination. To address this, we propose the Guided Texture and Feature Modulation Network (GTFMN), a novel framework that decouples the LLSR task into two sub-problems: illumination estimation and texture restoration. First, our network employs a dedicated Illumination Stream whose purpose is to predict a spatially varying illumination map that accurately captures lighting distribution. Further, this map is utilized as an explicit guide within our novel Illumination Guided Modulation Block (IGM Block) to dynamically modulate features in the Texture Stream. This mechanism achieves spatially adaptive restoration, enabling the network to intensify enhancement in poorly lit regions while preserving details in well-exposed areas. Extensive experiments demonstrate that GTFMN achieves the best performance among competing methods on the OmniNormal5 and OmniNormal15 datasets, outperforming them in both quantitative metrics and visual quality.

