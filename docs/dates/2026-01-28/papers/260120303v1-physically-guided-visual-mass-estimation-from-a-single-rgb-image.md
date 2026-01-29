---
layout: default
title: Physically Guided Visual Mass Estimation from a Single RGB Image
---

# Physically Guided Visual Mass Estimation from a Single RGB Image
**arXiv**：[2601.20303v1](https://arxiv.org/abs/2601.20303) · [PDF](https://arxiv.org/pdf/2601.20303.pdf)  
**作者**：Sungjae Lee, Junhan Jeong, Yeonjoo Hong, Kwang In Kim  

**一句话要点**：提出物理结构化框架，从单张RGB图像估计物体质量，通过几何与语义对齐解决视觉歧义。

**关键词**：单图像质量估计, 物理引导学习, 几何体积恢复, 材料语义提取, 视觉语言模型, 门控融合

## 3 点简述
- 核心问题：质量估计因体积和密度不可直接观测而病态，需物理约束。
- 方法要点：结合单目深度估计几何体积，用视觉语言模型提取材料语义，通过门控机制融合。
- 实验效果：在image2mass和ABO-500数据集上优于现有方法。

## 摘要（原文）

> Estimating object mass from visual input is challenging because mass depends jointly on geometric volume and material-dependent density, neither of which is directly observable from RGB appearance. Consequently, mass prediction from pixels is ill-posed and therefore benefits from physically meaningful representations to constrain the space of plausible solutions. We propose a physically structured framework for single-image mass estimation that addresses this ambiguity by aligning visual cues with the physical factors governing mass. From a single RGB image, we recover object-centric three-dimensional geometry via monocular depth estimation to inform volume and extract coarse material semantics using a vision-language model to guide density-related reasoning. These geometry, semantic, and appearance representations are fused through an instance-adaptive gating mechanism, and two physically guided latent factors (volume- and density-related) are predicted through separate regression heads under mass-only supervision. Experiments on image2mass and ABO-500 show that the proposed method consistently outperforms state-of-the-art methods.

