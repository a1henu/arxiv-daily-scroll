---
layout: default
title: SR3R: Rethinking Super-Resolution 3D Reconstruction With Feed-Forward Gaussian Splatting
---

# SR3R: Rethinking Super-Resolution 3D Reconstruction With Feed-Forward Gaussian Splatting
**arXiv**：[2602.24020v1](https://arxiv.org/abs/2602.24020) · [PDF](https://arxiv.org/pdf/2602.24020.pdf)  
**作者**：Xiang Feng, Xiangbo Wang, Tieshi Zhong, Chengkai Wang, Yiting Zhao, Tianxiang Xu, Zhenzhong Kuang, Feiwei Qin, Xuefei Yin, Yanming Zhu  

**一句话要点**：提出SR3R框架，通过前馈映射从稀疏低分辨率视图直接预测高分辨率3D高斯溅射表示，以解决3D超分辨率重建的泛化与实时性问题。

**关键词**：3D超分辨率, 高斯溅射, 前馈映射, 零样本泛化, 稀疏视图重建

## 3 点简述
- 现有3D超分辨率方法依赖密集输入和逐场景优化，限制高频先验和泛化能力。
- SR3R将3D超分辨率重构为前馈映射，学习3D特定高频几何与外观，提升重建保真度。
- 实验表明SR3R在三个基准上超越现有方法，实现强零样本泛化，优于逐场景优化方法。

## 摘要（原文）

> 3D super-resolution (3DSR) aims to reconstruct high-resolution (HR) 3D scenes from low-resolution (LR) multi-view images. Existing methods rely on dense LR inputs and per-scene optimization, which restricts the high-frequency priors for constructing HR 3D Gaussian Splatting (3DGS) to those inherited from pretrained 2D super-resolution (2DSR) models. This severely limits reconstruction fidelity, cross-scene generalization, and real-time usability. We propose to reformulate 3DSR as a direct feed-forward mapping from sparse LR views to HR 3DGS representations, enabling the model to autonomously learn 3D-specific high-frequency geometry and appearance from large-scale, multi-scene data. This fundamentally changes how 3DSR acquires high-frequency knowledge and enables robust generalization to unseen scenes. Specifically, we introduce SR3R, a feed-forward framework that directly predicts HR 3DGS representations from sparse LR views via the learned mapping network. To further enhance reconstruction fidelity, we introduce Gaussian offset learning and feature refinement, which stabilize reconstruction and sharpen high-frequency details. SR3R is plug-and-play and can be paired with any feed-forward 3DGS reconstruction backbone: the backbone provides an LR 3DGS scaffold, and SR3R upscales it to an HR 3DGS. Extensive experiments across three 3D benchmarks demonstrate that SR3R surpasses state-of-the-art (SOTA) 3DSR methods and achieves strong zero-shot generalization, even outperforming SOTA per-scene optimization methods on unseen scenes.

