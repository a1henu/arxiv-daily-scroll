---
layout: default
title: CREST: Universal Safety Guardrails Through Cluster-Guided Cross-Lingual Transfer
---

# CREST: Universal Safety Guardrails Through Cluster-Guided Cross-Lingual Transfer
**arXiv**：[2512.02711v1](https://arxiv.org/abs/2512.02711) · [PDF](https://arxiv.org/pdf/2512.02711.pdf)  
**作者**：Lavish Bansal, Naman Mishra  

**一句话要点**：提出CREST模型，通过聚类引导的跨语言迁移实现多语言安全护栏，支持100种语言。

**关键词**：多语言安全分类, 跨语言迁移, 参数高效模型, 低资源语言, 安全护栏, 聚类引导

## 3 点简述
- 问题：现有安全护栏主要针对高资源语言，低资源语言安全防护不足。
- 方法：基于13种高资源语言训练，利用聚类实现跨语言迁移至100种语言，参数高效。
- 效果：在六个安全基准上超越同类规模模型，与更大参数模型竞争。

## 摘要（原文）

> Ensuring content safety in large language models (LLMs) is essential for their deployment in real-world applications. However, existing safety guardrails are predominantly tailored for high-resource languages, leaving a significant portion of the world's population underrepresented who communicate in low-resource languages. To address this, we introduce CREST (CRoss-lingual Efficient Safety Transfer), a parameter-efficient multilingual safety classification model that supports 100 languages with only 0.5B parameters. By training on a strategically chosen subset of only 13 high-resource languages, our model utilizes cluster-based cross-lingual transfer from a few to 100 languages, enabling effective generalization to both unseen high-resource and low-resource languages. This approach addresses the challenge of limited training data in low-resource settings. We conduct comprehensive evaluations across six safety benchmarks to demonstrate that CREST outperforms existing state-of-the-art guardrails of comparable scale and achieves competitive results against models with significantly larger parameter counts (2.5B parameters and above). Our findings highlight the limitations of language-specific guardrails and underscore the importance of developing universal, language-agnostic safety systems that can scale effectively to serve global populations.

