---
layout: default
title: Generative Data Transformation: From Mixed to Unified Data
---

# Generative Data Transformation: From Mixed to Unified Data
**arXiv**：[2602.22743v1](https://arxiv.org/abs/2602.22743) · [PDF](https://arxiv.org/pdf/2602.22743.pdf)  
**作者**：Jiaqing Zhang, Mingjia Yin, Hao Wang, Yuxin Tian, Yuyang Ye, Yawen Li, Wei Guo, Yong Liu, Enhong Chen  

**一句话要点**：提出Taesar框架，通过目标对齐序列再生解决跨域推荐中的数据稀疏与负迁移问题。

**关键词**：跨域推荐, 数据稀疏, 负迁移, 对比解码, 序列再生, 数据增强

## 3 点简述
- 核心问题：跨域数据混合存在领域差距，导致负迁移和模型性能下降。
- 方法要点：采用对比解码机制，将跨域上下文自适应编码为目标域序列。
- 实验或效果：Taesar优于模型中心方法，能泛化到多种序列模型，生成丰富数据集。

## 摘要（原文）

> Recommendation model performance is intrinsically tied to the quality, volume, and relevance of their training data. To address common challenges like data sparsity and cold start, recent researchs have leveraged data from multiple auxiliary domains to enrich information within the target domain. However, inherent domain gaps can degrade the quality of mixed-domain data, leading to negative transfer and diminished model performance. Existing prevailing \emph{model-centric} paradigm -- which relies on complex, customized architectures -- struggles to capture the subtle, non-structural sequence dependencies across domains, leading to poor generalization and high demands on computational resources. To address these shortcomings, we propose \textsc{Taesar}, a \emph{data-centric} framework for \textbf{t}arget-\textbf{a}lign\textbf{e}d \textbf{s}equenti\textbf{a}l \textbf{r}egeneration, which employs a contrastive decoding mechanism to adaptively encode cross-domain context into target-domain sequences. It employs contrastive decoding to encode cross-domain context into target sequences, enabling standard models to learn intricate dependencies without complex fusion architectures. Experiments show \textsc{Taesar} outperforms model-centric solutions and generalizes to various sequential models. By generating enriched datasets, \textsc{Taesar} effectively combines the strengths of data- and model-centric paradigms. The code accompanying this paper is available at~ \textcolor{blue}{https://github.com/USTC-StarTeam/Taesar}.

