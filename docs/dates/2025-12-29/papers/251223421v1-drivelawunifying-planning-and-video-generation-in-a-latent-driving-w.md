---
layout: default
title: DriveLaW:Unifying Planning and Video Generation in a Latent Driving World
---

# DriveLaW:Unifying Planning and Video Generation in a Latent Driving World
**arXiv**：[2512.23421v1](https://arxiv.org/abs/2512.23421) · [PDF](https://arxiv.org/pdf/2512.23421.pdf)  
**作者**：Tianze Xia, Yongkang Li, Lijun Zhou, Jingfeng Yao, Kaixin Xiong, Haiyang Sun, Bing Wang, Kun Ma, Hangjun Ye, Wenyu Liu, Xinggang Wang  

**一句话要点**：提出DriveLaW以统一自动驾驶中的视频生成与运动规划，通过潜在表示注入确保一致性。

**关键词**：自动驾驶世界模型, 视频生成, 运动规划, 潜在表示, 扩散模型, 统一架构

## 3 点简述
- 核心问题：现有世界模型在自动驾驶中常将视频预测与运动规划解耦，导致不一致性。
- 方法要点：DriveLaW包含DriveLaW-Video生成高保真视频和DriveLaW-Act扩散规划器，通过潜在表示直接连接。
- 实验或效果：在视频预测任务中FID提升33.3%，FVD提升1.8%，并在NAVSIM规划基准上创下新纪录。

## 摘要（原文）

> World models have become crucial for autonomous driving, as they learn how scenarios evolve over time to address the long-tail challenges of the real world. However, current approaches relegate world models to limited roles: they operate within ostensibly unified architectures that still keep world prediction and motion planning as decoupled processes. To bridge this gap, we propose DriveLaW, a novel paradigm that unifies video generation and motion planning. By directly injecting the latent representation from its video generator into the planner, DriveLaW ensures inherent consistency between high-fidelity future generation and reliable trajectory planning. Specifically, DriveLaW consists of two core components: DriveLaW-Video, our powerful world model that generates high-fidelity forecasting with expressive latent representations, and DriveLaW-Act, a diffusion planner that generates consistent and reliable trajectories from the latent of DriveLaW-Video, with both components optimized by a three-stage progressive training strategy. The power of our unified paradigm is demonstrated by new state-of-the-art results across both tasks. DriveLaW not only advances video prediction significantly, surpassing best-performing work by 33.3% in FID and 1.8% in FVD, but also achieves a new record on the NAVSIM planning benchmark.

