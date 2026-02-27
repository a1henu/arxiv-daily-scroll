---
layout: default
title: DMAligner: Enhancing Image Alignment via Diffusion Model Based View Synthesis
---

# DMAligner: Enhancing Image Alignment via Diffusion Model Based View Synthesis
**arXiv**：[2602.23022v1](https://arxiv.org/abs/2602.23022) · [PDF](https://arxiv.org/pdf/2602.23022.pdf)  
**作者**：Xinglong Luo, Ao Luo, Zhengning Wang, Yueqi Yang, Chaoyu Feng, Lei Lei, Bing Zeng, Shuaicheng Liu  

**一句话要点**：提出DMAligner，通过扩散模型合成新视角以增强图像对齐效果。

**关键词**：图像对齐, 扩散模型, 视图合成, 动态感知, 数据集构建

## 3 点简述
- 核心问题：传统光流图像扭曲方法易受遮挡和光照变化影响，导致对齐质量下降。
- 方法要点：采用动态感知扩散训练，结合DMP模块区分动态前景与静态背景，实现对齐导向的视图合成。
- 实验或效果：在DSIA数据集和广泛视频数据集上验证了方法的优越性，代码已开源。

## 摘要（原文）

> Image alignment is a fundamental task in computer vision with broad applications. Existing methods predominantly employ optical flow-based image warping. However, this technique is susceptible to common challenges such as occlusions and illumination variations, leading to degraded alignment visual quality and compromised accuracy in downstream tasks. In this paper, we present DMAligner, a diffusion-based framework for image alignment through alignment-oriented view synthesis. DMAligner is crafted to tackle the challenges in image alignment from a new perspective, employing a generation-based solution that showcases strong capabilities and avoids the problems associated with flow-based image warping. Specifically, we propose a Dynamics-aware Diffusion Training approach for learning conditional image generation, synthesizing a novel view for image alignment. This incorporates a Dynamics-aware Mask Producing (DMP) module to adaptively distinguish dynamic foreground regions from static backgrounds, enabling the diffusion model to more effectively handle challenges that classical methods struggle to solve. Furthermore, we develop the Dynamic Scene Image Alignment (DSIA) dataset using Blender, which includes 1,033 indoor and outdoor scenes with over 30K image pairs tailored for image alignment. Extensive experimental results demonstrate the superiority of the proposed approach on DSIA benchmarks, as well as on a series of widely-used video datasets for qualitative comparisons. Our code is available at https://github.com/boomluo02/DMAligner.

