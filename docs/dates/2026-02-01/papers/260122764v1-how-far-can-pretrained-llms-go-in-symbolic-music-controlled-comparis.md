---
layout: default
title: How Far Can Pretrained LLMs Go in Symbolic Music? Controlled Comparisons of Supervised and Preference-based Adaptation
---

# How Far Can Pretrained LLMs Go in Symbolic Music? Controlled Comparisons of Supervised and Preference-based Adaptation
**arXiv**：[2601.22764v1](https://arxiv.org/abs/2601.22764) · [PDF](https://arxiv.org/pdf/2601.22764.pdf)  
**作者**：Deepak Kumar, Emmanouil Karystinaios, Gerhard Widmer, Markus Schedl  

**一句话要点**：比较监督与偏好微调策略在符号音乐任务中的适应效果

**关键词**：符号音乐生成, 大语言模型微调, 领域适应, ABC记谱法, 指令微调, 偏好学习

## 3 点简述
- 核心问题：指令微调LLMs在符号音乐理解与生成中的实际有效性未充分评估
- 方法要点：对比现成指令微调模型、领域适应变体和音乐专用LLM基线
- 实验或效果：基于多符号音乐语料库和评估信号，分析领域适应与先验信息保留的权衡

## 摘要（原文）

> Music often shares notable parallels with language, motivating the use of pretrained large language models (LLMs) for symbolic music understanding and generation. Despite growing interest, the practical effectiveness of adapting instruction-tuned LLMs to symbolic music remains insufficiently characterized. We present a controlled comparative study of finetuning strategies for ABC-based generation and understanding, comparing an off-the-shelf instruction-tuned backbone to domain-adapted variants and a music-specialized LLM baseline. Across multiple symbolic music corpora and evaluation signals, we provide some insights into adaptation choices for symbolic music applications. We highlight the domain adaptation vs.~preserving prior information tradeoff as well as the distinct behaviour of metrics used to measure the domain adaptation for symbolic music.

