---
layout: default
title: From Moderation to Mediation: Can LLMs Serve as Mediators in Online Flame Wars?
---

# From Moderation to Mediation: Can LLMs Serve as Mediators in Online Flame Wars?
**arXiv**：[2512.03005v1](https://arxiv.org/abs/2512.03005) · [PDF](https://arxiv.org/pdf/2512.03005.pdf)  
**作者**：Dawei Li, Abdullah Alnaibari, Arslan Bisharat, Manny Sandoval, Deborah Hall, Yasin Silva, Huan Liu  

**一句话要点**：提出LLM作为在线冲突调解者的框架，通过判断与引导任务评估其调解能力。

**关键词**：大型语言模型, 在线冲突调解, 情感分析, 对话生成, 评估框架, Reddit数据集

## 3 点简述
- 核心问题：探索LLM能否从内容审核扩展到在线冲突调解，以促进建设性对话。
- 方法要点：将调解分解为判断对话公平性与情感动态、生成共情消息引导解决两个子任务。
- 实验或效果：基于Reddit数据集评估，API模型在推理和干预对齐上优于开源模型，显示潜力与局限。

## 摘要（原文）

> The rapid advancement of large language models (LLMs) has opened new possibilities for AI for good applications. As LLMs increasingly mediate online communication, their potential to foster empathy and constructive dialogue becomes an important frontier for responsible AI research. This work explores whether LLMs can serve not only as moderators that detect harmful content, but as mediators capable of understanding and de-escalating online conflicts. Our framework decomposes mediation into two subtasks: judgment, where an LLM evaluates the fairness and emotional dynamics of a conversation, and steering, where it generates empathetic, de-escalatory messages to guide participants toward resolution. To assess mediation quality, we construct a large Reddit-based dataset and propose a multi-stage evaluation pipeline combining principle-based scoring, user simulation, and human comparison. Experiments show that API-based models outperform open-source counterparts in both reasoning and intervention alignment when doing mediation. Our findings highlight both the promise and limitations of current LLMs as emerging agents for online social mediation.

