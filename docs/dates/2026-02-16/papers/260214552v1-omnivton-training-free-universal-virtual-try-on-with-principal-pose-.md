---
layout: default
title: OmniVTON++: Training-Free Universal Virtual Try-On with Principal Pose Guidance
---

# OmniVTON++: Training-Free Universal Virtual Try-On with Principal Pose Guidance
**arXiv**：[2602.14552v1](https://arxiv.org/abs/2602.14552) · [PDF](https://arxiv.org/pdf/2602.14552.pdf)  
**作者**：Zhaotong Yang, Yong Du, Shengfeng He, Yuhui Li, Xinzhe Li, Yangyang Xu, Junyu Dong, Jian Yang  

**一句话要点**：提出OmniVTON++训练免费通用虚拟试穿框架，通过结构化服装变形、主姿态引导和连续边界缝合解决泛化挑战。

**关键词**：虚拟试穿, 训练免费框架, 扩散模型, 服装对齐, 姿态引导, 边界优化

## 3 点简述
- 核心问题：现有虚拟试穿方法依赖特定数据训练，泛化能力有限，难以作为统一解决方案部署。
- 方法要点：结合结构化服装变形实现服装对齐，主姿态引导调控扩散采样结构，连续边界缝合优化边界连续性。
- 实验或效果：在跨数据集和跨服装类型评估中达到先进性能，支持多服装、多人物和动漫角色试穿。

## 摘要（原文）

> Image-based Virtual Try-On (VTON) concerns the synthesis of realistic person imagery through garment re-rendering under human pose and body constraints. In practice, however, existing approaches are typically optimized for specific data conditions, making their deployment reliant on retraining and limiting their generalization as a unified solution. We present OmniVTON++, a training-free VTON framework designed for universal applicability. It addresses the intertwined challenges of garment alignment, human structural coherence, and boundary continuity by coordinating Structured Garment Morphing for correspondence-driven garment adaptation, Principal Pose Guidance for step-wise structural regulation during diffusion sampling, and Continuous Boundary Stitching for boundary-aware refinement, forming a cohesive pipeline without task-specific retraining. Experimental results demonstrate that OmniVTON++ achieves state-of-the-art performance across diverse generalization settings, including cross-dataset and cross-garment-type evaluations, while reliably operating across scenarios and diffusion backbones within a single formulation. In addition to single-garment, single-human cases, the framework supports multi-garment, multi-human, and anime character virtual try-on, expanding the scope of virtual try-on applications. The source code will be released to the public.

