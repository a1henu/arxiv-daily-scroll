---
layout: default
title: InpaintHuman: Reconstructing Occluded Humans with Multi-Scale UV Mapping and Identity-Preserving Diffusion Inpainting
---

# InpaintHuman: Reconstructing Occluded Humans with Multi-Scale UV Mapping and Identity-Preserving Diffusion Inpainting
**arXiv**：[2601.02098v1](https://arxiv.org/abs/2601.02098) · [PDF](https://arxiv.org/pdf/2601.02098.pdf)  
**作者**：Jinlong Fan, Shanshan Zhao, Liang Zheng, Jing Zhang, Yuxiang Yang, Mingming Gong  

**一句话要点**：提出InpaintHuman方法，通过多尺度UV映射和身份保持扩散修复，从遮挡单目视频重建完整可动画的3D人体化身。

**关键词**：3D人体重建, 遮挡修复, 扩散模型, UV映射, 单目视频, 身份保持

## 3 点简述
- 核心问题：从遮挡单目视频重建完整可动画3D人体化身时，现有方法在几何损坏和时间不一致方面存在挑战。
- 方法要点：采用多尺度UV参数化表示和身份保持扩散修复模块，结合文本反转和语义条件指导，实现鲁棒重建和身份保真。
- 实验或效果：在合成基准和真实场景实验中，展示了在多样姿态和视角下重建质量的竞争性性能和改进。

## 摘要（原文）

> Reconstructing complete and animatable 3D human avatars from monocular videos remains challenging, particularly under severe occlusions. While 3D Gaussian Splatting has enabled photorealistic human rendering, existing methods struggle with incomplete observations, often producing corrupted geometry and temporal inconsistencies. We present InpaintHuman, a novel method for generating high-fidelity, complete, and animatable avatars from occluded monocular videos. Our approach introduces two key innovations: (i) a multi-scale UV-parameterized representation with hierarchical coarse-to-fine feature interpolation, enabling robust reconstruction of occluded regions while preserving geometric details; and (ii) an identity-preserving diffusion inpainting module that integrates textual inversion with semantic-conditioned guidance for subject-specific, temporally coherent completion. Unlike SDS-based methods, our approach employs direct pixel-level supervision to ensure identity fidelity. Experiments on synthetic benchmarks (PeopleSnapshot, ZJU-MoCap) and real-world scenarios (OcMotion) demonstrate competitive performance with consistent improvements in reconstruction quality across diverse poses and viewpoints.

