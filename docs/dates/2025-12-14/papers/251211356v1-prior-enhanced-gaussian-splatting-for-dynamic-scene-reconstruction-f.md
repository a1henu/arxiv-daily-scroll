---
layout: default
title: Prior-Enhanced Gaussian Splatting for Dynamic Scene Reconstruction from Casual Video
---

# Prior-Enhanced Gaussian Splatting for Dynamic Scene Reconstruction from Casual Video
**arXiv**：[2512.11356v1](https://arxiv.org/abs/2512.11356) · [PDF](https://arxiv.org/pdf/2512.11356.pdf)  
**作者**：Meng-Li Shih, Ying-Huan Chen, Yu-Lun Liu, Brian Curless  

**一句话要点**：提出先验增强高斯泼溅方法，用于从随意拍摄的单目视频重建动态场景

**关键词**：动态场景重建, 高斯泼溅, 单目视频, 先验增强, 对象跟踪, 深度优化

## 3 点简述
- 核心问题：从随意拍摄的单目RGB视频自动重建动态场景，需处理薄结构和运动一致性
- 方法要点：结合视频分割与极线误差图生成对象级掩码，指导深度损失和跟踪，并引入虚拟视图深度损失和骨架投影损失
- 实验或效果：系统超越先前单目动态场景重建方法，渲染质量显著提升

## 摘要（原文）

> We introduce a fully automatic pipeline for dynamic scene reconstruction from casually captured monocular RGB videos. Rather than designing a new scene representation, we enhance the priors that drive Dynamic Gaussian Splatting. Video segmentation combined with epipolar-error maps yields object-level masks that closely follow thin structures; these masks (i) guide an object-depth loss that sharpens the consistent video depth, and (ii) support skeleton-based sampling plus mask-guided re-identification to produce reliable, comprehensive 2-D tracks. Two additional objectives embed the refined priors in the reconstruction stage: a virtual-view depth loss removes floaters, and a scaffold-projection loss ties motion nodes to the tracks, preserving fine geometry and coherent motion. The resulting system surpasses previous monocular dynamic scene reconstruction methods and delivers visibly superior renderings

