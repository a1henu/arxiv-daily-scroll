---
layout: default
title: Needle in the Web: A Benchmark for Retrieving Targeted Web Pages in the Wild
---

# Needle in the Web: A Benchmark for Retrieving Targeted Web Pages in the Wild
**arXiv**：[2512.16553v1](https://arxiv.org/abs/2512.16553) · [PDF](https://arxiv.org/pdf/2512.16553.pdf)  
**作者**：Yumeng Wang, Tianyu Fan, Lingrui Xu, Chao Huang  

**一句话要点**：提出Needle in the Web基准以评估搜索代理在模糊探索性查询下的网页检索能力

**关键词**：模糊探索性搜索, 网页检索基准, 语义模糊性, LLM评估, 搜索代理

## 3 点简述
- 核心问题：现有基准忽视模糊探索性搜索，即用户寻求最相关网页而非单一事实答案
- 方法要点：基于网页内容事实声明，生成可控难度的模糊查询，覆盖7个领域共663个问题
- 实验或效果：测试主流LLM和搜索代理，多数准确率低于35%，显示当前系统面临显著挑战

## 摘要（原文）

> Large Language Models (LLMs) have evolved from simple chatbots into sophisticated agents capable of automating complex real-world tasks, where browsing and reasoning over live web content is key to assessing retrieval and cognitive skills. Existing benchmarks like BrowseComp and xBench-DeepSearch emphasize complex reasoning searches requiring multi-hop synthesis but neglect Fuzzy Exploratory Search, namely queries that are vague and multifaceted, where users seek the most relevant webpage rather than a single factual answer. To address this gap, we introduce Needle in the Web, a novel benchmark specifically designed to evaluate modern search agents and LLM-based systems on their ability to retrieve and reason over real-world web content in response to ambiguous, exploratory queries under varying levels of difficulty. Needle in the Web comprises 663 questions spanning seven distinct domains. To ensure high query quality and answer uniqueness, we employ a flexible methodology that reliably generates queries of controllable difficulty based on factual claims of web contents. We benchmark three leading LLMs and three agent-based search systems on Needle in the Web, finding that most models struggle: many achieve below 35% accuracy, and none consistently excel across domains or difficulty levels. These findings reveal that Needle in the Web presents a significant challenge for current search systems and highlights the open problem of effective fuzzy retrieval under semantic ambiguity.

