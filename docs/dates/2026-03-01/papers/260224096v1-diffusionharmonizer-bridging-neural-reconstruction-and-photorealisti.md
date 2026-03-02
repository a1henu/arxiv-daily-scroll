---
layout: default
title: DiffusionHarmonizer: Bridging Neural Reconstruction and Photorealistic Simulation with Online Diffusion Enhancer
---

# DiffusionHarmonizer: Bridging Neural Reconstruction and Photorealistic Simulation with Online Diffusion Enhancer
**arXiv**：[2602.24096v1](https://arxiv.org/abs/2602.24096) · [PDF](https://arxiv.org/pdf/2602.24096.pdf)  
**作者**：Yuxuan Zhang, Katarína Tóthová, Zian Wang, Kangxue Yin, Haithem Turki, Riccardo de Lutio, Yen-Yu Chang, Or Litany, Sanja Fidler, Zan Gojcic  

**一句话要点**：提出DiffusionHarmonizer在线生成增强框架，以提升神经重建场景的仿真真实感与一致性。

**关键词**：神经重建增强, 扩散模型, 在线仿真, 时间一致性, 真实感渲染, 自动驾驶仿真

## 3 点简述
- 核心问题：神经重建方法如NeRF和3D高斯溅射在渲染新视角和集成动态对象时存在伪影与不真实问题。
- 方法要点：基于预训练多步图像扩散模型，开发单步时间条件增强器，实现在线仿真中的实时生成增强。
- 实验或效果：通过定制数据管道构建合成-真实对，显著提升仿真保真度，适用于研究和生产环境。

## 摘要（原文）

> Simulation is essential to the development and evaluation of autonomous robots such as self-driving vehicles. Neural reconstruction is emerging as a promising solution as it enables simulating a wide variety of scenarios from real-world data alone in an automated and scalable way. However, while methods such as NeRF and 3D Gaussian Splatting can produce visually compelling results, they often exhibit artifacts particularly when rendering novel views, and fail to realistically integrate inserted dynamic objects, especially when they were captured from different scenes. To overcome these limitations, we introduce DiffusionHarmonizer, an online generative enhancement framework that transforms renderings from such imperfect scenes into temporally consistent outputs while improving their realism. At its core is a single-step temporally-conditioned enhancer that is converted from a pretrained multi-step image diffusion model, capable of running in online simulators on a single GPU. The key to training it effectively is a custom data curation pipeline that constructs synthetic-real pairs emphasizing appearance harmonization, artifact correction, and lighting realism. The result is a scalable system that significantly elevates simulation fidelity in both research and production environments.

