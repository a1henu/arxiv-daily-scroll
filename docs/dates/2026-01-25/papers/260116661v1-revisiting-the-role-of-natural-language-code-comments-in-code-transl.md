---
layout: default
title: Revisiting the Role of Natural Language Code Comments in Code Translation
---

# Revisiting the Role of Natural Language Code Comments in Code Translation
**arXiv**：[2601.16661v1](https://arxiv.org/abs/2601.16661) · [PDF](https://arxiv.org/pdf/2601.16661.pdf)  
**作者**：Monika Gupta, Ajay Meena, Anamitra Roy Choudhury, Vijay Arya, Srikanta Bedathur  

**一句话要点**：提出COMMENTRA方法，利用代码注释提升大语言模型在跨语言代码翻译中的准确性。

**关键词**：代码翻译, 自然语言注释, 大语言模型, 跨语言编程, 实证研究, 翻译准确性

## 3 点简述
- 核心问题：现有代码翻译基准缺乏注释，其影响未知。
- 方法要点：通过大规模实证研究，分析注释对翻译质量的作用。
- 实验或效果：注释可显著提升翻译准确率，COMMENTRA方法性能翻倍。

## 摘要（原文）

> The advent of large language models (LLMs) has ushered in a new era in automated code translation across programming languages. Since most code-specific LLMs are pretrained on well-commented code from large repositories like GitHub, it is reasonable to hypothesize that natural language code comments could aid in improving translation quality. Despite their potential relevance, comments are largely absent from existing code translation benchmarks, rendering their impact on translation quality inadequately characterised. In this paper, we present a large-scale empirical study evaluating the impact of comments on translation performance. Our analysis involves more than $80,000$ translations, with and without comments, of $1100+$ code samples from two distinct benchmarks covering pairwise translations between five different programming languages: C, C++, Go, Java, and Python. Our results provide strong evidence that code comments, particularly those that describe the overall purpose of the code rather than line-by-line functionality, significantly enhance translation accuracy. Based on these findings, we propose COMMENTRA, a code translation approach, and demonstrate that it can potentially double the performance of LLM-based code translation. To the best of our knowledge, our study is the first in terms of its comprehensiveness, scale, and language coverage on how to improve code translation accuracy using code comments.

