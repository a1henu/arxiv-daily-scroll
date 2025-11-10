---
layout: default
title: Splatography: Sparse multi-view dynamic Gaussian Splatting for filmmaking challenges
---

# Splatography: Sparse multi-view dynamic Gaussian Splatting for filmmaking challenges
**arXiv**：[2511.05152v1](https://arxiv.org/abs/2511.05152) · [PDF](https://arxiv.org/pdf/2511.05152.pdf)  
**作者**：Adrian Azzarelli, Nantheera Anantrasirichai, David R Bull  

**一句话要点**：提出稀疏多视角动态高斯泼溅方法以解决低成本电影制作中动态3D重建难题

**关键词**：动态3D重建, 高斯泼溅, 稀疏多视角, 前景背景分割, 变形场建模, 电影制作应用

## 3 点简述
- 核心问题：稀疏相机配置限制现有方法捕捉复杂动态特征，影响电影制作成本效益
- 方法要点：分割高斯泼溅和变形场为前景与背景，使用稀疏掩码分别训练不同损失函数
- 实验或效果：在3D和2.5D数据集上实现SotA结果，PSNR提升高达3，模型尺寸减半

## 摘要（原文）

> Deformable Gaussian Splatting (GS) accomplishes photorealistic dynamic 3-D
> reconstruction from dense multi-view video (MVV) by learning to deform a
> canonical GS representation. However, in filmmaking, tight budgets can result
> in sparse camera configurations, which limits state-of-the-art (SotA) methods
> when capturing complex dynamic features. To address this issue, we introduce an
> approach that splits the canonical Gaussians and deformation field into
> foreground and background components using a sparse set of masks for frames at
> t=0. Each representation is separately trained on different loss functions
> during canonical pre-training. Then, during dynamic training, different
> parameters are modeled for each deformation field following common filmmaking
> practices. The foreground stage contains diverse dynamic features so changes in
> color, position and rotation are learned. While, the background containing
> film-crew and equipment, is typically dimmer and less dynamic so only changes
> in point position are learned. Experiments on 3-D and 2.5-D entertainment
> datasets show that our method produces SotA qualitative and quantitative
> results; up to 3 PSNR higher with half the model size on 3-D scenes. Unlike the
> SotA and without the need for dense mask supervision, our method also produces
> segmented dynamic reconstructions including transparent and dynamic textures.
> Code and video comparisons are available online:
> https://interims-git.github.io/

