---
layout: default
title: Evaluating LLMs for Zeolite Synthesis Event Extraction (ZSEE): A Systematic Analysis of Prompting Strategies
---

# Evaluating LLMs for Zeolite Synthesis Event Extraction (ZSEE): A Systematic Analysis of Prompting Strategies
**arXiv**：[2512.15312v1](https://arxiv.org/abs/2512.15312) · [PDF](https://arxiv.org/pdf/2512.15312.pdf)  
**作者**：Charan Prakash Rathore, Saumi Ray, Dhruv Kumar  

**一句话要点**：评估LLMs在沸石合成事件提取中的提示策略，揭示其高层面理解与精细提取的局限性。

**关键词**：科学信息提取, 提示策略评估, 沸石合成, LLMs性能分析, 事件提取

## 3 点简述
- 核心问题：LLMs在科学信息提取任务中，不同提示策略的有效性如何？
- 方法要点：系统评估零样本、少样本、事件特定和基于反思四种提示策略，覆盖六个先进LLMs。
- 实验或效果：事件类型分类F1达80-90%，但参数提取任务仅50-65%，提示策略改进有限。

## 摘要（原文）

> Extracting structured information from zeolite synthesis experimental procedures is critical for materials discovery, yet existing methods have not systematically evaluated Large Language Models (LLMs) for this domain-specific task. This work addresses a fundamental question: what is the efficacy of different prompting strategies when applying LLMs to scientific information extraction? We focus on four key subtasks: event type classification (identifying synthesis steps), trigger text identification (locating event mentions), argument role extraction (recognizing parameter types), and argument text extraction (extracting parameter values). We evaluate four prompting strategies - zero-shot, few-shot, event-specific, and reflection-based - across six state-of-the-art LLMs (Gemma-3-12b-it, GPT-5-mini, O4-mini, Claude-Haiku-3.5, DeepSeek reasoning and non-reasoning) using the ZSEE dataset of 1,530 annotated sentences. Results demonstrate strong performance on event type classification (80-90\% F1) but modest performance on fine-grained extraction tasks, particularly argument role and argument text extraction (50-65\% F1). GPT-5-mini exhibits extreme prompt sensitivity with 11-79\% F1 variation. Notably, advanced prompting strategies provide minimal improvements over zero-shot approaches, revealing fundamental architectural limitations. Error analysis identifies systematic hallucination, over-generalization, and inability to capture synthesis-specific nuances. Our findings demonstrate that while LLMs achieve high-level understanding, precise extraction of experimental parameters requires domain-adapted models, providing quantitative benchmarks for scientific information extraction.

