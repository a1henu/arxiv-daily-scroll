---
layout: default
title: What Do LLMs Associate with Your Name? A Human-Centered Black-Box Audit of Personal Data
---

# What Do LLMs Associate with Your Name? A Human-Centered Black-Box Audit of Personal Data
**arXiv**：[2602.17483v1](https://arxiv.org/abs/2602.17483) · [PDF](https://arxiv.org/pdf/2602.17483.pdf)  
**作者**：Dimitri Staufer, Kirsten Morehouse  

**一句话要点**：提出LMP2工具以审计LLMs对个人数据的关联，揭示模型生成PD的准确性与用户隐私担忧。

**关键词**：个人数据审计, 语言模型隐私, 黑盒评估, 用户中心设计, 数据隐私权利

## 3 点简述
- 核心问题：LLMs在训练和交互中暴露于个人数据，用户缺乏对模型如何关联信息到其身份的洞察。
- 方法要点：开发LMP2，一种以人为中心、保护隐私的审计工具，通过形成性研究优化，用于评估LLMs的PD关联。
- 实验或效果：实证显示模型对知名个体生成多类PD，GPT-4o对日常用户生成11个特征准确率≥60%，72%参与者寻求控制关联。

## 摘要（原文）

> Large language models (LLMs), and conversational agents based on them, are exposed to personal data (PD) during pre-training and during user interactions. Prior work shows that PD can resurface, yet users lack insight into how strongly models associate specific information to their identity. We audit PD across eight LLMs (3 open-source; 5 API-based, including GPT-4o), introduce LMP2 (Language Model Privacy Probe), a human-centered, privacy-preserving audit tool refined through two formative studies (N=20), and run two studies with EU residents to capture (i) intuitions about LLM-generated PD (N1=155) and (ii) reactions to tool output (N2=303). We show empirically that models confidently generate multiple PD categories for well-known individuals. For everyday users, GPT-4o generates 11 features with 60% or more accuracy (e.g., gender, hair color, languages). Finally, 72% of participants sought control over model-generated associations with their name, raising questions about what counts as PD and whether data privacy rights should extend to LLMs.

