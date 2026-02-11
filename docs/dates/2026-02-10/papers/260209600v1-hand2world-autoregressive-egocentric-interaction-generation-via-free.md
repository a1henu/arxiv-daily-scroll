---
layout: default
title: Hand2World: Autoregressive Egocentric Interaction Generation via Free-Space Hand Gestures
---

# Hand2World: Autoregressive Egocentric Interaction Generation via Free-Space Hand Gestures
**arXiv**：[2602.09600v1](https://arxiv.org/abs/2602.09600) · [PDF](https://arxiv.org/pdf/2602.09600.pdf)  
**作者**：Yuxi Wang, Wenqi Ouyang, Tianyi Wei, Yi Dong, Zhiqi Shen, Xingang Pan  

**一句话要点**：提出Hand2World自回归框架，通过自由空间手势生成以自我为中心的光照真实交互视频。

**关键词**：自我中心交互生成, 自由空间手势, 自回归框架, 遮挡不变条件化, Plücker射线嵌入, 蒸馏训练

## 3 点简述
- 核心问题：解决自由空间手势与接触训练数据分布偏移、单目视图中手部与相机运动模糊、以及任意长度视频生成的挑战。
- 方法要点：采用基于投影3D手部网格的遮挡不变手部条件化，注入像素级Plücker射线嵌入以稳定视角变化，并蒸馏双向扩散模型为因果生成器。
- 实验或效果：在三个以自我为中心的交互基准测试中，感知质量和3D一致性显著提升，支持相机控制和长时交互生成。

## 摘要（原文）

> Egocentric interactive world models are essential for augmented reality and embodied AI, where visual generation must respond to user input with low latency, geometric consistency, and long-term stability. We study egocentric interaction generation from a single scene image under free-space hand gestures, aiming to synthesize photorealistic videos in which hands enter the scene, interact with objects, and induce plausible world dynamics under head motion. This setting introduces fundamental challenges, including distribution shift between free-space gestures and contact-heavy training data, ambiguity between hand motion and camera motion in monocular views, and the need for arbitrary-length video generation. We present Hand2World, a unified autoregressive framework that addresses these challenges through occlusion-invariant hand conditioning based on projected 3D hand meshes, allowing visibility and occlusion to be inferred from scene context rather than encoded in the control signal. To stabilize egocentric viewpoint changes, we inject explicit camera geometry via per-pixel Plücker-ray embeddings, disentangling camera motion from hand motion and preventing background drift. We further develop a fully automated monocular annotation pipeline and distill a bidirectional diffusion model into a causal generator, enabling arbitrary-length synthesis. Experiments on three egocentric interaction benchmarks show substantial improvements in perceptual quality and 3D consistency while supporting camera control and long-horizon interactive generation.

