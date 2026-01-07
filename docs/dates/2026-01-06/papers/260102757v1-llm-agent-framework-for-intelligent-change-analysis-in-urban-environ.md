---
layout: default
title: LLM Agent Framework for Intelligent Change Analysis in Urban Environment using Remote Sensing Imagery
---

# LLM Agent Framework for Intelligent Change Analysis in Urban Environment using Remote Sensing Imagery
**arXiv**：[2601.02757v1](https://arxiv.org/abs/2601.02757) · [PDF](https://arxiv.org/pdf/2601.02757.pdf)  
**作者**：Zixuan Xiao, Jun Ma  

**一句话要点**：提出ChangeGPT框架，集成大语言模型与视觉基础模型，用于遥感影像的智能城市环境变化分析。

**关键词**：遥感影像分析, 变化检测, 大语言模型, 智能代理框架, 城市环境监测

## 3 点简述
- 现有变化检测方法缺乏处理多样化查询和全面分析的智能性。
- 采用分层结构集成LLM与视觉模型，减少幻觉，支持多步推理和工具选择。
- 在140个问题数据集上评估，GPT-4-turbo后端达到90.71%匹配率，并在深圳前海湾案例中验证实用性。

## 摘要（原文）

> Existing change detection methods often lack the versatility to handle diverse real-world queries and the intelligence for comprehensive analysis. This paper presents a general agent framework, integrating Large Language Models (LLM) with vision foundation models to form ChangeGPT. A hierarchical structure is employed to mitigate hallucination. The agent was evaluated on a curated dataset of 140 questions categorized by real-world scenarios, encompassing various question types (e.g., Size, Class, Number) and complexities. The evaluation assessed the agent's tool selection ability (Precision/Recall) and overall query accuracy (Match). ChangeGPT, especially with a GPT-4-turbo backend, demonstrated superior performance, achieving a 90.71 % Match rate. Its strength lies particularly in handling change-related queries requiring multi-step reasoning and robust tool selection. Practical effectiveness was further validated through a real-world urban change monitoring case study in Qianhai Bay, Shenzhen. By providing intelligence, adaptability, and multi-type change analysis, ChangeGPT offers a powerful solution for decision-making in remote sensing applications.

