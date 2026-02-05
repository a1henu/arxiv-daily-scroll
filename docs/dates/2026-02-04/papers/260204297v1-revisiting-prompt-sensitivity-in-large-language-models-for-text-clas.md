---
layout: default
title: Revisiting Prompt Sensitivity in Large Language Models for Text Classification: The Role of Prompt Underspecification
---

# Revisiting Prompt Sensitivity in Large Language Models for Text Classification: The Role of Prompt Underspecification
**arXiv**：[2602.04297v1](https://arxiv.org/abs/2602.04297) · [PDF](https://arxiv.org/pdf/2602.04297.pdf)  
**作者**：Branislav Pecher, Michal Spiegel, Robert Belanec, Jan Cegin  

**一句话要点**：揭示提示词欠规范是大型语言模型文本分类中提示敏感性的主要因素

**关键词**：提示敏感性, 提示词欠规范, 大型语言模型, 文本分类, 零样本学习, 线性探测

## 3 点简述
- 核心问题：提示词欠规范导致LLMs在零/少样本分类中性能波动大
- 方法要点：系统比较欠规范提示与具体指令提示的敏感性，使用性能、logit和线性探测分析
- 实验或效果：欠规范提示性能方差高、相关token logit值低，但内部表示影响有限

## 摘要（原文）

> Large language models (LLMs) are widely used as zero-shot and few-shot classifiers, where task behaviour is largely controlled through prompting. A growing number of works have observed that LLMs are sensitive to prompt variations, with small changes leading to large changes in performance. However, in many cases, the investigation of sensitivity is performed using underspecified prompts that provide minimal task instructions and weakly constrain the model's output space. In this work, we argue that a significant portion of the observed prompt sensitivity can be attributed to prompt underspecification. We systematically study and compare the sensitivity of underspecified prompts and prompts that provide specific instructions. Utilising performance analysis, logit analysis, and linear probing, we find that underspecified prompts exhibit higher performance variance and lower logit values for relevant tokens, while instruction-prompts suffer less from such problems. However, linear probing analysis suggests that the effects of prompt underspecification have only a marginal impact on the internal LLM representations, instead emerging in the final layers. Overall, our findings highlight the need for more rigour when investigating and mitigating prompt sensitivity.

