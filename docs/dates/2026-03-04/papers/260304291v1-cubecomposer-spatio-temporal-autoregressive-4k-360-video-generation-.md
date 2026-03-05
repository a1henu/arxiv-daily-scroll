---
layout: default
title: CubeComposer: Spatio-Temporal Autoregressive 4K 360° Video Generation from Perspective Video
---

# CubeComposer: Spatio-Temporal Autoregressive 4K 360° Video Generation from Perspective Video
**arXiv**：[2603.04291v1](https://arxiv.org/abs/2603.04291) · [PDF](https://arxiv.org/pdf/2603.04291.pdf)  
**作者**：Lingen Li, Guangzhi Wang, Xiaoyu Li, Zhaoyang Zhang, Qi Dou, Jinwei Gu, Tianfan Xue, Ying Shan  

**一句话要点**：提出CubeComposer以从视角视频生成4K 360°视频，支持VR应用。

**关键词**：360°视频生成, 自回归扩散模型, 立方体贴图, 高分辨率合成, 虚拟现实应用

## 3 点简述
- 核心问题：现有方法受限于计算，仅支持≤1K分辨率，依赖后处理超分辨率。
- 方法要点：使用立方体贴图表示和时空自回归策略，降低内存需求并提升分辨率。
- 实验或效果：在基准数据集上优于现有方法，支持高分辨率VR场景。

## 摘要（原文）

> Generating high-quality 360° panoramic videos from perspective input is one of the crucial applications for virtual reality (VR), whereby high-resolution videos are especially important for immersive experience. Existing methods are constrained by computational limitations of vanilla diffusion models, only supporting $\leq$ 1K resolution native generation and relying on suboptimal post super-resolution to increase resolution. We introduce CubeComposer, a novel spatio-temporal autoregressive diffusion model that natively generates 4K-resolution 360° videos. By decomposing videos into cubemap representations with six faces, CubeComposer autoregressively synthesizes content in a well-planned spatio-temporal order, reducing memory demands while enabling high-resolution output. Specifically, to address challenges in multi-dimensional autoregression, we propose: (1) a spatio-temporal autoregressive strategy that orchestrates 360° video generation across cube faces and time windows for coherent synthesis; (2) a cube face context management mechanism, equipped with a sparse context attention design to improve efficiency; and (3) continuity-aware techniques, including cube-aware positional encoding, padding, and blending to eliminate boundary seams. Extensive experiments on benchmark datasets demonstrate that CubeComposer outperforms state-of-the-art methods in native resolution and visual quality, supporting practical VR application scenarios. Project page: https://lg-li.github.io/project/cubecomposer

