---
layout: default
title: Deep Learning for Perishable Inventory Systems with Human Knowledge
---

# Deep Learning for Perishable Inventory Systems with Human Knowledge
**arXiv**：[2601.15589v1](https://arxiv.org/abs/2601.15589) · [PDF](https://arxiv.org/pdf/2601.15589.pdf)  
**作者**：Xuan Liao, Zhenkang Peng, Ying Rong  

**一句话要点**：提出结合人类知识的深度学习策略，以优化未知需求和随机提前期的易腐品库存管理。

**关键词**：易腐品库存管理, 深度学习策略, 端到端学习, 结构引导方法, 边际成本核算, 随机提前期

## 3 点简述
- 研究易腐品库存系统，需求和提前期分布未知，基于有限历史数据、协变量和系统状态进行决策。
- 采用边际成本核算方案，开发端到端深度学习策略，包括黑盒和结构引导两种变体，后者嵌入投影库存水平策略。
- 实验表明结构引导方法优于黑盒，并通过提升技术进一步优化，验证了结合人类知识能提高学习效率和鲁棒性。

## 摘要（原文）

> Managing perishable products with limited lifetimes is a fundamental challenge in inventory management, as poor ordering decisions can quickly lead to stockouts or excessive waste. We study a perishable inventory system with random lead times in which both the demand process and the lead time distribution are unknown. We consider a practical setting where orders are placed using limited historical data together with observed covariates and current system states. To improve learning efficiency under limited data, we adopt a marginal cost accounting scheme that assigns each order a single lifetime cost and yields a unified loss function for end-to-end learning. This enables training a deep learning-based policy that maps observed covariates and system states directly to order quantities. We develop two end-to-end variants: a purely black-box approach that outputs order quantities directly (E2E-BB), and a structure-guided approach that embeds the projected inventory level (PIL) policy, capturing inventory effects through explicit computation rather than additional learning (E2E-PIL). We further show that the objective induced by E2E-PIL is homogeneous of degree one, enabling a boosting technique from operational data analytics (ODA) that yields an enhanced policy (E2E-BPIL). Experiments on synthetic and real data establish a robust performance ordering: E2E-BB is dominated by E2E-PIL, which is further improved by E2E-BPIL. Using an excess-risk decomposition, we show that embedding heuristic policy structure reduces effective model complexity and improves learning efficiency with only a modest loss of flexibility. More broadly, our results suggest that deep learning-based decision tools are more effective and robust when guided by human knowledge, highlighting the value of integrating advanced analytics with inventory theory.

