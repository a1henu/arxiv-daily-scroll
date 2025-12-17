---
layout: default
title: Elastic3D: Controllable Stereo Video Conversion with Guided Latent Decoding
---

# Elastic3D: Controllable Stereo Video Conversion with Guided Latent Decoding
**arXiv**：[2512.14236v1](https://arxiv.org/abs/2512.14236) · [PDF](https://arxiv.org/pdf/2512.14236.pdf)  
**作者**：Nando Metzger, Prune Truong, Goutam Bhat, Konrad Schindler, Federico Tombari  

**一句话要点**：提出Elastic3D方法，基于条件潜在扩散实现可控的单目到立体视频转换。

**关键词**：立体视频转换, 潜在扩散模型, 引导解码, 可控视差, 端到端方法

## 3 点简述
- 核心问题：自动化单目到立体视频转换需求增长，传统方法因显式深度估计和扭曲易产生伪影。
- 方法要点：采用条件潜在扩散模型，避免显式深度估计；引入引导VAE解码器，确保立体视频输出锐利且极线一致。
- 实验或效果：在三个真实立体视频数据集上优于传统和近期基线，支持通过标量调节控制视差范围。

## 摘要（原文）

> The growing demand for immersive 3D content calls for automated monocular-to-stereo video conversion. We present Elastic3D, a controllable, direct end-to-end method for upgrading a conventional video to a binocular one. Our approach, based on (conditional) latent diffusion, avoids artifacts due to explicit depth estimation and warping. The key to its high-quality stereo video output is a novel, guided VAE decoder that ensures sharp and epipolar-consistent stereo video output. Moreover, our method gives the user control over the strength of the stereo effect (more precisely, the disparity range) at inference time, via an intuitive, scalar tuning knob. Experiments on three different datasets of real-world stereo videos show that our method outperforms both traditional warping-based and recent warping-free baselines and sets a new standard for reliable, controllable stereo video conversion. Please check the project page for the video samples https://elastic3d.github.io.

