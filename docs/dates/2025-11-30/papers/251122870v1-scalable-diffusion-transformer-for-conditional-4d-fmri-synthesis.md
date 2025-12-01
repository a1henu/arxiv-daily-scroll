---
layout: default
title: Scalable Diffusion Transformer for Conditional 4D fMRI Synthesis
---

# Scalable Diffusion Transformer for Conditional 4D fMRI Synthesis
**arXiv**：[2511.22870v1](https://arxiv.org/abs/2511.22870) · [PDF](https://arxiv.org/pdf/2511.22870.pdf)  
**作者**：Jungwoo Seo, David Keetae Park, Shinjae Yoo, Jiook Cha  

**一句话要点**：提出可扩展扩散Transformer，用于条件4D fMRI合成，以解决高维异质BOLD动态和验证不足的挑战。

**关键词**：扩散模型, Transformer, fMRI合成, 条件生成, 神经影像, 潜在压缩

## 3 点简述
- 核心问题：生成条件4D fMRI序列面临高维异质BOLD动态和缺乏神经科学验证的难题。
- 方法要点：结合3D VQ-GAN潜在压缩、CNN-Transformer骨干网络，以及AdaLN-Zero和交叉注意力进行强任务条件化。
- 实验或效果：在HCP任务fMRI上，模型再现任务激活图，保持表示结构，性能随规模提升，超越U-Net基线。

## 摘要（原文）

> Generating whole-brain 4D fMRI sequences conditioned on cognitive tasks remains challenging due to the high-dimensional, heterogeneous BOLD dynamics across subjects/acquisitions and the lack of neuroscience-grounded validation. We introduce the first diffusion transformer for voxelwise 4D fMRI conditional generation, combining 3D VQ-GAN latent compression with a CNN-Transformer backbone and strong task conditioning via AdaLN-Zero and cross-attention. On HCP task fMRI, our model reproduces task-evoked activation maps, preserves the inter-task representational structure observed in real data (RSA), achieves perfect condition specificity, and aligns ROI time-courses with canonical hemodynamic responses. Performance improves predictably with scale, reaching task-evoked map correlation of 0.83 and RSA of 0.98, consistently surpassing a U-Net baseline on all metrics. By coupling latent diffusion with a scalable backbone and strong conditioning, this work establishes a practical path to conditional 4D fMRI synthesis, paving the way for future applications such as virtual experiments, cross-site harmonization, and principled augmentation for downstream neuroimaging models.

