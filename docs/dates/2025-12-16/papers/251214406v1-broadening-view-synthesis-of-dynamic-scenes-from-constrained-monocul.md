---
layout: default
title: Broadening View Synthesis of Dynamic Scenes from Constrained Monocular Videos
---

# Broadening View Synthesis of Dynamic Scenes from Constrained Monocular Videos
**arXiv**：[2512.14406v1](https://arxiv.org/abs/2512.14406) · [PDF](https://arxiv.org/pdf/2512.14406.pdf)  
**作者**：Le Jiang, Shaotong Zhu, Yedi Luo, Shayda Moezzi, Sarah Ostadabbas  

**一句话要点**：提出ExpanDyNeRF框架，利用高斯先验和伪真值生成，解决动态NeRF在大视角偏移下的渲染不稳定问题。

**关键词**：动态神经辐射场, 单目视频合成, 高斯先验, 伪真值生成, 视角偏移渲染, 合成数据集

## 3 点简述
- 核心问题：动态NeRF在显著视角偏差下渲染不稳定，产生不真实结果。
- 方法要点：引入高斯先验和伪真值生成策略，优化密度和颜色特征以提升重建质量。
- 实验或效果：在SynDM和真实数据集上，ExpanDyNeRF在极端视角偏移下渲染保真度显著优于现有方法。

## 摘要（原文）

> In dynamic Neural Radiance Fields (NeRF) systems, state-of-the-art novel view synthesis methods often fail under significant viewpoint deviations, producing unstable and unrealistic renderings. To address this, we introduce Expanded Dynamic NeRF (ExpanDyNeRF), a monocular NeRF framework that leverages Gaussian splatting priors and a pseudo-ground-truth generation strategy to enable realistic synthesis under large-angle rotations. ExpanDyNeRF optimizes density and color features to improve scene reconstruction from challenging perspectives. We also present the Synthetic Dynamic Multiview (SynDM) dataset, the first synthetic multiview dataset for dynamic scenes with explicit side-view supervision-created using a custom GTA V-based rendering pipeline. Quantitative and qualitative results on SynDM and real-world datasets demonstrate that ExpanDyNeRF significantly outperforms existing dynamic NeRF methods in rendering fidelity under extreme viewpoint shifts. Further details are provided in the supplementary materials.

