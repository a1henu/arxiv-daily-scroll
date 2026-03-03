---
layout: default
title: Retrieval, Refinement, and Ranking for Text-to-Video Generation via Prompt Optimization and Test-Time Scaling
---

# Retrieval, Refinement, and Ranking for Text-to-Video Generation via Prompt Optimization and Test-Time Scaling
**arXiv**：[2603.01509v1](https://arxiv.org/abs/2603.01509) · [PDF](https://arxiv.org/pdf/2603.01509.pdf)  
**作者**：Zillur Rahman, Alex Sheng, Cristian Meo  

**一句话要点**：提出3R框架，通过提示优化和测试时缩放提升文本到视频生成质量

**关键词**：文本到视频生成, 提示优化, 检索增强生成, 扩散模型, 时序一致性

## 3 点简述
- 核心问题：现有文本到视频模型对输入提示敏感，依赖后处理或微调，可扩展性和可访问性受限
- 方法要点：基于RAG提取修饰符增强上下文，扩散偏好优化对齐人类偏好，时间帧插值确保时序一致性
- 实验或效果：实验显示3R能提高生成视频的静态保真度和动态连贯性，无需模型训练

## 摘要（原文）

> While large-scale datasets have driven significant progress in Text-to-Video (T2V) generative models, these models remain highly sensitive to input prompts, demonstrating that prompt design is critical to generation quality. Current methods for improving video output often fall short: they either depend on complex, post-editing models, risking the introduction of artifacts, or require expensive fine-tuning of the core generator, which severely limits both scalability and accessibility. In this work, we introduce 3R, a novel RAG based prompt optimization framework. 3R utilizes the power of current state-of-the-art T2V diffusion model and vision language model. It can be used with any T2V model without any kind of model training. The framework leverages three key strategies: RAG-based modifiers extraction for enriched contextual grounding, diffusion-based Preference Optimization for aligning outputs with human preferences, and temporal frame interpolation for producing temporally consistent visual contents. Together, these components enable more accurate, efficient, and contextually aligned text-to-video generation. Experimental results demonstrate the efficacy of 3R in enhancing the static fidelity and dynamic coherence of generated videos, underscoring the importance of optimizing user prompts.

