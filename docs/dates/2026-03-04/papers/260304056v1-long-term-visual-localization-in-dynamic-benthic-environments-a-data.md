---
layout: default
title: Long-Term Visual Localization in Dynamic Benthic Environments: A Dataset, Footprint-Based Ground Truth, and Visual Place Recognition Benchmark
---

# Long-Term Visual Localization in Dynamic Benthic Environments: A Dataset, Footprint-Based Ground Truth, and Visual Place Recognition Benchmark
**arXiv**：[2603.04056v1](https://arxiv.org/abs/2603.04056) · [PDF](https://arxiv.org/pdf/2603.04056.pdf)  
**作者**：Martin Kvisvik Larsen, Oscar Pizarro  

**一句话要点**：提出基于足迹的地面真值方法，以解决动态底栖环境中长期视觉定位的基准缺失问题。

**关键词**：长期视觉定位, 水下视觉, 数据集构建, 地面真值方法, 视觉地点识别, 底栖环境

## 3 点简述
- 核心问题：长期视觉定位在底栖环境中研究不足，缺乏基准数据集和精确地面真值。
- 方法要点：构建多站点长期水下数据集，并开发基于图像足迹的地面真值方法，确保视觉内容共享。
- 实验或效果：基准测试显示VPR方法性能低于现有基准，足迹方法优于传统位置阈值方法。

## 摘要（原文）

> Long-term visual localization has the potential to reduce cost and improve mapping quality in optical benthic monitoring with autonomous underwater vehicles (AUVs). Despite this potential, long-term visual localization in benthic environments remains understudied, primarily due to the lack of curated datasets for benchmarking. Moreover, limited georeferencing accuracy and image footprints necessitate precise geometric information for accurate ground-truthing. In this work, we address these gaps by presenting a curated dataset for long-term visual localization in benthic environments and a novel method to ground-truth visual localization results for near-nadir underwater imagery. Our dataset comprises georeferenced AUV imagery from five benthic reference sites, revisited over periods up to six years, and includes raw and color-corrected stereo imagery, camera calibrations, and sub-decimeter registered camera poses. To our knowledge, this is the first curated underwater dataset for long-term visual localization spanning multiple sites and photic-zone habitats. Our ground-truthing method estimates 3D seafloor image footprints and links camera views with overlapping footprints, ensuring that ground-truth links reflect shared visual content. Building on this dataset and ground truth, we benchmark eight state-of-the-art visual place recognition (VPR) methods and find that Recall@K is significantly lower on our dataset than on established terrestrial and underwater benchmarks. Finally, we compare our footprint-based ground truth to a traditional location-based ground truth and show that distance-threshold ground-truthing can overestimate VPR Recall@K at sites with rugged terrain and altitude variations. Together, the curated dataset, ground-truthing method, and VPR benchmark provide a stepping stone for advancing long-term visual localization in dynamic benthic environments.

