---
layout: default
title: Building from Scratch: A Multi-Agent Framework with Human-in-the-Loop for Multilingual Legal Terminology Mapping
---

# Building from Scratch: A Multi-Agent Framework with Human-in-the-Loop for Multilingual Legal Terminology Mapping
**arXiv**：[2512.12950v1](https://arxiv.org/abs/2512.12950) · [PDF](https://arxiv.org/pdf/2512.12950.pdf)  
**作者**：Lingyi Meng, Maolin Liu, Hao Wang, Yilan Cheng, Qi Yang, Idlkaid Mohanmmed  

**一句话要点**：提出人机协同多智能体框架以解决多语言法律术语映射的挑战

**关键词**：多语言法律术语映射, 人机协同, 多智能体框架, 大语言模型, 法律专家监督, 平行语料库

## 3 点简述
- 核心问题：中、日等语言存在大量同形异义词，现有资源和工具有限，导致法律术语跨语言映射困难。
- 方法要点：结合大语言模型与法律专家，通过多智能体系统分工处理文档预处理、对齐、术语提取等任务，强调人类监督。
- 实验或效果：基于中英日三语平行语料测试，该框架提高了映射精度和一致性，并展现出比传统方法更好的可扩展性。

## 摘要（原文）

> Accurately mapping legal terminology across languages remains a significant challenge, especially for language pairs like Chinese and Japanese, which share a large number of homographs with different meanings. Existing resources and standardized tools for these languages are limited. To address this, we propose a human-AI collaborative approach for building a multilingual legal terminology database, based on a multi-agent framework. This approach integrates advanced large language models and legal domain experts throughout the entire process-from raw document preprocessing, article-level alignment, to terminology extraction, mapping, and quality assurance. Unlike a single automated pipeline, our approach places greater emphasis on how human experts participate in this multi-agent system. Humans and AI agents take on different roles: AI agents handle specific, repetitive tasks, such as OCR, text segmentation, semantic alignment, and initial terminology extraction, while human experts provide crucial oversight, review, and supervise the outputs with contextual knowledge and legal judgment. We tested the effectiveness of this framework using a trilingual parallel corpus comprising 35 key Chinese statutes, along with their English and Japanese translations. The experimental results show that this human-in-the-loop, multi-agent workflow not only improves the precision and consistency of multilingual legal terminology mapping but also offers greater scalability compared to traditional manual methods.

