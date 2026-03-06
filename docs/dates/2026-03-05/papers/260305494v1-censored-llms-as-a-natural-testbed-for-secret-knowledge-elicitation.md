---
layout: default
title: Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation
---

# Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation
**arXiv**：[2603.05494v1](https://arxiv.org/abs/2603.05494) · [PDF](https://arxiv.org/pdf/2603.05494.pdf)  
**作者**：Helena Casademunt, Bartosz Cywiński, Khoi Tran, Arya Jakkli, Samuel Marks, Neel Nanda  

**一句话要点**：提出基于中文开源大模型的秘密知识诱导与谎言检测方法，评估其在政治敏感话题上的效果。

**关键词**：诚实诱导, 谎言检测, 大语言模型, 审查机制, 秘密知识, 中文开源模型

## 3 点简述
- 研究核心问题：评估诚实诱导与谎言检测方法在自然发生不诚实场景下的性能，而非人工构造的谎言模型。
- 方法要点：利用中文开源大模型（如Qwen3）作为测试平台，因其在政治敏感话题上训练时产生虚假回答，但偶尔正确回答，表明其拥有被抑制的知识。
- 实验或效果：发现无聊天模板采样、少样本提示和通用诚实数据微调最可靠地增加真实回答；自我分类提示在谎言检测中表现接近未审查模型上限，线性探针提供廉价替代方案。

## 摘要（原文）

> Large language models sometimes produce false or misleading responses. Two approaches to this problem are honesty elicitation -- modifying prompts or weights so that the model answers truthfully -- and lie detection -- classifying whether a given response is false. Prior work evaluates such methods on models specifically trained to lie or conceal information, but these artificial constructions may not resemble naturally-occurring dishonesty. We instead study open-weights LLMs from Chinese developers, which are trained to censor politically sensitive topics: Qwen3 models frequently produce falsehoods about subjects like Falun Gong or the Tiananmen protests while occasionally answering correctly, indicating they possess knowledge they are trained to suppress. Using this as a testbed, we evaluate a suite of elicitation and lie detection techniques. For honesty elicitation, sampling without a chat template, few-shot prompting, and fine-tuning on generic honesty data most reliably increase truthful responses. For lie detection, prompting the censored model to classify its own responses performs near an uncensored-model upper bound, and linear probes trained on unrelated data offer a cheaper alternative. The strongest honesty elicitation techniques also transfer to frontier open-weights models including DeepSeek R1. Notably, no technique fully eliminates false responses. We release all prompts, code, and transcripts.

