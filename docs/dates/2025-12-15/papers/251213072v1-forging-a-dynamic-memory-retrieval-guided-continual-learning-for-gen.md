---
layout: default
title: Forging a Dynamic Memory: Retrieval-Guided Continual Learning for Generalist Medical Foundation Models
---

# Forging a Dynamic Memory: Retrieval-Guided Continual Learning for Generalist Medical Foundation Models
**arXiv**：[2512.13072v1](https://arxiv.org/abs/2512.13072) · [PDF](https://arxiv.org/pdf/2512.13072.pdf)  
**作者**：Zizhi Chen, Yizhen Gao, Minghao Han, Yizhou Liu, Zhaoyu Chen, Dingkang Yang, Lihua Zhang  

**一句话要点**：提出检索增强生成与动态知识蒸馏框架，以解决医学多模态基础模型在持续学习中保留细粒度特征与跨模态域差距的难题。

**关键词**：医学多模态基础模型, 持续学习, 检索增强生成, 动态知识蒸馏, 医学任务增量学习, 跨模态域差距

## 3 点简述
- 核心问题：医学多模态视觉语言模型在持续学习中面临保留细粒度模态内特征与跨越模态域差距的困境。
- 方法要点：基于1800万医学检索数据库，集成多模态多层检索增强生成，并引入动态知识蒸馏框架，动态调节参数空间、知识粒度与数据分布。
- 实验或效果：设计医学通用任务增量学习基准，实验显示方法在所有指标上达到最先进性能，代码已提供。

## 摘要（原文）

> Multimodal biomedical Vision-Language Models (VLMs) exhibit immense potential in the field of Continual Learning (CL). However, they confront a core dilemma: how to preserve fine-grained intra-modality features while bridging the significant domain gap across different modalities. To address this challenge, we propose a comprehensive framework. Leveraging our 18-million multimodal and comprehensive medical retrieval database derived from PubMed scientific papers, we pioneer the integration of Retrieval-Augmented Generation (RAG) into CL. Specifically, we employ a multi-modal, multi-layer RAG system that provides real-time guidance for model fine-tuning through dynamic, on-demand knowledge retrieval. Building upon this, we introduce a dynamic knowledge distillation framework. This framework precisely resolves the aforementioned core dilemma by dynamically modulating the importance of the parameter space, the granularity of the distilled knowledge, and the data distribution of the reference dataset in accordance with the required level of detail. To thoroughly validate the clinical value of our strategy, we have designed a more rigorous \textbf{M}edical Generalist Task Incremental Learning (MGTIL) benchmark. This benchmark is engineered to simultaneously evaluate the model's capacity for adaptation to significant domain shifts, retention of subtle intra-domain features, and real-time learning of novel and complex medical tasks. Extensive experimental results demonstrate that our proposed method achieves state-of-the-art (SOTA) performance across all metrics. The code is provided in the supplementary materials.

