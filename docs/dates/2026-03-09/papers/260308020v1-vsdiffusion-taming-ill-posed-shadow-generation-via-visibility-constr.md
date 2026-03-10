---
layout: default
title: VSDiffusion: Taming Ill-Posed Shadow Generation via Visibility-Constrained Diffusion
---

# VSDiffusion: Taming Ill-Posed Shadow Generation via Visibility-Constrained Diffusion
**arXiv**：[2603.08020v1](https://arxiv.org/abs/2603.08020) · [PDF](https://arxiv.org/pdf/2603.08020.pdf)  
**作者**：Jing Li, Jing Zhang  

**一句话要点**：提出VSDiffusion以解决图像合成中前景物体投射阴影生成的病态问题

**关键词**：阴影生成, 扩散模型, 图像合成, 几何一致性, 可见性先验

## 3 点简述
- 核心问题：图像合成中前景物体投射阴影生成因阴影形成病态而难以保持几何一致性
- 方法要点：采用两阶段框架，通过可见性先验约束扩散过程，包括粗掩模预测和条件扩散生成
- 实验或效果：在DESOBAv2数据集上实现SOTA结果，生成准确阴影并提升评估指标

## 摘要（原文）

> Generating realistic cast shadows for inserted foreground objects is a crucial yet challenging problem in image composition, where maintaining geometric consistency of shadow and object in complex scenes remains difficult due to the ill-posed nature of shadow formation. To address this issue, we propose VSDiffusion, a visibility-constrained two-stage framework designed to narrow the solution space by incorporating visibility priors. In Stage I, we predict a coarse shadow mask to localize plausible shadow generated regions. And in Stage II, conditional diffusion is performed guided by lighting and depth cues estimated from the composite to generate accurate shadows. In VSDiffusion, we inject visibility priors through two complementary pathways. First, a visibility control branch with shadow-gated cross attention that provides multi-scale structural guidance. Then, a learned soft prior map that reweights training loss in error-prone regions to enhance geometric correction. Additionally, we also introduce high-frequency guided enhancement module to sharpen boundaries and improve texture interaction with the background. Experiments on widely used public DESOBAv2 dataset demonstrated that our proposed VSDiffusion can generate accurate shadow, and establishes new SOTA results across most evaluation metrics.

