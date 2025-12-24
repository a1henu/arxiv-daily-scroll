---
layout: default
title: Field-Space Attention for Structure-Preserving Earth System Transformers
---

# Field-Space Attention for Structure-Preserving Earth System Transformers
**arXiv**：[2512.20350v1](https://arxiv.org/abs/2512.20350) · [PDF](https://arxiv.org/pdf/2512.20350.pdf)  
**作者**：Maximilian Witte, Johannes Meuer, Étienne Plésiat, Christopher Kadow  

**一句话要点**：提出场空间注意力机制，用于构建结构保持的地球系统Transformer，以提升地球系统建模的准确性和物理一致性。

**关键词**：地球系统建模, 场空间注意力, 结构保持Transformer, 多尺度分解, 物理约束嵌入, 超分辨率

## 3 点简述
- 核心问题：地球系统建模需在连续地球物理场上操作并保持其几何结构，传统方法可能缺乏物理可解释性和稳定性。
- 方法要点：引入场空间注意力，在物理域而非潜在空间计算注意力，使用固定多尺度分解学习结构保持变形，确保中间表示为连续场。
- 实验或效果：应用于全球温度超分辨率任务，相比传统Vision Transformer和U-Net基线，收敛更快更稳定，参数更少，提升保真度和可靠性。

## 摘要（原文）

> Accurate and physically consistent modeling of Earth system dynamics requires machine-learning architectures that operate directly on continuous geophysical fields and preserve their underlying geometric structure. Here we introduce Field-Space attention, a mechanism for Earth system Transformers that computes attention in the physical domain rather than in a learned latent space. By maintaining all intermediate representations as continuous fields on the sphere, the architecture enables interpretable internal states and facilitates the enforcement of scientific constraints. The model employs a fixed, non-learned multiscale decomposition and learns structure-preserving deformations of the input field, allowing coherent integration of coarse and fine-scale information while avoiding the optimization instabilities characteristic of standard single-scale Vision Transformers. Applied to global temperature super-resolution on a HEALPix grid, Field-Space Transformers converge more rapidly and stably than conventional Vision Transformers and U-Net baselines, while requiring substantially fewer parameters. The explicit preservation of field structure throughout the network allows physical and statistical priors to be embedded directly into the architecture, yielding improved fidelity and reliability in data-driven Earth system modeling. These results position Field-Space Attention as a compact, interpretable, and physically grounded building block for next-generation Earth system prediction and generative modeling frameworks.

