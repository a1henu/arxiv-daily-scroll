---
layout: default
title: Evaluating LLM Alignment With Human Trust Models
---

# Evaluating LLM Alignment With Human Trust Models
**arXiv**：[2603.05839v1](https://arxiv.org/abs/2603.05839) · [PDF](https://arxiv.org/pdf/2603.05839.pdf)  
**作者**：Anushka Debnath, Stephen Cranefield, Bastin Tony Roy Savarimuthu, Emiliano Lorini  

**一句话要点**：提出白盒分析方法，评估GPT-J-6B内部信任表示与人类信任模型的对齐度。

**关键词**：信任表示, 白盒分析, 对比提示, 嵌入向量, 社会认知模型, LLM对齐

## 3 点简述
- 核心问题：LLM内部如何表示和推理信任，缺乏深入理解。
- 方法要点：使用对比提示生成嵌入向量，分析激活空间中的信任表示。
- 实验或效果：GPT-J-6B的信任表示最接近Castelfranchi模型，支持社会认知理论分析。

## 摘要（原文）

> Trust plays a pivotal role in enabling effective cooperation, reducing uncertainty, and guiding decision-making in both human interactions and multi-agent systems. Although it is significant, there is limited understanding of how large language models (LLMs) internally conceptualize and reason about trust. This work presents a white-box analysis of trust representation in EleutherAI/gpt-j-6B, using contrastive prompting to generate embedding vectors within the activation space of the LLM for diadic trust and related interpersonal relationship attributes. We first identified trust-related concepts from five established human trust models. We then determined a threshold for significant conceptual alignment by computing pairwise cosine similarities across 60 general emotional concepts. Then we measured the cosine similarities between the LLM's internal representation of trust and the derived trust-related concepts. Our results show that the internal trust representation of EleutherAI/gpt-j-6B aligns most closely with the Castelfranchi socio-cognitive model, followed by the Marsh Model. These findings indicate that LLMs encode socio-cognitive constructs in their activation space in ways that support meaningful comparative analyses, inform theories of social cognition, and support the design of human-AI collaborative systems.

