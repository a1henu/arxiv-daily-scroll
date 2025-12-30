---
layout: default
title: Multilingual Hidden Prompt Injection Attacks on LLM-Based Academic Reviewing
---

# Multilingual Hidden Prompt Injection Attacks on LLM-Based Academic Reviewing
**arXiv**：[2512.23684v1](https://arxiv.org/abs/2512.23684) · [PDF](https://arxiv.org/pdf/2512.23684.pdf)  
**作者**：Panagiotis Theocharopoulos, Ajinkya Kulkarni, Mathew Magimai. -Doss  

**一句话要点**：评估多语言隐藏提示注入攻击对基于LLM的学术评审的影响

**关键词**：隐藏提示注入攻击, 多语言对抗攻击, 学术评审系统, 大型语言模型安全, 文档级攻击

## 3 点简述
- 核心问题：LLM在学术评审中易受文档级隐藏提示注入攻击
- 方法要点：在约500篇ICML论文中嵌入四种语言的语义等效对抗提示
- 实验或效果：英语、日语和中文注入显著改变评审分数和决策，阿拉伯语影响未知

## 摘要（原文）

> Large language models (LLMs) are increasingly considered for use in high-impact workflows, including academic peer review. However, LLMs are vulnerable to document-level hidden prompt injection attacks. In this work, we construct a dataset of approximately 500 real academic papers accepted to ICML and evaluate the effect of embedding hidden adversarial prompts within these documents. Each paper is injected with semantically equivalent instructions in four different languages and reviewed using an LLM. We find that prompt injection induces substantial changes in review scores and accept/reject decisions for English, Japanese, and Chinese injections, while Arabic injections produce little to no effect. These results highlight the susceptibility of LLM-based reviewing systems to document-level prompt injection and reveal notable differences in vulnerability across languages.

