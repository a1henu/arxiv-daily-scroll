---
layout: default
title: Controllable Reasoning Models Are Private Thinkers
---

# Controllable Reasoning Models Are Private Thinkers
**arXiv**：[2602.24210v1](https://arxiv.org/abs/2602.24210) · [PDF](https://arxiv.org/pdf/2602.24210.pdf)  
**作者**：Haritz Puerto, Haonan Li, Xudong Han, Timothy Baldwin, Iryna Gurevych  

**一句话要点**：提出可控推理模型训练方法以增强AI代理的隐私保护能力

**关键词**：可控推理模型, 隐私保护, 指令微调, LoRA适配器, AI代理

## 3 点简述
- 核心问题：AI推理模型在处理敏感数据时，推理轨迹难以控制，可能导致隐私泄露。
- 方法要点：通过指令微调训练模型遵循推理轨迹约束，并采用分离LoRA适配器解耦推理与答案生成。
- 实验或效果：在指令遵循和隐私基准测试中取得显著提升，但可能牺牲任务效用。

## 摘要（原文）

> AI agents powered by reasoning models require access to sensitive user data. However, their reasoning traces are difficult to control, which can result in the unintended leakage of private information to external parties. We propose training models to follow instructions not only in the final answer, but also in reasoning traces, potentially under different constraints. We hypothesize that improving their instruction following abilities in the reasoning traces can improve their privacy-preservation skills. To demonstrate this, we fine-tune models on a new instruction-following dataset with explicit restrictions on reasoning traces. We further introduce a generation strategy that decouples reasoning and answer generation using separate LoRA adapters. We evaluate our approach on six models from two model families, ranging from 1.7B to 14B parameters, across two instruction-following benchmarks and two privacy benchmarks. Our method yields substantial improvements, achieving gains of up to 20.9 points in instruction-following performance and up to 51.9 percentage points on privacy benchmarks. These improvements, however, can come at the cost of task utility, due to the trade-off between reasoning performance and instruction-following abilities. Overall, our results show that improving instruction-following behavior in reasoning models can significantly enhance privacy, suggesting a promising direction for the development of future privacy-aware agents. Our code and data are available at https://github.com/UKPLab/arxiv2026-controllable-reasoning-models

