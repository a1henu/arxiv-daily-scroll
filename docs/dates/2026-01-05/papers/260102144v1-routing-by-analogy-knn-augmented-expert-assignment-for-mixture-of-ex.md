---
layout: default
title: Routing by Analogy: kNN-Augmented Expert Assignment for Mixture-of-Experts
---

# Routing by Analogy: kNN-Augmented Expert Assignment for Mixture-of-Experts
**arXiv**：[2601.02144v1](https://arxiv.org/abs/2601.02144) · [PDF](https://arxiv.org/pdf/2601.02144.pdf)  
**作者**：Boxuan Lyu, Soichiro Murakami, Hidetaka Kamigaito, Peinan Zhang  

**一句话要点**：提出kNN-MoE框架，通过检索增强路由解决MoE模型在分布偏移下的脆弱性问题。

**关键词**：混合专家模型, 检索增强路由, 分布偏移, k近邻, 语言模型扩展

## 3 点简述
- 核心问题：MoE架构中冻结的路由器在分布偏移时决策脆弱，影响模型性能。
- 方法要点：引入检索增强路由，基于相似历史案例重用最优专家分配，并利用邻居相似度作为置信度混合系数。
- 实验或效果：kNN-MoE在实验中优于零样本基线，可与计算昂贵的监督微调相媲美。

## 摘要（原文）

> Mixture-of-Experts (MoE) architectures scale large language models efficiently by employing a parametric "router" to dispatch tokens to a sparse subset of experts. Typically, this router is trained once and then frozen, rendering routing decisions brittle under distribution shifts. We address this limitation by introducing kNN-MoE, a retrieval-augmented routing framework that reuses optimal expert assignments from a memory of similar past cases. This memory is constructed offline by directly optimizing token-wise routing logits to maximize the likelihood on a reference set. Crucially, we use the aggregate similarity of retrieved neighbors as a confidence-driven mixing coefficient, thus allowing the method to fall back to the frozen router when no relevant cases are found. Experiments show kNN-MoE outperforms zero-shot baselines and rivals computationally expensive supervised fine-tuning.

