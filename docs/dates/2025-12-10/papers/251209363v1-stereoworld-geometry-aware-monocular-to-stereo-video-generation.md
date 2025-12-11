---
layout: default
title: StereoWorld: Geometry-Aware Monocular-to-Stereo Video Generation
---

# StereoWorld: Geometry-Aware Monocular-to-Stereo Video Generation
**arXiv**：[2512.09363v1](https://arxiv.org/abs/2512.09363) · [PDF](https://arxiv.org/pdf/2512.09363.pdf)  
**作者**：Ke Xing, Longfei Li, Yuyang Yin, Hanwen Liang, Guixun Luo, Chen Fang, Jue Wang, Konstantinos N. Plataniotis, Xiaojie Jin, Yao Zhao, Yunchao Wei  

**一句话要点**：提出StereoWorld框架，利用预训练视频生成器实现高质量单目到立体视频转换，解决XR设备立体视频制作成本高和伪影问题。

**关键词**：立体视频生成, 单目到立体转换, 几何感知正则化, 时空分块, XR设备应用, 视频生成框架

## 3 点简述
- 核心问题：XR设备普及推动高质量立体视频需求，但现有制作方法成本高且易产生伪影。
- 方法要点：基于预训练视频生成器，结合几何感知正则化确保3D结构保真，并集成时空分块方案实现高效高分辨率合成。
- 实验或效果：构建大规模高清立体视频数据集，实验显示StereoWorld在视觉保真度和几何一致性上显著优于先前方法。

## 摘要（原文）

> The growing adoption of XR devices has fueled strong demand for high-quality stereo video, yet its production remains costly and artifact-prone. To address this challenge, we present StereoWorld, an end-to-end framework that repurposes a pretrained video generator for high-fidelity monocular-to-stereo video generation. Our framework jointly conditions the model on the monocular video input while explicitly supervising the generation with a geometry-aware regularization to ensure 3D structural fidelity. A spatio-temporal tiling scheme is further integrated to enable efficient, high-resolution synthesis. To enable large-scale training and evaluation, we curate a high-definition stereo video dataset containing over 11M frames aligned to natural human interpupillary distance (IPD). Extensive experiments demonstrate that StereoWorld substantially outperforms prior methods, generating stereo videos with superior visual fidelity and geometric consistency. The project webpage is available at https://ke-xing.github.io/StereoWorld/.

