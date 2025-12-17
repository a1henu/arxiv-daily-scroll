---
layout: default
title: Distill Video Datasets into Images
---

# Distill Video Datasets into Images
**arXiv**：[2512.14621v1](https://arxiv.org/abs/2512.14621) · [PDF](https://arxiv.org/pdf/2512.14621.pdf)  
**作者**：Zhenghao Zhao, Haoxuan Wang, Kai Wang, Yuzhang Shang, Yuan Hong, Yan Yan  

**一句话要点**：提出单帧视频集蒸馏框架以解决视频数据集蒸馏中参数过多导致的优化难题

**关键词**：视频数据集蒸馏, 单帧蒸馏, 可微分插值, 优化效率, 判别语义, 时间信息整合

## 3 点简述
- 核心问题：视频数据集蒸馏因时间维度引入大量可学习参数，导致优化复杂和收敛困难
- 方法要点：利用单帧捕获视频判别语义，通过可微分插值将蒸馏帧转换为视频序列进行匹配
- 实验或效果：在多个基准测试中显著优于先前方法，在MiniUCF上提升达5.3%

## 摘要（原文）

> Dataset distillation aims to synthesize compact yet informative datasets that allow models trained on them to achieve performance comparable to training on the full dataset. While this approach has shown promising results for image data, extending dataset distillation methods to video data has proven challenging and often leads to suboptimal performance. In this work, we first identify the core challenge in video set distillation as the substantial increase in learnable parameters introduced by the temporal dimension of video, which complicates optimization and hinders convergence. To address this issue, we observe that a single frame is often sufficient to capture the discriminative semantics of a video. Leveraging this insight, we propose Single-Frame Video set Distillation (SFVD), a framework that distills videos into highly informative frames for each class. Using differentiable interpolation, these frames are transformed into video sequences and matched with the original dataset, while updates are restricted to the frames themselves for improved optimization efficiency. To further incorporate temporal information, the distilled frames are combined with sampled real videos from real videos during the matching process through a channel reshaping layer. Extensive experiments on multiple benchmarks demonstrate that SFVD substantially outperforms prior methods, achieving improvements of up to 5.3% on MiniUCF, thereby offering a more effective solution.

