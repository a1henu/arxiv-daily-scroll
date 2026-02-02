---
layout: default
title: FOTBCD: A Large-Scale Building Change Detection Benchmark from French Orthophotos and Topographic Data
---

# FOTBCD: A Large-Scale Building Change Detection Benchmark from French Orthophotos and Topographic Data
**arXiv**：[2601.22596v1](https://arxiv.org/abs/2601.22596) · [PDF](https://arxiv.org/pdf/2601.22596.pdf)  
**作者**：Abdelrrahman Moubane  

**一句话要点**：提出FOTBCD大规模建筑变化检测基准，基于法国正射影像和地形数据，用于地理域转移评估。

**关键词**：建筑变化检测, 大规模数据集, 地理域转移, 正射影像, 基准测试

## 3 点简述
- 核心问题：现有建筑变化检测数据集地理范围有限，缺乏大规模跨区域基准。
- 方法要点：构建覆盖法国28个省的多样化数据集，包括二元和实例级标注，支持地理域转移研究。
- 实验或效果：通过基准测试，证明数据集地理多样性有助于提升跨域泛化性能。

## 摘要（原文）

> We introduce FOTBCD, a large-scale building change detection dataset derived from authoritative French orthophotos and topographic building data provided by IGN France. Unlike existing benchmarks that are geographically constrained to single cities or limited regions, FOTBCD spans 28 departments across mainland France, with 25 used for training and three geographically disjoint departments held out for evaluation. The dataset covers diverse urban, suburban, and rural environments at 0.2m/pixel resolution. We publicly release FOTBCD-Binary, a dataset comprising approximately 28,000 before/after image pairs with pixel-wise binary building change masks, each associated with patch-level spatial metadata. The dataset is designed for large-scale benchmarking and evaluation under geographic domain shift, with validation and test samples drawn from held-out departments and manually verified to ensure label quality. In addition, we publicly release FOTBCD-Instances, a publicly available instance-level annotated subset comprising several thousand image pairs, which illustrates the complete annotation schema used in the full instance-level version of FOTBCD. Using a fixed reference baseline, we benchmark FOTBCD-Binary against LEVIR-CD+ and WHU-CD, providing strong empirical evidence that geographic diversity at the dataset level is associated with improved cross-domain generalization in building change detection.

