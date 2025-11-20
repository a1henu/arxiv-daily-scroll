---
layout: default
title: Jointly Conditioned Diffusion Model for Multi-View Pose-Guided Person Image Synthesis
---

# Jointly Conditioned Diffusion Model for Multi-View Pose-Guided Person Image Synthesis
**arXiv**：[2511.15092v1](https://arxiv.org/abs/2511.15092) · [PDF](https://arxiv.org/pdf/2511.15092.pdf)  
**作者**：Chengyu Xie, Zhi Gong, Junchi Ren, Linkun Yu, Si Shen, Fei Shen, Xiaoyu Du  

**一句话要点**：提出联合条件扩散模型以解决多视角姿态引导人物图像合成中的纹理不完整和跨视角交互缺失问题

**关键词**：人物图像合成, 扩散模型, 多视角学习, 姿态引导生成, 条件注入

## 3 点简述
- 核心问题：单参考视图纹理不完整，缺乏显式跨视角交互，影响人物图像合成质量
- 方法要点：使用外观先验模块推断整体身份先验，联合条件注入机制融合多视角线索并注入共享条件
- 实验或效果：实验显示在保真度和跨视角一致性方面达到先进水平，支持可变参考视图数

## 摘要（原文）

> Pose-guided human image generation is limited by incomplete textures from single reference views and the absence of explicit cross-view interaction. We present jointly conditioned diffusion model (JCDM), a jointly conditioned diffusion framework that exploits multi-view priors. The appearance prior module (APM) infers a holistic identity preserving prior from incomplete references, and the joint conditional injection (JCI) mechanism fuses multi-view cues and injects shared conditioning into the denoising backbone to align identity, color, and texture across poses. JCDM supports a variable number of reference views and integrates with standard diffusion backbones with minimal and targeted architectural modifications. Experiments demonstrate state of the art fidelity and cross-view consistency.

