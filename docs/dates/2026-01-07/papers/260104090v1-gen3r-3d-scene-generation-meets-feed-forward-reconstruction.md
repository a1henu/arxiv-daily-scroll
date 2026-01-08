---
layout: default
title: Gen3R: 3D Scene Generation Meets Feed-Forward Reconstruction
---

# Gen3R: 3D Scene Generation Meets Feed-Forward Reconstruction
**arXiv**：[2601.04090v1](https://arxiv.org/abs/2601.04090) · [PDF](https://arxiv.org/pdf/2601.04090.pdf)  
**作者**：Jiaxin Huang, Yuanbo Yang, Bangbang Yang, Lin Ma, Yuewen Ma, Yiyi Liao  

**一句话要点**：提出Gen3R方法，结合重建与生成模型先验，实现场景级3D生成与重建增强。

**关键词**：3D场景生成, 重建模型, 视频扩散模型, 潜在对齐, 点云生成, 多模态融合

## 3 点简述
- 核心问题：如何融合基础重建模型与视频扩散模型先验，实现高效场景级3D生成。
- 方法要点：通过适配器训练，对齐VGGT重建模型的几何潜在与视频扩散模型的外观潜在，联合生成解耦但对齐的潜在表示。
- 实验或效果：在单图和多图条件下达到先进水平，并利用生成先验增强重建鲁棒性，展示耦合模型的互惠效益。

## 摘要（原文）

> We present Gen3R, a method that bridges the strong priors of foundational reconstruction models and video diffusion models for scene-level 3D generation. We repurpose the VGGT reconstruction model to produce geometric latents by training an adapter on its tokens, which are regularized to align with the appearance latents of pre-trained video diffusion models. By jointly generating these disentangled yet aligned latents, Gen3R produces both RGB videos and corresponding 3D geometry, including camera poses, depth maps, and global point clouds. Experiments demonstrate that our approach achieves state-of-the-art results in single- and multi-image conditioned 3D scene generation. Additionally, our method can enhance the robustness of reconstruction by leveraging generative priors, demonstrating the mutual benefit of tightly coupling reconstruction and generative models.

