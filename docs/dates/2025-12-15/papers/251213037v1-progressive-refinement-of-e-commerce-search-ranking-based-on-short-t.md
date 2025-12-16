---
layout: default
title: Progressive Refinement of E-commerce Search Ranking Based on Short-Term Activities of the Buyer
---

# Progressive Refinement of E-commerce Search Ranking Based on Short-Term Activities of the Buyer
**arXiv**：[2512.13037v1](https://arxiv.org/abs/2512.13037) · [PDF](https://arxiv.org/pdf/2512.13037.pdf)  
**作者**：Taoran Sheng, Sathappan Muthiah, Atiq Islam, Jinming Feng  

**一句话要点**：提出基于买家短期活动的渐进式搜索排序优化方法，以提升电商搜索结果的上下文适配性。

**关键词**：电商搜索排序, 上下文适配, 渐进式优化, 序列模型, A/B测试, 平均倒数排名

## 3 点简述
- 核心问题：电商搜索中，如何根据买家从浏览到购买的动态意图变化，实时调整搜索结果以匹配其即时需求。
- 方法要点：从基础启发式特征开始，逐步整合上下文信息和先进序列模型，构建渐进式框架来优化搜索引擎结果页的排序。
- 实验或效果：通过离线与在线A/B测试，该方法显著提升了平均倒数排名（MRR），增强了生产排序器的性能。

## 摘要（原文）

> In e-commerce shopping, aligning search results with a buyer's immediate needs and preferences presents a significant challenge, particularly in adapting search results throughout the buyer's shopping journey as they move from the initial stages of browsing to making a purchase decision or shift from one intent to another. This study presents a systematic approach to adapting e-commerce search results based on the current context. We start with basic methods and incrementally incorporate more contextual information and state-of-the-art techniques to improve the search outcomes. By applying this evolving contextual framework to items displayed on the search engine results page (SERP), we progressively align search outcomes more closely with the buyer's interests and current search intentions. Our findings demonstrate that this incremental enhancement, from simple heuristic autoregressive features to advanced sequence models, significantly improves ranker performance. The integration of contextual techniques enhances the performance of our production ranker, leading to improved search results in both offline and online A/B testing in terms of Mean Reciprocal Rank (MRR). Overall, the paper details iterative methodologies and their substantial contributions to search result contextualization on e-commerce platforms.

