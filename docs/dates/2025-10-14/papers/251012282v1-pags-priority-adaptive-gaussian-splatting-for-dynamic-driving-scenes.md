---
layout: default
title: PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes
---

# PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes
**arXiv**：[2510.12282v1](https://arxiv.org/abs/2510.12282) · [PDF](https://arxiv.org/pdf/2510.12282.pdf)  
**作者**：Ying A, Wenzhang Sun, Chang Zeng, Chunfeng Wang, Hao Li, Jianxun Cui  

**一句话要点**：提出PAGS框架，通过语义优先级优化动态驾驶场景的3D重建与渲染效率

**关键词**：3D场景重建, 高斯泼溅, 语义优先级, 动态驾驶场景, 渲染加速, 计算优化

## 3 点简述
- 核心问题：动态3D城市场景重建在保真度与计算成本间存在权衡，现有方法资源分配不均
- 方法要点：引入语义引导剪枝与正则化策略，以及优先级驱动渲染管道，优化资源分配
- 实验或效果：在Waymo和KITTI数据集上验证，提升重建质量并加速渲染至超过350 FPS

## 摘要（原文）

> Reconstructing dynamic 3D urban scenes is crucial for autonomous driving, yet
> current methods face a stark trade-off between fidelity and computational cost.
> This inefficiency stems from their semantically agnostic design, which
> allocates resources uniformly, treating static backgrounds and safety-critical
> objects with equal importance. To address this, we introduce Priority-Adaptive
> Gaussian Splatting (PAGS), a framework that injects task-aware semantic
> priorities directly into the 3D reconstruction and rendering pipeline. PAGS
> introduces two core contributions: (1) Semantically-Guided Pruning and
> Regularization strategy, which employs a hybrid importance metric to
> aggressively simplify non-critical scene elements while preserving fine-grained
> details on objects vital for navigation. (2) Priority-Driven Rendering
> pipeline, which employs a priority-based depth pre-pass to aggressively cull
> occluded primitives and accelerate the final shading computations. Extensive
> experiments on the Waymo and KITTI datasets demonstrate that PAGS achieves
> exceptional reconstruction quality, particularly on safety-critical objects,
> while significantly reducing training time and boosting rendering speeds to
> over 350 FPS.

