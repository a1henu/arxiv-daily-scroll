---
layout: default
title: Assessing the Software Security Comprehension of Large Language Models
---

# Assessing the Software Security Comprehension of Large Language Models
**arXiv**：[2512.21238v1](https://arxiv.org/abs/2512.21238) · [PDF](https://arxiv.org/pdf/2512.21238.pdf)  
**作者**：Mohammed Latif Siddiq, Natalie Sekerak, Antonio Karam, Maria Leal, Arvin Islam-Gomes, Joanna C. S. Santos  

**一句话要点**：评估五大LLM在软件安全理解上的认知边界与误区模式

**关键词**：软件安全评估, 大型语言模型, 布鲁姆分类法, 认知维度分析, 安全知识边界, 误区模式识别

## 3 点简述
- 核心问题：LLM在软件开发中应用广泛，但其软件安全专业知识水平尚不明确
- 方法要点：基于布鲁姆分类法，系统评估LLM在六个认知维度的安全理解能力
- 实验或效果：LLM在低阶任务表现良好，高阶任务性能显著下降，识别出51个常见误区模式

## 摘要（原文）

> Large language models (LLMs) are increasingly used in software development, but their level of software security expertise remains unclear. This work systematically evaluates the security comprehension of five leading LLMs: GPT-4o-Mini, GPT-5-Mini, Gemini-2.5-Flash, Llama-3.1, and Qwen-2.5, using Blooms Taxonomy as a framework. We assess six cognitive dimensions: remembering, understanding, applying, analyzing, evaluating, and creating. Our methodology integrates diverse datasets, including curated multiple-choice questions, vulnerable code snippets (SALLM), course assessments from an Introduction to Software Security course, real-world case studies (XBOW), and project-based creation tasks from a Secure Software Engineering course. Results show that while LLMs perform well on lower-level cognitive tasks such as recalling facts and identifying known vulnerabilities, their performance degrades significantly on higher-order tasks that require reasoning, architectural evaluation, and secure system creation. Beyond reporting aggregate accuracy, we introduce a software security knowledge boundary that identifies the highest cognitive level at which a model consistently maintains reliable performance. In addition, we identify 51 recurring misconception patterns exhibited by LLMs across Blooms levels.

