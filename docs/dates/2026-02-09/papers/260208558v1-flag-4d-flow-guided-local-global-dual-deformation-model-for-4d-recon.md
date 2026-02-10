---
layout: default
title: FLAG-4D: Flow-Guided Local-Global Dual-Deformation Model for 4D Reconstruction
---

# FLAG-4D: Flow-Guided Local-Global Dual-Deformation Model for 4D Reconstruction
**arXiv**：[2602.08558v1](https://arxiv.org/abs/2602.08558) · [PDF](https://arxiv.org/pdf/2602.08558.pdf)  
**作者**：Guan Yuan Tan, Ngoc Tuan Vu, Arghya Pal, Sailaja Rajanala, Raphael Phan C. -W., Mettu Srinivas, Chee-Ming Ting  

**一句话要点**：提出FLAG-4D框架，通过双变形网络和光流引导解决动态场景4D重建中复杂运动建模问题。

**关键词**：4D重建, 动态场景建模, 3D高斯, 光流引导, 双变形网络, 时间一致性

## 3 点简述
- 现有方法依赖单一MLP建模时间变形，难以从稀疏视图捕获复杂点运动和细节。
- FLAG-4D采用双变形网络（IDN和GMN）和光流特征，实现局部-全局变形建模与时间平滑。
- 实验显示FLAG-4D在保真度、时间一致性和细节保留上优于先进方法。

## 摘要（原文）

> We introduce FLAG-4D, a novel framework for generating novel views of dynamic scenes by reconstructing how 3D Gaussian primitives evolve through space and time. Existing methods typically rely on a single Multilayer Perceptron (MLP) to model temporal deformations, and they often struggle to capture complex point motions and fine-grained dynamic details consistently over time, especially from sparse input views. Our approach, FLAG-4D, overcomes this by employing a dual-deformation network that dynamically warps a canonical set of 3D Gaussians over time into new positions and anisotropic shapes. This dual-deformation network consists of an Instantaneous Deformation Network (IDN) for modeling fine-grained, local deformations and a Global Motion Network (GMN) for capturing long-range dynamics, refined through mutual learning. To ensure these deformations are both accurate and temporally smooth, FLAG-4D incorporates dense motion features from a pretrained optical flow backbone. We fuse these motion cues from adjacent timeframes and use a deformation-guided attention mechanism to align this flow information with the current state of each evolving 3D Gaussian. Extensive experiments demonstrate that FLAG-4D achieves higher-fidelity and more temporally coherent reconstructions with finer detail preservation than state-of-the-art methods.

