---
layout: default
title: Salient Object Detection in Complex Weather Conditions via Noise Indicators
---

# Salient Object Detection in Complex Weather Conditions via Noise Indicators
**arXiv**：[2512.10592v1](https://arxiv.org/abs/2512.10592) · [PDF](https://arxiv.org/pdf/2512.10592.pdf)  
**作者**：Quan Chen, Xiaokai Yang, Tingyu Wang, Rongfeng Lu, Xichun Sheng, Yaoqi Sun, Chenggang Yan  

**一句话要点**：提出噪声指示器融合模块以增强复杂天气条件下的显著目标检测

**关键词**：显著目标检测, 天气噪声, 特征调制, 多模态学习, 鲁棒性增强

## 3 点简述
- 核心问题：现有显著目标检测方法忽略天气噪声导致的精度下降，缺乏对复杂天气的鲁棒性。
- 方法要点：设计噪声指示器表示天气类型，通过噪声指示器融合模块自适应调制特征，嵌入天气感知先验。
- 实验或效果：在WXSOD数据集上验证，该框架（特别是增强编码器）在多种训练规模下提升复杂天气下的分割精度。

## 摘要（原文）

> Salient object detection (SOD), a foundational task in computer vision, has advanced from single-modal to multi-modal paradigms to enhance generalization. However, most existing SOD methods assume low-noise visual conditions, overlooking the degradation of segmentation accuracy caused by weather-induced noise in real-world scenarios. In this paper, we propose a SOD framework tailored for diverse weather conditions, encompassing a specific encoder and a replaceable decoder. To enable handling of varying weather noises, we introduce a one-hot vector as a noise indicator to represent different weather types and design a Noise Indicator Fusion Module (NIFM). The NIFM takes both semantic features and the noise indicator as dual inputs and is inserted between consecutive stages of the encoder to embed weather-aware priors via adaptive feature modulation. Critically, the proposed specific encoder retains compatibility with mainstream SOD decoders. Extensive experiments are conducted on the WXSOD dataset under varying training data scales (100%, 50%, 30% of the full training set), three encoder and seven decoder configurations. Results show that the proposed SOD framework (particularly the NIFM-enhanced specific encoder) improves segmentation accuracy under complex weather conditions compared to a vanilla encoder.

