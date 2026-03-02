---
layout: default
title: HumanOrbit: 3D Human Reconstruction as 360° Orbit Generation
---

# HumanOrbit: 3D Human Reconstruction as 360° Orbit Generation
**arXiv**：[2602.24148v1](https://arxiv.org/abs/2602.24148) · [PDF](https://arxiv.org/pdf/2602.24148.pdf)  
**作者**：Keito Suzuki, Kunyao Chen, Lei Wang, Bang Du, Runfa Blark Li, Peng Liu, Ning Bi, Truong Nguyen  

**一句话要点**：提出HumanOrbit视频扩散模型，从单张图像生成360度环绕视频以重建3D人体模型

**关键词**：视频扩散模型, 多视角合成, 3D人体重建, 单图输入, 几何一致性, 身份保持

## 3 点简述
- 核心问题：现有方法从单图生成多视角图像时，存在视角不一致和身份失真问题
- 方法要点：利用视频扩散模型生成连续旋转视角，确保几何一致性和身份保持
- 实验或效果：实验验证模型在多视角生成和3D重建中优于现有基线，提升完整性和保真度

## 摘要（原文）

> We present a method for generating a full 360° orbit video around a person from a single input image. Existing methods typically adapt image-based diffusion models for multi-view synthesis, but yield inconsistent results across views and with the original identity. In contrast, recent video diffusion models have demonstrated their ability in generating photorealistic results that align well with the given prompts. Inspired by these results, we propose HumanOrbit, a video diffusion model for multi-view human image generation. Our approach enables the model to synthesize continuous camera rotations around the subject, producing geometrically consistent novel views while preserving the appearance and identity of the person. Using the generated multi-view frames, we further propose a reconstruction pipeline that recovers a textured mesh of the subject. Experimental results validate the effectiveness of HumanOrbit for multi-view image generation and that the reconstructed 3D models exhibit superior completeness and fidelity compared to those from state-of-the-art baselines.

