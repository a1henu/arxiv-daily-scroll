---
layout: default
title: Adaptive Quality-Diversity Trade-offs for Large-Scale Batch Recommendation
---

# Adaptive Quality-Diversity Trade-offs for Large-Scale Batch Recommendation
**arXiv**：[2602.02024v1](https://arxiv.org/abs/2602.02024) · [PDF](https://arxiv.org/pdf/2602.02024.pdf)  
**作者**：Clémence Réda, Tomas Rigaux, Hiba Bederina, Koh Takeuchi, Hisashi Kashima, Jill-Jênn Vie  

**一句话要点**：提出B-DivRec算法以解决大规模批量推荐中的质量-多样性权衡问题

**关键词**：批量推荐, 质量-多样性权衡, 行列式点过程, 自适应算法, 大规模推荐系统

## 3 点简述
- 核心问题：如何在推荐系统中平衡项目相关性与多样性，以提升用户参与度并降低流失风险
- 方法要点：结合行列式点过程和模糊去冗余程序，自适应调整多样性程度，优化质量-多样性权衡
- 实验或效果：在电影推荐和药物重定位数据集上验证了算法的性能和适应性

## 摘要（原文）

> A core research question in recommender systems is to propose batches of highly relevant and diverse items, that is, items personalized to the user's preferences, but which also might get the user out of their comfort zone. This diversity might induce properties of serendipidity and novelty which might increase user engagement or revenue. However, many real-life problems arise in that case: e.g., avoiding to recommend distinct but too similar items to reduce the churn risk, and computational cost for large item libraries, up to millions of items. First, we consider the case when the user feedback model is perfectly observed and known in advance, and introduce an efficient algorithm called B-DivRec combining determinantal point processes and a fuzzy denuding procedure to adjust the degree of item diversity. This helps enforcing a quality-diversity trade-off throughout the user history. Second, we propose an approach to adaptively tailor the quality-diversity trade-off to the user, so that diversity in recommendations can be enhanced if it leads to positive feedback, and vice-versa. Finally, we illustrate the performance and versatility of B-DivRec in the two settings on synthetic and real-life data sets on movie recommendation and drug repurposing.

