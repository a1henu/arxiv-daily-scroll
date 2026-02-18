---
layout: default
title: Scenario Approach with Post-Design Certification of User-Specified Properties
---

# Scenario Approach with Post-Design Certification of User-Specified Properties
**arXiv**：[2602.15568v1](https://arxiv.org/abs/2602.15568) · [PDF](https://arxiv.org/pdf/2602.15568.pdf)  
**作者**：Algo Carè, Marco C. Campi, Simone Garatti  

**一句话要点**：提出后设计认证框架以保障用户指定属性，扩展场景方法的应用范围。

**关键词**：场景方法, 后设计认证, 数据驱动设计, 风险边界, H2控制, 极点配置

## 3 点简述
- 核心问题：如何在数据驱动设计中确保设计后未考虑的额外属性可靠性。
- 方法要点：引入两级适当性框架，提供无分布风险上界，无需额外测试数据。
- 实验或效果：在H2和极点配置问题中验证方法，并推断性能指标分布知识。

## 摘要（原文）

> The scenario approach is an established data-driven design framework that comes equipped with a powerful theory linking design complexity to generalization properties. In this approach, data are simultaneously used both for design and for certifying the design's reliability, without resorting to a separate test dataset. This paper takes a step further by guaranteeing additional properties, useful in post-design usage but not considered during the design phase. To this end, we introduce a two-level framework of appropriateness: baseline appropriateness, which guides the design process, and post-design appropriateness, which serves as a criterion for a posteriori evaluation. We provide distribution-free upper bounds on the risk of failing to meet the post-design appropriateness; these bounds are computable without using any additional test data. Under additional assumptions, lower bounds are also derived. As part of an effort to demonstrate the usefulness of the proposed methodology, the paper presents two practical examples in H2 and pole-placement problems. Moreover, a method is provided to infer comprehensive distributional knowledge of relevant performance indexes from the available dataset.

