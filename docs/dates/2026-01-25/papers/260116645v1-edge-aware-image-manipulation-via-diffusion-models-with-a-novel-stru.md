---
layout: default
title: Edge-Aware Image Manipulation via Diffusion Models with a Novel Structure-Preservation Loss
---

# Edge-Aware Image Manipulation via Diffusion Models with a Novel Structure-Preservation Loss
**arXiv**：[2601.16645v1](https://arxiv.org/abs/2601.16645) · [PDF](https://arxiv.org/pdf/2601.16645.pdf)  
**作者**：Minsu Gong, Nuri Ryu, Jungseul Ok, Sunghyun Cho  

**一句话要点**：提出结构保持损失以解决潜在扩散模型图像编辑中的边缘结构保持问题

**关键词**：图像编辑, 潜在扩散模型, 结构保持损失, 边缘感知, 无训练方法, 后处理优化

## 3 点简述
- 核心问题：潜在扩散模型在图像编辑中难以保持像素级边缘结构，影响真实感编辑效果。
- 方法要点：引入基于局部线性模型的结构保持损失，无训练集成到扩散生成过程，辅以后处理、掩码和颜色保持策略。
- 实验或效果：实验验证结构保真度提升，在潜在扩散图像编辑中达到先进性能，代码将公开。

## 摘要（原文）

> Recent advances in image editing leverage latent diffusion models (LDMs) for versatile, text-prompt-driven edits across diverse tasks. Yet, maintaining pixel-level edge structures-crucial for tasks such as photorealistic style transfer or image tone adjustment-remains as a challenge for latent-diffusion-based editing. To overcome this limitation, we propose a novel Structure Preservation Loss (SPL) that leverages local linear models to quantify structural differences between input and edited images. Our training-free approach integrates SPL directly into the diffusion model's generative process to ensure structural fidelity. This core mechanism is complemented by a post-processing step to mitigate LDM decoding distortions, a masking strategy for precise edit localization, and a color preservation loss to preserve hues in unedited areas. Experiments confirm SPL enhances structural fidelity, delivering state-of-the-art performance in latent-diffusion-based image editing. Our code will be publicly released at https://github.com/gongms00/SPL.

