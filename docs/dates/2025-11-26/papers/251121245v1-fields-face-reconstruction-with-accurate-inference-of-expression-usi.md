---
layout: default
title: FIELDS: Face reconstruction with accurate Inference of Expression using Learning with Direct Supervision
---

# FIELDS: Face reconstruction with accurate Inference of Expression using Learning with Direct Supervision
**arXiv**：[2511.21245v1](https://arxiv.org/abs/2511.21245) · [PDF](https://arxiv.org/pdf/2511.21245.pdf)  
**作者**：Chen Ling, Henglin Shi, Hedvig Kjellström  

**一句话要点**：提出FIELDS方法，通过直接3D监督解决单图像3D人脸重建中表情细节丢失问题。

**关键词**：3D人脸重建, 表情参数监督, 情感识别, 自监督学习, 单图像重建

## 3 点简述
- 核心问题：现有3D人脸重建方法依赖2D监督，缺乏3D真实数据，导致细微情感细节丢失。
- 方法要点：结合自监督2D图像一致性与直接3D表情参数监督，并添加情感识别分支。
- 实验或效果：从单图像生成高保真3D人脸模型，提升野外表情识别性能，保持自然度。

## 摘要（原文）

> Facial expressions convey the bulk of emotional information in human communication, yet existing 3D face reconstruction methods often miss subtle affective details due to reliance on 2D supervision and lack of 3D ground truth. We propose FIELDS (Face reconstruction with accurate Inference of Expression using Learning with Direct Supervision) to address these limitations by extending self-supervised 2D image consistency cues with direct 3D expression parameter supervision and an auxiliary emotion recognition branch. Our encoder is guided by authentic expression parameters from spontaneous 4D facial scans, while an intensity-aware emotion loss encourages the 3D expression parameters to capture genuine emotion content without exaggeration. This dual-supervision strategy bridges the 2D/3D domain gap and mitigates expression-intensity bias, yielding high-fidelity 3D reconstructions that preserve subtle emotional cues. From a single image, FIELDS produces emotion-rich face models with highly realistic expressions, significantly improving in-the-wild facial expression recognition performance without sacrificing naturalness.

