---
layout: default
title: CurricuLLM: Designing Personalized and Workforce-Aligned Cybersecurity Curricula Using Fine-Tuned LLMs
---

# CurricuLLM: Designing Personalized and Workforce-Aligned Cybersecurity Curricula Using Fine-Tuned LLMs
**arXiv**：[2601.04940v1](https://arxiv.org/abs/2601.04940) · [PDF](https://arxiv.org/pdf/2601.04940.pdf)  
**作者**：Arthur Nijdam, Harri Kähkönen, Valtteri Niemi, Paul Stankovski Wagner, Sara Ramezanian  

**一句话要点**：提出CurricuLLM框架，利用微调LLM自动化设计个性化网络安全课程以解决教育与行业需求脱节问题。

**关键词**：网络安全课程设计, 大型语言模型微调, BERT模型, 个性化教育, 行业需求对齐

## 3 点简述
- 核心问题：网络安全课程设计成本高、更新慢，导致毕业生技能与行业需求脱节。
- 方法要点：采用两阶段框架，包括数据预处理和基于BERT的课程内容分类，实现自动化课程设计。
- 实验或效果：通过专家验证，证明CurricuLLM能高效替代人工分析，并支持课程与岗位需求对齐。

## 摘要（原文）

> The cybersecurity landscape is constantly evolving, driven by increased digitalization and new cybersecurity threats. Cybersecurity programs often fail to equip graduates with skills demanded by the workforce, particularly concerning recent developments in cybersecurity, as curriculum design is costly and labor-intensive. To address this misalignment, we present a novel Large Language Model (LLM)-based framework for automated design and analysis of cybersecurity curricula, called CurricuLLM. Our approach provides three key contributions: (1) automation of personalized curriculum design, (2) a data-driven pipeline aligned with industry demands, and (3) a comprehensive methodology for leveraging fine-tuned LLMs in curriculum development.
>   CurricuLLM utilizes a two-tier approach consisting of PreprocessLM, which standardizes input data, and ClassifyLM, which assigns course content to nine Knowledge Areas in cybersecurity. We systematically evaluated multiple Natural Language Processing (NLP) architectures and fine-tuning strategies, ultimately selecting the Bidirectional Encoder Representations from Transformers (BERT) model as ClassifyLM, fine-tuned on foundational cybersecurity concepts and workforce competencies.
>   We are the first to validate our method with human experts who analyzed real-world cybersecurity curricula and frameworks, motivating that CurricuLLM is an efficient solution to replace labor-intensive curriculum analysis. Moreover, once course content has been classified, it can be integrated with established cybersecurity role-based weights, enabling alignment of the educational program with specific job roles, workforce categories, or general market needs. This lays the foundation for personalized, workforce-aligned cybersecurity curricula that prepare students for the evolving demands in cybersecurity.

