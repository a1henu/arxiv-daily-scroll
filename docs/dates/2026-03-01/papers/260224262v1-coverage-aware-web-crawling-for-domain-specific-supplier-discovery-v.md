---
layout: default
title: Coverage-Aware Web Crawling for Domain-Specific Supplier Discovery via a Web--Knowledge--Web Pipeline
---

# Coverage-Aware Web Crawling for Domain-Specific Supplier Discovery via a Web--Knowledge--Web Pipeline
**arXiv**：[2602.24262v1](https://arxiv.org/abs/2602.24262) · [PDF](https://arxiv.org/pdf/2602.24262.pdf)  
**作者**：Yijiashun Qi, Yijiazhen Qi, Tanmay Wagh  

**一句话要点**：提出Web--Knowledge--Web管道以解决专业领域供应商发现中的覆盖度不足问题。

**关键词**：供应商发现, 网络爬虫, 知识图谱, 覆盖度估计, 中小企业识别, 迭代优化

## 3 点简述
- 核心问题：现有商业数据库在细分行业（如半导体设备制造）中覆盖度不足，难以识别中小企业和次级供应商。
- 方法要点：通过迭代的Web--Knowledge--Web管道，结合知识图谱拓扑和覆盖度信号指导网络爬虫，优化供应商发现。
- 实验或效果：在相同爬取预算下，该方法在半导体设备制造领域达到最高精度和F1分数，构建了包含765个实体和586个关系的知识图谱。

## 摘要（原文）

> Identifying the full landscape of small and medium-sized enterprises (SMEs) in specialized industry sectors is critical for supply-chain resilience, yet existing business databases suffer from substantial coverage gaps -- particularly for sub-tier suppliers and firms in emerging niche markets. We propose a \textbf{Web--Knowledge--Web (W$\to$K$\to$W)} pipeline that iteratively (1)~crawls domain-specific web sources to discover candidate supplier entities, (2)~extracts and consolidates structured knowledge into a heterogeneous knowledge graph, and (3)~uses the knowledge graph's topology and coverage signals to guide subsequent crawling toward under-represented regions of the supplier space. To quantify discovery completeness, we introduce a \textbf{coverage estimation framework} inspired by ecological species-richness estimators (Chao1, ACE) adapted for web-entity populations. Experiments on the semiconductor equipment manufacturing sector (NAICS 333242) demonstrate that the W$\to$K$\to$W pipeline achieves the highest precision (0.138) and F1 (0.118) among all methods using the same 213-page crawl budget, building a knowledge graph of 765 entities and 586 relations while reaching peak recall by iteration~3 with only 112 pages.

