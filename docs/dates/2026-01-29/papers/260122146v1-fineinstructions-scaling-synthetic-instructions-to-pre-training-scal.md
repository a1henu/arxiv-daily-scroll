---
layout: default
title: FineInstructions: Scaling Synthetic Instructions to Pre-Training Scale
---

# FineInstructions: Scaling Synthetic Instructions to Pre-Training Scale
**arXiv**：[2601.22146v1](https://arxiv.org/abs/2601.22146) · [PDF](https://arxiv.org/pdf/2601.22146.pdf)  
**作者**：Ajay Patel, Colin Raffel, Chris Callison-Burch  

**一句话要点**：提出FineInstructions方法，通过大规模合成指令数据，使LLM从零开始仅用指令调优目标进行预训练。

**关键词**：合成指令数据, 指令调优, 预训练, 大语言模型, 数据增强

## 3 点简述
- 核心问题：LLM预训练依赖无监督文本，指令调优数据有限，影响下游用户提示响应效果。
- 方法要点：从预训练文档生成数十亿合成指令-答案对，基于真实用户查询模板匹配文档实例化。
- 实验或效果：在标准基准测试中，FineInstructions预训练优于标准预训练和其他合成预训练技术。

## 摘要（原文）

> Due to limited supervised training data, large language models (LLMs) are typically pre-trained via a self-supervised "predict the next word" objective on a vast amount of unstructured text data. To make the resulting model useful to users, it is further trained on a far smaller amount of "instruction-tuning" data comprised of supervised training examples of instructions and responses. To overcome the limited amount of supervised data, we propose a procedure that can transform the knowledge in internet-scale pre-training documents into billions of synthetic instruction and answer training pairs. The resulting dataset, called FineInstructions, uses ~18M instruction templates created from real user-written queries and prompts. These instruction templates are matched to and instantiated with human-written source documents from unstructured pre-training corpora. With "supervised" synthetic training data generated at this scale, an LLM can be pre-trained from scratch solely with the instruction-tuning objective, which is far more in-distribution with the expected downstream usage of LLMs (responding to user prompts). We conduct controlled token-for-token training experiments and find pre-training on FineInstructions outperforms standard pre-training and other proposed synthetic pre-training techniques on standard benchmarks measuring free-form response quality. Our resources can be found at https://huggingface.co/fineinstructions .

