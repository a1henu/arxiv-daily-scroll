---
layout: default
title: Search-Based Risk Feature Discovery in Document Structure Spaces under a Constrained Budget
---

# Search-Based Risk Feature Discovery in Document Structure Spaces under a Constrained Budget
**arXiv**：[2601.21608v1](https://arxiv.org/abs/2601.21608) · [PDF](https://arxiv.org/pdf/2601.21608.pdf)  
**作者**：Saisubramaniam Gopalakrishnan, Harikrishnan P M, Dagnachew Birru  

**一句话要点**：提出基于搜索的文档结构风险特征发现方法，以在有限预算下最大化企业智能文档处理系统的故障类型多样性

**关键词**：智能文档处理, 基于搜索的软件测试, 风险特征发现, 故障多样性, 求解器互补性, 企业系统验证

## 3 点简述
- 核心问题：企业智能文档处理系统在早期验证阶段需在有限预算内发现多样故障机制，而非单一最坏情况文档
- 方法要点：将问题形式化为基于搜索的软件测试，在文档配置组合空间中生成结构风险特征以诱导真实故障
- 实验或效果：通过多策略基准测试，显示不同求解器互补，无单一策略绝对主导，联合方法能更早发现重要风险

## 摘要（原文）

> Enterprise-grade Intelligent Document Processing (IDP) systems support high-stakes workflows across finance, insurance, and healthcare. Early-phase system validation under limited budgets mandates uncovering diverse failure mechanisms, rather than identifying a single worst-case document. We formalize this challenge as a Search-Based Software Testing (SBST) problem, aiming to identify complex interactions between document variables, with the objective to maximize the number of distinct failure types discovered within a fixed evaluation budget. Our methodology operates on a combinatorial space of document configurations, rendering instances of structural \emph{risk features} to induce realistic failure conditions. We benchmark a diverse portfolio of search strategies spanning evolutionary, swarm-based, quality-diversity, learning-based, and quantum under identical budget constraints. Through configuration-level exclusivity, win-rate, and cross-temporal overlap analyses, we show that different solvers consistently uncover failure modes that remain undiscovered by specific alternatives at comparable budgets. Crucially, cross-temporal analysis reveals persistent solver-specific discoveries across all evaluated budgets, with no single strategy exhibiting absolute dominance. While the union of all solvers eventually recovers the observed failure space, reliance on any individual method systematically delays the discovery of important risks. These results demonstrate intrinsic solver complementarity and motivate portfolio-based SBST strategies for robust industrial IDP validation.

