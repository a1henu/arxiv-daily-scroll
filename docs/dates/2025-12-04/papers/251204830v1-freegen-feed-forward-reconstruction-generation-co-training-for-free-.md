---
layout: default
title: FreeGen: Feed-Forward Reconstruction-Generation Co-Training for Free-Viewpoint Driving Scene Synthesis
---

# FreeGen: Feed-Forward Reconstruction-Generation Co-Training for Free-Viewpoint Driving Scene Synthesis
**arXiv**：[2512.04830v1](https://arxiv.org/abs/2512.04830) · [PDF](https://arxiv.org/pdf/2512.04830.pdf)  
**作者**：Shijie Chen, Peixi Peng  

**一句话要点**：提出FreeGen框架，通过重建-生成协同训练实现自由视角驾驶场景合成

**关键词**：自由视角合成, 驾驶场景生成, 重建-生成协同训练, 几何感知增强, 插值一致性

## 3 点简述
- 核心问题：现有方法难以在自由视角合成中同时保证插值一致性和外推真实性
- 方法要点：重建模型提供几何表示确保一致性，生成模型进行几何感知增强提升真实性
- 实验或效果：FreeGen在自由视角驾驶场景合成中达到最先进性能

## 摘要（原文）

> Closed-loop simulation and scalable pre-training for autonomous driving require synthesizing free-viewpoint driving scenes. However, existing datasets and generative pipelines rarely provide consistent off-trajectory observations, limiting large-scale evaluation and training. While recent generative models demonstrate strong visual realism, they struggle to jointly achieve interpolation consistency and extrapolation realism without per-scene optimization. To address this, we propose FreeGen, a feed-forward reconstruction-generation co-training framework for free-viewpoint driving scene synthesis. The reconstruction model provides stable geometric representations to ensure interpolation consistency, while the generation model performs geometry-aware enhancement to improve realism at unseen viewpoints. Through co-training, generative priors are distilled into the reconstruction model to improve off-trajectory rendering, and the refined geometry in turn offers stronger structural guidance for generation. Experiments demonstrate that FreeGen achieves state-of-the-art performance for free-viewpoint driving scene synthesis.

