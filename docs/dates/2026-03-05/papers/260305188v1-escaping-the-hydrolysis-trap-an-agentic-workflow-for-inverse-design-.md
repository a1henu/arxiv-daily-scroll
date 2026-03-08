---
layout: default
title: Escaping the Hydrolysis Trap: An Agentic Workflow for Inverse Design of Durable Photocatalytic Covalent Organic Frameworks
---

# Escaping the Hydrolysis Trap: An Agentic Workflow for Inverse Design of Durable Photocatalytic Covalent Organic Frameworks
**arXiv**：[2603.05188v1](https://arxiv.org/abs/2603.05188) · [PDF](https://arxiv.org/pdf/2603.05188.pdf)  
**作者**：Iman Peivaste, Nicolas D. Boscher, Ahmed Makradi, Salim Belouettar  

**一句话要点**：提出Ara大语言模型代理以解决光催化共价有机框架的稳定性-活性权衡问题

**关键词**：共价有机框架, 光催化, 大语言模型代理, 材料逆设计, 水解稳定性, 多准则优化

## 3 点简述
- 核心问题：光催化共价有机框架中，活性高的亚胺键易水解，导致稳定性与活性难以兼顾。
- 方法要点：Ara代理结合预训练化学知识、给体-受体理论等，指导多准则材料搜索，包括带隙、带边和水解稳定性。
- 实验或效果：在组合设计空间中，Ara的命中率比随机搜索高11.5倍，显著优于贝叶斯优化，并揭示可解释的化学逻辑。

## 摘要（原文）

> Covalent organic frameworks (COFs) are promising photocatalysts for solar hydrogen production, yet the most electronically favorable linkages, imines, hydrolyze rapidly in water, creating a stability--activity trade-off that limits practical deployment. Navigating the combinatorial design space of nodes, linkers, linkages, and functional groups to identify candidates that are simultaneously active and durable remains a formidable challenge. Here we introduce Ara, a large-language-model (LLM) agent that leverages pretrained chemical knowledge, donor--acceptor theory, conjugation effects, and linkage stability hierarchies, to guide the search for photocatalytic COFs satisfying joint band-gap, band-edge, and hydrolytic-stability criteria. Evaluated against random search and Bayesian optimization (BO) over a space consisting of candidates with various nodes, linkers, linkages, and r-groups, screened with a GFN1-xTB fragment pipeline, Ara achieves a 52.7\% hit rate (11.5$\times$ random, p = 0.006), finds its first hit at iteration 12 versus 25 for random search, and significantly outperforms BO (p = 0.006). Inspection of the agent's reasoning traces reveals interpretable chemical logic: early convergence on vinylene and beta-ketoenamine linkages for stability, node selection informed by electron-withdrawing character, and systematic R-group optimization to center the band gap at 2.0 eV. Exhaustive evaluation of the full search space uncovers a complementary exploitation--exploration trade-off between the agent and BO, suggesting that hybrid strategies may combine the strengths of both approaches. These results demonstrate that LLM chemical priors can substantially accelerate multi-criteria materials discovery.

