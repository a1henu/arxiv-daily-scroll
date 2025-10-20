---
layout: default
title: MARIS: Marine Open-Vocabulary Instance Segmentation with Geometric Enhancement and Semantic Alignment
---

# MARIS: Marine Open-Vocabulary Instance Segmentation with Geometric Enhancement and Semantic Alignment
**arXiv**：[2510.15398v1](https://arxiv.org/abs/2510.15398) · [PDF](https://arxiv.org/pdf/2510.15398.pdf)  
**作者**：Bingyu Li, Feiyu Wang, Da Zhang, Zhiyuan Zhao, Junyu Gao, Xuelong Li  

**一句话要点**：提出MARIS框架以解决水下开放词汇实例分割中的视觉退化和语义错位问题

**关键词**：水下实例分割, 开放词汇分割, 几何先验增强, 语义对齐, 海洋视觉基准, 跨域评估

## 3 点简述
- 核心问题：水下场景中视觉退化和语义错位限制开放词汇分割性能
- 方法要点：结合几何先验增强和语义对齐注入，提升对象一致性和识别能力
- 实验或效果：在MARIS基准上优于现有基线，支持跨域和域内评估

## 摘要（原文）

> Most existing underwater instance segmentation approaches are constrained by
> close-vocabulary prediction, limiting their ability to recognize novel marine
> categories. To support evaluation, we introduce \textbf{MARIS}
> (\underline{Mar}ine Open-Vocabulary \underline{I}nstance
> \underline{S}egmentation), the first large-scale fine-grained benchmark for
> underwater Open-Vocabulary (OV) segmentation, featuring a limited set of seen
> categories and diverse unseen categories. Although OV segmentation has shown
> promise on natural images, our analysis reveals that transfer to underwater
> scenes suffers from severe visual degradation (e.g., color attenuation) and
> semantic misalignment caused by lack underwater class definitions. To address
> these issues, we propose a unified framework with two complementary components.
> The Geometric Prior Enhancement Module (\textbf{GPEM}) leverages stable
> part-level and structural cues to maintain object consistency under degraded
> visual conditions. The Semantic Alignment Injection Mechanism (\textbf{SAIM})
> enriches language embeddings with domain-specific priors, mitigating semantic
> ambiguity and improving recognition of unseen categories. Experiments show that
> our framework consistently outperforms existing OV baselines both In-Domain and
> Cross-Domain setting on MARIS, establishing a strong foundation for future
> underwater perception research.

