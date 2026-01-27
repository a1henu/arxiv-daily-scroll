---
layout: default
title: Splat-Portrait: Generalizing Talking Heads with Gaussian Splatting
---

# Splat-Portrait: Generalizing Talking Heads with Gaussian Splatting
**arXiv**：[2601.18633v1](https://arxiv.org/abs/2601.18633) · [PDF](https://arxiv.org/pdf/2601.18633.pdf)  
**作者**：Tong Shi, Melonie de Almeida, Daniela Ivanova, Nicolas Pugeault, Paul Henderson  

**一句话要点**：提出Splat-Portrait方法，基于高斯泼溅解决单肖像图像生成3D说话头与唇部运动合成的挑战。

**关键词**：说话头生成, 高斯泼溅, 3D重建, 唇部运动合成, 无监督训练, 新视角合成

## 3 点简述
- 核心问题：现有3D说话头生成方法依赖领域特定启发式，导致3D重建不准确，影响动画真实感。
- 方法要点：自动从单肖像图像解耦静态3D高斯泼溅重建与2D背景，基于音频生成唇部运动，无需运动驱动先验。
- 实验或效果：在说话头生成和新视角合成上表现优越，视觉质量优于先前工作，训练无3D监督或地标。

## 摘要（原文）

> Talking Head Generation aims at synthesizing natural-looking talking videos from speech and a single portrait image. Previous 3D talking head generation methods have relied on domain-specific heuristics such as warping-based facial motion representation priors to animate talking motions, yet still produce inaccurate 3D avatar reconstructions, thus undermining the realism of generated animations. We introduce Splat-Portrait, a Gaussian-splatting-based method that addresses the challenges of 3D head reconstruction and lip motion synthesis. Our approach automatically learns to disentangle a single portrait image into a static 3D reconstruction represented as static Gaussian Splatting, and a predicted whole-image 2D background. It then generates natural lip motion conditioned on input audio, without any motion driven priors. Training is driven purely by 2D reconstruction and score-distillation losses, without 3D supervision nor landmarks. Experimental results demonstrate that Splat-Portrait exhibits superior performance on talking head generation and novel view synthesis, achieving better visual quality compared to previous works. Our project code and supplementary documents are public available at https://github.com/stonewalking/Splat-portrait.

