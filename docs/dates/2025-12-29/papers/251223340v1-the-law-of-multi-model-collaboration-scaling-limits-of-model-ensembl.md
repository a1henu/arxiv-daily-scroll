---
layout: default
title: The Law of Multi-Model Collaboration: Scaling Limits of Model Ensembling for Large Language Models
---

# The Law of Multi-Model Collaboration: Scaling Limits of Model Ensembling for Large Language Models
**arXiv**：[2512.23340v1](https://arxiv.org/abs/2512.23340) · [PDF](https://arxiv.org/pdf/2512.23340.pdf)  
**作者**：Dakuan Lu, Jiaqi Zhang, Cheng Yuan, Jiawei Shao, Chi Zhang, Xuelong Li  

**一句话要点**：提出多模型协作定律以预测大语言模型集成性能的缩放极限

**关键词**：大语言模型, 模型集成, 缩放定律, 多模型协作, 性能预测, 模型多样性

## 3 点简述
- 核心问题：缺乏多模型协作性能缩放的理论框架，单模型能力有限。
- 方法要点：基于参数预算，采用方法无关公式和理想化集成预言机量化协作上限。
- 实验或效果：多模型系统遵循幂律缩放，异质模型家族集成性能更优，模型多样性驱动增益。

## 摘要（原文）

> Recent advances in large language models (LLMs) have been largely driven by scaling laws for individual models, which predict performance improvements as model parameters and data volume increase. However, the capabilities of any single LLM are inherently bounded. One solution originates from intricate interactions among multiple LLMs, rendering their collective performance surpasses that of any constituent model. Despite the rapid proliferation of multi-model integration techniques such as model routing and post-hoc ensembling, a unifying theoretical framework of performance scaling for multi-model collaboration remains absent. In this work, we propose the Law of Multi-model Collaboration, a scaling law that predicts the performance limits of LLM ensembles based on their aggregated parameter budget. To quantify the intrinsic upper bound of multi-model collaboration, we adopt a method-agnostic formulation and assume an idealized integration oracle where the total cross-entropy loss of each sample is determined by the minimum loss of any model in the model pool. Experimental results reveal that multi-model systems follow a power-law scaling with respect to the total parameter count, exhibiting a more significant improvement trend and a lower theoretical loss floor compared to single model scaling. Moreover, ensembles of heterogeneous model families achieve better performance scaling than those formed within a single model family, indicating that model diversity is a primary driver of collaboration gains. These findings suggest that model collaboration represents a critical axis for extending the intelligence frontier of LLMs.

