---
layout: default
title: SparkMe: Adaptive Semi-Structured Interviewing for Qualitative Insight Discovery
---

# SparkMe: Adaptive Semi-Structured Interviewing for Qualitative Insight Discovery
**arXiv**：[2602.21136v1](https://arxiv.org/abs/2602.21136) · [PDF](https://arxiv.org/pdf/2602.21136.pdf)  
**作者**：David Anugraha, Vishakh Padmakumar, Diyi Yang  

**一句话要点**：提出SparkMe多智能体LLM面试系统，通过优化问题选择实现自适应半结构化访谈以提升定性洞察发现。

**关键词**：自适应访谈, 大语言模型, 多智能体系统, 优化问题, 定性洞察发现, 半结构化访谈

## 3 点简述
- 核心问题：现有LLM自动化访谈系统缺乏平衡预定义主题覆盖与自适应探索的机制，难以处理对话中涌现的主题。
- 方法要点：将自适应半结构化访谈建模为优化问题，基于覆盖度、发现度和成本定义效用，采用多智能体LLM进行模拟对话规划以选择高效用问题。
- 实验或效果：在基于LLM的受控实验中，SparkMe相比基线提高了主题指南覆盖度4.7%，并能在更少对话轮次中引发更丰富的涌现洞察。

## 摘要（原文）

> Qualitative insights from user experiences are critical for informing product and policy decisions, but collecting such data at scale is constrained by the time and availability of experts to conduct semi-structured interviews. Recent work has explored using large language models (LLMs) to automate interviewing, yet existing systems lack a principled mechanism for balancing systematic coverage of predefined topics with adaptive exploration, or the ability to pursue follow-ups, deep dives, and emergent themes that arise organically during conversation. In this work, we formulate adaptive semi-structured interviewing as an optimization problem over the interviewer's behavior. We define interview utility as a trade-off between coverage of a predefined interview topic guide, discovery of relevant emergent themes, and interview cost measured by length. Based on this formulation, we introduce SparkMe, a multi-agent LLM interviewer that performs deliberative planning via simulated conversation rollouts to select questions with high expected utility. We evaluate SparkMe through controlled experiments with LLM-based interviewees, showing that it achieves higher interview utility, improving topic guide coverage (+4.7% over the best baseline) and eliciting richer emergent insights while using fewer conversational turns than prior LLM interviewing approaches. We further validate SparkMe in a user study with 70 participants across 7 professions on the impact of AI on their workflows. Domain experts rate SparkMe as producing high-quality adaptive interviews that surface helpful profession-specific insights not captured by prior approaches. The code, datasets, and evaluation protocols for SparkMe are available as open-source at https://github.com/SALT-NLP/SparkMe.

