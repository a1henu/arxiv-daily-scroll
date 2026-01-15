---
layout: default
title: Efficient Camera-Controlled Video Generation of Static Scenes via Sparse Diffusion and 3D Rendering
---

# Efficient Camera-Controlled Video Generation of Static Scenes via Sparse Diffusion and 3D Rendering
**arXiv**：[2601.09697v1](https://arxiv.org/abs/2601.09697) · [PDF](https://arxiv.org/pdf/2601.09697.pdf)  
**作者**：Jieying Chen, Jeffrey Hu, Joan Lasenby, Ayush Tewari  

**一句话要点**：提出SRENDER方法，通过稀疏扩散与3D渲染实现静态场景的高效相机控制视频生成。

**关键词**：相机控制视频生成, 稀疏扩散模型, 3D重建渲染, 计算效率优化, 静态场景合成

## 3 点简述
- 核心问题：基于扩散模型的视频生成计算效率低，难以满足实时交互应用需求。
- 方法要点：使用扩散模型生成稀疏关键帧，通过3D重建和渲染合成完整视频，并自适应预测关键帧数量。
- 实验或效果：相比基线方法，生成20秒视频速度提升40倍以上，保持高视觉保真度和时间稳定性。

## 摘要（原文）

> Modern video generative models based on diffusion models can produce very realistic clips, but they are computationally inefficient, often requiring minutes of GPU time for just a few seconds of video. This inefficiency poses a critical barrier to deploying generative video in applications that require real-time interactions, such as embodied AI and VR/AR. This paper explores a new strategy for camera-conditioned video generation of static scenes: using diffusion-based generative models to generate a sparse set of keyframes, and then synthesizing the full video through 3D reconstruction and rendering. By lifting keyframes into a 3D representation and rendering intermediate views, our approach amortizes the generation cost across hundreds of frames while enforcing geometric consistency. We further introduce a model that predicts the optimal number of keyframes for a given camera trajectory, allowing the system to adaptively allocate computation. Our final method, SRENDER, uses very sparse keyframes for simple trajectories and denser ones for complex camera motion. This results in video generation that is more than 40 times faster than the diffusion-based baseline in generating 20 seconds of video, while maintaining high visual fidelity and temporal stability, offering a practical path toward efficient and controllable video synthesis.

