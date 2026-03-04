---
layout: default
title: APRES: An Agentic Paper Revision and Evaluation System
---

# APRES: An Agentic Paper Revision and Evaluation System
**arXiv**：[2603.03142v1](https://arxiv.org/abs/2603.03142) · [PDF](https://arxiv.org/pdf/2603.03142.pdf)  
**作者**：Bingchen Zhao, Jenny Zhang, Chenxi Whitehouse, Minqi Jiang, Michael Shvartsman, Abhishek Charnalia, Despoina Magka, Tatiana Shavrina, Derek Dunfield, Oisin Mac Aodha, Yoram Bachrach  

**一句话要点**：提出APRES系统，利用大语言模型基于评估准则自动修订科学论文以提升质量和影响力

**关键词**：大语言模型, 论文修订, 同行评审, 科学传播, 自动化评估

## 3 点简述
- 核心问题：当前同行评审反馈不一致，阻碍论文改进和影响力提升
- 方法要点：基于大语言模型，自动发现预测未来引用数的准则并修订论文文本
- 实验或效果：修订后论文在人类专家评估中79%优于原稿，未来引用预测误差降低19.6%

## 摘要（原文）

> Scientific discoveries must be communicated clearly to realize their full potential. Without effective communication, even the most groundbreaking findings risk being overlooked or misunderstood. The primary way scientists communicate their work and receive feedback from the community is through peer review. However, the current system often provides inconsistent feedback between reviewers, ultimately hindering the improvement of a manuscript and limiting its potential impact. In this paper, we introduce a novel method APRES powered by Large Language Models (LLMs) to update a scientific papers text based on an evaluation rubric. Our automated method discovers a rubric that is highly predictive of future citation counts, and integrate it with APRES in an automated system that revises papers to enhance their quality and impact. Crucially, this objective should be met without altering the core scientific content. We demonstrate the success of APRES, which improves future citation prediction by 19.6% in mean averaged error over the next best baseline, and show that our paper revision process yields papers that are preferred over the originals by human expert evaluators 79% of the time. Our findings provide strong empirical support for using LLMs as a tool to help authors stress-test their manuscripts before submission. Ultimately, our work seeks to augment, not replace, the essential role of human expert reviewers, for it should be humans who discern which discoveries truly matter, guiding science toward advancing knowledge and enriching lives.

