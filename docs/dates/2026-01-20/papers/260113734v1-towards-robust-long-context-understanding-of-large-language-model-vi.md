---
layout: default
title: Towards robust long-context understanding of large language model via active recap learning
---

# Towards robust long-context understanding of large language model via active recap learning
**arXiv**：[2601.13734v1](https://arxiv.org/abs/2601.13734) · [PDF](https://arxiv.org/pdf/2601.13734.pdf)  
**作者**：Chenyu Hui  

**一句话要点**：提出主动回顾学习框架以增强大语言模型的长上下文理解能力

**关键词**：长上下文理解, 主动回顾学习, 持续预训练, 递归记忆机制, 大语言模型增强

## 3 点简述
- 核心问题：大语言模型在长上下文理解中存在性能瓶颈，需提升记忆与信息整合能力。
- 方法要点：通过损失差距识别关键令牌，构建序列进行持续预训练，并在推理时自主生成回顾摘要。
- 实验或效果：在RULER和LongBench基准上分别实现26.8%和9.44%的性能提升。

## 摘要（原文）

> In this paper, we propose active recap learning (ARL), a framework for enhancing large language model (LLM) in understanding long contexts. ARL enables models to revisit and summarize earlier content through targeted sequence construction during contined pretraining and retrospective summarization at inference. First, we identify key tokens in prepared long context based on loss gaps between long and short forward contexts and find most revant preceding paragraphs, then summarize them using an LLM. Second, ARL equips models with the ability to autonomously generate and utilize these retrospective summaries during inference, thereby establishing a recursive memory mechanism across paragraphs. Experimental results show substantial gains, with ARL achieving a 26.8% improvement on RULER and a 9.44% improvement on LongBench. Overall, ARL offers a simple yet effective continued pretraining-based approach to strengthen long-context understanding, advancing scalable memory augmentation in LLM

