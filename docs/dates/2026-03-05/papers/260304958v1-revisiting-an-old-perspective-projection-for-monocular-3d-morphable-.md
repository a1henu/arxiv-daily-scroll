---
layout: default
title: Revisiting an Old Perspective Projection for Monocular 3D Morphable Models Regression
---

# Revisiting an Old Perspective Projection for Monocular 3D Morphable Models Regression
**arXiv**：[2603.04958v1](https://arxiv.org/abs/2603.04958) · [PDF](https://arxiv.org/pdf/2603.04958.pdf)  
**作者**：Toby Chong, Ryota Nakajima  

**一句话要点**：提出带收缩参数的伪透视投影模型，以解决头戴相机近景面部图像中3D形变模型回归的失真问题。

**关键词**：单目3D形变模型, 透视投影, 头戴相机, 近景面部图像, 模型回归

## 3 点简述
- 核心问题：正交投影在近景面部图像中忽略透视失真，导致3D形变模型回归不准确。
- 方法要点：扩展正交投影，引入收缩参数实现伪透视效果，保持稳定性并兼容现有模型微调。
- 实验或效果：使用头戴相机自定义数据集进行定量和定性比较，验证了改进的有效性。

## 摘要（原文）

> We introduce a novel camera model for monocular 3D Morphable Model (3DMM) regression methods that effectively captures the perspective distortion effect commonly seen in close-up facial images.
>   Fitting 3D morphable models to video is a key technique in content creation. In particular, regression-based approaches have produced fast and accurate results by matching the rendered output of the morphable model to the target image. These methods typically achieve stable performance with orthographic projection, which eliminates the ambiguity between focal length and object distance. However, this simplification makes them unsuitable for close-up footage, such as that captured with head-mounted cameras.
>   We extend orthographic projection with a new shrinkage parameter, incorporating a pseudo-perspective effect while preserving the stability of the original projection. We present several techniques that allow finetuning of existing models, and demonstrate the effectiveness of our modification through both quantitative and qualitative comparisons using a custom dataset recorded with head-mounted cameras.

