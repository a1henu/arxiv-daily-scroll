---
layout: default
title: Towards Understanding What State Space Models Learn About Code
---

# Towards Understanding What State Space Models Learn About Code
**arXiv**：[2602.06774v1](https://arxiv.org/abs/2602.06774) · [PDF](https://arxiv.org/pdf/2602.06774.pdf)  
**作者**：Jiali Wu, Abhinav Anand, Shweta Verma, Mira Mezini  

**一句话要点**：提出SSM-Interpret框架以分析状态空间模型在代码理解中的学习机制

**关键词**：状态空间模型, 代码理解, 频谱分析, 模型解释性, 微调优化

## 3 点简述
- 核心问题：状态空间模型在代码任务中的内部机制不明确，与Transformer对比不足
- 方法要点：引入频率域框架SSM-Interpret，揭示微调时的频谱偏移现象
- 实验或效果：通过架构改进显著提升SSM模型性能，验证分析有效性

## 摘要（原文）

> State Space Models (SSMs) have emerged as an efficient alternative to the transformer architecture. Recent studies show that SSMs can match or surpass Transformers on code understanding tasks, such as code retrieval, when trained under similar conditions. However, their internal mechanisms remain a black box. We present the first systematic analysis of what SSM-based code models actually learn and perform the first comparative analysis of SSM and Transformer-based code models. Our analysis reveals that SSMs outperform Transformers at capturing code syntax and semantics in pretraining but forgets certain syntactic and semantic relations during fine-tuning on task, especially when the task emphasizes short-range dependencies. To diagnose this, we introduce SSM-Interpret, a frequency-domain framework that exposes a spectral shift toward short-range dependencies during fine-tuning. Guided by these findings, we propose architectural modifications that significantly improve the performance of SSM-based code model, validating that our analysis directly enables better models.

