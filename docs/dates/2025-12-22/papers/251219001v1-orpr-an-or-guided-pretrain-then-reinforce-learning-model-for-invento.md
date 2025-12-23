---
layout: default
title: ORPR: An OR-Guided Pretrain-then-Reinforce Learning Model for Inventory Management
---

# ORPR: An OR-Guided Pretrain-then-Reinforce Learning Model for Inventory Management
**arXiv**：[2512.19001v1](https://arxiv.org/abs/2512.19001) · [PDF](https://arxiv.org/pdf/2512.19001.pdf)  
**作者**：Lingjie Zhao, Xue Yu, Yongzhi Qi, Hao Hu, Jianshen Zhang, Yingzheng Ma, Shuyu Han, Wei Qi, Zuo-Jun Max Shen  

**一句话要点**：提出OR引导的预训练-强化学习框架以优化库存管理

**关键词**：库存管理, 运筹学引导, 预训练-强化学习, 仿真增强模型, 深度对齐机制, 供应链智能

## 3 点简述
- 核心问题：如何融合AI的适应性与OR的结构化严谨性以处理复杂库存系统。
- 方法要点：通过仿真增强OR模型生成参考决策，预训练深度学习基础模型，再以强化学习进行微调和对齐。
- 实验或效果：在京东部署中实现库存周转减少5.27天、现货率提升2.29%，持有成本降低29.95%。

## 摘要（原文）

> As the pursuit of synergy between Artificial Intelligence (AI) and Operations Research (OR) gains momentum in handling complex inventory systems, a critical challenge persists: how to effectively reconcile AI's adaptive perception with OR's structural rigor. To bridge this gap, we propose a novel OR-Guided "Pretrain-then-Reinforce" framework. To provide structured guidance, we propose a simulation-augmented OR model that generates high-quality reference decisions, implicitly capturing complex business constraints and managerial preferences. Leveraging these OR-derived decisions as foundational training labels, we design a domain-informed deep learning foundation model to establish foundational decision-making capabilities, followed by a reinforcement learning (RL) fine-tuning stage. Uniquely, we position RL as a deep alignment mechanism that enables the AI agent to internalize the optimality principles of OR, while simultaneously leveraging exploration for general policy refinement and allowing expert guidance for scenario-specific adaptation (e.g., promotional events). Validated through extensive numerical experiments and a field deployment at JD.com augmented by a Difference-in-Differences (DiD) analysis, our model significantly outperforms incumbent industrial practices, delivering real-world gains of a 5.27-day reduction in turnover and a 2.29% increase in in-stock rates, alongside a 29.95% decrease in holding costs. Contrary to the prevailing trend of brute-force model scaling, our study demonstrates that a lightweight, domain-informed model can deliver state-of-the-art performance and robust transferability when guided by structured OR logic. This approach offers a scalable and cost-effective paradigm for intelligent supply chain management, highlighting the value of deeply aligning AI with OR.

