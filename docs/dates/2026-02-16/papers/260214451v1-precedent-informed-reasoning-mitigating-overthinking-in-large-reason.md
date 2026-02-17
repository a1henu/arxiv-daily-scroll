---
layout: default
title: Precedent-Informed Reasoning: Mitigating Overthinking in Large Reasoning Models via Test-Time Precedent Learning
---

# Precedent-Informed Reasoning: Mitigating Overthinking in Large Reasoning Models via Test-Time Precedent Learning
**arXiv**：[2602.14451v1](https://arxiv.org/abs/2602.14451) · [PDF](https://arxiv.org/pdf/2602.14451.pdf)  
**作者**：Qianyue Wang, Jinwu Hu, Huanxiang Lin, Bolin Chen, Zhiquan Wen, Yaofo Chen, Yu Rong, Mingkui Tan  

**一句话要点**：提出先例知情推理以缓解大型推理模型中的过度思考问题

**关键词**：大型语言模型, 推理优化, 先例学习, 测试时学习, 计算效率

## 3 点简述
- 核心问题：大型语言模型推理时存在冗余自我探索，导致计算成本高且性能下降
- 方法要点：通过自适应先例选择和测试时经验内化，从先例中学习以指导推理
- 实验或效果：在数学推理、科学问答和代码生成中缩短推理轨迹并保持或提升准确性

## 摘要（原文）

> Reasoning in Large Language Models (LLMs) often suffers from inefficient long chain-of-thought traces with redundant self-exploration and validation, which inflate computational costs and even degrade performance. Inspired by human reasoning patterns where people solve new problems by leveraging past related cases to constrain search spaces and reduce trial-and-error, we propose Precedent Informed Reasoning (PIR) transforming LRMs'reasoning paradigm from exhaustive self-exploration to guided learning from precedents. PIR addresses two key challenges: what precedents to adopt and how to utilize them. First, Adaptive Precedent Selection (APS) constructs, for each question and LRM, a compact set of precedents that are both semantically related and informative for the model. It ranks examples by a joint score with semantic similarity and model perplexity, then adapts the amount of precedents to maximize perplexity reduction. Second, Test-time Experience Internalization (TEI) is treated as the test-time learning on precedent-informed instruction, updating lightweight adapters to internalize solution patterns and use them as a prior during subsequent reasoning. Experiments across mathematical reasoning, scientific QA, and code generation demonstrate that PIR consistently shortens reasoning traces while maintaining or improving final accuracy across LLMs, yielding outstanding accuracy-efficiency trade-offs.

