---
layout: default
title: Human Video Generation from a Single Image with 3D Pose and View Control
---

# Human Video Generation from a Single Image with 3D Pose and View Control
**arXiv**：[2602.21188v1](https://arxiv.org/abs/2602.21188) · [PDF](https://arxiv.org/pdf/2602.21188.pdf)  
**作者**：Tiantian Wang, Chun-Han Yao, Tao Hu, Mallikarjun Byrasandra Ramalinga Reddy, Ming-Hsuan Yang, Varun Jampani  

**一句话要点**：提出HVG模型，通过3D姿态和视角控制从单图像生成高质量4D人体视频

**关键词**：人体视频生成, 扩散模型, 3D姿态控制, 多视角一致性, 时空对齐

## 3 点简述
- 核心问题：从单图像生成人体视频时，视角一致性和运动相关衣物褶皱推断困难
- 方法要点：采用关节姿态调制、视角与时间对齐、渐进时空采样确保多视角一致性和平滑过渡
- 实验或效果：在图像到视频任务中，HVG优于现有方法，生成高质量4D人体视频

## 摘要（原文）

> Recent diffusion methods have made significant progress in generating videos from single images due to their powerful visual generation capabilities. However, challenges persist in image-to-video synthesis, particularly in human video generation, where inferring view-consistent, motion-dependent clothing wrinkles from a single image remains a formidable problem. In this paper, we present Human Video Generation in 4D (HVG), a latent video diffusion model capable of generating high-quality, multi-view, spatiotemporally coherent human videos from a single image with 3D pose and view control. HVG achieves this through three key designs: (i) Articulated Pose Modulation, which captures the anatomical relationships of 3D joints via a novel dual-dimensional bone map and resolves self-occlusions across views by introducing 3D information; (ii) View and Temporal Alignment, which ensures multi-view consistency and alignment between a reference image and pose sequences for frame-to-frame stability; and (iii) Progressive Spatio-Temporal Sampling with temporal alignment to maintain smooth transitions in long multi-view animations. Extensive experiments on image-to-video tasks demonstrate that HVG outperforms existing methods in generating high-quality 4D human videos from diverse human images and pose inputs.

