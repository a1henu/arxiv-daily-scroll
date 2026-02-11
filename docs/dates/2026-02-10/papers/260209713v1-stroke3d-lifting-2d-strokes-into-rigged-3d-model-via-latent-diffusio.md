---
layout: default
title: Stroke3D: Lifting 2D strokes into rigged 3D model via latent diffusion models
---

# Stroke3D: Lifting 2D strokes into rigged 3D model via latent diffusion models
**arXiv**：[2602.09713v1](https://arxiv.org/abs/2602.09713) · [PDF](https://arxiv.org/pdf/2602.09713.pdf)  
**作者**：Ruisi Zhao, Haoren Zheng, Zongxin Yang, Hehe Fan, Yi Yang  

**一句话要点**：提出Stroke3D框架，通过2D笔画和文本提示生成可动画的3D模型

**关键词**：3D模型生成, 骨骼绑定, 潜在扩散模型, 笔画控制, 网格合成, 动画内容创建

## 3 点简述
- 核心问题：现有3D生成方法难以生成可动画几何，而骨骼绑定技术缺乏对骨骼创建的细粒度结构控制。
- 方法要点：采用两阶段流程，包括基于骨骼图VAE和DiT的可控骨骼生成，以及通过TextuRig数据集和SKA-DPO优化的增强网格合成。
- 实验或效果：实验表明Stroke3D能生成合理的骨骼和高质量网格，首次实现基于用户绘制2D笔画的绑定3D网格生成。

## 摘要（原文）

> Rigged 3D assets are fundamental to 3D deformation and animation. However, existing 3D generation methods face challenges in generating animatable geometry, while rigging techniques lack fine-grained structural control over skeleton creation. To address these limitations, we introduce Stroke3D, a novel framework that directly generates rigged meshes from user inputs: 2D drawn strokes and a descriptive text prompt. Our approach pioneers a two-stage pipeline that separates the generation into: 1) Controllable Skeleton Generation, we employ the Skeletal Graph VAE (Sk-VAE) to encode the skeleton's graph structure into a latent space, where the Skeletal Graph DiT (Sk-DiT) generates a skeletal embedding. The generation process is conditioned on both the text for semantics and the 2D strokes for explicit structural control, with the VAE's decoder reconstructing the final high-quality 3D skeleton; and 2) Enhanced Mesh Synthesis via TextuRig and SKA-DPO, where we then synthesize a textured mesh conditioned on the generated skeleton. For this stage, we first enhance an existing skeleton-to-mesh model by augmenting its training data with TextuRig: a dataset of textured and rigged meshes with captions, curated from Objaverse-XL. Additionally, we employ a preference optimization strategy, SKA-DPO, guided by a skeleton-mesh alignment score, to further improve geometric fidelity. Together, our framework enables a more intuitive workflow for creating ready to animate 3D content. To the best of our knowledge, our work is the first to generate rigged 3D meshes conditioned on user-drawn 2D strokes. Extensive experiments demonstrate that Stroke3D produces plausible skeletons and high-quality meshes.

