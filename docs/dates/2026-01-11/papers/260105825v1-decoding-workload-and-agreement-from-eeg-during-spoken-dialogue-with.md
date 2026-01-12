---
layout: default
title: Decoding Workload and Agreement From EEG During Spoken Dialogue With Conversational AI
---

# Decoding Workload and Agreement From EEG During Spoken Dialogue With Conversational AI
**arXiv**：[2601.05825v1](https://arxiv.org/abs/2601.05825) · [PDF](https://arxiv.org/pdf/2601.05825.pdf)  
**作者**：Lucija Mihić Zidar, Philipp Wicke, Praneel Bhatia, Rosa Lutz, Marius Klug, Thorsten O. Zander  

**一句话要点**：提出基于EEG的被动脑机接口方法，用于解码口语人机对话中的工作负荷与隐含同意。

**关键词**：被动脑机接口, EEG解码, 口语对话, 工作负荷分类, 隐含同意检测, 跨范式迁移

## 3 点简述
- 核心问题：探索EEG分类器能否从受控任务迁移到口语人机对话，解码工作负荷和隐含同意。
- 方法要点：引入两种对话范式（拼写蜜蜂和句子补全）及端到端流程，对齐单词级事件与连续EEG输出。
- 实验或效果：初步研究显示工作负荷解码有可解释趋势，隐含同意解码能连续应用并与事件对齐，但存在迁移限制。

## 摘要（原文）

> Passive brain-computer interfaces offer a potential source of implicit feedback for alignment of large language models, but most mental state decoding has been done in controlled tasks. This paper investigates whether established EEG classifiers for mental workload and implicit agreement can be transferred to spoken human-AI dialogue. We introduce two conversational paradigms - a Spelling Bee task and a sentence completion task- and an end-to-end pipeline for transcribing, annotating, and aligning word-level conversational events with continuous EEG classifier output. In a pilot study, workload decoding showed interpretable trends during spoken interaction, supporting cross-paradigm transfer. For implicit agreement, we demonstrate continuous application and precise temporal alignment to conversational events, while identifying limitations related to construct transfer and asynchronous application of event-based classifiers. Overall, the results establish feasibility and constraints for integrating passive BCI signals into conversational AI systems.

