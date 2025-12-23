---
layout: default
title: WorldWarp: Propagating 3D Geometry with Asynchronous Video Diffusion
---

# WorldWarp: Propagating 3D Geometry with Asynchronous Video Diffusion
**arXiv**：[2512.19678v1](https://arxiv.org/abs/2512.19678) · [PDF](https://arxiv.org/pdf/2512.19678.pdf)  
**作者**：Hanyang Kong, Xingyi Yang, Xiaoxu Zheng, Xinchao Wang  

**一句话要点**：提出WorldWarp框架，通过3D几何缓存与时空扩散模型解决长视频生成中的几何一致性问题。

**关键词**：视频生成, 3D几何一致性, 高斯溅射, 时空扩散模型, 变噪声调度, 长视频合成

## 3 点简述
- 核心问题：长视频生成需3D几何一致性，但现有方法在潜在空间中操作，导致遮挡区域和复杂相机轨迹处理困难。
- 方法要点：结合3D高斯溅射构建几何缓存作为结构锚点，并设计时空扩散模型进行填充与精修，采用变噪声调度。
- 实验或效果：通过动态更新3D缓存，在视频块间保持一致性，实现高保真度生成，达到先进水平。

## 摘要（原文）

> Generating long-range, geometrically consistent video presents a fundamental dilemma: while consistency demands strict adherence to 3D geometry in pixel space, state-of-the-art generative models operate most effectively in a camera-conditioned latent space. This disconnect causes current methods to struggle with occluded areas and complex camera trajectories. To bridge this gap, we propose WorldWarp, a framework that couples a 3D structural anchor with a 2D generative refiner. To establish geometric grounding, WorldWarp maintains an online 3D geometric cache built via Gaussian Splatting (3DGS). By explicitly warping historical content into novel views, this cache acts as a structural scaffold, ensuring each new frame respects prior geometry. However, static warping inevitably leaves holes and artifacts due to occlusions. We address this using a Spatio-Temporal Diffusion (ST-Diff) model designed for a "fill-and-revise" objective. Our key innovation is a spatio-temporal varying noise schedule: blank regions receive full noise to trigger generation, while warped regions receive partial noise to enable refinement. By dynamically updating the 3D cache at every step, WorldWarp maintains consistency across video chunks. Consequently, it achieves state-of-the-art fidelity by ensuring that 3D logic guides structure while diffusion logic perfects texture. Project page: \href{https://hyokong.github.io/worldwarp-page/}{https://hyokong.github.io/worldwarp-page/}.

