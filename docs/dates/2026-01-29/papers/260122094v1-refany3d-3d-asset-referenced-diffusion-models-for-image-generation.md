---
layout: default
title: RefAny3D: 3D Asset-Referenced Diffusion Models for Image Generation
---

# RefAny3D: 3D Asset-Referenced Diffusion Models for Image Generation
**arXiv**：[2601.22094v1](https://arxiv.org/abs/2601.22094) · [PDF](https://arxiv.org/pdf/2601.22094.pdf)  
**作者**：Hanzhuo Huang, Qingyang Bao, Zekai Gu, Zhongshuo Du, Cheng Lin, Yuan Liu, Sibei Yang  

**一句话要点**：提出RefAny3D，一种基于3D资产参考的扩散模型，用于生成与3D资产一致的图像。

**关键词**：3D资产参考, 扩散模型, 图像生成, 双分支感知, 跨域生成

## 3 点简述
- 现有基于参考的图像生成方法局限于单图像参考，无法利用3D资产，限制了实际应用。
- 采用双分支感知的跨域扩散模型，结合多视角RGB图像和点云图，联合建模颜色和规范空间坐标。
- 实验表明，该方法能有效利用3D资产作为参考，生成与给定资产一致的图像。

## 摘要（原文）

> In this paper, we propose a 3D asset-referenced diffusion model for image generation, exploring how to integrate 3D assets into image diffusion models. Existing reference-based image generation methods leverage large-scale pretrained diffusion models and demonstrate strong capability in generating diverse images conditioned on a single reference image. However, these methods are limited to single-image references and cannot leverage 3D assets, constraining their practical versatility. To address this gap, we present a cross-domain diffusion model with dual-branch perception that leverages multi-view RGB images and point maps of 3D assets to jointly model their colors and canonical-space coordinates, achieving precise consistency between generated images and the 3D references. Our spatially aligned dual-branch generation architecture and domain-decoupled generation mechanism ensure the simultaneous generation of two spatially aligned but content-disentangled outputs, RGB images and point maps, linking 2D image attributes with 3D asset attributes. Experiments show that our approach effectively uses 3D assets as references to produce images consistent with the given assets, opening new possibilities for combining diffusion models with 3D content creation.

