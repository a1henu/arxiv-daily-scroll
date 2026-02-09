---
layout: default
title: Uncertainty-Aware 4D Gaussian Splatting for Monocular Occluded Human Rendering
---

# Uncertainty-Aware 4D Gaussian Splatting for Monocular Occluded Human Rendering
**arXiv**：[2602.06343v1](https://arxiv.org/abs/2602.06343) · [PDF](https://arxiv.org/pdf/2602.06343.pdf)  
**作者**：Weiquan Wang, Feifei Shao, Lin Li, Zhen Wang, Jun Xiao, Long Chen  

**一句话要点**：提出U-4DGS框架，通过不确定性感知方法解决单目视频中动态人体被遮挡时的渲染退化问题

**关键词**：4D高斯溅射, 不确定性感知渲染, 单目动态人体重建, 遮挡处理, 概率变形网络, 自适应梯度调制

## 3 点简述
- 核心问题：单目视频动态人体渲染在遮挡下严重退化，现有方法存在时间闪烁或几何启发式局限
- 方法要点：构建最大后验估计框架，集成概率变形网络与双重光栅化，生成像素对齐不确定性图以自适应调制梯度
- 实验或效果：在ZJU-MoCap和OcMotion数据集上实现最先进的渲染保真度与鲁棒性

## 摘要（原文）

> High-fidelity rendering of dynamic humans from monocular videos typically degrades catastrophically under occlusions. Existing solutions incorporate external priors-either hallucinating missing content via generative models, which induces severe temporal flickering, or imposing rigid geometric heuristics that fail to capture diverse appearances. To this end, we reformulate the task as a Maximum A Posteriori estimation problem under heteroscedastic observation noise. In this paper, we propose U-4DGS, a framework integrating a Probabilistic Deformation Network and a Double Rasterization pipeline. This architecture renders pixel-aligned uncertainty maps that act as an adaptive gradient modulator, automatically attenuating artifacts from unreliable observations. Furthermore, to prevent geometric drift in regions lacking reliable visual cues, we enforce Confidence-Aware Regularizations, which leverage the learned uncertainty to selectively propagate spatial-temporal validity. Extensive experiments on ZJU-MoCap and OcMotion demonstrate that U-4DGS achieves SOTA rendering fidelity and robustness.

