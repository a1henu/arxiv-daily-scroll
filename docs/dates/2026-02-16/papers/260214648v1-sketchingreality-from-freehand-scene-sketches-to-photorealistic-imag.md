---
layout: default
title: SketchingReality: From Freehand Scene Sketches To Photorealistic Images
---

# SketchingReality: From Freehand Scene Sketches To Photorealistic Images
**arXiv**：[2602.14648v1](https://arxiv.org/abs/2602.14648) · [PDF](https://arxiv.org/pdf/2602.14648.pdf)  
**作者**：Ahmed Bourouis, Mikhail Bessmeltsev, Yulia Gryaditskaya  

**一句话要点**：提出基于调制的方法，从自由手绘场景草图生成逼真图像，平衡真实性与草图语义对齐。

**关键词**：草图生成图像, 自由手绘草图, 语义对齐, 调制方法, 无监督训练, 生成对抗网络

## 3 点简述
- 核心问题：自由手绘草图缺乏像素对齐的真实图像作为监督，且存在抽象和失真。
- 方法要点：采用调制方法优先语义解释，而非严格边缘对齐，并引入新损失函数进行训练。
- 实验或效果：在语义对齐、真实感和整体质量上优于现有方法。

## 摘要（原文）

> Recent years have witnessed remarkable progress in generative AI, with natural language emerging as the most common conditioning input. As underlying models grow more powerful, researchers are exploring increasingly diverse conditioning signals, such as depth maps, edge maps, camera parameters, and reference images, to give users finer control over generation. Among different modalities, sketches are a natural and long-standing form of human communication, enabling rapid expression of visual concepts. Previous literature has largely focused on edge maps, often misnamed 'sketches', yet algorithms that effectively handle true freehand sketches, with their inherent abstraction and distortions, remain underexplored. We pursue the challenging goal of balancing photorealism with sketch adherence when generating images from freehand input. A key obstacle is the absence of ground-truth, pixel-aligned images: by their nature, freehand sketches do not have a single correct alignment. To address this, we propose a modulation-based approach that prioritizes semantic interpretation of the sketch over strict adherence to individual edge positions. We further introduce a novel loss that enables training on freehand sketches without requiring ground-truth pixel-aligned images. We show that our method outperforms existing approaches in both semantic alignment with freehand sketch inputs and in the realism and overall quality of the generated images.

