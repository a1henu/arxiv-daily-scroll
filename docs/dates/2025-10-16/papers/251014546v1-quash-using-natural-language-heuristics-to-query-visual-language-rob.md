---
layout: default
title: QuASH: Using Natural-Language Heuristics to Query Visual-Language Robotic Maps
---

# QuASH: Using Natural-Language Heuristics to Query Visual-Language Robotic Maps
**arXiv**：[2510.14546v1](https://arxiv.org/abs/2510.14546) · [PDF](https://arxiv.org/pdf/2510.14546.pdf)  
**作者**：Matti Pekkanen, Francesco Verdoja, Ville Kyrki  

**一句话要点**：提出QuASH方法，利用自然语言启发式查询视觉语言机器人地图。

**关键词**：视觉语言模型, 机器人地图, 自然语言查询, 嵌入空间, 分类器训练, 开放词汇理解

## 3 点简述
- 核心问题：机器人需确定环境哪些部分与查询相关，以执行任务。
- 方法要点：利用查询的同义词和反义词，训练分类器划分环境匹配区域。
- 实验效果：在多种地图和图像基准上评估，提升查询能力且方法通用。

## 摘要（原文）

> Embeddings from Visual-Language Models are increasingly utilized to represent
> semantics in robotic maps, offering an open-vocabulary scene understanding that
> surpasses traditional, limited labels. Embeddings enable on-demand querying by
> comparing embedded user text prompts to map embeddings via a similarity metric.
> The key challenge in performing the task indicated in a query is that the robot
> must determine the parts of the environment relevant to the query.
>   This paper proposes a solution to this challenge. We leverage
> natural-language synonyms and antonyms associated with the query within the
> embedding space, applying heuristics to estimate the language space relevant to
> the query, and use that to train a classifier to partition the environment into
> matches and non-matches. We evaluate our method through extensive experiments,
> querying both maps and standard image benchmarks. The results demonstrate
> increased queryability of maps and images. Our querying technique is agnostic
> to the representation and encoder used, and requires limited training.

