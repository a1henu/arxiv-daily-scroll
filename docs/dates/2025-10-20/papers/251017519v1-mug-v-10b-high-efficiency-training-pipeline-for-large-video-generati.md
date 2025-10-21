---
layout: default
title: MUG-V 10B: High-efficiency Training Pipeline for Large Video Generation Models
---

# MUG-V 10B: High-efficiency Training Pipeline for Large Video Generation Models
**arXiv**：[2510.17519v1](https://arxiv.org/abs/2510.17519) · [PDF](https://arxiv.org/pdf/2510.17519.pdf)  
**作者**：Yongshun Zhang, Zhongyi Fan, Yonghang Zhang, Zhangzikang Li, Weifeng Chen, Zhongwei Feng, Chaoyue Wang, Peng Hou, Anxiang Zeng  

**一句话要点**：提出高效训练框架以解决大规模视频生成模型的资源挑战

**关键词**：大规模视频生成, 高效训练框架, 跨模态对齐, 开源代码, 多节点扩展

## 3 点简述
- 核心问题：大规模视频生成训练面临跨模态对齐、长序列和时空依赖等资源密集型挑战
- 方法要点：优化数据处理、模型架构、训练策略和基础设施四大支柱，提升效率
- 实验或效果：MUG-V 10B模型在电商视频生成任务中超越开源基线，并开源完整堆栈

## 摘要（原文）

> In recent years, large-scale generative models for visual content
> (\textit{e.g.,} images, videos, and 3D objects/scenes) have made remarkable
> progress. However, training large-scale video generation models remains
> particularly challenging and resource-intensive due to cross-modal text-video
> alignment, the long sequences involved, and the complex spatiotemporal
> dependencies. To address these challenges, we present a training framework that
> optimizes four pillars: (i) data processing, (ii) model architecture, (iii)
> training strategy, and (iv) infrastructure for large-scale video generation
> models. These optimizations delivered significant efficiency gains and
> performance improvements across all stages of data preprocessing, video
> compression, parameter scaling, curriculum-based pretraining, and
> alignment-focused post-training. Our resulting model, MUG-V 10B, matches recent
> state-of-the-art video generators overall and, on e-commerce-oriented video
> generation tasks, surpasses leading open-source baselines in human evaluations.
> More importantly, we open-source the complete stack, including model weights,
> Megatron-Core-based large-scale training code, and inference pipelines for
> video generation and enhancement. To our knowledge, this is the first public
> release of large-scale video generation training code that exploits
> Megatron-Core to achieve high training efficiency and near-linear multi-node
> scaling, details are available in
> \href{https://github.com/Shopee-MUG/MUG-V}{our webpage}.

