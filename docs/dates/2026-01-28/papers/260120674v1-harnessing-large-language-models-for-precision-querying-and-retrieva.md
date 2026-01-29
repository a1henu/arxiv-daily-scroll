---
layout: default
title: Harnessing Large Language Models for Precision Querying and Retrieval-Augmented Knowledge Extraction in Clinical Data Science
---

# Harnessing Large Language Models for Precision Querying and Retrieval-Augmented Knowledge Extraction in Clinical Data Science
**arXiv**：[2601.20674v1](https://arxiv.org/abs/2601.20674) · [PDF](https://arxiv.org/pdf/2601.20674.pdf)  
**作者**：Juan Jose Rubio Jan, Jack Wu, Julia Ive  

**一句话要点**：应用大语言模型于临床数据科学，支持结构化查询与非结构化文本信息提取

**关键词**：大语言模型, 临床数据科学, 检索增强生成, 电子健康记录, 结构化查询, 信息提取

## 3 点简述
- 核心问题：评估大语言模型在电子健康记录结构化数据查询和非结构化临床文本信息提取中的准确性与可靠性
- 方法要点：采用检索增强生成管道和自动生成合成问答对的灵活评估框架，结合本地与API模型
- 实验或效果：在MIMIC III数据集上测试，结合精确匹配、语义相似度和人工评估，展示模型潜力

## 摘要（原文）

> This study applies Large Language Models (LLMs) to two foundational Electronic Health Record (EHR) data science tasks: structured data querying (using programmatic languages, Python/Pandas) and information extraction from unstructured clinical text via a Retrieval Augmented Generation (RAG) pipeline. We test the ability of LLMs to interact accurately with large structured datasets for analytics and the reliability of LLMs in extracting semantically correct information from free text health records when supported by RAG. To this end, we presented a flexible evaluation framework that automatically generates synthetic question and answer pairs tailored to the characteristics of each dataset or task. Experiments were conducted on a curated subset of MIMIC III, (four structured tables and one clinical note type), using a mix of locally hosted and API-based LLMs. Evaluation combined exact-match metrics, semantic similarity, and human judgment. Our findings demonstrate the potential of LLMs to support precise querying and accurate information extraction in clinical workflows.

