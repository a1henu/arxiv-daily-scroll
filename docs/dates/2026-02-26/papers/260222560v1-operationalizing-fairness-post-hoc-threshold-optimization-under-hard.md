---
layout: default
title: Operationalizing Fairness: Post-Hoc Threshold Optimization Under Hard Resource Limits
---

# Operationalizing Fairness: Post-Hoc Threshold Optimization Under Hard Resource Limits
**arXiv**：[2602.22560v1](https://arxiv.org/abs/2602.22560) · [PDF](https://arxiv.org/pdf/2602.22560.pdf)  
**作者**：Moirangthem Tiken Singh, Amit Kalita, Sapam Jitu Singh  

**一句话要点**：提出后处理阈值优化框架，在严格资源限制下平衡安全、效率和公平性。

**关键词**：公平机器学习, 阈值优化, 资源约束, 后处理框架, 伦理权衡

## 3 点简述
- 核心问题：现有公平性干预假设资源无约束，违反反歧视法规且忽视容量限制。
- 方法要点：引入模型无关的全局阈值优化，结合参数化伦理损失函数和有限决策规则。
- 实验或效果：在25%容量限制下保持高风险识别，而标准启发式方法效用接近零。

## 摘要（原文）

> The deployment of machine learning in high-stakes domains requires a balance between predictive safety and algorithmic fairness. However, existing fairness interventions often as- sume unconstrained resources and employ group-specific decision thresholds that violate anti- discrimination regulations. We introduce a post-hoc, model-agnostic threshold optimization framework that jointly balances safety, efficiency, and equity under strict and hard capacity constraints. To ensure legal compliance, the framework enforces a single, global decision thresh- old. We formulated a parameterized ethical loss function coupled with a bounded decision rule that mathematically prevents intervention volumes from exceeding the available resources. An- alytically, we prove the key properties of the deployed threshold, including local monotonicity with respect to ethical weighting and the formal identification of critical capacity regimes. We conducted extensive experimental evaluations on diverse high-stakes datasets. The principal re- sults demonstrate that capacity constraints dominate ethical priorities; the strict resource limit determines the final deployed threshold in over 80% of the tested configurations. Furthermore, under a restrictive 25% capacity limit, the proposed framework successfully maintains high risk identification (recall ranging from 0.409 to 0.702), whereas standard unconstrained fairness heuristics collapse to a near-zero utility. We conclude that theoretical fairness objectives must be explicitly subordinated to operational capacity limits to remain in deployment. By decou- pling predictive scoring from policy evaluation and strictly bounding intervention rates, this framework provides a practical and legally compliant mechanism for stakeholders to navigate unavoidable ethical trade-offs in resource-constrained environments.

