---
layout: default
title: LADFA: A Framework of Using Large Language Models and Retrieval-Augmented Generation for Personal Data Flow Analysis in Privacy Policies
---

# LADFA: A Framework of Using Large Language Models and Retrieval-Augmented Generation for Personal Data Flow Analysis in Privacy Policies
**arXiv**：[2601.10413v1](https://arxiv.org/abs/2601.10413) · [PDF](https://arxiv.org/pdf/2601.10413.pdf)  
**作者**：Haiyue Yuan, Nikolay Matyunin, Ali Raza, Shujun Li  

**一句话要点**：提出LADFA框架，结合大语言模型与检索增强生成，用于隐私政策中的个人数据流分析。

**关键词**：隐私政策分析, 个人数据流提取, 大语言模型应用, 检索增强生成, 数据流图构建

## 3 点简述
- 隐私政策因法律语言复杂且实践不一致，难以自动化分析个人数据流。
- LADFA框架集成大语言模型与检索增强生成，基于定制知识库提取数据流并构建图。
- 通过汽车行业十个隐私政策的案例研究，验证了方法的有效性和准确性。

## 摘要（原文）

> Privacy policies help inform people about organisations' personal data processing practices, covering different aspects such as data collection, data storage, and sharing of personal data with third parties. Privacy policies are often difficult for people to fully comprehend due to the lengthy and complex legal language used and inconsistent practices across different sectors and organisations. To help conduct automated and large-scale analyses of privacy policies, many researchers have studied applications of machine learning and natural language processing techniques, including large language models (LLMs). While a limited number of prior studies utilised LLMs for extracting personal data flows from privacy policies, our approach builds on this line of work by combining LLMs with retrieval-augmented generation (RAG) and a customised knowledge base derived from existing studies. This paper presents the development of LADFA, an end-to-end computational framework, which can process unstructured text in a given privacy policy, extract personal data flows and construct a personal data flow graph, and conduct analysis of the data flow graph to facilitate insight discovery. The framework consists of a pre-processor, an LLM-based processor, and a data flow post-processor. We demonstrated and validated the effectiveness and accuracy of the proposed approach by conducting a case study that involved examining ten selected privacy policies from the automotive industry. Moreover, it is worth noting that LADFA is designed to be flexible and customisable, making it suitable for a range of text-based analysis tasks beyond privacy policy analysis.

