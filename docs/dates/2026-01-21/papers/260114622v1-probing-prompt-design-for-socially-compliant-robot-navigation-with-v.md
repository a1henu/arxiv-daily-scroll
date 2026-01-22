---
layout: default
title: Probing Prompt Design for Socially Compliant Robot Navigation with Vision Language Models
---

# Probing Prompt Design for Socially Compliant Robot Navigation with Vision Language Models
**arXiv**：[2601.14622v1](https://arxiv.org/abs/2601.14622) · [PDF](https://arxiv.org/pdf/2601.14622.pdf)  
**作者**：Ling Xiao, Toshihiko Yamasaki  

**一句话要点**：提出基于认知理论的提示设计方法，以提升小型视觉语言模型在社交机器人导航中的决策准确性。

**关键词**：社交机器人导航, 视觉语言模型, 提示设计, 决策约束, 动机框架, 微调对比

## 3 点简述
- 核心问题：现有社交机器人导航基准忽视提示设计，小型视觉语言模型决策能力弱，影响导航准确性。
- 方法要点：从系统指导（动作、推理、感知推理提示）和动机框架（竞争人类、AI或自身）两个维度设计提示。
- 实验或效果：实验显示，提示设计能显著提升动作准确性，优于直接微调，并揭示模型、数据集与提示的耦合效应。

## 摘要（原文）

> Language models are increasingly used for social robot navigation, yet existing benchmarks largely overlook principled prompt design for socially compliant behavior. This limitation is particularly relevant in practice, as many systems rely on small vision language models (VLMs) for efficiency. Compared to large language models, small VLMs exhibit weaker decision-making capabilities, making effective prompt design critical for accurate navigation. Inspired by cognitive theories of human learning and motivation, we study prompt design along two dimensions: system guidance (action-focused, reasoning-oriented, and perception-reasoning prompts) and motivational framing, where models compete against humans, other AI systems, or their past selves. Experiments on two socially compliant navigation datasets reveal three key findings. First, for non-finetuned GPT-4o, competition against humans achieves the best performance, while competition against other AI systems performs worst. For finetuned models, competition against the model's past self yields the strongest results, followed by competition against humans, with performance further influenced by coupling effects among prompt design, model choice, and dataset characteristics. Second, inappropriate system prompt design can significantly degrade performance, even compared to direct finetuning. Third, while direct finetuning substantially improves semantic-level metrics such as perception, prediction, and reasoning, it yields limited gains in action accuracy. In contrast, our system prompts produce a disproportionately larger improvement in action accuracy, indicating that the proposed prompt design primarily acts as a decision-level constraint rather than a representational enhancement.

