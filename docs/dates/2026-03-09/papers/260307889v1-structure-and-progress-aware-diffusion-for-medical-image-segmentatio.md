---
layout: default
title: Structure and Progress Aware Diffusion for Medical Image Segmentation
---

# Structure and Progress Aware Diffusion for Medical Image Segmentation
**arXiv**：[2603.07889v1](https://arxiv.org/abs/2603.07889) · [PDF](https://arxiv.org/pdf/2603.07889.pdf)  
**作者**：Siyuan Song, Guyue Hu, Chenglong Li, Dengdi Sun, Zhe Jin, Jin Tang  

**一句话要点**：提出结构感知扩散模型以解决医学图像分割中粗结构与细边界学习不平衡问题

**关键词**：医学图像分割, 扩散模型, 结构感知学习, 边界优化, 进度感知调度

## 3 点简述
- 核心问题：医学图像分割需同时学习粗形态语义结构和细边界，但细边界常因噪声和模糊性不可靠，现有方法在整个训练中同时学习两者，导致效果受限。
- 方法要点：设计结构感知扩散（SPAD），包含语义集中扩散和边界集中扩散，通过进度感知调度器调制噪声强度，形成从粗到细的扩散范式。
- 实验或效果：未知，但方法旨在鼓励模型早期关注粗结构，后期转向细边界，以提升分割准确性。

## 摘要（原文）

> Medical image segmentation is crucial for computer-aided diagnosis, which necessitates understanding both coarse morphological and semantic structures, as well as carving fine boundaries. The morphological and semantic structures in medical images are beneficial and stable clues for target understanding. While the fine boundaries of medical targets (like tumors and lesions) are usually ambiguous and noisy since lesion overlap, annotation uncertainty, and so on, making it not reliable to serve as early supervision. However, existing methods simultaneously learn coarse structures and fine boundaries throughout the training process. In this paper, we propose a structure and progress-aware diffusion (SPAD) for medical image segmentation, which consists of a semantic-concentrated diffusion (ScD) and a boundary-centralized diffusion (BcD) modulated by a progress-aware scheduler (PaS). Specifically, the semantic-concentrated diffusion introduces anchor-preserved target perturbation, which perturbs pixels within a medical target but preserves unaltered areas as semantic anchors, encouraging the model to infer noisy target areas from the surrounding semantic context. The boundary-centralized diffusion introduces progress-aware boundary noise, which blurs unreliable and ambiguous boundaries, thus compelling the model to focus on coarse but stable anatomical morphology and global semantics. Furthermore, the progress-aware scheduler gradually modulates noise intensity of the ScD and BcD forming a coarse-to-fine diffusion paradigm, which encourage focusing on coarse morphological and semantic structures during early target understanding stages and gradually shifting to fine target boundaries during later contour adjusting stages.

