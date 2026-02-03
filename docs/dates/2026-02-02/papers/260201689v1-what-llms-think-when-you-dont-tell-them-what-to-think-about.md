---
layout: default
title: What LLMs Think When You Don't Tell Them What to Think About?
---

# What LLMs Think When You Don't Tell Them What to Think About?
**arXiv**：[2602.01689v1](https://arxiv.org/abs/2602.01689) · [PDF](https://arxiv.org/pdf/2602.01689.pdf)  
**作者**：Yongchan Kwon, James Zou  

**一句话要点**：研究大语言模型在无主题输入下的生成行为，揭示其系统性主题偏好与退化模式

**关键词**：大语言模型行为分析, 无约束生成, 主题偏好, 模型退化, AI安全监控, 数据集发布

## 3 点简述
- 核心问题：现有分析依赖特定主题提示，限制了对LLMs无约束生成行为的观察
- 方法要点：使用最小化、主题中立的输入，分析16个LLMs的256,000个样本生成内容
- 实验或效果：发现模型家族具有强主题偏好，如GPT-OSS偏向编程，Llama偏向文学，并观察到退化行为如重复短语

## 摘要（原文）

> Characterizing the behavior of large language models (LLMs) across diverse settings is critical for reliable monitoring and AI safety. However, most existing analyses rely on topic- or task-specific prompts, which can substantially limit what can be observed. In this work, we study what LLMs generate from minimal, topic-neutral inputs and probe their near-unconstrained generative behavior. Despite the absence of explicit topics, model outputs cover a broad semantic space, and surprisingly, each model family exhibits strong and systematic topical preferences. GPT-OSS predominantly generates programming (27.1%) and mathematical content (24.6%), whereas Llama most frequently generates literary content (9.1%). DeepSeek often generates religious content, while Qwen frequently generates multiple-choice questions. Beyond topical preferences, we also observe differences in content specialization and depth: GPT-OSS often generates more technically advanced content (e.g., dynamic programming) compared with other models (e.g., basic Python). Furthermore, we find that the near-unconstrained generation often degenerates into repetitive phrases, revealing interesting behaviors unique to each model family. For instance, degenerate outputs from Llama include multiple URLs pointing to personal Facebook and Instagram accounts. We release the complete dataset of 256,000 samples from 16 LLMs, along with a reproducible codebase.

