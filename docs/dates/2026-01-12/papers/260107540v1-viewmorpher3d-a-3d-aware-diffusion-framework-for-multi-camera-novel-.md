---
layout: default
title: ViewMorpher3D: A 3D-aware Diffusion Framework for Multi-Camera Novel View Synthesis in Autonomous Driving
---

# ViewMorpher3D: A 3D-aware Diffusion Framework for Multi-Camera Novel View Synthesis in Autonomous Driving
**arXiv**：[2601.07540v1](https://arxiv.org/abs/2601.07540) · [PDF](https://arxiv.org/pdf/2601.07540.pdf)  
**作者**：Farhad G. Zanjani, Hong Cai, Amirhossein Habibian  

**一句话要点**：提出ViewMorpher3D，一个基于扩散模型的3D感知框架，用于提升自动驾驶中多相机新视角合成的真实感和一致性。

**关键词**：自动驾驶模拟, 多视角合成, 扩散模型, 3D感知, 图像增强

## 3 点简述
- 核心问题：自动驾驶模拟器中，基于3D重建的新视角渲染常出现伪影，尤其在稀疏观测或外推视角下。
- 方法要点：联合处理多视图图像，结合相机姿态、3D几何先验和参考视图，以推断缺失细节并增强跨视图一致性。
- 实验或效果：在真实驾驶数据集上，图像质量指标显著提升，有效减少伪影并保持几何保真度。

## 摘要（原文）

> Autonomous driving systems rely heavily on multi-view images to ensure accurate perception and robust decision-making. To effectively develop and evaluate perception stacks and planning algorithms, realistic closed-loop simulators are indispensable. While 3D reconstruction techniques such as Gaussian Splatting offer promising avenues for simulator construction, the rendered novel views often exhibit artifacts, particularly in extrapolated perspectives or when available observations are sparse.
>   We introduce ViewMorpher3D, a multi-view image enhancement framework based on image diffusion models, designed to elevate photorealism and multi-view coherence in driving scenes. Unlike single-view approaches, ViewMorpher3D jointly processes a set of rendered views conditioned on camera poses, 3D geometric priors, and temporally adjacent or spatially overlapping reference views. This enables the model to infer missing details, suppress rendering artifacts, and enforce cross-view consistency.
>   Our framework accommodates variable numbers of cameras and flexible reference/target view configurations, making it adaptable to diverse sensor setups. Experiments on real-world driving datasets demonstrate substantial improvements in image quality metrics, effectively reducing artifacts while preserving geometric fidelity.

