---
layout: default
title: SceMoS: Scene-Aware 3D Human Motion Synthesis by Planning with Geometry-Grounded Tokens
---

# SceMoS: Scene-Aware 3D Human Motion Synthesis by Planning with Geometry-Grounded Tokens
**arXiv**：[2602.20476v1](https://arxiv.org/abs/2602.20476) · [PDF](https://arxiv.org/pdf/2602.20476.pdf)  
**作者**：Anindita Ghosh, Vladislav Golyanik, Taku Komura, Philipp Slusallek, Christian Theobalt, Rishabh Dabral  

**一句话要点**：提出SceMoS框架，利用结构化2D场景表示合成文本驱动的3D人体运动，以解决物理可行性和计算效率问题。

**关键词**：3D人体运动合成, 场景感知, 2D场景表示, 几何接地令牌化, 鸟瞰图规划, 物理约束

## 3 点简述
- 核心问题：合成文本驱动的3D人体运动需兼顾语义意图和物理可行性，现有方法依赖昂贵3D数据，计算成本高。
- 方法要点：采用解耦策略，基于鸟瞰图进行全局规划，结合局部高度图通过几何接地令牌化实现精细物理约束。
- 实验或效果：在TRUMANS基准上达到最先进运动真实性和接触精度，场景编码参数减少超50%。

## 摘要（原文）

> Synthesizing text-driven 3D human motion within realistic scenes requires learning both semantic intent ("walk to the couch") and physical feasibility (e.g., avoiding collisions). Current methods use generative frameworks that simultaneously learn high-level planning and low-level contact reasoning, and rely on computationally expensive 3D scene data such as point clouds or voxel occupancy grids. We propose SceMoS, a scene-aware motion synthesis framework that shows that structured 2D scene representations can serve as a powerful alternative to full 3D supervision in physically grounded motion synthesis. SceMoS disentangles global planning from local execution using lightweight 2D cues and relying on (1) a text-conditioned autoregressive global motion planner that operates on a bird's-eye-view (BEV) image rendered from an elevated corner of the scene, encoded with DINOv2 features, as the scene representation, and (2) a geometry-grounded motion tokenizer trained via a conditional VQ-VAE, that uses 2D local scene heightmap, thus embedding surface physics directly into a discrete vocabulary. This 2D factorization reaches an efficiency-fidelity trade-off: BEV semantics capture spatial layout and affordance for global reasoning, while local heightmaps enforce fine-grained physical adherence without full 3D volumetric reasoning. SceMoS achieves state-of-the-art motion realism and contact accuracy on the TRUMANS benchmark, reducing the number of trainable parameters for scene encoding by over 50%, showing that 2D scene cues can effectively ground 3D human-scene interaction.

