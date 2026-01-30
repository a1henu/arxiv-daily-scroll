---
layout: default
title: Trajectory-Guided Diffusion for Foreground-Preserving Background Generation in Multi-Layer Documents
---

# Trajectory-Guided Diffusion for Foreground-Preserving Background Generation in Multi-Layer Documents
**arXiv**：[2601.21857v1](https://arxiv.org/abs/2601.21857) · [PDF](https://arxiv.org/pdf/2601.21857.pdf)  
**作者**：Taewon Kang  

**一句话要点**：提出基于轨迹引导的扩散框架，用于多页文档中前景保留的背景生成

**关键词**：文档背景生成, 扩散模型, 前景保留, 风格一致性, 潜在空间设计, 轨迹引导

## 3 点简述
- 核心问题：多页文档背景生成中前景内容易被破坏，且风格一致性难以维持。
- 方法要点：通过设计潜在空间中的初始噪声和几何对齐，引导扩散轨迹避开前景区域，并引入缓存风格方向确保跨页风格一致。
- 实验或效果：无需训练，兼容现有扩散模型，在复杂文档中实现视觉连贯且前景保留的生成结果。

## 摘要（原文）

> We present a diffusion-based framework for document-centric background generation that achieves foreground preservation and multi-page stylistic consistency through latent-space design rather than explicit constraints. Instead of suppressing diffusion updates or applying masking heuristics, our approach reinterprets diffusion as the evolution of stochastic trajectories through a structured latent space. By shaping the initial noise and its geometric alignment, background generation naturally avoids designated foreground regions, allowing readable content to remain intact without auxiliary mechanisms. To address the long-standing issue of stylistic drift across pages, we decouple style control from text conditioning and introduce cached style directions as persistent vectors in latent space. Once selected, these directions constrain diffusion trajectories to a shared stylistic subspace, ensuring consistent appearance across pages and editing iterations. This formulation eliminates the need for repeated prompt-based style specification and provides a more stable foundation for multi-page generation. Our framework admits a geometric and physical interpretation, where diffusion paths evolve on a latent manifold shaped by preferred directions, and foreground regions are rarely traversed as a consequence of trajectory initialization rather than explicit exclusion. The proposed method is training-free, compatible with existing diffusion backbones, and produces visually coherent, foreground-preserving results across complex documents. By reframing diffusion as trajectory design in latent space, we offer a principled approach to consistent and structured generative modeling.

