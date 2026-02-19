---
layout: default
title: Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution
---

# Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution
**arXiv**：[2602.16154v1](https://arxiv.org/abs/2602.16154) · [PDF](https://arxiv.org/pdf/2602.16154.pdf)  
**作者**：Nithin Sivakumaran, Shoubin Yu, Hyunji Lee, Yue Zhang, Ali Payani, Mohit Bansal, Elias Stengel-Eskin  

**一句话要点**：提出多监听器软执行方法REMUL，以平衡推理忠实性与任务性能

**关键词**：思维链推理, 忠实性优化, 多监听器强化学习, 掩码监督微调, 推理基准评估

## 3 点简述
- 核心问题：思维链推理可能不忠实反映大语言模型计算，且优化忠实性常降低性能
- 方法要点：通过多监听器强化学习，奖励生成可被其他方执行的推理轨迹，结合掩码监督微调
- 实验或效果：在多个推理基准上显著提升忠实性指标和准确性，推理轨迹更短更直接

## 摘要（原文）

> Chain-of-thought (CoT) reasoning sometimes fails to faithfully reflect the true computation of a large language model (LLM), hampering its utility in explaining how LLMs arrive at their answers. Moreover, optimizing for faithfulness and interpretability in reasoning often degrades task performance. To address this tradeoff and improve CoT faithfulness, we propose Reasoning Execution by Multiple Listeners (REMUL), a multi-party reinforcement learning approach. REMUL builds on the hypothesis that reasoning traces which other parties can follow will be more faithful. A speaker model generates a reasoning trace, which is truncated and passed to a pool of listener models who "execute" the trace, continuing the trace to an answer. Speakers are rewarded for producing reasoning that is clear to listeners, with additional correctness regularization via masked supervised finetuning to counter the tradeoff between faithfulness and performance. On multiple reasoning benchmarks (BIG-Bench Extra Hard, MuSR, ZebraLogicBench, and FOLIO), REMUL consistently and substantially improves three measures of faithfulness -- hint attribution, early answering area over the curve (AOC), and mistake injection AOC -- while also improving accuracy. Our analysis finds that these gains are robust across training domains, translate to legibility gains, and are associated with shorter and more direct CoTs.

