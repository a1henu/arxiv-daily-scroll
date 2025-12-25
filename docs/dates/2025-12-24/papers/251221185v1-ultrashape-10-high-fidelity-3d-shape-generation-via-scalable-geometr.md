---
layout: default
title: UltraShape 1.0: High-Fidelity 3D Shape Generation via Scalable Geometric Refinement
---

# UltraShape 1.0: High-Fidelity 3D Shape Generation via Scalable Geometric Refinement
**arXiv**：[2512.21185v1](https://arxiv.org/abs/2512.21185) · [PDF](https://arxiv.org/pdf/2512.21185.pdf)  
**作者**：Tanghui Jia, Dongyu Yan, Dehao Hao, Yang Li, Kaiyi Zhang, Xianyi He, Lanjiong Li, Jinnan Chen, Lutao Jiang, Qishen Yin, Long Quan, Ying-Cong Chen, Li Yuan  

**一句话要点**：提出UltraShape 1.0，通过可扩展几何精炼实现高保真3D形状生成

**关键词**：3D形状生成, 扩散模型, 几何精炼, 数据处理, 高保真几何, 可扩展框架

## 3 点简述
- 核心问题：现有3D生成方法在几何细节和保真度方面存在不足，需高效处理低质量数据。
- 方法要点：采用两阶段生成流程，先合成粗全局结构，再通过解耦空间定位与细节合成的扩散模型进行精炼。
- 实验或效果：在公开数据集上训练，评估显示在数据处理质量和几何生成上具有竞争力，代码模型将开源。

## 摘要（原文）

> In this report, we introduce UltraShape 1.0, a scalable 3D diffusion framework for high-fidelity 3D geometry generation. The proposed approach adopts a two-stage generation pipeline: a coarse global structure is first synthesized and then refined to produce detailed, high-quality geometry. To support reliable 3D generation, we develop a comprehensive data processing pipeline that includes a novel watertight processing method and high-quality data filtering. This pipeline improves the geometric quality of publicly available 3D datasets by removing low-quality samples, filling holes, and thickening thin structures, while preserving fine-grained geometric details. To enable fine-grained geometry refinement, we decouple spatial localization from geometric detail synthesis in the diffusion process. We achieve this by performing voxel-based refinement at fixed spatial locations, where voxel queries derived from coarse geometry provide explicit positional anchors encoded via RoPE, allowing the diffusion model to focus on synthesizing local geometric details within a reduced, structured solution space. Our model is trained exclusively on publicly available 3D datasets, achieving strong geometric quality despite limited training resources. Extensive evaluations demonstrate that UltraShape 1.0 performs competitively with existing open-source methods in both data processing quality and geometry generation. All code and trained models will be released to support future research.

