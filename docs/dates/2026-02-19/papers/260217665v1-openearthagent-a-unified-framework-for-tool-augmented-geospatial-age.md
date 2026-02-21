---
layout: default
title: OpenEarthAgent: A Unified Framework for Tool-Augmented Geospatial Agents
---

# OpenEarthAgent: A Unified Framework for Tool-Augmented Geospatial Agents
**arXiv**：[2602.17665v1](https://arxiv.org/abs/2602.17665) · [PDF](https://arxiv.org/pdf/2602.17665.pdf)  
**作者**：Akashah Shabbir, Muhammad Umer Sheikh, Muhammad Akhtar Munir, Hiyam Debary, Mustansar Fiaz, Muhammad Zaigham Zaheer, Paolo Fraccaro, Fahad Shahbaz Khan, Muhammad Haris Khan, Xiao Xiang Zhu, Salman Khan  

**一句话要点**：提出OpenEarthAgent统一框架，通过工具增强的遥感代理解决多模态地理空间推理挑战。

**关键词**：遥感代理, 多模态推理, 工具增强, 地理空间分析, 结构化训练, 卫星影像处理

## 3 点简述
- 核心问题：遥感领域需处理空间尺度、地理结构和多光谱指数，保持多步逻辑推理。
- 方法要点：基于监督微调结构化推理轨迹，整合卫星影像、自然语言查询和工具交互。
- 实验或效果：在14,538训练实例上实现稳定空间理解和可解释行为，优于基线模型。

## 摘要（原文）

> Recent progress in multimodal reasoning has enabled agents that can interpret imagery, connect it with language, and perform structured analytical tasks. Extending such capabilities to the remote sensing domain remains challenging, as models must reason over spatial scale, geographic structures, and multispectral indices while maintaining coherent multi-step logic. To bridge this gap, OpenEarthAgent introduces a unified framework for developing tool-augmented geospatial agents trained on satellite imagery, natural-language queries, and detailed reasoning traces. The training pipeline relies on supervised fine-tuning over structured reasoning trajectories, aligning the model with verified multistep tool interactions across diverse analytical contexts. The accompanying corpus comprises 14,538 training and 1,169 evaluation instances, with more than 100K reasoning steps in the training split and over 7K reasoning steps in the evaluation split. It spans urban, environmental, disaster, and infrastructure domains, and incorporates GIS-based operations alongside index analyses such as NDVI, NBR, and NDBI. Grounded in explicit reasoning traces, the learned agent demonstrates structured reasoning, stable spatial understanding, and interpretable behaviour through tool-driven geospatial interactions across diverse conditions. We report consistent improvements over a strong baseline and competitive performance relative to recent open and closed-source models.

