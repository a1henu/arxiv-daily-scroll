---
layout: default
title: History-Enhanced Two-Stage Transformer for Aerial Vision-and-Language Navigation
---

# History-Enhanced Two-Stage Transformer for Aerial Vision-and-Language Navigation
**arXiv**：[2512.14222v1](https://arxiv.org/abs/2512.14222) · [PDF](https://arxiv.org/pdf/2512.14222.pdf)  
**作者**：Xichen Ding, Jianzhe Gao, Cong Pan, Wenguan Wang, Jie Qin  

**一句话要点**：提出历史增强两阶段Transformer，通过粗到细导航解决无人机视觉语言导航中全局与局部平衡问题。

**关键词**：无人机视觉语言导航, 两阶段Transformer, 历史增强, 粗到细导航, 空间记忆, CityNav数据集

## 3 点简述
- 核心问题：现有无人机视觉语言导航框架难以平衡全局环境推理与局部场景理解。
- 方法要点：设计两阶段Transformer，先融合空间地标和历史上下文预测粗粒度目标位置，再通过细粒度视觉分析精炼动作。
- 实验或效果：在精炼的CityNav数据集上验证性能显著提升，消融研究确认各组件有效性。

## 摘要（原文）

> Aerial Vision-and-Language Navigation (AVLN) requires Unmanned Aerial Vehicle (UAV) agents to localize targets in large-scale urban environments based on linguistic instructions. While successful navigation demands both global environmental reasoning and local scene comprehension, existing UAV agents typically adopt mono-granularity frameworks that struggle to balance these two aspects. To address this limitation, this work proposes a History-Enhanced Two-Stage Transformer (HETT) framework, which integrates the two aspects through a coarse-to-fine navigation pipeline. Specifically, HETT first predicts coarse-grained target positions by fusing spatial landmarks and historical context, then refines actions via fine-grained visual analysis. In addition, a historical grid map is designed to dynamically aggregate visual features into a structured spatial memory, enhancing comprehensive scene awareness. Additionally, the CityNav dataset annotations are manually refined to enhance data quality. Experiments on the refined CityNav dataset show that HETT delivers significant performance gains, while extensive ablation studies further verify the effectiveness of each component.

