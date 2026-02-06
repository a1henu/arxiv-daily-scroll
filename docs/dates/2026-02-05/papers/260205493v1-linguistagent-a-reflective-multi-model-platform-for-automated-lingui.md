---
layout: default
title: LinguistAgent: A Reflective Multi-Model Platform for Automated Linguistic Annotation
---

# LinguistAgent: A Reflective Multi-Model Platform for Automated Linguistic Annotation
**arXiv**：[2602.05493v1](https://arxiv.org/abs/2602.05493) · [PDF](https://arxiv.org/pdf/2602.05493.pdf)  
**作者**：Bingru Li  

**一句话要点**：提出LinguistAgent平台，通过反思性多模型架构自动化语言标注，解决人文学科数据标注瓶颈。

**关键词**：语言标注自动化, 反思性多模型架构, 隐喻识别, 双代理工作流, 实时评估

## 3 点简述
- 核心问题：人文学科中复杂语义任务（如隐喻识别）的数据标注效率低下，LLMs理论能力与实际应用存在差距。
- 方法要点：采用双代理工作流（标注者与审阅者）模拟同行评审，支持提示工程、检索增强生成和微调三种范式比较。
- 实验或效果：以隐喻识别为例，提供实时令牌级评估（精确率、召回率、F1分数），对比人类黄金标准，展示平台有效性。

## 摘要（原文）

> Data annotation remains a significant bottleneck in the Humanities and Social Sciences, particularly for complex semantic tasks such as metaphor identification. While Large Language Models (LLMs) show promise, a significant gap remains between the theoretical capability of LLMs and their practical utility for researchers. This paper introduces LinguistAgent, an integrated, user-friendly platform that leverages a reflective multi-model architecture to automate linguistic annotation. The system implements a dual-agent workflow, comprising an Annotator and a Reviewer, to simulate a professional peer-review process. LinguistAgent supports comparative experiments across three paradigms: Prompt Engineering (Zero/Few-shot), Retrieval-Augmented Generation, and Fine-tuning. We demonstrate LinguistAgent's efficacy using the task of metaphor identification as an example, providing real-time token-level evaluation (Precision, Recall, and $F_1$ score) against human gold standards. The application and codes are released on https://github.com/Bingru-Li/LinguistAgent.

