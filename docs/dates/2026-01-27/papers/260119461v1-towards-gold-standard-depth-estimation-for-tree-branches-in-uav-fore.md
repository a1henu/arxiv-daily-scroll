---
layout: default
title: Towards Gold-Standard Depth Estimation for Tree Branches in UAV Forestry: Benchmarking Deep Stereo Matching Methods
---

# Towards Gold-Standard Depth Estimation for Tree Branches in UAV Forestry: Benchmarking Deep Stereo Matching Methods
**arXiv**：[2601.19461v1](https://arxiv.org/abs/2601.19461) · [PDF](https://arxiv.org/pdf/2601.19461.pdf)  
**作者**：Yida Lin, Bing Xue, Mengjie Zhang, Sam Schofield, Richard Green  

**一句话要点**：提出首个无人机林业树枝深度估计基准，评估八种立体匹配方法在植被密集场景的零样本性能。

**关键词**：深度估计, 立体匹配, 无人机林业, 零样本评估, 植被场景, 基准测试

## 3 点简述
- 核心问题：现有深度估计评估集中于城市和室内场景，缺乏针对植被密集环境的系统分析。
- 方法要点：使用官方预训练权重，在四个标准基准和新树枝数据集上零样本评估八种立体匹配方法。
- 实验效果：发现场景依赖性模式，DEFOM在植被深度估计中表现最佳，被确立为黄金标准基线。

## 摘要（原文）

> Autonomous UAV forestry operations require robust depth estimation with strong cross-domain generalization, yet existing evaluations focus on urban and indoor scenarios, leaving a critical gap for vegetation-dense environments. We present the first systematic zero-shot evaluation of eight stereo methods spanning iterative refinement, foundation model, diffusion-based, and 3D CNN paradigms. All methods use officially released pretrained weights (trained on Scene Flow) and are evaluated on four standard benchmarks (ETH3D, KITTI 2012/2015, Middlebury) plus a novel 5,313-pair Canterbury Tree Branches dataset ($1920 \times 1080$). Results reveal scene-dependent patterns: foundation models excel on structured scenes (BridgeDepth: 0.23 px on ETH3D; DEFOM: 4.65 px on Middlebury), while iterative methods show variable cross-benchmark performance (IGEV++: 0.36 px on ETH3D but 6.77 px on Middlebury; IGEV: 0.33 px on ETH3D but 4.99 px on Middlebury). Qualitative evaluation on the Tree Branches dataset establishes DEFOM as the gold-standard baseline for vegetation depth estimation, with superior cross-domain consistency (consistently ranking 1st-2nd across benchmarks, average rank 1.75). DEFOM predictions will serve as pseudo-ground-truth for future benchmarking.

