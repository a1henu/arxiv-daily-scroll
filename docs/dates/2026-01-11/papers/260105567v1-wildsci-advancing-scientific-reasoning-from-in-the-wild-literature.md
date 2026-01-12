---
layout: default
title: WildSci: Advancing Scientific Reasoning from In-the-Wild Literature
---

# WildSci: Advancing Scientific Reasoning from In-the-Wild Literature
**arXiv**：[2601.05567v1](https://arxiv.org/abs/2601.05567) · [PDF](https://arxiv.org/pdf/2601.05567.pdf)  
**作者**：Tengxiao Liu, Deepak Nathani, Zekun Li, Kevin Yang, William Yang Wang  

**一句话要点**：提出WildSci数据集以解决科学领域大语言模型推理数据不足与评估难题

**关键词**：科学推理, 数据集构建, 强化学习, 多领域科学, 大语言模型微调, 评估基准

## 3 点简述
- 核心问题：科学领域如医学和材料科学缺乏高质量数据和客观评估指标，限制大语言模型推理进展。
- 方法要点：从同行评审文献自动合成多领域科学问题，构建多选格式数据集，支持强化学习微调。
- 实验或效果：在科学基准测试中验证数据集有效性，分析训练动态和泛化趋势，促进可持续研究。

## 摘要（原文）

> Recent progress in large language model (LLM) reasoning has focused on domains like mathematics and coding, where abundant high-quality data and objective evaluation metrics are readily available. In contrast, progress in LLM reasoning models remains limited in scientific domains such as medicine and materials science due to limited dataset coverage and the inherent complexity of open-ended scientific questions. To address these challenges, we introduce WildSci, a new dataset of domain-specific science questions automatically synthesized from peer-reviewed literature, covering 9 scientific disciplines and 26 subdomains. By framing complex scientific reasoning tasks in a multiple-choice format, we enable scalable training with well-defined reward signals. We further apply reinforcement learning to finetune models on these data and analyze the resulting training dynamics, including domain-specific performance changes, response behaviors, and generalization trends. Experiments on a suite of scientific benchmarks demonstrate the effectiveness of our dataset and approach. We release WildSci to enable scalable and sustainable research in scientific reasoning, available at https://huggingface.co/datasets/JustinTX/WildSci.

