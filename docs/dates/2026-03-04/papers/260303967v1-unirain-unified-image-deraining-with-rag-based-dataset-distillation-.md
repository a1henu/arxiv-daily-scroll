---
layout: default
title: UniRain: Unified Image Deraining with RAG-based Dataset Distillation and Multi-objective Reweighted Optimization
---

# UniRain: Unified Image Deraining with RAG-based Dataset Distillation and Multi-objective Reweighted Optimization
**arXiv**：[2603.03967v1](https://arxiv.org/abs/2603.03967) · [PDF](https://arxiv.org/pdf/2603.03967.pdf)  
**作者**：Qianfeng Yang, Qiyuan Guan, Xiang Chen, Jiyu Jin, Guiyue Jin, Jiangxin Dong  

**一句话要点**：提出UniRain统一图像去雨框架，通过RAG数据集蒸馏和多目标重加权优化处理多种雨退化场景。

**关键词**：图像去雨, 统一框架, 数据集蒸馏, 多目标优化, 检索增强生成

## 3 点简述
- 核心问题：现有方法难以统一处理雨线和雨滴等不同雨退化类型，泛化能力有限。
- 方法要点：采用RAG数据集蒸馏选择高质量训练样本，结合多目标重加权优化提升模型鲁棒性。
- 实验或效果：在多个公共数据集上表现优于现有先进模型，验证了统一去雨的有效性。

## 摘要（原文）

> Despite significant progress has been made in image deraining, we note that most existing methods are often developed for only specific types of rain degradation and fail to generalize across diverse real-world rainy scenes. How to effectively model different rain degradations within a universal framework is important for real-world image deraining. In this paper, we propose UniRain, an effective unified image deraining framework capable of restoring images degraded by rain streak and raindrop under both daytime and nighttime conditions. To better enhance unified model generalization, we construct an intelligent retrieval augmented generation (RAG)-based dataset distillation pipeline that selects high-quality training samples from all public deraining datasets for better mixed training. Furthermore, we incorporate a simple yet effective multi-objective reweighted optimization strategy into the asymmetric mixture-of-experts (MoE) architecture to facilitate consistent performance and improve robustness across diverse scenes. Extensive experiments show that our framework performs favorably against the state-of-the-art models on our proposed benchmarks and multiple public datasets.

