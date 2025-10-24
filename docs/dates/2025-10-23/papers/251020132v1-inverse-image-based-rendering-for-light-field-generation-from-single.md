---
layout: default
title: Inverse Image-Based Rendering for Light Field Generation from Single Images
---

# Inverse Image-Based Rendering for Light Field Generation from Single Images
**arXiv**：[2510.20132v1](https://arxiv.org/abs/2510.20132) · [PDF](https://arxiv.org/pdf/2510.20132.pdf)  
**作者**：Hyunjun Jung, Hae-Gon Jeon  

**一句话要点**：提出逆图像渲染方法，从单图像生成光场以支持新视角合成

**关键词**：光场生成, 新视角合成, 逆图像渲染, 神经渲染, 单图像处理

## 3 点简述
- 核心问题：光场获取需多视图或专用设备，成本高且不便。
- 方法要点：设计神经渲染器，通过交叉注意力重建光流，迭代生成新视图。
- 实验或效果：在挑战性数据集上表现优异，无需重训练，超越现有方法。

## 摘要（原文）

> A concept of light-fields computed from multiple view images on regular grids
> has proven its benefit for scene representations, and supported realistic
> renderings of novel views and photographic effects such as refocusing and
> shallow depth of field. In spite of its effectiveness of light flow
> computations, obtaining light fields requires either computational costs or
> specialized devices like a bulky camera setup and a specialized microlens
> array. In an effort to broaden its benefit and applicability, in this paper, we
> propose a novel view synthesis method for light field generation from only
> single images, named inverse image-based rendering. Unlike previous attempts to
> implicitly rebuild 3D geometry or to explicitly represent objective scenes, our
> method reconstructs light flows in a space from image pixels, which behaves in
> the opposite way to image-based rendering. To accomplish this, we design a
> neural rendering pipeline to render a target ray in an arbitrary viewpoint. Our
> neural renderer first stores the light flow of source rays from the input
> image, then computes the relationships among them through cross-attention, and
> finally predicts the color of the target ray based on these relationships.
> After the rendering pipeline generates the first novel view from a single input
> image, the generated out-of-view contents are updated to the set of source
> rays. This procedure is iteratively performed while ensuring the consistent
> generation of occluded contents. We demonstrate that our inverse image-based
> rendering works well with various challenging datasets without any retraining
> or finetuning after once trained on synthetic dataset, and outperforms relevant
> state-of-the-art novel view synthesis methods.

