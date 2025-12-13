---
layout: default
title: GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting
---

# GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting
**arXiv**：[2512.10939v1](https://arxiv.org/abs/2512.10939) · [PDF](https://arxiv.org/pdf/2512.10939.pdf)  
**作者**：Madhav Agarwal, Mingtian Zhang, Laura Sevilla-Lara, Steven McDonagh  

**一句话要点**：提出GaussianHeadTalk，通过音频驱动高斯溅射和3D形变模型，生成实时稳定的3D说话头像。

**关键词**：3D说话头像, 高斯溅射, 音频驱动, 时间一致性, 实时生成

## 3 点简述
- 核心问题：现有说话头像方法在实时性和时间稳定性上存在不足，高斯溅射方法因面部跟踪不准确导致输出不稳定。
- 方法要点：结合3D形变模型映射高斯溅射，使用基于Transformer的音频直接预测模型参数，确保时间一致性。
- 实验或效果：从单目视频和独立音频输入生成实时说话头像视频，在定量和定性评估中表现竞争性。

## 摘要（原文）

> Speech-driven talking heads have recently emerged and enable interactive avatars. However, real-world applications are limited, as current methods achieve high visual fidelity but slow or fast yet temporally unstable. Diffusion methods provide realistic image generation, yet struggle with oneshot settings. Gaussian Splatting approaches are real-time, yet inaccuracies in facial tracking, or inconsistent Gaussian mappings, lead to unstable outputs and video artifacts that are detrimental to realistic use cases. We address this problem by mapping Gaussian Splatting using 3D Morphable Models to generate person-specific avatars. We introduce transformer-based prediction of model parameters, directly from audio, to drive temporal consistency. From monocular video and independent audio speech inputs, our method enables generation of real-time talking head videos where we report competitive quantitative and qualitative performance.

