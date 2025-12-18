---
layout: default
title: Off The Grid: Detection of Primitives for Feed-Forward 3D Gaussian Splatting
---

# Off The Grid: Detection of Primitives for Feed-Forward 3D Gaussian Splatting
**arXiv**：[2512.15508v1](https://arxiv.org/abs/2512.15508) · [PDF](https://arxiv.org/pdf/2512.15508.pdf)  
**作者**：Arthur Moreau, Richard Shaw, Michal Nazarczuk, Jisu Shin, Thomas Tanay, Zhensong Zhang, Songcen Xu, Eduardo Pérez-Pellitero  

**一句话要点**：提出Off The Grid架构以优化前馈3D高斯溅射的基元检测，提升实时场景生成质量与效率。

**关键词**：3D高斯溅射, 前馈模型, 基元检测, 新视角合成, 自监督学习, 实时渲染

## 3 点简述
- 前馈3D高斯溅射模型因像素对齐基元放置依赖密集刚性网格，导致质量和效率受限。
- 引入多分辨率解码器，在子像素级别检测3D高斯基元，实现自适应分布，替代像素网格。
- 模型通过自监督学习端到端训练，在秒级生成逼真场景，使用更少基元达到最先进的新视角合成效果。

## 摘要（原文）

> Feed-forward 3D Gaussian Splatting (3DGS) models enable real-time scene generation but are hindered by suboptimal pixel-aligned primitive placement, which relies on a dense, rigid grid and limits both quality and efficiency. We introduce a new feed-forward architecture that detects 3D Gaussian primitives at a sub-pixel level, replacing the pixel grid with an adaptive, "Off The Grid" distribution. Inspired by keypoint detection, our multi-resolution decoder learns to distribute primitives across image patches. This module is trained end-to-end with a 3D reconstruction backbone using self-supervised learning. Our resulting pose-free model generates photorealistic scenes in seconds, achieving state-of-the-art novel view synthesis for feed-forward models. It outperforms competitors while using far fewer primitives, demonstrating a more accurate and efficient allocation that captures fine details and reduces artifacts. Moreover, we observe that by learning to render 3D Gaussians, our 3D reconstruction backbone improves camera pose estimation, suggesting opportunities to train these foundational models without labels.

