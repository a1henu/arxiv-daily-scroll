---
layout: default
title: SplatSearch: Instance Image Goal Navigation for Mobile Robots using 3D Gaussian Splatting and Diffusion Models
---

# SplatSearch: Instance Image Goal Navigation for Mobile Robots using 3D Gaussian Splatting and Diffusion Models
**arXiv**：[2511.12972v1](https://arxiv.org/abs/2511.12972) · [PDF](https://arxiv.org/pdf/2511.12972.pdf)  
**作者**：Siddarth Narasimhan, Matthew Lisondra, Haitong Wang, Goldie Nejat  

**一句话要点**：提出SplatSearch架构，利用3D高斯泼溅和扩散模型解决实例图像目标导航问题。

**关键词**：实例图像目标导航, 3D高斯泼溅, 扩散模型, 前沿探索策略, 稀疏视图重建, 机器人导航

## 3 点简述
- 核心问题：移动机器人在未知环境中使用单张参考图像搜索特定目标，面临任意视角和稀疏视图重建挑战。
- 方法要点：结合稀疏视图3D高斯泼溅重建、多视图扩散模型补全图像和语义视觉前沿探索策略。
- 实验或效果：在真实和仿真家庭环境中验证，成功率和路径长度优于现有方法，消融研究支持设计。

## 摘要（原文）

> The Instance Image Goal Navigation (IIN) problem requires mobile robots deployed in unknown environments to search for specific objects or people of interest using only a single reference goal image of the target. This problem can be especially challenging when: 1) the reference image is captured from an arbitrary viewpoint, and 2) the robot must operate with sparse-view scene reconstructions. In this paper, we address the IIN problem, by introducing SplatSearch, a novel architecture that leverages sparse-view 3D Gaussian Splatting (3DGS) reconstructions. SplatSearch renders multiple viewpoints around candidate objects using a sparse online 3DGS map, and uses a multi-view diffusion model to complete missing regions of the rendered images, enabling robust feature matching against the goal image. A novel frontier exploration policy is introduced which uses visual context from the synthesized viewpoints with semantic context from the goal image to evaluate frontier locations, allowing the robot to prioritize frontiers that are semantically and visually relevant to the goal image. Extensive experiments in photorealistic home and real-world environments validate the higher performance of SplatSearch against current state-of-the-art methods in terms of Success Rate and Success Path Length. An ablation study confirms the design choices of SplatSearch.

