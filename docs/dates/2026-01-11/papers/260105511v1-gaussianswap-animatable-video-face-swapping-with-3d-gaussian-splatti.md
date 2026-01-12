---
layout: default
title: GaussianSwap: Animatable Video Face Swapping with 3D Gaussian Splatting
---

# GaussianSwap: Animatable Video Face Swapping with 3D Gaussian Splatting
**arXiv**：[2601.05511v1](https://arxiv.org/abs/2601.05511) · [PDF](https://arxiv.org/pdf/2601.05511.pdf)  
**作者**：Xuan Cheng, Jiahao Rao, Chengyang Li, Wenhao Wang, Weilin Chen, Lvqing Yang  

**一句话要点**：提出GaussianSwap框架，基于3D高斯泼溅构建可动画视频人脸交换，解决传统像素方法缺乏交互控制的问题。

**关键词**：视频人脸交换, 3D高斯泼溅, FLAME模型, 身份嵌入, 动态控制, 交互应用

## 3 点简述
- 传统视频人脸交换方法生成像素表示，无法支持动画或交互操作。
- 框架通过提取FLAME参数和相机姿态，将3D高斯泼溅绑定到FLAME模型，实现动态面部控制。
- 实验显示，该方法在身份保持、视觉清晰度和时间一致性方面表现优越，支持交互应用。

## 摘要（原文）

> We introduce GaussianSwap, a novel video face swapping framework that constructs a 3D Gaussian Splatting based face avatar from a target video while transferring identity from a source image to the avatar. Conventional video swapping frameworks are limited to generating facial representations in pixel-based formats. The resulting swapped faces exist merely as a set of unstructured pixels without any capacity for animation or interactive manipulation. Our work introduces a paradigm shift from conventional pixel-based video generation to the creation of high-fidelity avatar with swapped faces. The framework first preprocesses target video to extract FLAME parameters, camera poses and segmentation masks, and then rigs 3D Gaussian splats to the FLAME model across frames, enabling dynamic facial control. To ensure identity preserving, we propose an compound identity embedding constructed from three state-of-the-art face recognition models for avatar finetuning. Finally, we render the face-swapped avatar on the background frames to obtain the face-swapped video. Experimental results demonstrate that GaussianSwap achieves superior identity preservation, visual clarity and temporal consistency, while enabling previously unattainable interactive applications.

