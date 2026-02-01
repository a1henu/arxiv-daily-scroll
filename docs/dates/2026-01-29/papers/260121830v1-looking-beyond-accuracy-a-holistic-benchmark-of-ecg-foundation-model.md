---
layout: default
title: Looking Beyond Accuracy: A Holistic Benchmark of ECG Foundation Models
---

# Looking Beyond Accuracy: A Holistic Benchmark of ECG Foundation Models
**arXiv**：[2601.21830v1](https://arxiv.org/abs/2601.21830) · [PDF](https://arxiv.org/pdf/2601.21830.pdf)  
**作者**：Francesca Filice, Edoardo De Rose, Simone Bartucci, Francesco Calimeri, Simona Perri  

**一句话要点**：提出基于SHAP和UMAT的基准框架，全面评估心电图基础模型的表示能力与泛化性。

**关键词**：心电图基础模型, 基准评估, 表示学习, SHAP分析, UMAT可视化, 医疗AI

## 3 点简述
- 核心问题：现有基准主要关注下游性能，缺乏对心电图基础模型嵌入表示泛化性的深入评估。
- 方法要点：结合性能评估与表示层分析，利用SHAP和UMAT技术构建综合基准框架。
- 实验或效果：在跨大陆数据集和数据稀缺场景下评估多个模型，揭示嵌入模式与泛化性。

## 摘要（原文）

> The electrocardiogram (ECG) is a cost-effective, highly accessible and widely employed diagnostic tool. With the advent of Foundation Models (FMs), the field of AI-assisted ECG interpretation has begun to evolve, as they enable model reuse across different tasks by relying on embeddings. However, to responsibly employ FMs, it is crucial to rigorously assess to which extent the embeddings they produce are generalizable, particularly in error-sensitive domains such as healthcare. Although prior works have already addressed the problem of benchmarking ECG-expert FMs, they focus predominantly on the evaluation of downstream performance. To fill this gap, this study aims to find an in-depth, comprehensive benchmarking framework for FMs, with a specific focus on ECG-expert ones. To this aim, we introduce a benchmark methodology that complements performance-based evaluation with representation-level analysis, leveraging SHAP and UMAP techniques. Furthermore, we rely on the methodology for carrying out an extensive evaluation of several ECG-expert FMs pretrained via state-of-the-art techniques over different cross-continental datasets and data availability settings; this includes ones featuring data scarcity, a fairly common situation in real-world medical scenarios. Experimental results show that our benchmarking protocol provides a rich insight of ECG-expert FMs' embedded patterns, enabling a deeper understanding of their representational structure and generalizability.

