---
layout: default
title: $A^3$-Bench: Benchmarking Memory-Driven Scientific Reasoning via Anchor and Attractor Activation
---

# $A^3$-Bench: Benchmarking Memory-Driven Scientific Reasoning via Anchor and Attractor Activation
**arXiv**：[2601.09274v1](https://arxiv.org/abs/2601.09274) · [PDF](https://arxiv.org/pdf/2601.09274.pdf)  
**作者**：Jian Zhang, Yu He, Zhiyuan Wang, Zhangqi Wang, Kai He, Fangzhi Xu, Qika Lin, Jun Liu  

**一句话要点**：提出A³-Bench基准，通过锚点与吸引子激活评估记忆驱动的科学推理

**关键词**：科学推理基准, 记忆驱动机制, 锚点激活, 吸引子激活, 双尺度评估, AAUI指标

## 3 点简述
- 现有基准忽视记忆驱动机制，主要评估最终答案或步骤连贯性
- 基于锚点与吸引子激活理论，构建双尺度记忆评估框架与AAUI指标
- 在多个模型上验证基准有效性，分析记忆激活对推理性能的影响

## 摘要（原文）

> Scientific reasoning relies not only on logical inference but also on activating prior knowledge and experiential structures. Memory can efficiently reuse knowledge and enhance reasoning consistency and stability. However, existing benchmarks mainly evaluate final answers or step-by-step coherence, overlooking the \textit{memory-driven} mechanisms that underlie human reasoning, which involves activating anchors and attractors, then integrating them into multi-step inference. To address this gap, we propose $A^3$-Bench~ https://a3-bench.github.io, a benchmark designed to evaluate scientific reasoning through dual-scale memory-driven activation, grounded in Anchor and Attractor Activation. First, we annotate 2,198 science reasoning problems across domains using the SAPM process(subject, anchor & attractor, problem, and memory developing). Second, we introduce a dual-scale memory evaluation framework utilizing anchors and attractors, along with the AAUI(Anchor--Attractor Utilization Index) metric to measure memory activation rates. Finally, through experiments with various base models and paradigms, we validate $A^3$-Bench and analyze how memory activation impacts reasoning performance, providing insights into memory-driven scientific reasoning.

