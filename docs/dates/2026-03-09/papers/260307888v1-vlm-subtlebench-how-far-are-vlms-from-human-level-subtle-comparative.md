---
layout: default
title: VLM-SubtleBench: How Far Are VLMs from Human-Level Subtle Comparative Reasoning?
---

# VLM-SubtleBench: How Far Are VLMs from Human-Level Subtle Comparative Reasoning?
**arXiv**：[2603.07888v1](https://arxiv.org/abs/2603.07888) · [PDF](https://arxiv.org/pdf/2603.07888.pdf)  
**作者**：Minkyu Kim, Sangheon Lee, Dongmin Park  

**一句话要点**：提出VLM-SubtleBench以评估视觉语言模型在细微比较推理上的性能差距

**关键词**：视觉语言模型, 细微比较推理, 基准评估, 多领域图像, 性能差距分析

## 3 点简述
- 现有视觉语言模型基准主要关注图像间显著差异，忽略细微比较推理需求
- 新基准涵盖十种差异类型，跨工业、航拍和医疗等多领域图像数据集
- 评估显示模型与人类性能存在系统性差距，尤其在特定差异类型和领域

## 摘要（原文）

> The ability to distinguish subtle differences between visually similar images is essential for diverse domains such as industrial anomaly detection, medical imaging, and aerial surveillance. While comparative reasoning benchmarks for vision-language models (VLMs) have recently emerged, they primarily focus on images with large, salient differences and fail to capture the nuanced reasoning required for real-world applications. In this work, we introduce VLM-SubtleBench, a benchmark designed to evaluate VLMs on subtle comparative reasoning. Our benchmark covers ten difference types - Attribute, State, Emotion, Temporal, Spatial, Existence, Quantity, Quality, Viewpoint, and Action - and curate paired question-image sets reflecting these fine-grained variations. Unlike prior benchmarks restricted to natural image datasets, our benchmark spans diverse domains, including industrial, aerial, and medical imagery. Through extensive evaluation of both proprietary and open-source VLMs, we reveal systematic gaps between model and human performance across difference types and domains, and provide controlled analyses highlighting where VLMs' reasoning sharply deteriorates. Together, our benchmark and findings establish a foundation for advancing VLMs toward human-level comparative reasoning.

