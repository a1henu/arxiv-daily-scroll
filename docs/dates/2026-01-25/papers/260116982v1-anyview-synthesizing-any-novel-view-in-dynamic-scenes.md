---
layout: default
title: AnyView: Synthesizing Any Novel View in Dynamic Scenes
---

# AnyView: Synthesizing Any Novel View in Dynamic Scenes
**arXiv**：[2601.16982v1](https://arxiv.org/abs/2601.16982) · [PDF](https://arxiv.org/pdf/2601.16982.pdf)  
**作者**：Basile Van Hoorick, Dian Chen, Shun Iwase, Pavel Tokmakov, Muhammad Zubair Irshad, Igor Vasiljevic, Swati Gupta, Fangzhou Cheng, Sergey Zakharov, Vitor Campagnolo Guizilini  

**一句话要点**：提出AnyView框架，基于扩散模型实现动态场景中任意视角的视频合成

**关键词**：动态视角合成, 扩散模型, 视频生成, 时空一致性, 零样本学习

## 3 点简述
- 核心问题：现有生成视频模型在高度动态真实环境中难以保持多视角和时空一致性
- 方法要点：利用多源数据训练通用时空隐式表示，支持零样本从任意相机轨迹生成视频
- 实验或效果：在标准基准上表现竞争性，在极端动态视角合成新基准上优于基线

## 摘要（原文）

> Modern generative video models excel at producing convincing, high-quality outputs, but struggle to maintain multi-view and spatiotemporal consistency in highly dynamic real-world environments. In this work, we introduce \textbf{AnyView}, a diffusion-based video generation framework for \emph{dynamic view synthesis} with minimal inductive biases or geometric assumptions. We leverage multiple data sources with various levels of supervision, including monocular (2D), multi-view static (3D) and multi-view dynamic (4D) datasets, to train a generalist spatiotemporal implicit representation capable of producing zero-shot novel videos from arbitrary camera locations and trajectories. We evaluate AnyView on standard benchmarks, showing competitive results with the current state of the art, and propose \textbf{AnyViewBench}, a challenging new benchmark tailored towards \emph{extreme} dynamic view synthesis in diverse real-world scenarios. In this more dramatic setting, we find that most baselines drastically degrade in performance, as they require significant overlap between viewpoints, while AnyView maintains the ability to produce realistic, plausible, and spatiotemporally consistent videos when prompted from \emph{any} viewpoint. Results, data, code, and models can be viewed at: https://tri-ml.github.io/AnyView/

