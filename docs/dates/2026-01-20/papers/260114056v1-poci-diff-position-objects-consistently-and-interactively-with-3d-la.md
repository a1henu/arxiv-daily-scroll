---
layout: default
title: POCI-Diff: Position Objects Consistently and Interactively with 3D-Layout Guided Diffusion
---

# POCI-Diff: Position Objects Consistently and Interactively with 3D-Layout Guided Diffusion
**arXiv**：[2601.14056v1](https://arxiv.org/abs/2601.14056) · [PDF](https://arxiv.org/pdf/2601.14056.pdf)  
**作者**：Andrea Rigo, Luca Stornaiuolo, Weijie Wang, Mauro Martino, Bruno Lepri, Nicu Sebe  

**一句话要点**：提出POCI-Diff以解决文本到图像生成中3D布局控制与编辑的一致性问题

**关键词**：文本到图像生成, 3D布局控制, 扩散模型, 对象一致性, 交互式编辑

## 3 点简述
- 核心问题：现有方法在空间控制时易扭曲对象几何且编辑间缺乏一致性
- 方法要点：通过混合潜在扩散绑定文本到3D边界框，实现无扭曲的生成编辑
- 实验或效果：在视觉保真度和布局遵循上优于先进方法，消除几何伪影

## 摘要（原文）

> We propose a diffusion-based approach for Text-to-Image (T2I) generation with consistent and interactive 3D layout control and editing. While prior methods improve spatial adherence using 2D cues or iterative copy-warp-paste strategies, they often distort object geometry and fail to preserve consistency across edits. To address these limitations, we introduce a framework for Positioning Objects Consistently and Interactively (POCI-Diff), a novel formulation for jointly enforcing 3D geometric constraints and instance-level semantic binding within a unified diffusion process. Our method enables explicit per-object semantic control by binding individual text descriptions to specific 3D bounding boxes through Blended Latent Diffusion, allowing one-shot synthesis of complex multi-object scenes. We further propose a warping-free generative editing pipeline that supports object insertion, removal, and transformation via regeneration rather than pixel deformation. To preserve object identity and consistency across edits, we condition the diffusion process on reference images using IP-Adapter, enabling coherent object appearance throughout interactive 3D editing while maintaining global scene coherence. Experimental results demonstrate that POCI-Diff produces high-quality images consistent with the specified 3D layouts and edits, outperforming state-of-the-art methods in both visual fidelity and layout adherence while eliminating warping-induced geometric artifacts.

