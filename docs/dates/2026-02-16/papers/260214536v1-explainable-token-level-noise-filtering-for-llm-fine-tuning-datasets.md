---
layout: default
title: Explainable Token-level Noise Filtering for LLM Fine-tuning Datasets
---

# Explainable Token-level Noise Filtering for LLM Fine-tuning Datasets
**arXiv**：[2602.14536v1](https://arxiv.org/abs/2602.14536) · [PDF](https://arxiv.org/pdf/2602.14536.pdf)  
**作者**：Yuchen Yang, Wenze Lin, Enhao Huang, Zhixuan Chu, Hongbin Zhou, Lan Tao, Yiming Li, Zhan Qin, Kui Ren  

**一句话要点**：提出可解释的令牌级噪声过滤框架XTF，以优化大语言模型微调数据集性能。

**关键词**：大语言模型微调, 令牌级噪声过滤, 可解释性框架, 数据集优化, 梯度屏蔽, 下游任务性能

## 3 点简述
- 核心问题：句子级微调数据集与令牌级优化机制不匹配，引入令牌级噪声影响性能。
- 方法要点：将令牌贡献分解为推理重要性、知识新颖性和任务相关性三个属性，通过评分方法评估并屏蔽噪声令牌梯度。
- 实验或效果：在数学、代码和医学任务上测试7个主流大语言模型，下游性能提升最高达13.7%。

## 摘要（原文）

> Large Language Models (LLMs) have seen remarkable advancements, achieving state-of-the-art results in diverse applications. Fine-tuning, an important step for adapting LLMs to specific downstream tasks, typically involves further training on corresponding datasets. However, a fundamental discrepancy exists between current fine-tuning datasets and the token-level optimization mechanism of LLMs: most datasets are designed at the sentence-level, which introduces token-level noise, causing negative influence to final performance. In this paper, we propose XTF, an explainable token-level noise filtering framework. XTF decomposes the complex and subtle contributions of token-level data to the fine-tuning process into three distinct and explicit attributes (reasoning importance, knowledge novelty, and task relevance), which can be assessed using scoring methods, and then masks the gradients of selected noisy tokens accordingly to optimize the performance of fine-tuned LLMs. We conduct extensive experiments on three representative downstream tasks (math, code and medicine) across 7 mainstream LLMs. The results demonstrate that XTF can significantly improve downstream performance by up to 13.7% compared to regular fine-tuning. Our work highlights the importance of token-level dataset optimization, and demonstrates the potential of strategies based on attribute decomposition for explaining complex training mechanisms.

