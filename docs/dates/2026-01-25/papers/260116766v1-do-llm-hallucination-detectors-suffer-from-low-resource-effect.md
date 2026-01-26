---
layout: default
title: Do LLM hallucination detectors suffer from low-resource effect?
---

# Do LLM hallucination detectors suffer from low-resource effect?
**arXiv**：[2601.16766v1](https://arxiv.org/abs/2601.16766) · [PDF](https://arxiv.org/pdf/2601.16766.pdf)  
**作者**：Debtanu Datta, Mohan Kishore Chilukuri, Yash Kumar, Saptarshi Ghosh, Muhammad Bilal Zafar  

**一句话要点**：探究幻觉检测器在低资源语言中的性能变化，发现其准确性下降小于任务准确性下降。

**关键词**：幻觉检测, 低资源语言, 多语言评估, LLM不确定性, 跨语言设置

## 3 点简述
- 核心问题：研究幻觉检测器是否受低资源效应影响，即性能在低资源语言中是否显著下降。
- 方法要点：在三个领域（事实回忆、STEM、人文学科）的五个任务上，使用四个LLM和三个幻觉检测器进行实验。
- 实验或效果：发现任务准确性在低资源语言中大幅下降，但检测器准确性下降幅度小得多，表明LLM内部机制可能编码不确定性信号。

## 摘要（原文）

> LLMs, while outperforming humans in a wide range of tasks, can still fail in unanticipated ways. We focus on two pervasive failure modes: (i) hallucinations, where models produce incorrect information about the world, and (ii) the low-resource effect, where the models show impressive performance in high-resource languages like English but the performance degrades significantly in low-resource languages like Bengali. We study the intersection of these issues and ask: do hallucination detectors suffer from the low-resource effect? We conduct experiments on five tasks across three domains (factual recall, STEM, and Humanities). Experiments with four LLMs and three hallucination detectors reveal a curious finding: As expected, the task accuracies in low-resource languages experience large drops (compared to English). However, the drop in detectors' accuracy is often several times smaller than the drop in task accuracy. Our findings suggest that even in low-resource languages, the internal mechanisms of LLMs might encode signals about their uncertainty. Further, the detectors are robust within language (even for non-English) and in multilingual setups, but not in cross-lingual settings without in-language supervision.

