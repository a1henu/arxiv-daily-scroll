---
layout: default
title: ReVSeg: Incentivizing the Reasoning Chain for Video Segmentation with Reinforcement Learning
---

# ReVSeg: Incentivizing the Reasoning Chain for Video Segmentation with Reinforcement Learning
**arXiv**：[2512.02835v1](https://arxiv.org/abs/2512.02835) · [PDF](https://arxiv.org/pdf/2512.02835.pdf)  
**作者**：Yifan Li, Yingda Yin, Lingting Zhu, Weikai Chen, Shengju Qian, Xin Wang, Yanwei Fu  

**一句话要点**：提出ReVSeg，通过强化学习优化多步推理链以解决视频对象分割中的复杂推理问题。

**关键词**：视频对象分割, 推理链优化, 强化学习, 视觉语言模型, 多步决策, 可解释性

## 3 点简述
- 核心问题：现有方法将动态、因果和时间交互简化为潜在嵌入，导致推理链不透明且难以处理。
- 方法要点：采用显式分解视角，执行语义解释、时间证据选择和空间定位三步操作，并利用强化学习优化推理链。
- 实验或效果：在标准视频对象分割基准上达到最先进性能，并生成可解释的推理轨迹。

## 摘要（原文）

> Reasoning-centric video object segmentation is an inherently complex task: the query often refers to dynamics, causality, and temporal interactions, rather than static appearances. Yet existing solutions generally collapse these factors into simplified reasoning with latent embeddings, rendering the reasoning chain opaque and essentially intractable. We therefore adopt an explicit decomposition perspective and introduce ReVSeg, which executes reasoning as sequential decisions in the native interface of pretrained vision language models (VLMs). Rather than folding all reasoning into a single-step prediction, ReVSeg executes three explicit operations -- semantics interpretation, temporal evidence selection, and spatial grounding -- aligning pretrained capabilities. We further employ reinforcement learning to optimize the multi-step reasoning chain, enabling the model to self-refine its decision quality from outcome-driven signals. Experimental results demonstrate that ReVSeg attains state-of-the-art performances on standard video object segmentation benchmarks and yields interpretable reasoning trajectories. Project page is available at https://clementine24.github.io/ReVSeg/ .

