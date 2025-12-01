---
layout: default
title: Image Valuation in NeRF-based 3D reconstruction
---

# Image Valuation in NeRF-based 3D reconstruction
**arXiv**：[2511.23052v1](https://arxiv.org/abs/2511.23052) · [PDF](https://arxiv.org/pdf/2511.23052.pdf)  
**作者**：Grigorios Aris Cheimariotis, Antonis Karakottas, Vangelis Chatzis, Angelos Kanlis, Dimitrios Zarpalas  

**一句话要点**：提出基于PSNR和MSE的图像贡献量化方法，以评估NeRF重建中野外图像集的个体效用。

**关键词**：NeRF重建, 图像贡献评估, 数据估值, 重建质量指标, 野外场景

## 3 点简述
- 核心问题：野外图像集在NeRF重建中质量不均，导致输入效用差异。
- 方法要点：通过重建质量指标（PSNR和MSE）量化每张图像的贡献。
- 实验或效果：验证中移除低贡献图像，测量对重建保真度的影响。

## 摘要（原文）

> Data valuation and monetization are becoming increasingly important across domains such as eXtended Reality (XR) and digital media. In the context of 3D scene reconstruction from a set of images -- whether casually or professionally captured -- not all inputs contribute equally to the final output. Neural Radiance Fields (NeRFs) enable photorealistic 3D reconstruction of scenes by optimizing a volumetric radiance field given a set of images. However, in-the-wild scenes often include image captures of varying quality, occlusions, and transient objects, resulting in uneven utility across inputs. In this paper we propose a method to quantify the individual contribution of each image to NeRF-based reconstructions of in-the-wild image sets. Contribution is assessed through reconstruction quality metrics based on PSNR and MSE. We validate our approach by removing low-contributing images during training and measuring the resulting impact on reconstruction fidelity.

