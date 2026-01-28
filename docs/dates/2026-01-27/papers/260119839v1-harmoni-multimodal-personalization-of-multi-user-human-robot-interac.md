---
layout: default
title: HARMONI: Multimodal Personalization of Multi-User Human-Robot Interactions with LLMs
---

# HARMONI: Multimodal Personalization of Multi-User Human-Robot Interactions with LLMs
**arXiv**：[2601.19839v1](https://arxiv.org/abs/2601.19839) · [PDF](https://arxiv.org/pdf/2601.19839.pdf)  
**作者**：Jeanne Malécot, Hamed Rahimi, Jeanne Cattoni, Marie Samson, Mouad Abrini, Mahdi Khoramshahi, Maribel Pino, Mohamed Chetouani  

**一句话要点**：提出HARMONI框架，利用大语言模型实现多用户人机交互中的多模态个性化与动态适应。

**关键词**：多模态人机交互, 大语言模型, 个性化框架, 多用户环境, 社会辅助机器人

## 3 点简述
- 现有系统缺乏多用户环境下的持续个性化与动态适应机制，限制实际部署效果。
- 框架整合感知、世界建模、用户建模和生成模块，支持长期多用户交互管理。
- 在四个数据集和养老院场景的用户研究中，HARMONI在用户建模准确性和个性化质量上优于基线方法。

## 摘要（原文）

> Existing human-robot interaction systems often lack mechanisms for sustained personalization and dynamic adaptation in multi-user environments, limiting their effectiveness in real-world deployments. We present HARMONI, a multimodal personalization framework that leverages large language models to enable socially assistive robots to manage long-term multi-user interactions. The framework integrates four key modules: (i) a perception module that identifies active speakers and extracts multimodal input; (ii) a world modeling module that maintains representations of the environment and short-term conversational context; (iii) a user modeling module that updates long-term speaker-specific profiles; and (iv) a generation module that produces contextually grounded and ethically informed responses. Through extensive evaluation and ablation studies on four datasets, as well as a real-world scenario-driven user-study in a nursing home environment, we demonstrate that HARMONI supports robust speaker identification, online memory updating, and ethically aligned personalization, outperforming baseline LLM-driven approaches in user modeling accuracy, personalization quality, and user satisfaction.

