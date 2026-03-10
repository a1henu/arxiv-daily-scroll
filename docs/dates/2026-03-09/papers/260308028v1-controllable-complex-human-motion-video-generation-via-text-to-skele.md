---
layout: default
title: Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades
---

# Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades
**arXiv**：[2603.08028v1](https://arxiv.org/abs/2603.08028) · [PDF](https://arxiv.org/pdf/2603.08028.pdf)  
**作者**：Ashkan Taghipour, Morteza Ghahremani, Zinuo Li, Hamid Laga, Farid Boussaid, Mohammed Bennamoun  

**一句话要点**：提出文本到骨架级联框架以生成可控复杂人体运动视频

**关键词**：复杂人体运动生成, 文本到骨架模型, 姿态条件视频合成, 自回归预测, 合成数据集, 视频扩散模型

## 3 点简述
- 核心问题：文本条件在细粒度运动控制上存在时间模糊性，而基于姿态的控制需要昂贵完整骨架序列。
- 方法要点：采用两阶段级联框架，先通过自回归文本到骨架模型生成2D姿态序列，再通过姿态条件视频扩散模型合成视频。
- 实验或效果：在合成数据集和Motion-X Fitness基准上，模型在FID、R-precision、运动多样性和VBench指标上优于现有方法。

## 摘要（原文）

> Generating videos of complex human motions such as flips, cartwheels, and martial arts remains challenging for current video diffusion models. Text-only conditioning is temporally ambiguous for fine-grained motion control, while explicit pose-based controls, though effective, require users to provide complete skeleton sequences that are costly to produce for long and dynamic actions.
>   We propose a two-stage cascaded framework that addresses both limitations. First, an autoregressive text-to-skeleton model generates 2D pose sequences from natural language descriptions by predicting each joint conditioned on previously generated poses. This design captures long-range temporal dependencies and inter-joint coordination required for complex motions. Second, a pose-conditioned video diffusion model synthesizes videos from a reference image and the generated skeleton sequence. It employs DINO-ALF (Adaptive Layer Fusion), a multi-level reference encoder that preserves appearance and clothing details under large pose changes and self-occlusions.
>   To address the lack of publicly available datasets for complex human motion video generation, we introduce a Blender-based synthetic dataset containing 2,000 videos with diverse characters performing acrobatic and stunt-like motions. The dataset provides full control over appearance, motion, and environment. It fills an important gap because existing benchmarks significantly under-represent acrobatic motions while web-collected datasets raise copyright and privacy concerns.
>   Experiments on our synthetic dataset and the Motion-X Fitness benchmark show that our text-to-skeleton model outperforms prior methods on FID, R-precision, and motion diversity. Our pose-to-video model also achieves the best results among all compared methods on VBench metrics for temporal consistency, motion smoothness, and subject preservation.

