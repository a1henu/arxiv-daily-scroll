---
layout: default
title: Understanding LLM-Driven Test Oracle Generation
---

# Understanding LLM-Driven Test Oracle Generation
**arXiv**：[2601.05542v1](https://arxiv.org/abs/2601.05542) · [PDF](https://arxiv.org/pdf/2601.05542.pdf)  
**作者**：Adam Bodicoat, Gunel Jahangirova, Valerio Terragni  

**一句话要点**：实证研究LLM生成测试预言以暴露软件缺陷的有效性

**关键词**：测试预言生成, 大型语言模型, 自动化测试, 软件质量, 提示工程

## 3 点简述
- 核心问题：现有自动化单元测试生成技术主要生成回归预言，未解决区分程序行为正确性的预言问题。
- 方法要点：利用大型语言模型生成反映预期行为的测试预言，探索不同提示策略和上下文输入水平的影响。
- 实验或效果：通过实证研究评估LLM生成预言的质量，揭示其在基础模型时代的优势与局限。

## 摘要（原文）

> Automated unit test generation aims to improve software quality while reducing the time and effort required for creating tests manually. However, existing techniques primarily generate regression oracles that predicate on the implemented behavior of the class under test. They do not address the oracle problem: the challenge of distinguishing correct from incorrect program behavior. With the rise of Foundation Models (FMs), particularly Large Language Models (LLMs), there is a new opportunity to generate test oracles that reflect intended behavior. This positions LLMs as enablers of Promptware, where software creation and testing are driven by natural-language prompts. This paper presents an empirical study on the effectiveness of LLMs in generating test oracles that expose software failures. We investigate how different prompting strategies and levels of contextual input impact the quality of LLM-generated oracles. Our findings offer insights into the strengths and limitations of LLM-based oracle generation in the FM era, improving our understanding of their capabilities and fostering future research in this area.

