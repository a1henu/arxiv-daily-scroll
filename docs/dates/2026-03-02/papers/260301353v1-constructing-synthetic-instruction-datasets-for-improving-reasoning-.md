---
layout: default
title: Constructing Synthetic Instruction Datasets for Improving Reasoning in Domain-Specific LLMs: A Case Study in the Japanese Financial Domain
---

# Constructing Synthetic Instruction Datasets for Improving Reasoning in Domain-Specific LLMs: A Case Study in the Japanese Financial Domain
**arXiv**：[2603.01353v1](https://arxiv.org/abs/2603.01353) · [PDF](https://arxiv.org/pdf/2603.01353.pdf)  
**作者**：Yuma Okochi, Fabio Milentiansen Sim, Tomoyasu Okada  

**一句话要点**：提出基于领域词汇构建合成指令数据的方法，以提升日本金融领域LLMs的推理能力。

**关键词**：合成指令数据, 领域特定LLMs, 链式思维推理, 金融领域, 日语处理

## 3 点简述
- 核心问题：LLMs在特定领域应用中，难以同时实现领域专业知识和推理能力。
- 方法要点：从领域词汇出发，构建大规模合成指令数据集，包含链式思维推理轨迹。
- 实验或效果：在金融基准测试中，模型性能优于基线，并开源了模型和数据集。

## 摘要（原文）

> In adapting LLMs to specific domains, achieving both domain expertise and reasoning ability remains an urgent challenge. This study proposes a general method for constructing high-quality synthetic instruction data for any domain, starting from domain-specific vocabulary. As a demonstration, we applied this method to the financial domain and constructed a large-scale instruction dataset totaling approximately 9.5 billion tokens with Chain-of-Thought reasoning traces. Evaluation results confirmed performance improvements over baseline models on financial benchmarks, demonstrating the effectiveness of our approach. We also report findings on the impact of reasoning trace length on performance and its limitations. Lastly, we open-source our models and datasets on https://huggingface.co/nri-ai .

