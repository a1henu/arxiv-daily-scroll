---
layout: default
title: Birth of a Painting: Differentiable Brushstroke Reconstruction
---

# Birth of a Painting: Differentiable Brushstroke Reconstruction
**arXiv**：[2511.13191v1](https://arxiv.org/abs/2511.13191) · [PDF](https://arxiv.org/pdf/2511.13191.pdf)  
**作者**：Ying Jiang, Jiayin Lu, Yunuo Chen, Yumeng He, Kui Wu, Yin Yang, Chenfanfu Jiang  

**一句话要点**：提出可微分笔触重建框架以统一绘画、纹理生成和涂抹过程

**关键词**：可微分渲染, 笔触重建, 绘画合成, 风格生成, 涂抹操作

## 3 点简述
- 核心问题：现有方法缺乏显式笔触结构，无法生成平滑真实阴影
- 方法要点：优化贝塞尔笔触，结合风格生成和可微分涂抹算子
- 实验效果：在油画、水彩等风格中实现真实笔触重建和色调过渡

## 摘要（原文）

> Painting embodies a unique form of visual storytelling, where the creation process is as significant as the final artwork. Although recent advances in generative models have enabled visually compelling painting synthesis, most existing methods focus solely on final image generation or patch-based process simulation, lacking explicit stroke structure and failing to produce smooth, realistic shading. In this work, we present a differentiable stroke reconstruction framework that unifies painting, stylized texturing, and smudging to faithfully reproduce the human painting-smudging loop. Given an input image, our framework first optimizes single- and dual-color Bezier strokes through a parallel differentiable paint renderer, followed by a style generation module that synthesizes geometry-conditioned textures across diverse painting styles. We further introduce a differentiable smudge operator to enable natural color blending and shading. Coupled with a coarse-to-fine optimization strategy, our method jointly optimizes stroke geometry, color, and texture under geometric and semantic guidance. Extensive experiments on oil, watercolor, ink, and digital paintings demonstrate that our approach produces realistic and expressive stroke reconstructions, smooth tonal transitions, and richly stylized appearances, offering a unified model for expressive digital painting creation. See our project page for more demos: https://yingjiang96.github.io/DiffPaintWebsite/.

