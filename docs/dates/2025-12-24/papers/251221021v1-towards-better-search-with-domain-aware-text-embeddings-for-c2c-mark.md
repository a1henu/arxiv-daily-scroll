---
layout: default
title: Towards Better Search with Domain-Aware Text Embeddings for C2C Marketplaces
---

# Towards Better Search with Domain-Aware Text Embeddings for C2C Marketplaces
**arXiv**：[2512.21021v1](https://arxiv.org/abs/2512.21021) · [PDF](https://arxiv.org/pdf/2512.21021.pdf)  
**作者**：Andre Rusli, Miao Cao, Shoma Ishimoto, Sho Akiyama, Max Frenzel  

**一句话要点**：提出领域感知文本嵌入方法，以提升C2C市场搜索质量

**关键词**：文本嵌入, C2C市场搜索, Matryoshka表示学习, 领域适应, 查询-标题匹配

## 3 点简述
- 针对C2C市场搜索中短查询、噪声列表和生产约束的挑战
- 采用基于购买数据的微调、角色前缀建模和Matryoshka表示学习
- 离线评估和在线A/B测试显示搜索相关性和效率显著提升

## 摘要（原文）

> Consumer-to-consumer (C2C) marketplaces pose distinct retrieval challenges: short, ambiguous queries; noisy, user-generated listings; and strict production constraints. This paper reports our experiment to build a domain-aware Japanese text-embedding approach to improve the quality of search at Mercari, Japan's largest C2C marketplace. We experimented with fine-tuning on purchase-driven query-title pairs, using role-specific prefixes to model query-item asymmetry. To meet production constraints, we apply Matryoshka Representation Learning to obtain compact, truncation-robust embeddings. Offline evaluation on historical search logs shows consistent gains over a strong generic encoder, with particularly large improvements when replacing PCA compression with Matryoshka truncation. A manual assessment further highlights better handling of proper nouns, marketplace-specific semantics, and term-importance alignment. Additionally, an initial online A/B test demonstrates statistically significant improvements in revenue per user and search-flow efficiency, with transaction frequency maintained. Results show that domain-aware embeddings improve relevance and efficiency at scale and form a practical foundation for richer LLM-era search experiences.

