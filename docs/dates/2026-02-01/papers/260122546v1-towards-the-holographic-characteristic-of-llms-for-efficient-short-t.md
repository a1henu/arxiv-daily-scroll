---
layout: default
title: Towards the Holographic Characteristic of LLMs for Efficient Short-text Generation
---

# Towards the Holographic Characteristic of LLMs for Efficient Short-text Generation
**arXiv**：[2601.22546v1](https://arxiv.org/abs/2601.22546) · [PDF](https://arxiv.org/pdf/2601.22546.pdf)  
**作者**：Shun Qian, Bingquan Liu, Chengjie Sun, Zhen Xu, Baoxun Wang  

**一句话要点**：提出HOLO插件以提升大语言模型在短文本生成中的推理效率

**关键词**：大语言模型, 短文本生成, 全息特性, 推理效率, 词汇约束生成

## 3 点简述
- 核心问题：探索大语言模型生成能力的具体特性，如全息特性，以改进推理效率。
- 方法要点：利用全息特性提取关键词，结合并行词汇约束生成方法补充句子。
- 实验或效果：在多种架构和规模的模型上验证，HOLO在自动和人工评估中达到基线可比性能。

## 摘要（原文）

> The recent advancements in Large Language Models (LLMs) have attracted interest in exploring their in-context learning abilities and chain-of-thought capabilities. However, there are few studies investigating the specific traits related to the powerful generation capacity of LLMs. This paper aims to delve into the generation characteristics exhibited by LLMs. Through our investigation, we have discovered that language models tend to capture target-side keywords at the beginning of the generation process. We name this phenomenon the Holographic Characteristic of language models. For the purpose of exploring this characteristic and further improving the inference efficiency of language models, we propose a plugin called HOLO, which leverages the Holographic Characteristic to extract target-side keywords from language models within a limited number of generation steps and complements the sentence with a parallel lexically constrained text generation method. To verify the effectiveness of HOLO, we conduct massive experiments on language models of varying architectures and scales in the short-text generation scenario. The results demonstrate that HOLO achieves comparable performance to the baselines in terms of both automatic and human-like evaluation metrics and highlight the potential of the Holographic Characteristic.

