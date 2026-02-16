---
layout: default
title: RAT-Bench: A Comprehensive Benchmark for Text Anonymization
---

# RAT-Bench: A Comprehensive Benchmark for Text Anonymization
**arXiv**：[2602.12806v1](https://arxiv.org/abs/2602.12806) · [PDF](https://arxiv.org/pdf/2602.12806.pdf)  
**作者**：Nataša Krčo, Zexi Yao, Matthieu Meeus, Yves-Alexandre de Montjoye  

**一句话要点**：提出RAT-Bench基准以评估文本匿名化工具的重识别风险

**关键词**：文本匿名化, 重识别风险, 基准测试, 隐私保护, 大型语言模型

## 3 点简述
- 核心问题：现有工具评估多关注标识符移除，重识别风险未知
- 方法要点：基于美国人口统计生成合成文本，评估NER和LLM工具
- 实验或效果：发现LLM工具隐私-效用权衡更优，但计算成本高

## 摘要（原文）

> Data containing personal information is increasingly used to train, fine-tune, or query Large Language Models (LLMs). Text is typically scrubbed of identifying information prior to use, often with tools such as Microsoft's Presidio or Anthropic's PII purifier. These tools have traditionally been evaluated on their ability to remove specific identifiers (e.g., names), yet their effectiveness at preventing re-identification remains unclear. We introduce RAT-Bench, a comprehensive benchmark for text anonymization tools based on re-identification risk. Using U.S. demographic statistics, we generate synthetic text containing various direct and indirect identifiers across domains, languages, and difficulty levels. We evaluate a range of NER- and LLM-based text anonymization tools and, based on the attributes an LLM-based attacker is able to correctly infer from the anonymized text, we report the risk of re-identification in the U.S. population, while properly accounting for the disparate impact of identifiers. We find that, while capabilities vary widely, even the best tools are far from perfect in particular when direct identifiers are not written in standard ways and when indirect identifiers enable re-identification. Overall we find LLM-based anonymizers, including new iterative anonymizers, to provide a better privacy-utility trade-off albeit at a higher computational cost. Importantly, we also find them to work well across languages. We conclude with recommendations for future anonymization tools and will release the benchmark and encourage community efforts to expand it, in particular to other geographies.

