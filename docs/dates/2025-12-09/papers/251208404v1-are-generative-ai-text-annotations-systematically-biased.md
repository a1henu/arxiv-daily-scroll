---
layout: default
title: Are generative AI text annotations systematically biased?
---

# Are generative AI text annotations systematically biased?
**arXiv**：[2512.08404v1](https://arxiv.org/abs/2512.08404) · [PDF](https://arxiv.org/pdf/2512.08404.pdf)  
**作者**：Sjoerd B. Stolwijk, Mark Boukes, Damian Trilling  

**一句话要点**：揭示生成式AI文本标注存在系统性偏见，与人工标注差异显著

**关键词**：生成式AI, 文本标注, 系统性偏见, 大语言模型, 人工标注对比

## 3 点简述
- 研究生成式大语言模型在文本标注中的偏见问题，概念性复现人工标注
- 使用多种GLLM和提示评估五个概念，发现F1分数尚可但存在系统性偏差
- GLLM标注与人工标注在流行度和下游结果上差异大，F1分数无法充分反映偏见程度

## 摘要（原文）

> This paper investigates bias in GLLM annotations by conceptually replicating manual annotations of Boukes (2024). Using various GLLMs (Llama3.1:8b, Llama3.3:70b, GPT4o, Qwen2.5:72b) in combination with five different prompts for five concepts (political content, interactivity, rationality, incivility, and ideology). We find GLLMs perform adequate in terms of F1 scores, but differ from manual annotations in terms of prevalence, yield substantively different downstream results, and display systematic bias in that they overlap more with each other than with manual annotations. Differences in F1 scores fail to account for the degree of bias.

