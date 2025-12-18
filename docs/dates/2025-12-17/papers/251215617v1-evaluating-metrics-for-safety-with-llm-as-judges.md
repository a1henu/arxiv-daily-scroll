---
layout: default
title: Evaluating Metrics for Safety with LLM-as-Judges
---

# Evaluating Metrics for Safety with LLM-as-Judges
**arXiv**：[2512.15617v1](https://arxiv.org/abs/2512.15617) · [PDF](https://arxiv.org/pdf/2512.15617.pdf)  
**作者**：Kester Clegg, Richard Hawkins, Ibrahim Habli, Tom Lawton  

**一句话要点**：提出加权指标组合方法以降低LLM-as-Judges在安全关键任务中的错误风险

**关键词**：LLM-as-Judges, 安全评估, 加权指标, 置信度阈值, 人工审查

## 3 点简述
- 核心问题：LLM在安全关键信息流中引入错误风险，需确保其安全可靠
- 方法要点：采用加权指标组合，结合上下文敏感性和置信度阈值，触发人工审查
- 实验或效果：未知具体实验，但论证了通过指标设计可降低评估风险

## 摘要（原文）

> LLMs (Large Language Models) are increasingly used in text processing pipelines to intelligently respond to a variety of inputs and generation tasks. This raises the possibility of replacing human roles that bottleneck existing information flows, either due to insufficient staff or process complexity. However, LLMs make mistakes and some processing roles are safety critical. For example, triaging post-operative care to patients based on hospital referral letters, or updating site access schedules in nuclear facilities for work crews. If we want to introduce LLMs into critical information flows that were previously performed by humans, how can we make them safe and reliable? Rather than make performative claims about augmented generation frameworks or graph-based techniques, this paper argues that the safety argument should focus on the type of evidence we get from evaluation points in LLM processes, particularly in frameworks that employ LLM-as-Judges (LaJ) evaluators. This paper argues that although we cannot get deterministic evaluations from many natural language processing tasks, by adopting a basket of weighted metrics it may be possible to lower the risk of errors within an evaluation, use context sensitivity to define error severity and design confidence thresholds that trigger human review of critical LaJ judgments when concordance across evaluators is low.

