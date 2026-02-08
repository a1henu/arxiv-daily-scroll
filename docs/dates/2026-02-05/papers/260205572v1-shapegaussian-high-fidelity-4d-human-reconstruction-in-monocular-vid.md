---
layout: default
title: ShapeGaussian: High-Fidelity 4D Human Reconstruction in Monocular Videos via Vision Priors
---

# ShapeGaussian: High-Fidelity 4D Human Reconstruction in Monocular Videos via Vision Priors
**arXiv**：[2602.05572v1](https://arxiv.org/abs/2602.05572) · [PDF](https://arxiv.org/pdf/2602.05572.pdf)  
**作者**：Zhenxiao Liang, Ning Zhang, Youbao Tang, Ruei-Sung Lin, Qixing Huang, Peng Chang, Jing Xiao  

**一句话要点**：提出ShapeGaussian，通过视觉先验实现单目视频中高保真4D人体重建

**关键词**：4D人体重建, 单目视频, 视觉先验, 神经变形模型, 高保真重建

## 3 点简述
- 核心问题：现有方法在单目视频中难以兼顾高保真与鲁棒性，模板方法易受姿态估计误差影响。
- 方法要点：采用两阶段流程，先学习粗几何，再通过神经变形模型细化，利用2D视觉先验避免姿态误差。
- 实验或效果：在多样人体运动中超越模板方法，实现更高重建精度和视觉质量。

## 摘要（原文）

> We introduce ShapeGaussian, a high-fidelity, template-free method for 4D human reconstruction from casual monocular videos. Generic reconstruction methods lacking robust vision priors, such as 4DGS, struggle to capture high-deformation human motion without multi-view cues. While template-based approaches, primarily relying on SMPL, such as HUGS, can produce photorealistic results, they are highly susceptible to errors in human pose estimation, often leading to unrealistic artifacts. In contrast, ShapeGaussian effectively integrates template-free vision priors to achieve both high-fidelity and robust scene reconstructions. Our method follows a two-step pipeline: first, we learn a coarse, deformable geometry using pretrained models that estimate data-driven priors, providing a foundation for reconstruction. Then, we refine this geometry using a neural deformation model to capture fine-grained dynamic details. By leveraging 2D vision priors, we mitigate artifacts from erroneous pose estimation in template-based methods and employ multiple reference frames to resolve the invisibility issue of 2D keypoints in a template-free manner. Extensive experiments demonstrate that ShapeGaussian surpasses template-based methods in reconstruction accuracy, achieving superior visual quality and robustness across diverse human motions in casual monocular videos.

