---
layout: default
title: A model of errors in transformers
---

# A model of errors in transformers
**arXiv**：[2601.14175v1](https://arxiv.org/abs/2601.14175) · [PDF](https://arxiv.org/pdf/2601.14175.pdf)  
**作者**：Suvrat Raju, Praneeth Netrapalli  

**一句话要点**：提出基于注意力误差累积的Transformer错误率模型，用于预测LLM在确定性任务中的准确性。

**关键词**：Transformer错误分析, 注意力机制误差, 确定性任务准确性, 双参数模型, LLM实证测试

## 3 点简述
- 研究LLM在算术等确定性任务中的错误率，关注小误差在注意力机制中的累积效应。
- 建立双参数模型，将错误率与任务复杂度关联，参数可解释为基本噪声率和错误令牌数。
- 使用Gemini和DeepSeek模型进行实证测试，模型预测与观测准确性高度一致，但存在未知偏差。

## 摘要（原文）

> We study the error rate of LLMs on tasks like arithmetic that require a deterministic output, and repetitive processing of tokens drawn from a small set of alternatives. We argue that incorrect predictions arise when small errors in the attention mechanism accumulate to cross a threshold, and use this insight to derive a quantitative two-parameter relationship between the accuracy and the complexity of the task. The two parameters vary with the prompt and the model; they can be interpreted in terms of an elementary noise rate, and the number of plausible erroneous tokens that can be predicted. Our analysis is inspired by an ``effective field theory'' perspective: the LLM's many raw parameters can be reorganized into just two parameters that govern the error rate. We perform extensive empirical tests, using Gemini 2.5 Flash, Gemini 2.5 Pro and DeepSeek R1, and find excellent agreement between the predicted and observed accuracy for a variety of tasks, although we also identify deviations in some cases. Our model provides an alternative to suggestions that errors made by LLMs on long repetitive tasks indicate the ``collapse of reasoning'', or an inability to express ``compositional'' functions. Finally, we show how to construct prompts to reduce the error rate.

