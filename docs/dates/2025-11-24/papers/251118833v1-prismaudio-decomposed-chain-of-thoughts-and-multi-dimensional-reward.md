---
layout: default
title: PrismAudio: Decomposed Chain-of-Thoughts and Multi-dimensional Rewards for Video-to-Audio Generation
---

# PrismAudio: Decomposed Chain-of-Thoughts and Multi-dimensional Rewards for Video-to-Audio Generation
**arXiv**：[2511.18833v1](https://arxiv.org/abs/2511.18833) · [PDF](https://arxiv.org/pdf/2511.18833.pdf)  
**作者**：Huadai Liu, Kaicheng Luo, Wen Wang, Qian Chen, Peiwen Sun, Rongjie Huang, Xiangang Li, Jieping Ye, Wei Xue  

**一句话要点**：提出PrismAudio框架，通过分解思维链和多维奖励解决视频到音频生成的客观纠缠问题。

**关键词**：视频到音频生成, 强化学习, 思维链分解, 多维奖励优化, AudioCanvas基准

## 3 点简述
- 核心问题：现有方法在视频到音频生成中存在客观纠缠，混淆多个感知维度的目标。
- 方法要点：引入分解思维链和对应奖励函数，结合强化学习进行多维优化。
- 实验或效果：在VGGSound和AudioCanvas基准上实现所有四个感知维度的最先进性能。

## 摘要（原文）

> Video-to-Audio (V2A) generation requires balancing four critical perceptual dimensions: semantic consistency, audio-visual temporal synchrony, aesthetic quality, and spatial accuracy; yet existing methods suffer from objective entanglement that conflates competing goals in single loss functions and lack human preference alignment. We introduce PrismAudio, the first framework to integrate Reinforcement Learning into V2A generation with specialized Chain-of-Thought (CoT) planning. Our approach decomposes monolithic reasoning into four specialized CoT modules (Semantic, Temporal, Aesthetic, and Spatial CoT), each paired with targeted reward functions. This CoT-reward correspondence enables multidimensional RL optimization that guides the model to jointly generate better reasoning across all perspectives, solving the objective entanglement problem while preserving interpretability. To make this optimization computationally practical, we propose Fast-GRPO, which employs hybrid ODE-SDE sampling that dramatically reduces the training overhead compared to existing GRPO implementations. We also introduce AudioCanvas, a rigorous benchmark that is more distributionally balanced and covers more realistically diverse and challenging scenarios than existing datasets, with 300 single-event classes and 501 multi-event samples. Experimental results demonstrate that PrismAudio achieves state-of-the-art performance across all four perceptual dimensions on both the in-domain VGGSound test set and out-of-domain AudioCanvas benchmark. The project page is available at https://PrismAudio-Project.github.io.

