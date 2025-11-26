---
layout: default
title: SONIC: Spectral Optimization of Noise for Inpainting with Consistency
---

# SONIC: Spectral Optimization of Noise for Inpainting with Consistency
**arXiv**：[2511.19985v1](https://arxiv.org/abs/2511.19985) · [PDF](https://arxiv.org/pdf/2511.19985.pdf)  
**作者**：Seungyeon Baek, Erqun Dong, Shadan Namazifard, Mark J. Matthews, Kwang Moo Yi  

**一句话要点**：提出谱域优化初始噪声方法，提升无训练修复性能

**关键词**：图像修复, 无训练方法, 噪声优化, 谱域优化, 线性近似

## 3 点简述
- 核心问题：基于引导的无训练修复方法效果有限，需专用模型
- 方法要点：优化初始噪声以匹配未掩码数据，采用线性近似和谱域优化
- 实验或效果：在多种修复任务中表现优异，超越现有技术

## 摘要（原文）

> We propose a novel training-free method for inpainting with off-the-shelf text-to-image models. While guidance-based methods in theory allow generic models to be used for inverse problems such as inpainting, in practice, their effectiveness is limited, leading to the necessity of specialized inpainting-specific models. In this work, we argue that the missing ingredient for training-free inpainting is the optimization (guidance) of the initial seed noise. We propose to optimize the initial seed noise to approximately match the unmasked parts of the data - with as few as a few tens of optimization steps. We then apply conventional training-free inpainting methods on top of our optimized initial seed noise. Critically, we propose two core ideas to effectively implement this idea: (i) to avoid the costly unrolling required to relate the initial noise and the generated outcome, we perform linear approximation; and (ii) to stabilize the optimization, we optimize the initial seed noise in the spectral domain. We demonstrate the effectiveness of our method on various inpainting tasks, outperforming the state of the art. Project page: https://ubc-vision.github.io/sonic/

