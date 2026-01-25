---
layout: default
title: Skywork UniPic 3.0: Unified Multi-Image Composition via Sequence Modeling
---

# Skywork UniPic 3.0: Unified Multi-Image Composition via Sequence Modeling
**arXiv**：[2601.15664v1](https://arxiv.org/abs/2601.15664) · [PDF](https://arxiv.org/pdf/2601.15664.pdf)  
**作者**：Hongyang Wei, Hongbo Liu, Zidong Wang, Yi Peng, Baixin Xu, Size Wu, Xuying Zhang, Xianglong He, Zexiang Liu, Peiyu Wang, Xuchen Song, Yangguang Li, Yang Liu, Yahui Zhou  

**一句话要点**：提出Skywork UniPic 3.0统一多模态框架，通过序列建模解决多图像组合任务中的一致性与质量问题。

**关键词**：多图像组合, 序列建模, 人-物交互, 统一框架, 加速推理

## 3 点简述
- 核心问题：多图像组合在一致性与质量上比单图像编辑更具挑战，现有模型缺乏高质量融合方法细节。
- 方法要点：设计数据收集与合成流程，将多图像组合建模为序列问题，集成轨迹映射和分布匹配加速推理。
- 实验或效果：在单图像编辑基准上达到最优，多图像组合基准上超越Nano-Banana和Seedream 4.0，推理速度提升12.5倍。

## 摘要（原文）

> The recent surge in popularity of Nano-Banana and Seedream 4.0 underscores the community's strong interest in multi-image composition tasks. Compared to single-image editing, multi-image composition presents significantly greater challenges in terms of consistency and quality, yet existing models have not disclosed specific methodological details for achieving high-quality fusion. Through statistical analysis, we identify Human-Object Interaction (HOI) as the most sought-after category by the community. We therefore systematically analyze and implement a state-of-the-art solution for multi-image composition with a primary focus on HOI-centric tasks. We present Skywork UniPic 3.0, a unified multimodal framework that integrates single-image editing and multi-image composition. Our model supports an arbitrary (1~6) number and resolution of input images, as well as arbitrary output resolutions (within a total pixel budget of 1024x1024). To address the challenges of multi-image composition, we design a comprehensive data collection, filtering, and synthesis pipeline, achieving strong performance with only 700K high-quality training samples. Furthermore, we introduce a novel training paradigm that formulates multi-image composition as a sequence-modeling problem, transforming conditional generation into unified sequence synthesis. To accelerate inference, we integrate trajectory mapping and distribution matching into the post-training stage, enabling the model to produce high-fidelity samples in just 8 steps and achieve a 12.5x speedup over standard synthesis sampling. Skywork UniPic 3.0 achieves state-of-the-art performance on single-image editing benchmark and surpasses both Nano-Banana and Seedream 4.0 on multi-image composition benchmark, thereby validating the effectiveness of our data pipeline and training paradigm. Code, models and dataset are publicly available.

