---
layout: default
title: Cross-Domain Fake News Detection on Unseen Domains via LLM-Based Domain-Aware User Modeling
---

# Cross-Domain Fake News Detection on Unseen Domains via LLM-Based Domain-Aware User Modeling
**arXiv**：[2602.01726v1](https://arxiv.org/abs/2602.01726) · [PDF](https://arxiv.org/pdf/2602.01726.pdf)  
**作者**：Xuankai Yang, Yan Wang, Jiajie Zhu, Pengfei Ding, Hongyang Liu, Xiuzhen Zhang, Huan Liu  

**一句话要点**：提出DAUD框架，利用LLM进行领域感知用户建模，以解决未见领域跨域假新闻检测问题。

**关键词**：跨域假新闻检测, 未见领域, 大语言模型, 领域感知建模, 用户行为表示, 知识迁移

## 3 点简述
- 核心问题：现有跨域假新闻检测方法在未见领域面临语义建模不足和标注数据稀缺的挑战。
- 方法要点：DAUD使用LLM提取新闻高级语义，建模用户单域和跨域参与行为，并融合数据驱动特征以增强表示可靠性。
- 实验或效果：在真实数据集上，DAUD在通用和未见领域设置中均优于现有基线方法。

## 摘要（原文）

> Cross-domain fake news detection (CD-FND) transfers knowledge from a source domain to a target domain and is crucial for real-world fake news mitigation. This task becomes particularly important yet more challenging when the target domain is previously unseen (e.g., the COVID-19 outbreak or the Russia-Ukraine war). However, existing CD-FND methods overlook such scenarios and consequently suffer from the following two key limitations: (1) insufficient modeling of high-level semantics in news and user engagements; and (2) scarcity of labeled data in unseen domains. Targeting these limitations, we find that large language models (LLMs) offer strong potential for CD-FND on unseen domains, yet their effective use remains non-trivial. Nevertheless, two key challenges arise: (1) how to capture high-level semantics from both news content and user engagements using LLMs; and (2) how to make LLM-generated features more reliable and transferable for CD-FND on unseen domains. To tackle these challenges, we propose DAUD, a novel LLM-Based Domain-Aware framework for fake news detection on Unseen Domains. DAUD employs LLMs to extract high-level semantics from news content. It models users' single- and cross-domain engagements to generate domain-aware behavioral representations. In addition, DAUD captures the relations between original data-driven features and LLM-derived features of news, users, and user engagements. This allows it to extract more reliable domain-shared representations that improve knowledge transfer to unseen domains. Extensive experiments on real-world datasets demonstrate that DAUD outperforms state-of-the-art baselines in both general and unseen-domain CD-FND settings.

