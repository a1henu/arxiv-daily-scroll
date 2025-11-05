---
layout: default
title: PercHead: Perceptual Head Model for Single-Image 3D Head Reconstruction & Editing
---

# PercHead: Perceptual Head Model for Single-Image 3D Head Reconstruction & Editing
**arXiv**：[2511.02777v1](https://arxiv.org/abs/2511.02777) · [PDF](https://arxiv.org/pdf/2511.02777.pdf)  
**作者**：Antonio Oroz, Matthias Nießner, Tobias Kirschstein  

**一句话要点**：提出PercHead方法，用于单图像3D头部重建与语义编辑，解决遮挡和编辑模糊问题。

**关键词**：3D头部重建, 语义编辑, 感知监督, 高斯溅射, 单图像处理, ViT解码器

## 3 点简述
- 核心问题：单图像3D头部重建面临严重遮挡、弱感知监督和3D编辑模糊性挑战。
- 方法要点：采用双分支编码器和ViT解码器，结合DINOv2与SAM2.1进行感知监督，使用高斯溅射渲染。
- 实验或效果：在视角合成中达到SOTA，对极端视角鲁棒，支持通过分割图和文本/图像进行语义编辑。

## 摘要（原文）

> We present PercHead, a method for single-image 3D head reconstruction and
> semantic 3D editing - two tasks that are inherently challenging due to severe
> view occlusions, weak perceptual supervision, and the ambiguity of editing in
> 3D space. We develop a unified base model for reconstructing view-consistent 3D
> heads from a single input image. The model employs a dual-branch encoder
> followed by a ViT-based decoder that lifts 2D features into 3D space through
> iterative cross-attention. Rendering is performed using Gaussian Splatting. At
> the heart of our approach is a novel perceptual supervision strategy based on
> DINOv2 and SAM2.1, which provides rich, generalized signals for both geometric
> and appearance fidelity. Our model achieves state-of-the-art performance in
> novel-view synthesis and, furthermore, exhibits exceptional robustness to
> extreme viewing angles compared to established baselines. Furthermore, this
> base model can be seamlessly extended for semantic 3D editing by swapping the
> encoder and finetuning the network. In this variant, we disentangle geometry
> and style through two distinct input modalities: a segmentation map to control
> geometry and either a text prompt or a reference image to specify appearance.
> We highlight the intuitive and powerful 3D editing capabilities of our model
> through a lightweight, interactive GUI, where users can effortlessly sculpt
> geometry by drawing segmentation maps and stylize appearance via natural
> language or image prompts.
>   Project Page: https://antoniooroz.github.io/PercHead Video:
> https://www.youtube.com/watch?v=4hFybgTk4kE

