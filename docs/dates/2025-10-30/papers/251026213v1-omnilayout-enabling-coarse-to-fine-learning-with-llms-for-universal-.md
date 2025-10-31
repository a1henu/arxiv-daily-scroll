---
layout: default
title: OmniLayout: Enabling Coarse-to-Fine Learning with LLMs for Universal Document Layout Generation
---

# OmniLayout: Enabling Coarse-to-Fine Learning with LLMs for Universal Document Layout Generation
**arXiv**：[2510.26213v1](https://arxiv.org/abs/2510.26213) · [PDF](https://arxiv.org/pdf/2510.26213.pdf)  
**作者**：Hengrui Kang, Zhuangcheng Gu, Zhiyuan Zhao, Zichen Wen, Bin Wang, Weijia Li, Conghui He  

**一句话要点**：提出OmniLayout-LLM与OmniLayout-1M数据集，以解决通用文档布局生成中的多样性与连贯性问题。

**关键词**：文档布局生成, 粗到细学习, 大型语言模型, 数据集构建, 多领域评估

## 3 点简述
- 核心问题：文档布局生成领域缺乏多样布局数据，现有方法在复杂领域和长序列布局中表现不佳。
- 方法要点：构建百万级OmniLayout-1M数据集，并设计0.5B参数模型采用粗到细两阶段学习范式。
- 实验或效果：在M$^{6}$Doc数据集上超越现有布局生成专家和通用LLMs，表现强劲。

## 摘要（原文）

> Document AI has advanced rapidly and is attracting increasing attention. Yet,
> while most efforts have focused on document layout analysis (DLA), its
> generative counterpart, document layout generation, remains underexplored. A
> major obstacle lies in the scarcity of diverse layouts: academic papers with
> Manhattan-style structures dominate existing studies, while open-world genres
> such as newspapers and magazines remain severely underrepresented. To address
> this gap, we curate OmniLayout-1M, the first million-scale dataset of diverse
> document layouts, covering six common document types and comprising
> contemporary layouts collected from multiple sources. Moreover, since existing
> methods struggle in complex domains and often fail to arrange long sequences
> coherently, we introduce OmniLayout-LLM, a 0.5B model with designed two-stage
> Coarse-to-Fine learning paradigm: 1) learning universal layout principles from
> OmniLayout-1M with coarse category definitions, and 2) transferring the
> knowledge to a specific domain with fine-grained annotations. Extensive
> experiments demonstrate that our approach achieves strong performance on
> multiple domains in M$^{6}$Doc dataset, substantially surpassing both existing
> layout generation experts and several latest general-purpose LLMs. Our code,
> models, and dataset will be publicly released.

