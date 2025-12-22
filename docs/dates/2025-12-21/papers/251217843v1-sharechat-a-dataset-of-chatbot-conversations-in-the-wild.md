---
layout: default
title: ShareChat: A Dataset of Chatbot Conversations in the Wild
---

# ShareChat: A Dataset of Chatbot Conversations in the Wild
**arXiv**：[2512.17843v1](https://arxiv.org/abs/2512.17843) · [PDF](https://arxiv.org/pdf/2512.17843.pdf)  
**作者**：Yueru Yan, Tuc Nguyen, Bo Su, Melissa Lieffers, Thai Le  

**一句话要点**：提出ShareChat数据集以解决现有公开数据集缺乏界面上下文的问题

**关键词**：聊天机器人对话数据集, 跨平台数据收集, 界面上下文保留, 多语言对话分析, 用户交互研究

## 3 点简述
- 核心问题：现有数据集将LLMs视为通用文本生成器，忽略了界面设计对用户交互的影响
- 方法要点：收集142,808个跨平台对话，保留推理痕迹、来源链接等原生平台特性
- 实验或效果：通过对话完整性、引用行为和时间分析展示数据集的多方面应用价值

## 摘要（原文）

> While Large Language Models (LLMs) have evolved into distinct platforms with unique interface designs and capabilities, existing public datasets treat models as generic text generators, stripping away the interface context that actively shapes user interaction. To address this limitation, we present ShareChat, a large-scale, cross-platform corpus comprising 142,808 conversations and over 660,000 turns collected from publicly shared URLs across five major platforms: ChatGPT, Claude, Gemini, Perplexity, and Grok. ShareChat distinguishes itself by preserving native platform affordances often lost in standard logs, including reasoning traces, source links, and code artifacts, while spanning 101 languages over the period from April 2023 to October 2025. Furthermore, ShareChat offers substantially longer context windows and greater interaction depth than prior datasets. We demonstrate the dataset's multifaceted utility through three representative analyses: (1) analyzing conversation completeness to measure user intent satisfaction; (2) evaluating source citation behaviors in content generation; and (3) conducting temporal analysis to track evolving usage patterns. This work provides the community with a vital and timely resource for understanding authentic user-LLM chatbot interactions in the wild.

