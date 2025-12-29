---
layout: default
title: A2P-Vis: an Analyzer-to-Presenter Agentic Pipeline for Visual Insights Generation and Reporting
---

# A2P-Vis: an Analyzer-to-Presenter Agentic Pipeline for Visual Insights Generation and Reporting
**arXiv**：[2512.22101v1](https://arxiv.org/abs/2512.22101) · [PDF](https://arxiv.org/pdf/2512.22101.pdf)  
**作者**：Shuyu Gan, Renxiang Wang, James Mooney, Dongyeop Kang  

**一句话要点**：提出A2P-Vis以解决AI代理在自动化数据科学流程中生成高质量可视化报告的问题。

**关键词**：自动化数据科学, 多代理系统, 可视化报告生成, 端到端管道, AI代理协作

## 3 点简述
- 核心问题：AI代理自动化数据科学流程在生成多样化视觉证据和整合成连贯报告方面存在不足。
- 方法要点：采用两阶段多代理管道，包括数据分析和报告呈现，确保从原始数据到高质量报告的端到端转换。
- 实验或效果：通过质量保证的分析器和叙事呈现器结合，提升自动化数据分析在实践中的实用性，生成可发布的报告。

## 摘要（原文）

> Automating end-to-end data science pipeline with AI agents still stalls on two gaps: generating insightful, diverse visual evidence and assembling it into a coherent, professional report. We present A2P-Vis, a two-part, multi-agent pipeline that turns raw datasets into a high-quality data-visualization report. The Data Analyzer orchestrates profiling, proposes diverse visualization directions, generates and executes plotting code, filters low-quality figures with a legibility checker, and elicits candidate insights that are automatically scored for depth, correctness, specificity, depth and actionability. The Presenter then orders topics, composes chart-grounded narratives from the top-ranked insights, writes justified transitions, and revises the document for clarity and consistency, yielding a coherent, publication-ready report. Together, these agents convert raw data into curated materials (charts + vetted insights) and into a readable narrative without manual glue work. We claim that by coupling a quality-assured Analyzer with a narrative Presenter, A2P-Vis operationalizes co-analysis end-to-end, improving the real-world usefulness of automated data analysis for practitioners. For the complete dataset report, please see: https://www.visagent.org/api/output/f2a3486d-2c3b-4825-98d4-5af25a819f56.

