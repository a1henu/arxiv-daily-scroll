---
layout: default
title: RISE: Rule-Driven SQL Dialect Translation via Query Reduction
---

# RISE: Rule-Driven SQL Dialect Translation via Query Reduction
**arXiv**：[2601.05579v1](https://arxiv.org/abs/2601.05579) · [PDF](https://arxiv.org/pdf/2601.05579.pdf)  
**作者**：Xudong Xie, Yuwei Zhang, Wensheng Dou, Yu Gao, Ziyu Cui, Jiansen Song, Rui Yang, Jun Wei  

**一句话要点**：提出RISE方法，通过查询简化与规则提取，准确翻译复杂SQL方言以支持云迁移。

**关键词**：SQL方言翻译, 查询简化, 规则提取, 大型语言模型, 数据库迁移

## 3 点简述
- 核心问题：传统SQL方言翻译工具依赖人工规则，难以处理长复杂查询，LLMs直接翻译效果不佳。
- 方法要点：先简化查询去除方言无关元素，再用LLMs翻译简化查询并自动提取规则，最后应用规则到原查询。
- 实验或效果：在TPC-DS和SQLProcBench基准上，RISE准确率分别达97.98%和100%，显著优于基线方法。

## 摘要（原文）

> Translating SQL dialects across different relational database management systems (RDBMSs) is crucial for migrating RDBMS-based applications to the cloud. Traditional SQL dialect translation tools rely on manually-crafted rules, necessitating significant manual effort to support new RDBMSs and dialects. Although large language models (LLMs) can assist in translating SQL dialects, they often struggle with lengthy and complex SQL queries.
>   In this paper, we propose RISE, a novel LLM-based SQL dialect translation approach that can accurately handle lengthy and complex SQL queries. Given a complex source query $Q_c$ that contains a SQL dialect $d$, we first employ a dialect-aware query reduction technique to derive a simplified query $Q_{s}$ by removing $d$-irrelevant SQL elements from $Q_c$. Subsequently, we utilize LLMs to translate $Q_{s}$ into $Q_{s^{'}}$, and automatically extract the translation rule $r_d$ for dialect $d$ based on the relationship between $Q_{s}$ and $Q_{s^{'}}$. By applying $r_d$ to $Q_c$, we can effectively translate the dialect $d$ within $Q_c$, thereby bypassing the complexity of the source query $Q_c$. We evaluate RISE on two real-world benchmarks, i.e., TPC-DS and SQLProcBench, comparing its performance against both the traditional rule-based tools and the LLM-based approaches with respect to translation accuracy. RISE achieves accuracies of 97.98% on TPC-DS and 100% on SQLProcBench, outperforming the baselines by an average improvement of 24.62% and 238.41%, respectively.

