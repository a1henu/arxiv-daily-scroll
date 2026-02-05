---
layout: default
title: Generative Modeling via Drifting
---

# Generative Modeling via Drifting
**arXiv**：[2602.04770v1](https://arxiv.org/abs/2602.04770) · [PDF](https://arxiv.org/pdf/2602.04770.pdf)  
**作者**：Mingyang Deng, He Li, Tianhong Li, Yilun Du, Kaiming He  

**一句话要点**：提出Drifting Models以实现高质量一步生成，在ImageNet 256x256上达到SOTA效果。

**关键词**：生成建模, 一步推理, 漂移模型, 分布匹配, ImageNet生成

## 3 点简述
- 核心问题：生成建模需学习映射使推前分布匹配数据分布，但现有方法如扩散模型需多步推理。
- 方法要点：引入漂移场控制样本移动，训练时演化分布，实现一步推理，优化目标由神经网络驱动。
- 实验效果：在ImageNet 256x256上，一步生成器在潜空间FID为1.54，像素空间FID为1.61，达到SOTA。

## 摘要（原文）

> Generative modeling can be formulated as learning a mapping f such that its pushforward distribution matches the data distribution. The pushforward behavior can be carried out iteratively at inference time, for example in diffusion and flow-based models. In this paper, we propose a new paradigm called Drifting Models, which evolve the pushforward distribution during training and naturally admit one-step inference. We introduce a drifting field that governs the sample movement and achieves equilibrium when the distributions match. This leads to a training objective that allows the neural network optimizer to evolve the distribution. In experiments, our one-step generator achieves state-of-the-art results on ImageNet at 256 x 256 resolution, with an FID of 1.54 in latent space and 1.61 in pixel space. We hope that our work opens up new opportunities for high-quality one-step generation.

