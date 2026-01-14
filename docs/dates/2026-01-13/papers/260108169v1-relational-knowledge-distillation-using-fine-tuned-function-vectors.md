---
layout: default
title: Relational Knowledge Distillation Using Fine-tuned Function Vectors
---

# Relational Knowledge Distillation Using Fine-tuned Function Vectors
**arXiv**：[2601.08169v1](https://arxiv.org/abs/2601.08169) · [PDF](https://arxiv.org/pdf/2601.08169.pdf)  
**作者**：Andrea Kang, Yingnian Wu, Hongjing Lu  

**一句话要点**：提出微调函数向量以增强关系知识蒸馏，提升语言模型类比推理性能

**关键词**：函数向量, 关系知识蒸馏, 类比推理, 激活修补, 语言模型微调, 因果中介分析

## 3 点简述
- 核心问题：如何高效编码和操作关系知识以提升语言模型推理能力
- 方法要点：通过微调函数向量优化关系表示，并引入复合函数向量支持类比推理
- 实验或效果：在关系词补全和类比任务中表现优于原始向量，增强与人类判断对齐

## 摘要（原文）

> Representing relations between concepts is a core prerequisite for intelligent systems to make sense of the world. Recent work using causal mediation analysis has shown that a small set of attention heads encodes task representation in in-context learning, captured in a compact representation known as the function vector. We show that fine-tuning function vectors with only a small set of examples (about 20 word pairs) yields better performance on relation-based word-completion tasks than using the original vectors derived from causal mediation analysis. These improvements hold for both small and large language models. Moreover, the fine-tuned function vectors yield improved decoding performance for relation words and show stronger alignment with human similarity judgments of semantic relations. Next, we introduce the composite function vector - a weighted combination of fine-tuned function vectors - to extract relational knowledge and support analogical reasoning. At inference time, inserting this composite vector into LLM activations markedly enhances performance on challenging analogy problems drawn from cognitive science and SAT benchmarks. Our results highlight the potential of activation patching as a controllable mechanism for encoding and manipulating relational knowledge, advancing both the interpretability and reasoning capabilities of large language models.

