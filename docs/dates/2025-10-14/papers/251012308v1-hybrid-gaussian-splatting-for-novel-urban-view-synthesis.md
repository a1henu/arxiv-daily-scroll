---
layout: default
title: Hybrid Gaussian Splatting for Novel Urban View Synthesis
---

# Hybrid Gaussian Splatting for Novel Urban View Synthesis
**arXiv**：[2510.12308v1](https://arxiv.org/abs/2510.12308) · [PDF](https://arxiv.org/pdf/2510.12308.pdf)  
**作者**：Mohamed Omran, Farhad Zanjani, Davide Abati, Jens Petersen, Amirhossein Habibian  

**一句话要点**：提出混合高斯溅射与扩散模型方法，用于城市街景新视角合成。

**关键词**：新视角合成, 高斯溅射, 扩散模型, 3D重建, 街景渲染

## 3 点简述
- 核心问题：从训练轨迹的车载帧生成不同轨迹（如不同车道）的新视角街景渲染。
- 方法要点：先拟合3D场景重建并渲染新视角，再用单步扩散模型增强图像质量。
- 实验或效果：在ICCV 2025挑战中获第二名，PSNR、SSIM和LPIPS指标评估性能。

## 摘要（原文）

> This paper describes the Qualcomm AI Research solution to the RealADSim-NVS
> challenge, hosted at the RealADSim Workshop at ICCV 2025. The challenge
> concerns novel view synthesis in street scenes, and participants are required
> to generate, starting from car-centric frames captured during some training
> traversals, renders of the same urban environment as viewed from a different
> traversal (e.g. different street lane or car direction). Our solution is
> inspired by hybrid methods in scene generation and generative simulators
> merging gaussian splatting and diffusion models, and it is composed of two
> stages: First, we fit a 3D reconstruction of the scene and render novel views
> as seen from the target cameras. Then, we enhance the resulting frames with a
> dedicated single-step diffusion model. We discuss specific choices made in the
> initialization of gaussian primitives as well as the finetuning of the enhancer
> model and its training data curation. We report the performance of our model
> design and we ablate its components in terms of novel view quality as measured
> by PSNR, SSIM and LPIPS. On the public leaderboard reporting test results, our
> proposal reaches an aggregated score of 0.432, achieving the second place
> overall.

