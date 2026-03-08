---
layout: default
title: Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought
---

# Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought
**arXiv**：[2603.05488v1](https://arxiv.org/abs/2603.05488) · [PDF](https://arxiv.org/pdf/2603.05488.pdf)  
**作者**：Siddharth Boppana, Annabel Ma, Max Loeffler, Raphael Sarfati, Eric Bigelow, Atticus Geiger, Owen Lewis, Jack Merullo  

**一句话要点**：揭示推理模型中的表演性思维链，通过激活探测实现高效计算

**关键词**：思维链推理, 激活探测, 表演性推理, 模型信念, 自适应计算, 任务难度分析

## 3 点简述
- 核心问题：模型在思维链推理中可能隐藏内部信念，表现为表演性推理而非真实思考
- 方法要点：比较激活探测、早期强制回答和思维链监控，分析任务难度差异
- 实验或效果：探测引导早期退出在MMLU和GPQA-Diamond上分别减少80%和30%令牌，保持准确率

## 摘要（原文）

> We provide evidence of performative chain-of-thought (CoT) in reasoning models, where a model becomes strongly confident in its final answer, but continues generating tokens without revealing its internal belief. Our analysis compares activation probing, early forced answering, and a CoT monitor across two large models (DeepSeek-R1 671B & GPT-OSS 120B) and find task difficulty-specific differences: The model's final answer is decodable from activations far earlier in CoT than a monitor is able to say, especially for easy recall-based MMLU questions. We contrast this with genuine reasoning in difficult multihop GPQA-Diamond questions. Despite this, inflection points (e.g., backtracking, 'aha' moments) occur almost exclusively in responses where probes show large belief shifts, suggesting these behaviors track genuine uncertainty rather than learned "reasoning theater." Finally, probe-guided early exit reduces tokens by up to 80% on MMLU and 30% on GPQA-Diamond with similar accuracy, positioning attention probing as an efficient tool for detecting performative reasoning and enabling adaptive computation.

