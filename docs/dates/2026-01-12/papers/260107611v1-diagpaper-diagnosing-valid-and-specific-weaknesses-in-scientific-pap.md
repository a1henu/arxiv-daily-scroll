---
layout: default
title: DIAGPaper: Diagnosing Valid and Specific Weaknesses in Scientific Papers via Multi-Agent Reasoning
---

# DIAGPaper: Diagnosing Valid and Specific Weaknesses in Scientific Papers via Multi-Agent Reasoning
**arXiv**：[2601.07611v1](https://arxiv.org/abs/2601.07611) · [PDF](https://arxiv.org/pdf/2601.07611.pdf)  
**作者**：Zhuoyang Zou, Abolfazl Ansari, Delvin Ce Zhang, Dongwon Lee, Wenpeng Yin  

**一句话要点**：提出DIAGPaper多智能体框架，通过定制化、反驳和优先级模块解决科学论文弱点诊断的局限性。

**关键词**：多智能体推理, 论文弱点诊断, 评审标准模拟, 作者反驳验证, 弱点优先级排序

## 3 点简述
- 现有方法在模拟专家评审、验证弱点有效性和优先级排序方面存在不足。
- DIAGPaper集成定制化、反驳和优先级模块，模拟评审标准、作者反驳和弱点严重性评估。
- 在AAAR和ReviewCritique基准上，DIAGPaper在生成有效和特定弱点方面显著优于现有方法。

## 摘要（原文）

> Paper weakness identification using single-agent or multi-agent LLMs has attracted increasing attention, yet existing approaches exhibit key limitations. Many multi-agent systems simulate human roles at a surface level, missing the underlying criteria that lead experts to assess complementary intellectual aspects of a paper. Moreover, prior methods implicitly assume identified weaknesses are valid, ignoring reviewer bias, misunderstanding, and the critical role of author rebuttals in validating review quality. Finally, most systems output unranked weakness lists, rather than prioritizing the most consequential issues for users. In this work, we propose DIAGPaper, a novel multi-agent framework that addresses these challenges through three tightly integrated modules. The customizer module simulates human-defined review criteria and instantiates multiple reviewer agents with criterion-specific expertise. The rebuttal module introduces author agents that engage in structured debate with reviewer agents to validate and refine proposed weaknesses. The prioritizer module learns from large-scale human review practices to assess the severity of validated weaknesses and surfaces the top-K severest ones to users. Experiments on two benchmarks, AAAR and ReviewCritique, demonstrate that DIAGPaper substantially outperforms existing methods by producing more valid and more paper-specific weaknesses, while presenting them in a user-oriented, prioritized manner.

