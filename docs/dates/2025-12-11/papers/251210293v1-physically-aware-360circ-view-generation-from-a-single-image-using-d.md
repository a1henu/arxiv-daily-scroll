---
layout: default
title: Physically Aware 360$^\circ$ View Generation from a Single Image using Disentangled Scene Embeddings
---

# Physically Aware 360$^\circ$ View Generation from a Single Image using Disentangled Scene Embeddings
**arXiv**：[2512.10293v1](https://arxiv.org/abs/2512.10293) · [PDF](https://arxiv.org/pdf/2512.10293.pdf)  
**作者**：Karthikeya KV, Narendra Bandaru  

**一句话要点**：提出Disentangled360，通过解耦场景嵌入从单图像生成物理感知的360°视图，用于医学成像和自然场景重建。

**关键词**：单图像视图合成, 360度渲染, 解耦表示, 医学成像, Gaussian Splatting, 物理感知渲染

## 3 点简述
- 核心问题：现有方法简化各向异性光行为或缺乏跨场景泛化能力，难以从单图像生成物理准确的360°视图。
- 方法要点：在Gaussian Splatting骨干中区分各向同性和各向异性贡献，采用双分支条件框架和混合姿态无关锚定方法。
- 实验或效果：在Mip-NeRF 360等数据集上SSIM和LPIPS表现优越，支持交互式应用，无需场景特定微调或昂贵光子模拟。

## 摘要（原文）

> We introduce Disentangled360, an innovative 3D-aware technology that integrates the advantages of direction disentangled volume rendering with single-image 360° unique view synthesis for applications in medical imaging and natural scene reconstruction. In contrast to current techniques that either oversimplify anisotropic light behavior or lack generalizability across various contexts, our framework distinctly differentiates between isotropic and anisotropic contributions inside a Gaussian Splatting backbone. We implement a dual-branch conditioning framework, one optimized for CT intensity driven scattering in volumetric data and the other for real-world RGB scenes through normalized camera embeddings. To address scale ambiguity and maintain structural realism, we present a hybrid pose agnostic anchoring method that adaptively samples scene depth and material transitions, functioning as stable pivots during scene distillation. Our design integrates preoperative radiography simulation and consumer-grade 360° rendering into a singular inference pipeline, facilitating rapid, photorealistic view synthesis with inherent directionality. Evaluations on the Mip-NeRF 360, RealEstate10K, and DeepDRR datasets indicate superior SSIM and LPIPS performance, while runtime assessments confirm its viability for interactive applications. Disentangled360 facilitates mixed-reality medical supervision, robotic perception, and immersive content creation, eliminating the necessity for scene-specific finetuning or expensive photon simulations.

