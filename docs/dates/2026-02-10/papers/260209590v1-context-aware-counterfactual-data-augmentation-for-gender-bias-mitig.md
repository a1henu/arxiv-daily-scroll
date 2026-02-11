---
layout: default
title: Context-Aware Counterfactual Data Augmentation for Gender Bias Mitigation in Language Models
---

# Context-Aware Counterfactual Data Augmentation for Gender Bias Mitigation in Language Models
**arXiv**：[2602.09590v1](https://arxiv.org/abs/2602.09590) · [PDF](https://arxiv.org/pdf/2602.09590.pdf)  
**作者**：Shweta Parihar, Liu Guangliang, Natalie Parde, Lu Cheng  

**一句话要点**：提出Context-CDA方法，通过增强上下文和不确定性过滤，在微调语言模型中缓解性别偏见而不损害语言建模能力。

**关键词**：反事实数据增强, 性别偏见缓解, 语言模型微调, 上下文增强, 不确定性过滤, 社会偏见分析

## 3 点简述
- 核心问题：传统反事实数据增强在缓解偏见时可能导致语言建模能力下降，因生成数据与真实分布不符或忽略社会上下文。
- 方法要点：使用大语言模型增强反事实数据的多样性和上下文相关性，并通过不确定性过滤提升微调语料质量。
- 实验或效果：在性别偏见基准测试中，Context-CDA有效缓解偏见，同时保持语言建模性能，并分析生成概率分布以洞察社会偏见。

## 摘要（原文）

> A challenge in mitigating social bias in fine-tuned language models (LMs) is the potential reduction in language modeling capability, which can harm downstream performance. Counterfactual data augmentation (CDA), a widely used method for fine-tuning, highlights this issue by generating synthetic data that may align poorly with real-world distributions or creating overly simplistic counterfactuals that ignore the social context of altered sensitive attributes (e.g., gender) in the pretraining corpus. To address these limitations, we propose a simple yet effective context-augmented CDA method, Context-CDA, which uses large LMs to enhance the diversity and contextual relevance of the debiasing corpus. By minimizing discrepancies between the debiasing corpus and pretraining data through augmented context, this approach ensures better alignment, enhancing language modeling capability. We then employ uncertainty-based filtering to exclude generated counterfactuals considered low-quality by the target smaller LMs (i.e., LMs to be debiased), further improving the fine-tuning corpus quality. Experimental results on gender bias benchmarks demonstrate that Context-CDA effectively mitigates bias without sacrificing language modeling performance while offering insights into social biases by analyzing distribution shifts in next-token generation probabilities.

