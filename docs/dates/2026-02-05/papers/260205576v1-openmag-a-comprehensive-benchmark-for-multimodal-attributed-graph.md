---
layout: default
title: OpenMAG: A Comprehensive Benchmark for Multimodal-Attributed Graph
---

# OpenMAG: A Comprehensive Benchmark for Multimodal-Attributed Graph
**arXiv**：[2602.05576v1](https://arxiv.org/abs/2602.05576) · [PDF](https://arxiv.org/pdf/2602.05576.pdf)  
**作者**：Chenxi Wan, Xunkai Li, Yilong Zuo, Haokun Deng, Sihan Li, Bowen Fan, Hongchao Qin, Ronghua Li, Guoren Wang  

**一句话要点**：提出OpenMAG基准以解决多模态属性图学习评估标准不统一的问题

**关键词**：多模态属性图, 基准测试, 图学习, 跨模态语义, 标准化评估, 下游任务

## 3 点简述
- 核心问题：现有基准在领域覆盖、编码器灵活性、模型多样性和任务范围上存在局限，阻碍公平评估
- 方法要点：集成19个数据集和16种编码器，支持静态和可训练特征编码，实现标准化模型库
- 实验或效果：通过系统评估得出14个基本见解，指导未来多模态属性图学习的发展

## 摘要（原文）

> Multimodal-Attributed Graph (MAG) learning has achieved remarkable success in modeling complex real-world systems by integrating graph topology with rich attributes from multiple modalities. With the rapid proliferation of novel MAG models capable of handling intricate cross-modal semantics and structural dependencies, establishing a rigorous and unified evaluation standard has become imperative. Although existing benchmarks have facilitated initial progress, they exhibit critical limitations in domain coverage, encoder flexibility, model diversity, and task scope, presenting significant challenges to fair evaluation. To bridge this gap, we present OpenMAG, a comprehensive benchmark that integrates 19 datasets across 6 domains and incorporates 16 encoders to support both static and trainable feature encoding. OpenMAG further implements a standardized library of 24 state-of-the-art models and supports 8 downstream tasks, enabling fair comparisons within a unified framework. Through systematic assessment of necessity, data quality, effectiveness, robustness, and efficiency, we derive 14 fundamental insights into MAG learning to guide future advancements. Our code is available at https://github.com/YUKI-N810/OpenMAG.

