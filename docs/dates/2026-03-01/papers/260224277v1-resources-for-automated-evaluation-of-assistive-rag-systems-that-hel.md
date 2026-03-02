---
layout: default
title: Resources for Automated Evaluation of Assistive RAG Systems that Help Readers with News Trustworthiness Assessment
---

# Resources for Automated Evaluation of Assistive RAG Systems that Help Readers with News Trustworthiness Assessment
**arXiv**：[2602.24277v1](https://arxiv.org/abs/2602.24277) · [PDF](https://arxiv.org/pdf/2602.24277.pdf)  
**作者**：Dake Zhang, Mark D. Smucker, Charles L. A. Clarke  

**一句话要点**：提出自动化评估资源以支持辅助新闻可信度评估的RAG系统评测

**关键词**：新闻可信度评估, RAG系统, 自动化评测, TREC DRAGUN, 报告生成, 问题生成

## 3 点简述
- 核心问题：在线新闻可信度评估困难，需辅助RAG系统生成基于证据的报告。
- 方法要点：基于TREC 2025 DRAGUN赛道，开发可重用任务和自动化评估流程AutoJudge。
- 实验或效果：AutoJudge与人工评估相关性高（Task 1 τ=0.678，Task 2 τ=0.872）。

## 摘要（原文）

> Many readers today struggle to assess the trustworthiness of online news because reliable reporting coexists with misinformation. The TREC 2025 DRAGUN (Detection, Retrieval, and Augmented Generation for Understanding News) Track provided a venue for researchers to develop and evaluate assistive RAG systems that support readers' news trustworthiness assessment by producing reader-oriented, well-attributed reports. As the organizers of the DRAGUN track, we describe the resources that we have newly developed to allow for the reuse of the track's tasks. The track had two tasks: (Task 1) Question Generation, producing 10 ranked investigative questions; and (Task 2, the main task) Report Generation, producing a 250-word report grounded in the MS MARCO V2.1 Segmented Corpus. As part of the track's evaluation, we had TREC assessors create importance-weighted rubrics of questions with expected short answers for 30 different news articles. These rubrics represent the information that assessors believe is important for readers to assess an article's trustworthiness. The assessors then used their rubrics to manually judge the participating teams' submitted runs. To make these tasks and their rubrics reusable, we have created an automated process to judge runs not part of the original assessing. We show that our AutoJudge ranks existing runs well compared to the TREC human-assessed evaluation (Kendall's $τ= 0.678$ for Task 1 and $τ= 0.872$ for Task 2). These resources enable both the evaluation of RAG systems for assistive news trustworthiness assessment and, with the human evaluation as a benchmark, research on improving automated RAG evaluation.

