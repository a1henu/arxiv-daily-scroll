---
layout: default
title: Seeing through Imagination: Learning Scene Geometry via Implicit Spatial World Modeling
---

# Seeing through Imagination: Learning Scene Geometry via Implicit Spatial World Modeling
**arXiv**：[2512.01821v1](https://arxiv.org/abs/2512.01821) · [PDF](https://arxiv.org/pdf/2512.01821.pdf)  
**作者**：Meng Cao, Haokun Lin, Haoyuan Li, Haoran Tang, Rongtao Xu, Dong An, Xue Liu, Ian Reid, Xiaodan Liang  

**一句话要点**：提出MILO隐式空间世界建模范式，通过视觉生成器增强多模态大语言模型的空间推理能力。

**关键词**：空间推理, 隐式建模, 多模态大语言模型, 几何感知, 相对位置编码, 生成数据集

## 3 点简述
- 核心问题：多模态大语言模型依赖文本描述学习空间概念，缺乏视觉连接，导致空间推理能力不足。
- 方法要点：引入MILO范式，集成视觉生成器提供几何感知反馈，并设计RePE编码方案捕捉相对相机位姿变换。
- 实验或效果：构建GeoGen数据集，实验显示方法显著提升多个基线和基准测试的空间推理性能。

## 摘要（原文）

> Spatial reasoning, the ability to understand and interpret the 3D structure of the world, is a critical yet underdeveloped capability in Multimodal Large Language Models (MLLMs). Current methods predominantly rely on verbal descriptive tuning, which suffers from visual illiteracy, i.e., they learn spatial concepts through textual symbols alone, devoid of connection to their visual manifestations. To bridge this gap, this paper introduces MILO, an Implicit spatIaL wOrld modeling paradigm that simulates human-like spatial imagination. MILO integrates a visual generator to provide geometry-aware feedback, thereby implicitly grounding the MLLM's symbolic reasoning in perceptual experience. Complementing this paradigm, we propose RePE (Relative Positional Encoding), a novel encoding scheme that captures relative camera-pose transformations, offering superior performance over absolute coordinate systems. To support the training, we construct GeoGen, a large-scale Geometry-aware Generative dataset with approximately 2,241 videos and 67,827 observation-action-outcome triplets. Experiments demonstrate that our approach significantly enhances spatial reasoning capabilities across multiple baselines and benchmarks, offering a more holistic understanding of 3D space.

