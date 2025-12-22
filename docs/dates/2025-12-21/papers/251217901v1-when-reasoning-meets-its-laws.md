---
layout: default
title: When Reasoning Meets Its Laws
---

# When Reasoning Meets Its Laws
**arXiv**：[2512.17901v1](https://arxiv.org/abs/2512.17901) · [PDF](https://arxiv.org/pdf/2512.17901.pdf)  
**作者**：Junyu Zhang, Yifan Sun, Tianang Leng, Jingyan Shen, Liu Ziyin, Paul Pu Liang, Huan Zhang  

**一句话要点**：提出推理定律框架以提升大型推理模型的推理行为与性能

**关键词**：大型推理模型, 推理定律, 基准评估, 微调方法, 组合性, 单调性

## 3 点简述
- 核心问题：大型推理模型的推理行为常反直觉，导致推理能力次优。
- 方法要点：提出推理定律框架，包括计算定律和准确率定律，并引入LoRe-Bench基准评估单调性和组合性。
- 实验或效果：微调方法增强组合性，实验显示更好遵循推理定律能提升多基准推理性能。

## 摘要（原文）

> Despite the superior performance of Large Reasoning Models (LRMs), their reasoning behaviors are often counterintuitive, leading to suboptimal reasoning capabilities. To theoretically formalize the desired reasoning behaviors, this paper presents the Laws of Reasoning (LoRe), a unified framework that characterizes intrinsic reasoning patterns in LRMs. We first propose compute law with the hypothesis that the reasoning compute should scale linearly with question complexity. Beyond compute, we extend LoRe with a supplementary accuracy law. Since the question complexity is difficult to quantify in practice, we examine these hypotheses by two properties of the laws, monotonicity and compositionality. We therefore introduce LoRe-Bench, a benchmark that systematically measures these two tractable properties for large reasoning models. Evaluation shows that most reasoning models exhibit reasonable monotonicity but lack compositionality. In response, we develop an effective finetuning approach that enforces compute-law compositionality. Extensive empirical studies demonstrate that better compliance with compute laws yields consistently improved reasoning performance on multiple benchmarks, and uncovers synergistic effects across properties and laws. Project page: https://lore-project.github.io/

