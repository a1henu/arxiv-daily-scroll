---
layout: default
title: Anytime Safe PAC Efficient Reasoning
---

# Anytime Safe PAC Efficient Reasoning
**arXiv**：[2601.22446v1](https://arxiv.org/abs/2601.22446) · [PDF](https://arxiv.org/pdf/2601.22446.pdf)  
**作者**：Chengyao Yu, Hao Zeng, Youxin Zhu, Jianguo Huang, Huajun Zeng, Bingyi Jing  

**一句话要点**：提出B-PAC推理方法，实现在线环境下安全高效的大模型推理

**关键词**：在线推理, 选择性思考, 性能损失控制, 大推理模型, 逆倾向评分

## 3 点简述
- 核心问题：大推理模型计算成本高，现有选择性策略在非平稳在线场景中易产生不可控误差
- 方法要点：基于逆倾向评分估计器构建测试超鞅，动态调整路由阈值以控制性能损失
- 实验或效果：实验显示计算开销显著降低，思考模型使用减少达81.01%，性能损失控制在用户指定水平

## 摘要（原文）

> Large Reasoning Models (LRMs) have demonstrated remarkable performance on complex tasks but suffer from high computational costs and latency. While selective thinking strategies improve efficiency by routing easy queries to non-thinking models, existing approaches often incur uncontrollable errors, especially in online settings where the performance loss of a non-thinking model is only partially observed and data are non-stationary. To address this, we propose Betting Probably Approximately Correct (B-PAC) reasoning, a principled method that enables anytime safe and efficient online reasoning under partial feedback. Specifically, we utilize inverse propensity scoring estimators to construct test supermartingales for candidate thresholds, and then dynamically adjust the routing threshold based on the accumulated statistical evidence of safety. Theoretically, we establish the anytime-valid performance loss control and the efficiency of B-PAC reasoning. Extensive experiments demonstrate that B-PAC reasoning significantly reduces computational overhead, decreasing thinking model usage by up to 81.01\%, while controlling the performance loss below the user-specified level.

