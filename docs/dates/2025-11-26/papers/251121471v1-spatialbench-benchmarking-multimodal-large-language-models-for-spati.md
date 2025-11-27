---
layout: default
title: SpatialBench: Benchmarking Multimodal Large Language Models for Spatial Cognition
---

# SpatialBench: Benchmarking Multimodal Large Language Models for Spatial Cognition
**arXiv**：[2511.21471v1](https://arxiv.org/abs/2511.21471) · [PDF](https://arxiv.org/pdf/2511.21471.pdf)  
**作者**：Peiran Xu, Sudong Wang, Yao Zhu, Jianing Li, Yunjian Zhang  

**一句话要点**：提出SpatialBench基准以评估多模态大语言模型的空间认知能力

**关键词**：空间认知, 多模态大语言模型, 基准测试, 分层框架, 统一度量, 符号推理

## 3 点简述
- 现有基准过度简化空间认知，缺乏层次化评估框架
- 构建分层空间认知框架和统一度量，覆盖15个任务
- 实验显示模型感知强但推理弱，人类测试揭示模型缺乏空间意图

## 摘要（原文）

> Spatial cognition is fundamental to real-world multimodal intelligence, allowing models to effectively interact with the physical environment. While multimodal large language models (MLLMs) have made significant strides, existing benchmarks often oversimplify spatial cognition, reducing it to a single-dimensional metric, which fails to capture the hierarchical structure and interdependence of spatial abilities. To address this gap, we propose a hierarchical spatial cognition framework that decomposes spatial intelligence into five progressively complex levels from basic observation to high-level planning. Building upon this taxonomy, we construct SpatialBench, a large-scale, fine-grained benchmark covering 15 tasks aligned with these cognitive levels. To provide a unified evaluation across heterogeneous tasks, we further introduce a high-level capability-oriented metric that reliably assesses a model's overall spatial reasoning ability. Extensive experiments over massive MLLMs reveal distinct performance stratification across cognitive levels: models exhibit strong perceptual grounding yet remain limited in symbolic reasoning, causal inference, and planning. Additional human tests demonstrate that humans perform selective, goal-directed abstraction, while MLLMs tend to over-attend to surface details without coherent spatial intent. Our work establishes the first systematic framework for measuring hierarchical spatial cognition in MLLMs, laying the foundation for future spatially intelligent systems.

