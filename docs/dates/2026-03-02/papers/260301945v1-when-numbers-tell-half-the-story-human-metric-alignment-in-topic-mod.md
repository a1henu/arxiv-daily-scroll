---
layout: default
title: When Numbers Tell Half the Story: Human-Metric Alignment in Topic Model Evaluation
---

# When Numbers Tell Half the Story: Human-Metric Alignment in Topic Model Evaluation
**arXiv**：[2603.01945v1](https://arxiv.org/abs/2603.01945) · [PDF](https://arxiv.org/pdf/2603.01945.pdf)  
**作者**：Thibault Prouteau, Francis Lareau, Nicolas Dugué, Jean-Charles Lamirel, Christophe Malaterre  

**一句话要点**：提出Topic Word Mixing任务以评估主题模型在专业领域的人类感知区分度

**关键词**：主题模型评估, 人类评估任务, 专业领域语料, Topic Word Mixing, 自动化指标对齐

## 3 点简述
- 核心问题：主题模型评估中自动化指标与人类判断不一致，尤其在专业领域。
- 方法要点：引入Topic Word Mixing任务，通过混合主题词集测试人类区分能力，补充现有评估方法。
- 实验或效果：在哲学科学语料上比较六种模型，发现自动化指标与人类评估存在差异，TWM能捕捉人类感知的区分度。

## 摘要（原文）

> Topic models uncover latent thematic structures in text corpora, yet evaluating their quality remains challenging, particularly in specialized domains. Existing methods often rely on automated metrics like topic coherence and diversity, which may not fully align with human judgment. Human evaluation tasks, such as word intrusion, provide valuable insights but are costly and primarily validated on general-domain corpora. This paper introduces Topic Word Mixing (TWM), a novel human evaluation task assessing inter-topic distinctness by testing whether annotators can distinguish between word sets from single or mixed topics. TWM complements word intrusion's focus on intra-topic coherence and provides a human-grounded counterpart to diversity metrics. We evaluate six topic models - both statistical and embedding-based (LDA, NMF, Top2Vec, BERTopic, CFMF, CFMF-emb) - comparing automated metrics with human evaluation methods based on nearly 4,000 annotations from a domain-specific corpus of philosophy of science publications. Our findings reveal that word intrusion and coherence metrics do not always align, particularly in specialized domains, and that TWM captures human-perceived distinctness while appearing to align with diversity metrics. We release the annotated dataset and task generation code. This work highlights the need for evaluation frameworks bridging automated and human assessments, particularly for domain-specific corpora.

