---
layout: default
title: FineInstructions: Scaling Synthetic Instructions to Pre-Training Scale
---

# FineInstructions: Scaling Synthetic Instructions to Pre-Training Scale
**arXiv**：[2601.22146v1](https://arxiv.org/abs/2601.22146) · [PDF](https://arxiv.org/pdf/2601.22146.pdf)  
**作者**：Ajay Patel, Colin Raffel, Chris Callison-Burch  

**一句话要点**：提出FineInstructions方法，通过大规模合成指令数据，使LLM仅用指令调优目标从头预训练。

**关键词**：指令调优, 合成数据生成, 大语言模型预训练, 自监督学习, 下游任务对齐

## 3 点简述
- 核心问题：指令调优数据有限，影响LLM下游应用效果。
- 方法要点：从预训练文档生成数十亿合成指令-答案对，基于真实查询模板。
- 实验或效果：在标准基准测试中，优于传统预训练及其他合成方法。

## 摘要（原文）

> Due to limited supervised training data, large language models (LLMs) are typically pre-trained via a self-supervised "predict the next word" objective on a vast amount of unstructured text data. To make the resulting model useful to users, it is further trained on a far smaller amount of "instruction-tuning" data comprised of supervised training examples of instructions and responses. To overcome the limited amount of supervised data, we propose a procedure that can transform the knowledge in internet-scale pre-training documents into billions of synthetic instruction and answer training pairs. The resulting dataset, called FineInstructions, uses ~18M instruction templates created from real user-written queries and prompts. These instruction templates are matched to and instantiated with human-written source documents from unstructured pre-training corpora. With "supervised" synthetic training data generated at this scale, an LLM can be pre-trained from scratch solely with the instruction-tuning objective, which is far more in-distribution with the expected downstream usage of LLMs (responding to user prompts). We conduct controlled token-for-token training experiments and find pre-training on FineInstructions outperforms standard pre-training and other proposed synthetic pre-training techniques on standard benchmarks measuring free-form response quality. Our resources can be found at https://huggingface.co/fineinstructions .

