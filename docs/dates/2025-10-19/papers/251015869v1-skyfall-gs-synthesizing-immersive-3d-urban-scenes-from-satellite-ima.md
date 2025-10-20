---
layout: default
title: Skyfall-GS: Synthesizing Immersive 3D Urban Scenes from Satellite Imagery
---

# Skyfall-GS: Synthesizing Immersive 3D Urban Scenes from Satellite Imagery
**arXiv**：[2510.15869v1](https://arxiv.org/abs/2510.15869) · [PDF](https://arxiv.org/pdf/2510.15869.pdf)  
**作者**：Jie-Ying Lee, Yi-Ruei Liu, Shr-Ruei Tsai, Wei-Cheng Chang, Chung-Ho Wu, Jiewen Chan, Zhenjun Zhao, Chieh Hubert Lin, Yu-Lun Liu  

**一句话要点**：提出Skyfall-GS框架，从卫星图像合成沉浸式3D城市场景，无需3D标注

**关键词**：3D场景合成, 卫星图像, 扩散模型, 几何优化, 沉浸式探索

## 3 点简述
- 核心问题：缺乏大规模高质量3D扫描数据，难以训练通用生成模型
- 方法要点：结合卫星图像提供粗几何与扩散模型生成近景外观，采用课程驱动迭代优化
- 实验或效果：在跨视角几何一致性和纹理真实感上优于现有方法，支持实时沉浸探索

## 摘要（原文）

> Synthesizing large-scale, explorable, and geometrically accurate 3D urban
> scenes is a challenging yet valuable task in providing immersive and embodied
> applications. The challenges lie in the lack of large-scale and high-quality
> real-world 3D scans for training generalizable generative models. In this
> paper, we take an alternative route to create large-scale 3D scenes by
> synergizing the readily available satellite imagery that supplies realistic
> coarse geometry and the open-domain diffusion model for creating high-quality
> close-up appearances. We propose \textbf{Skyfall-GS}, the first city-block
> scale 3D scene creation framework without costly 3D annotations, also featuring
> real-time, immersive 3D exploration. We tailor a curriculum-driven iterative
> refinement strategy to progressively enhance geometric completeness and
> photorealistic textures. Extensive experiments demonstrate that Skyfall-GS
> provides improved cross-view consistent geometry and more realistic textures
> compared to state-of-the-art approaches. Project page:
> https://skyfall-gs.jayinnn.dev/

