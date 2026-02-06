---
layout: default
title: Reasoning-guided Collaborative Filtering with Language Models for Explainable Recommendation
---

# Reasoning-guided Collaborative Filtering with Language Models for Explainable Recommendation
**arXiv**：[2602.05544v1](https://arxiv.org/abs/2602.05544) · [PDF](https://arxiv.org/pdf/2602.05544.pdf)  
**作者**：Fahad Anwaar, Adil Mehmood Khan, Muhammad Khalid, Usman Zia, Kezhi Wang  

**一句话要点**：提出RGCF-XRec框架，通过推理引导的协同过滤知识增强语言模型，实现一步式可解释序列推荐。

**关键词**：可解释推荐, 协同过滤, 语言模型, 序列推荐, 推理引导, 统一表示学习

## 3 点简述
- 核心问题：现有方法忽视协同信号或将推荐与解释分离，导致内存开销和性能限制。
- 方法要点：引入推理引导的协同过滤知识，结合高效评分机制和统一表示学习网络，优化解释质量。
- 实验或效果：在Amazon数据集上提升HR@10和ROUGE-L指标，减少冷启动差距，并实现训练效率。

## 摘要（原文）

> Large Language Models (LLMs) exhibit potential for explainable recommendation systems but overlook collaborative signals, while prevailing methods treat recommendation and explanation as separate tasks, resulting in a memory footprint. We present RGCF-XRec, a hybrid framework that introduces reasoning-guided collaborative filtering (CF) knowledge into a language model to deliver explainable sequential recommendations in a single step. Theoretical grounding and empirical findings reveal that RGCF-XRec offers three key merits over leading CF-aware LLM-based methods: (1) reasoning-guided augmentation of CF knowledge through contextual prompting to discover latent preferences and interpretable reasoning paths; (2) an efficient scoring mechanism based on four dimensions: coherence, completeness, relevance, and consistency to mitigate noisy CF reasoning traces and retain high-quality explanations; (3) a unified representation learning network that encodes collaborative and semantic signals, enabling a structured prompt to condition the LLM for explainable sequential recommendation. RGCF-XRec demonstrates consistent improvements across Amazon datasets, Sports, Toys, and Beauty, comprising 642,503 user-item interactions. It improves HR@10 by 7.38\% in Sports and 4.59\% in Toys, along with ROUGE-L by 8.02\% and 3.49\%, respectively. It reduces the cold warm performance gap, achieving overall gains of 14.5\% in cold-start and 11.9\% in warm start scenarios, and enhances zero-shot HR@5 by 18.54\% in Beauty and 23.16\% in Toys, highlighting effective generalization and robustness. Moreover, RGCF-XRec achieves training efficiency with a lightweight LLaMA 3.2-3B backbone, ensuring scalability for real-world applications.

