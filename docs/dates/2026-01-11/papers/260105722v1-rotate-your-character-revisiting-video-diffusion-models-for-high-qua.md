---
layout: default
title: Rotate Your Character: Revisiting Video Diffusion Models for High-Quality 3D Character Generation
---

# Rotate Your Character: Revisiting Video Diffusion Models for High-Quality 3D Character Generation
**arXiv**：[2601.05722v1](https://arxiv.org/abs/2601.05722) · [PDF](https://arxiv.org/pdf/2601.05722.pdf)  
**作者**：Jin Wang, Jianxiang Lu, Comi Chen, Guangzheng Xu, Haoyu Yang, Peng Chen, Na Zhang, Yifan Xu, Longhuang Wu, Shuai Shao, Qinglin Lu, Ping Luo  

**一句话要点**：提出RCM框架，通过视频扩散模型解决单图像生成高质量3D角色的挑战

**关键词**：3D角色生成, 新视图合成, 视频扩散模型, 图像到视频框架, 姿态转换

## 3 点简述
- 核心问题：单图像生成3D角色时，复杂姿态和自遮挡导致质量不佳
- 方法要点：将任意姿态角色转换到规范姿态，实现全视角一致的新视图合成
- 实验或效果：在1024x1024分辨率下，RCM在新视图合成和3D生成质量上优于现有方法

## 摘要（原文）

> Generating high-quality 3D characters from single images remains a significant challenge in digital content creation, particularly due to complex body poses and self-occlusion. In this paper, we present RCM (Rotate your Character Model), an advanced image-to-video diffusion framework tailored for high-quality novel view synthesis (NVS) and 3D character generation. Compared to existing diffusion-based approaches, RCM offers several key advantages: (1) transferring characters with any complex poses into a canonical pose, enabling consistent novel view synthesis across the entire viewing orbit, (2) high-resolution orbital video generation at 1024x1024 resolution, (3) controllable observation positions given different initial camera poses, and (4) multi-view conditioning supporting up to 4 input images, accommodating diverse user scenarios. Extensive experiments demonstrate that RCM outperforms state-of-the-art methods in both novel view synthesis and 3D generation quality.

