---
layout: default
title: DiffPlace: Street View Generation via Place-Controllable Diffusion Model Enhancing Place Recognition
---

# DiffPlace: Street View Generation via Place-Controllable Diffusion Model Enhancing Place Recognition
**arXiv**：[2602.11875v1](https://arxiv.org/abs/2602.11875) · [PDF](https://arxiv.org/pdf/2602.11875.pdf)  
**作者**：Ji Li, Zhiwei Li, Shihao Li, Zhenjiang Yu, Boyang Wang, Haiou Liu  

**一句话要点**：提出DiffPlace框架，通过地点可控扩散模型增强街景生成以支持地点识别

**关键词**：街景生成, 扩散模型, 地点识别, 多视角图像合成, 自动驾驶, 对比学习

## 3 点简述
- 现有多视角扩散模型在生成地点感知和背景一致的街景时存在困难，限制了地点识别任务的应用
- DiffPlace引入地点ID控制器，利用线性投影、感知器变换器和对比学习，将地点嵌入映射到CLIP空间，实现背景一致且前景可变的图像合成
- 实验表明DiffPlace在生成质量和地点识别训练支持方面优于现有方法，提升了自动驾驶中的场景级合成能力

## 摘要（原文）

> Generative models have advanced significantly in realistic image synthesis, with diffusion models excelling in quality and stability. Recent multi-view diffusion models improve 3D-aware street view generation, but they struggle to produce place-aware and background-consistent urban scenes from text, BEV maps, and object bounding boxes. This limits their effectiveness in generating realistic samples for place recognition tasks. To address these challenges, we propose DiffPlace, a novel framework that introduces a place-ID controller to enable place-controllable multi-view image generation. The place-ID controller employs linear projection, perceiver transformer, and contrastive learning to map place-ID embeddings into a fixed CLIP space, allowing the model to synthesize images with consistent background buildings while flexibly modifying foreground objects and weather conditions. Extensive experiments, including quantitative comparisons and augmented training evaluations, demonstrate that DiffPlace outperforms existing methods in both generation quality and training support for visual place recognition. Our results highlight the potential of generative models in enhancing scene-level and place-aware synthesis, providing a valuable approach for improving place recognition in autonomous driving

