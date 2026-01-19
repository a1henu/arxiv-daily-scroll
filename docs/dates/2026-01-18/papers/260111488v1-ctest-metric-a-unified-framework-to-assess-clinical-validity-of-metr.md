---
layout: default
title: CTest-Metric: A Unified Framework to Assess Clinical Validity of Metrics for CT Report Generation
---

# CTest-Metric: A Unified Framework to Assess Clinical Validity of Metrics for CT Report Generation
**arXiv**：[2601.11488v1](https://arxiv.org/abs/2601.11488) · [PDF](https://arxiv.org/pdf/2601.11488.pdf)  
**作者**：Vanshali Sharma, Andrea Mia Bejar, Gorkem Durak, Ulas Bagci  

**一句话要点**：提出CTest-Metric框架以评估CT报告生成指标的临床有效性

**关键词**：CT报告生成, 指标评估框架, 临床有效性, 生成式AI, 放射学自动化

## 3 点简述
- 核心问题：放射学报告生成领域缺乏统一框架评估指标的临床适用性
- 方法要点：通过三个模块测试指标的风格泛化性、错误注入敏感性和专家相关性
- 实验或效果：发现GREEN Score与专家判断最一致，BERTScore-F1对事实错误最不敏感

## 摘要（原文）

> In the generative AI era, where even critical medical tasks are increasingly automated, radiology report generation (RRG) continues to rely on suboptimal metrics for quality assessment. Developing domain-specific metrics has therefore been an active area of research, yet it remains challenging due to the lack of a unified, well-defined framework to assess their robustness and applicability in clinical contexts. To address this, we present CTest-Metric, a first unified metric assessment framework with three modules determining the clinical feasibility of metrics for CT RRG. The modules test: (i) Writing Style Generalizability (WSG) via LLM-based rephrasing; (ii) Synthetic Error Injection (SEI) at graded severities; and (iii) Metrics-vs-Expert correlation (MvE) using clinician ratings on 175 "disagreement" cases. Eight widely used metrics (BLEU, ROUGE, METEOR, BERTScore-F1, F1-RadGraph, RaTEScore, GREEN Score, CRG) are studied across seven LLMs built on a CT-CLIP encoder. Using our novel framework, we found that lexical NLG metrics are highly sensitive to stylistic variations; GREEN Score aligns best with expert judgments (Spearman~0.70), while CRG shows negative correlation; and BERTScore-F1 is least sensitive to factual error injection. We will release the framework, code, and allowable portion of the anonymized evaluation data (rephrased/error-injected CT reports), to facilitate reproducible benchmarking and future metric development.

