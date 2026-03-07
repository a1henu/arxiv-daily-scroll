---
layout: default
title: Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation
---

# Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation
**arXiv**：[2603.05494v1](https://arxiv.org/abs/2603.05494) · [PDF](https://arxiv.org/pdf/2603.05494.pdf)  
**作者**：Helena Casademunt, Bartosz Cywiński, Khoi Tran, Arya Jakkli, Samuel Marks, Neel Nanda  

**一句话要点**：利用中文开源LLMs作为自然测试平台，评估秘密知识诱导与谎言检测技术

**关键词**：诚实诱导, 谎言检测, 开源语言模型, 审查机制, 秘密知识, 模型评估

## 3 点简述
- 研究核心问题：评估诚实诱导与谎言检测方法在自然发生不诚实场景中的有效性，而非人工构造的谎言模型
- 方法要点：以中文开发者开源LLMs为测试平台，这些模型因政治敏感话题训练而审查，产生虚假响应
- 实验或效果：发现采样无聊天模板、少样本提示和通用诚实数据微调最可靠提升真实响应，但无法完全消除虚假

## 摘要（原文）

> Large language models sometimes produce false or misleading responses. Two approaches to this problem are honesty elicitation -- modifying prompts or weights so that the model answers truthfully -- and lie detection -- classifying whether a given response is false. Prior work evaluates such methods on models specifically trained to lie or conceal information, but these artificial constructions may not resemble naturally-occurring dishonesty. We instead study open-weights LLMs from Chinese developers, which are trained to censor politically sensitive topics: Qwen3 models frequently produce falsehoods about subjects like Falun Gong or the Tiananmen protests while occasionally answering correctly, indicating they possess knowledge they are trained to suppress. Using this as a testbed, we evaluate a suite of elicitation and lie detection techniques. For honesty elicitation, sampling without a chat template, few-shot prompting, and fine-tuning on generic honesty data most reliably increase truthful responses. For lie detection, prompting the censored model to classify its own responses performs near an uncensored-model upper bound, and linear probes trained on unrelated data offer a cheaper alternative. The strongest honesty elicitation techniques also transfer to frontier open-weights models including DeepSeek R1. Notably, no technique fully eliminates false responses. We release all prompts, code, and transcripts.

