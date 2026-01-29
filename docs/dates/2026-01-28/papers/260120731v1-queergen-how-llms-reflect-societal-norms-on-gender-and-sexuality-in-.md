---
layout: default
title: QueerGen: How LLMs Reflect Societal Norms on Gender and Sexuality in Sentence Completion Tasks
---

# QueerGen: How LLMs Reflect Societal Norms on Gender and Sexuality in Sentence Completion Tasks
**arXiv**：[2601.20731v1](https://arxiv.org/abs/2601.20731) · [PDF](https://arxiv.org/pdf/2601.20731.pdf)  
**作者**：Mae Sosto, Delfina Sol Martinez Pandiani, Laura Hollink  

**一句话要点**：研究LLM在句子补全任务中如何反映性别与性取向的社会规范偏差

**关键词**：大语言模型, 社会规范偏差, 句子补全任务, 性别与性取向, 可测量偏差, 模型特性影响

## 3 点简述
- 核心问题：LLM是否复制社会规范，特别是异性恋顺性别规范，导致可测量的生成偏差
- 方法要点：通过三类主题（酷儿标记、非酷儿标记、未标记）分析LLM响应，操作化为情感、尊重、毒性和预测多样性四个维度
- 实验或效果：MLM对酷儿标记主题产生最不利情感和更高毒性，ARLM部分缓解，闭源ARLM对未标记主题输出更有害

## 摘要（原文）

> This paper examines how Large Language Models (LLMs) reproduce societal norms, particularly heterocisnormativity, and how these norms translate into measurable biases in their text generations. We investigate whether explicit information about a subject's gender or sexuality influences LLM responses across three subject categories: queer-marked, non-queer-marked, and the normalized "unmarked" category. Representational imbalances are operationalized as measurable differences in English sentence completions across four dimensions: sentiment, regard, toxicity, and prediction diversity. Our findings show that Masked Language Models (MLMs) produce the least favorable sentiment, higher toxicity, and more negative regard for queer-marked subjects. Autoregressive Language Models (ARLMs) partially mitigate these patterns, while closed-access ARLMs tend to produce more harmful outputs for unmarked subjects. Results suggest that LLMs reproduce normative social assumptions, though the form and degree of bias depend strongly on specific model characteristics, which may redistribute, but not eliminate, representational harms.

