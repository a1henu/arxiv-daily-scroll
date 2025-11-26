---
layout: default
title: Pedestrian Crossing Intention Prediction Using Multimodal Fusion Network
---

# Pedestrian Crossing Intention Prediction Using Multimodal Fusion Network
**arXiv**：[2511.20008v1](https://arxiv.org/abs/2511.20008) · [PDF](https://arxiv.org/pdf/2511.20008.pdf)  
**作者**：Yuanzhe Li, Steffen Müller  

**一句话要点**：提出多模态融合网络以预测行人过街意图，提升自动驾驶安全性。

**关键词**：行人意图预测, 多模态融合, 注意力机制, 自动驾驶, Transformer网络

## 3 点简述
- 核心问题：行人行为多样且依赖多上下文因素，预测意图对自动驾驶至关重要。
- 方法要点：融合视觉和运动七模态特征，使用Transformer提取和注意力机制整合。
- 实验或效果：在JAAD数据集上验证，性能优于基线方法。

## 摘要（原文）

> Pedestrian crossing intention prediction is essential for the deployment of autonomous vehicles (AVs) in urban environments. Ideal prediction provides AVs with critical environmental cues, thereby reducing the risk of pedestrian-related collisions. However, the prediction task is challenging due to the diverse nature of pedestrian behavior and its dependence on multiple contextual factors. This paper proposes a multimodal fusion network that leverages seven modality features from both visual and motion branches, aiming to effectively extract and integrate complementary cues across different modalities. Specifically, motion and visual features are extracted from the raw inputs using multiple Transformer-based extraction modules. Depth-guided attention module leverages depth information to guide attention towards salient regions in another modality through comprehensive spatial feature interactions. To account for the varying importance of different modalities and frames, modality attention and temporal attention are designed to selectively emphasize informative modalities and effectively capture temporal dependencies. Extensive experiments on the JAAD dataset validate the effectiveness of the proposed network, achieving superior performance compared to the baseline methods.

