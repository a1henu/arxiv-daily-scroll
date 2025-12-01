---
layout: default
title: Fast Multi-view Consistent 3D Editing with Video Priors
---

# Fast Multi-view Consistent 3D Editing with Video Priors
**arXiv**：[2511.23172v1](https://arxiv.org/abs/2511.23172) · [PDF](https://arxiv.org/pdf/2511.23172.pdf)  
**作者**：Liyi Chen, Ruihuang Li, Guowen Zhang, Pengfei Wang, Lei Zhang  

**一句话要点**：提出ViP3DE，利用视频先验实现单次前向传播的多视角一致3D编辑

**关键词**：3D编辑, 多视角一致性, 视频先验, 生成模型, 几何感知去噪

## 3 点简述
- 现有方法依赖迭代2D-3D-2D更新，导致效率低且结果过平滑
- ViP3DE基于视频生成模型，通过单编辑视图生成其他一致视图，避免迭代
- 实验显示ViP3DE在单次前向传播中实现高质量编辑，显著提升速度与质量

## 摘要（原文）

> Text-driven 3D editing enables user-friendly 3D object or scene editing with text instructions. Due to the lack of multi-view consistency priors, existing methods typically resort to employing 2D generation or editing models to process each view individually, followed by iterative 2D-3D-2D updating. However, these methods are not only time-consuming but also prone to over-smoothed results because the different editing signals gathered from different views are averaged during the iterative process. In this paper, we propose generative Video Prior based 3D Editing (ViP3DE) to employ the temporal consistency priors from pre-trained video generation models for multi-view consistent 3D editing in a single forward pass. Our key insight is to condition the video generation model on a single edited view to generate other consistent edited views for 3D updating directly, thereby bypassing the iterative editing paradigm. Since 3D updating requires edited views to be paired with specific camera poses, we propose motion-preserved noise blending for the video model to generate edited views at predefined camera poses. In addition, we introduce geometry-aware denoising to further enhance multi-view consistency by integrating 3D geometric priors into video models. Extensive experiments demonstrate that our proposed ViP3DE can achieve high-quality 3D editing results even within a single forward pass, significantly outperforming existing methods in both editing quality and speed.

