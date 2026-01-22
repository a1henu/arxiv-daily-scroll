---
layout: default
title: Local Language Models for Context-Aware Adaptive Anonymization of Sensitive Text
---

# Local Language Models for Context-Aware Adaptive Anonymization of Sensitive Text
**arXiv**：[2601.14683v1](https://arxiv.org/abs/2601.14683) · [PDF](https://arxiv.org/pdf/2601.14683.pdf)  
**作者**：Aisvarya Adeseye, Jouni Isoaho, Seppo Virtanen, Mohammad Tahir  

**一句话要点**：提出基于本地大语言模型的上下文感知自适应匿名化框架，用于保护定性研究文本隐私。

**关键词**：文本匿名化, 本地大语言模型, 上下文感知, 隐私保护, 定性研究, 自适应框架

## 3 点简述
- 核心问题：定性研究文本包含敏感信息，手动匿名化耗时且不一致，现有自动化工具缺乏上下文理解。
- 方法要点：引入结构化自适应匿名化框架，结合检测、分类和四种匿名化策略，基于隐私标准处理标识符。
- 实验或效果：使用本地模型LLaMA和Phi评估，Phi检测敏感数据准确率超91%，情感保持率94.8%，不影响数据分析。

## 摘要（原文）

> Qualitative research often contains personal, contextual, and organizational details that pose privacy risks if not handled appropriately. Manual anonymization is time-consuming, inconsistent, and frequently omits critical identifiers. Existing automated tools tend to rely on pattern matching or fixed rules, which fail to capture context and may alter the meaning of the data. This study uses local LLMs to build a reliable, repeatable, and context-aware anonymization process for detecting and anonymizing sensitive data in qualitative transcripts. We introduce a Structured Framework for Adaptive Anonymizer (SFAA) that includes three steps: detection, classification, and adaptive anonymization. The SFAA incorporates four anonymization strategies: rule-based substitution, context-aware rewriting, generalization, and suppression. These strategies are applied based on the identifier type and the risk level. The identifiers handled by the SFAA are guided by major international privacy and research ethics standards, including the GDPR, HIPAA, and OECD guidelines. This study followed a dual-method evaluation that combined manual and LLM-assisted processing. Two case studies were used to support the evaluation. The first includes 82 face-to-face interviews on gamification in organizations. The second involves 93 machine-led interviews using an AI-powered interviewer to test LLM awareness and workplace privacy. Two local models, LLaMA and Phi were used to evaluate the performance of the proposed framework. The results indicate that the LLMs found more sensitive data than a human reviewer. Phi outperformed LLaMA in finding sensitive data, but made slightly more errors. Phi was able to find over 91% of the sensitive data and 94.8% kept the same sentiment as the original text, which means it was very accurate, hence, it does not affect the analysis of the qualitative data.

