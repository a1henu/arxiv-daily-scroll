---
layout: default
title: Population-Aligned Audio Reproduction With LLM-Based Equalizers
---

# Population-Aligned Audio Reproduction With LLM-Based Equalizers
**arXiv**：[2601.09448v1](https://arxiv.org/abs/2601.09448) · [PDF](https://arxiv.org/pdf/2601.09448.pdf)  
**作者**：Ioannis Stylianou, Jon Francombe, Pablo Martinez-Nuevo, Sven Ewan Shepstone, Zheng-Hua Tan  

**一句话要点**：提出基于大语言模型的均衡器，通过自然语言提示实现人群对齐的音频均衡调整。

**关键词**：音频均衡, 大语言模型, 自然语言处理, 上下文学习, 参数高效微调, 分布对齐

## 3 点简述
- 传统音频均衡需手动调整，难以适应动态听音场景。
- 利用LLM将文本提示映射到均衡设置，支持对话式系统控制。
- 通过受控实验数据，模型在分布对齐上显著优于随机和静态基线。

## 摘要（原文）

> Conventional audio equalization is a static process that requires manual and cumbersome adjustments to adapt to changing listening contexts (e.g., mood, location, or social setting). In this paper, we introduce a Large Language Model (LLM)-based alternative that maps natural language text prompts to equalization settings. This enables a conversational approach to sound system control. By utilizing data collected from a controlled listening experiment, our models exploit in-context learning and parameter-efficient fine-tuning techniques to reliably align with population-preferred equalization settings. Our evaluation methods, which leverage distributional metrics that capture users' varied preferences, show statistically significant improvements in distributional alignment over random sampling and static preset baselines. These results indicate that LLMs could function as "artificial equalizers," contributing to the development of more accessible, context-aware, and expert-level audio tuning methods.

