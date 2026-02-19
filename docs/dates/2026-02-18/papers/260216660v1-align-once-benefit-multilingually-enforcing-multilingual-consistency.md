---
layout: default
title: Align Once, Benefit Multilingually: Enforcing Multilingual Consistency for LLM Safety Alignment
---

# Align Once, Benefit Multilingually: Enforcing Multilingual Consistency for LLM Safety Alignment
**arXiv**：[2602.16660v1](https://arxiv.org/abs/2602.16660) · [PDF](https://arxiv.org/pdf/2602.16660.pdf)  
**作者**：Yuyan Bu, Xiaohao Liu, ZhaoXing Ren, Yaodong Yang, Juntao Dai  

**一句话要点**：提出多语言一致性损失以在有限监督下提升大语言模型的多语言安全对齐

**关键词**：多语言安全对齐, 表示向量共线性, 有限监督学习, 大语言模型对齐, 跨语言泛化

## 3 点简述
- 核心问题：多语言安全对齐资源消耗大，扩展性受限
- 方法要点：引入可插拔的多语言一致性损失，增强多语言表示向量共线性
- 实验或效果：验证方法在不同模型和任务中有效，提升安全对齐且不影响通用能力

## 摘要（原文）

> The widespread deployment of large language models (LLMs) across linguistic communities necessitates reliable multilingual safety alignment. However, recent efforts to extend alignment to other languages often require substantial resources, either through large-scale, high-quality supervision in the target language or through pairwise alignment with high-resource languages, which limits scalability. In this work, we propose a resource-efficient method for improving multilingual safety alignment. We introduce a plug-and-play Multi-Lingual Consistency (MLC) loss that can be integrated into existing monolingual alignment pipelines. By improving collinearity between multilingual representation vectors, our method encourages directional consistency at the multilingual semantic level in a single update. This allows simultaneous alignment across multiple languages using only multilingual prompt variants without requiring additional response-level supervision in low-resource languages. We validate the proposed method across different model architectures and alignment paradigms, and demonstrate its effectiveness in enhancing multilingual safety with limited impact on general model utility. Further evaluation across languages and tasks indicates improved cross-lingual generalization, suggesting the proposed approach as a practical solution for multilingual consistency alignment under limited supervision.

