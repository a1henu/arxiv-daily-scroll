---
layout: default
title: MotionCrafter: Dense Geometry and Motion Reconstruction with a 4D VAE
---

# MotionCrafter: Dense Geometry and Motion Reconstruction with a 4D VAE
**arXiv**：[2602.08961v1](https://arxiv.org/abs/2602.08961) · [PDF](https://arxiv.org/pdf/2602.08961.pdf)  
**作者**：Ruijie Zhu, Jiahao Lu, Wenbo Hu, Xiaoguang Han, Jianfei Cai, Ying Shan, Chuanxia Zheng  

**一句话要点**：提出MotionCrafter框架，基于视频扩散联合重建单目视频的4D几何与稠密运动

**关键词**：4D重建, 稠密运动估计, 视频扩散模型, 单目视频处理, 几何重建, 场景流估计

## 3 点简述
- 核心问题：从单目视频联合重建4D几何和稠密运动，现有方法因强制对齐RGB VAE潜在分布导致性能不佳
- 方法要点：引入联合表示稠密3D点图和3D场景流，并设计4D VAE及新数据归一化策略以优化扩散先验迁移
- 实验或效果：在多个数据集上实现几何重建和运动估计的SOTA性能，分别提升38.64%和25.0%，无需后优化

## 摘要（原文）

> We introduce MotionCrafter, a video diffusion-based framework that jointly reconstructs 4D geometry and estimates dense motion from a monocular video. The core of our method is a novel joint representation of dense 3D point maps and 3D scene flows in a shared coordinate system, and a novel 4D VAE to effectively learn this representation. Unlike prior work that forces the 3D value and latents to align strictly with RGB VAE latents-despite their fundamentally different distributions-we show that such alignment is unnecessary and leads to suboptimal performance. Instead, we introduce a new data normalization and VAE training strategy that better transfers diffusion priors and greatly improves reconstruction quality. Extensive experiments across multiple datasets demonstrate that MotionCrafter achieves state-of-the-art performance in both geometry reconstruction and dense scene flow estimation, delivering 38.64% and 25.0% improvements in geometry and motion reconstruction, respectively, all without any post-optimization. Project page: https://ruijiezhu94.github.io/MotionCrafter_Page

