---
layout: default
title: Taipan: A Query-free Transfer-based Multiple Sensitive Attribute Inference Attack Solely from Publicly Released Graphs
---

# Taipan: A Query-free Transfer-based Multiple Sensitive Attribute Inference Attack Solely from Publicly Released Graphs
**arXiv**：[2602.06700v1](https://arxiv.org/abs/2602.06700) · [PDF](https://arxiv.org/pdf/2602.06700.pdf)  
**作者**：Ying Song, Balaji Palanisamy  

**一句话要点**：提出Taipan框架以解决仅从公开图数据中推断多个敏感属性的查询自由攻击问题

**关键词**：图属性推断攻击, 查询自由攻击, 多敏感属性推断, 分层知识路由, 攻击原型精炼, 图隐私保护

## 3 点简述
- 核心问题：现有图属性推断攻击依赖模型查询，不适用于实际场景，且忽视仅从公开图数据中泄露多个敏感属性的内在风险
- 方法要点：Taipan采用分层攻击知识路由捕获属性间复杂关联，并通过提示引导攻击原型精炼减轻负迁移和性能下降
- 实验或效果：在多种真实图数据集上，Taipan在相同分布、异构相似分布和分布外设置中均表现优异，且在差分隐私下仍有效

## 摘要（原文）

> Graph-structured data underpin a wide spectrum of modern applications. However, complex graph topologies and homophilic patterns can facilitate attribute inference attacks (AIAs) by enabling sensitive information leakage to propagate across local neighborhoods. Existing AIAs predominantly assume that adversaries can probe sensitive attributes through repeated model queries. Such assumptions are often impractical in real-world settings due to stringent data protection regulations, prohibitive query budgets, and heightened detection risks, especially when inferring multiple sensitive attributes. More critically, this model-centric perspective obscures a pervasive blind spot: \textbf{intrinsic multiple sensitive information leakage arising solely from publicly released graphs.} To exploit this unexplored vulnerability, we introduce a new attack paradigm and propose \textbf{Taipan, the first query-free transfer-based attack framework for multiple sensitive attribute inference attacks on graphs (G-MSAIAs).} Taipan integrates \emph{Hierarchical Attack Knowledge Routing} to capture intricate inter-attribute correlations, and \emph{Prompt-guided Attack Prototype Refinement} to mitigate negative transfer and performance degradation. We further present a systematic evaluation framework tailored to G-MSAIAs. Extensive experiments on diverse real-world graph datasets demonstrate that Taipan consistently achieves strong attack performance across same-distribution settings and heterogeneous similar- and out-of-distribution settings with mismatched feature dimensionalities, and remains effective even under rigorous differential privacy guarantees. Our findings underscore the urgent need for more robust multi-attribute privacy-preserving graph publishing methods and data-sharing practices.

