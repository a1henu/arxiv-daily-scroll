---
layout: default
title: Generative Latent Alignment for Interpretable Radar Based Occupancy Detection in Ambient Assisted Living
---

# Generative Latent Alignment for Interpretable Radar Based Occupancy Detection in Ambient Assisted Living
**arXiv**：[2601.19853v1](https://arxiv.org/abs/2601.19853) · [PDF](https://arxiv.org/pdf/2601.19853.pdf)  
**作者**：Huy Trinh  

**一句话要点**：提出生成式潜在对齐框架，以增强毫米波雷达在辅助生活场景中占用检测的可解释性。

**关键词**：毫米波雷达, 可解释性, 潜在对齐, 辅助生活, 变分自编码器, Grad-CAM

## 3 点简述
- 针对辅助生活场景中基于摄像头的传感引发隐私问题，研究毫米波雷达占用检测的可解释性。
- 结合轻量卷积变分自编码器和冻结CLIP文本编码器，学习雷达距离-角度热图的低维潜在表示，并与语义锚点软对齐。
- 在毫米波雷达数据集上，通过Grad-CAM可视化支持决策的空间区域，并消融实验验证雷达特定锚点的重要性。

## 摘要（原文）

> In this work, we study how to make mmWave radar presence detection more interpretable for Ambient Assisted Living (AAL) settings, where camera-based sensing raises privacy concerns. We propose a Generative Latent Alignment (GLA) framework that combines a lightweight convolutional variational autoencoder with a frozen CLIP text encoder to learn a low-dimensional latent representation of radar Range-Angle (RA) heatmaps. The latent space is softly aligned with two semantic anchors corresponding to "empty room" and "person present", and Grad-CAM is applied in this aligned latent space to visualize which spatial regions support each presence decision. On our mmWave radar dataset, we qualitatively observe that the "person present" class produces compact Grad-CAM blobs that coincide with strong RA returns, whereas "empty room" samples yield diffuse or no evidence. We also conduct an ablation study using unrelated text prompts, which degrades both reconstruction and localization, suggesting that radar-specific anchors are important for meaningful explanations in this setting.

