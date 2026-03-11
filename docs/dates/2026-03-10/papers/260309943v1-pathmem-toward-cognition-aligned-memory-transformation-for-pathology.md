---
layout: default
title: PathMem: Toward Cognition-Aligned Memory Transformation for Pathology MLLMs
---

# PathMem: Toward Cognition-Aligned Memory Transformation for Pathology MLLMs
**arXiv**：[2603.09943v1](https://arxiv.org/abs/2603.09943) · [PDF](https://arxiv.org/pdf/2603.09943.pdf)  
**作者**：Jinyue Li, Yuci Liang, Qiankun Li, Xinheng Lyu, Jiayu Qian, Huabao Chen, Kun Wang, Zhigang Zeng, Anil Anthony Bharath, Yang Liu  

**一句话要点**：提出PathMem框架，通过记忆转换机制解决病理学MLLMs中结构化知识整合不足的问题。

**关键词**：病理学多模态大语言模型, 记忆转换, 结构化知识整合, 工作记忆建模, 上下文感知推理

## 3 点简述
- 核心问题：现有病理学MLLMs缺乏结构化知识整合机制，难以在推理中一致应用诊断标准。
- 方法要点：引入记忆转换器，模拟从长时记忆到工作记忆的动态转换，实现上下文感知的知识精炼。
- 实验或效果：在WSI-Bench等基准上实现SOTA性能，报告生成和诊断准确率显著提升。

## 摘要（原文）

> Computational pathology demands both visual pattern recognition and dynamic integration of structured domain knowledge, including taxonomy, grading criteria, and clinical evidence. In practice, diagnostic reasoning requires linking morphological evidence with formal diagnostic and grading criteria. Although multimodal large language models (MLLMs) demonstrate strong vision language reasoning capabilities, they lack explicit mechanisms for structured knowledge integration and interpretable memory control. As a result, existing models struggle to consistently incorporate pathology-specific diagnostic standards during reasoning. Inspired by the hierarchical memory process of human pathologists, we propose PathMem, a memory-centric multimodal framework for pathology MLLMs. PathMem organizes structured pathology knowledge as a long-term memory (LTM) and introduces a Memory Transformer that models the dynamic transition from LTM to working memory (WM) through multimodal memory activation and context-aware knowledge grounding, enabling context-aware memory refinement for downstream reasoning. PathMem achieves SOTA performance across benchmarks, improving WSI-Bench report generation (12.8% WSI-Precision, 10.1% WSI-Relevance) and open-ended diagnosis by 9.7% and 8.9% over prior WSI-based models.

