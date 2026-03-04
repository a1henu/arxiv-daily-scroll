---
layout: default
title: Track4World: Feedforward World-centric Dense 3D Tracking of All Pixels
---

# Track4World: Feedforward World-centric Dense 3D Tracking of All Pixels
**arXiv**：[2603.02573v1](https://arxiv.org/abs/2603.02573) · [PDF](https://arxiv.org/pdf/2603.02573.pdf)  
**作者**：Jiahao Lu, Jiayi Xu, Wenbo Hu, Ruijie Zhu, Chengfeng Zhao, Sai-Kit Yeung, Ying Shan, Yuan Liu  

**一句话要点**：提出Track4World前馈模型，实现世界坐标系下所有像素的高效密集3D跟踪

**关键词**：单目3D跟踪, 密集场景流, 世界坐标系, 前馈模型, 4D重建

## 3 点简述
- 核心问题：单目视频中每个像素的3D轨迹估计，现有方法局限于稀疏点跟踪或慢速优化框架
- 方法要点：基于VGGT风格ViT编码全局3D场景，应用新3D相关方案估计任意帧对的像素级2D/3D密集流
- 实验或效果：在多个基准测试中，2D/3D流估计和3D跟踪性能优于现有方法，适用于真实世界4D重建

## 摘要（原文）

> Estimating the 3D trajectory of every pixel from a monocular video is crucial and promising for a comprehensive understanding of the 3D dynamics of videos. Recent monocular 3D tracking works demonstrate impressive performance, but are limited to either tracking sparse points on the first frame or a slow optimization-based framework for dense tracking. In this paper, we propose a feedforward model, called Track4World, enabling an efficient holistic 3D tracking of every pixel in the world-centric coordinate system. Built on the global 3D scene representation encoded by a VGGT-style ViT, Track4World applies a novel 3D correlation scheme to simultaneously estimate the pixel-wise 2D and 3D dense flow between arbitrary frame pairs. The estimated scene flow, along with the reconstructed 3D geometry, enables subsequent efficient 3D tracking of every pixel of this video. Extensive experiments on multiple benchmarks demonstrate that our approach consistently outperforms existing methods in 2D/3D flow estimation and 3D tracking, highlighting its robustness and scalability for real-world 4D reconstruction tasks.

