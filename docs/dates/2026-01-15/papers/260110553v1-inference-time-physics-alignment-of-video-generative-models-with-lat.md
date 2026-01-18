---
layout: default
title: Inference-time Physics Alignment of Video Generative Models with Latent World Models
---

# Inference-time Physics Alignment of Video Generative Models with Latent World Models
**arXiv**：[2601.10553v1](https://arxiv.org/abs/2601.10553) · [PDF](https://arxiv.org/pdf/2601.10553.pdf)  
**作者**：Jianhao Yuan, Xiaofeng Zhang, Felix Friedrich, Nicolas Beltran-Velez, Melissa Hall, Reyhane Askari-Hemmat, Xiaochuang Han, Nicolas Ballas, Michal Drozdzal, Adriana Romero-Soriano  

**一句话要点**：提出WMReward方法，利用潜在世界模型在推理时对齐视频生成模型的物理合理性

**关键词**：视频生成, 物理合理性, 推理时对齐, 潜在世界模型, WMReward, 去噪轨迹搜索

## 3 点简述
- 问题：现有视频生成模型常违反物理原理，影响实用性，部分源于推理策略不佳
- 方法：将物理合理性提升视为推理时对齐问题，用潜在世界模型（VJEPA-2）作为奖励搜索和引导去噪轨迹
- 效果：在多种生成设置中显著提升物理合理性，在ICCV 2025挑战赛中获第一名，超越先前最佳7.42%

## 摘要（原文）

> State-of-the-art video generative models produce promising visual content yet often violate basic physics principles, limiting their utility. While some attribute this deficiency to insufficient physics understanding from pre-training, we find that the shortfall in physics plausibility also stems from suboptimal inference strategies. We therefore introduce WMReward and treat improving physics plausibility of video generation as an inference-time alignment problem. In particular, we leverage the strong physics prior of a latent world model (here, VJEPA-2) as a reward to search and steer multiple candidate denoising trajectories, enabling scaling test-time compute for better generation performance. Empirically, our approach substantially improves physics plausibility across image-conditioned, multiframe-conditioned, and text-conditioned generation settings, with validation from human preference study. Notably, in the ICCV 2025 Perception Test PhysicsIQ Challenge, we achieve a final score of 62.64%, winning first place and outperforming the previous state of the art by 7.42%. Our work demonstrates the viability of using latent world models to improve physics plausibility of video generation, beyond this specific instantiation or parameterization.

