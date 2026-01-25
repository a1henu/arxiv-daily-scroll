---
layout: default
title: ActionMesh: Animated 3D Mesh Generation with Temporal 3D Diffusion
---

# ActionMesh: Animated 3D Mesh Generation with Temporal 3D Diffusion
**arXiv**：[2601.16148v1](https://arxiv.org/abs/2601.16148) · [PDF](https://arxiv.org/pdf/2601.16148.pdf)  
**作者**：Remy Sabathier, David Novotny, Niloy J. Mitra, Tom Monnier  

**一句话要点**：提出ActionMesh，通过时间3D扩散模型前馈生成动画3D网格，解决现有方法应用受限问题。

**关键词**：动画3D生成, 时间3D扩散, 3D网格生成, 视频到4D, 拓扑一致性, 前馈生成

## 3 点简述
- 核心问题：现有动画3D生成方法在设置、速度或质量上受限，难以实际应用。
- 方法要点：结合时间3D扩散生成独立形状序列，并通过时间3D自编码器转换为参考形状的变形动画。
- 实验或效果：在标准基准上实现几何精度和时间一致性的SOTA，快速生成拓扑一致、免绑定的网格。

## 摘要（原文）

> Generating animated 3D objects is at the heart of many applications, yet most advanced works are typically difficult to apply in practice because of their limited setup, their long runtime, or their limited quality. We introduce ActionMesh, a generative model that predicts production-ready 3D meshes "in action" in a feed-forward manner. Drawing inspiration from early video models, our key insight is to modify existing 3D diffusion models to include a temporal axis, resulting in a framework we dubbed "temporal 3D diffusion". Specifically, we first adapt the 3D diffusion stage to generate a sequence of synchronized latents representing time-varying and independent 3D shapes. Second, we design a temporal 3D autoencoder that translates a sequence of independent shapes into the corresponding deformations of a pre-defined reference shape, allowing us to build an animation. Combining these two components, ActionMesh generates animated 3D meshes from different inputs like a monocular video, a text description, or even a 3D mesh with a text prompt describing its animation. Besides, compared to previous approaches, our method is fast and produces results that are rig-free and topology consistent, hence enabling rapid iteration and seamless applications like texturing and retargeting. We evaluate our model on standard video-to-4D benchmarks (Consistent4D, Objaverse) and report state-of-the-art performances on both geometric accuracy and temporal consistency, demonstrating that our model can deliver animated 3D meshes with unprecedented speed and quality.

