---
layout: default
title: RoBoN: Routed Online Best-of-n for Test-Time Scaling with Multiple LLMs
---

# RoBoN: Routed Online Best-of-n for Test-Time Scaling with Multiple LLMs
**arXiv**：[2512.05542v1](https://arxiv.org/abs/2512.05542) · [PDF](https://arxiv.org/pdf/2512.05542.pdf)  
**作者**：Jonathan Geuter, Gregor Kornhardt  

**一句话要点**：提出RoBoN方法，通过在线路由多LLM提升测试时扩展性能

**关键词**：测试时扩展, 多模型推理, 在线路由, 奖励模型, LLM集成

## 3 点简述
- 核心问题：传统best-of-n依赖单一模型，未利用多模型互补优势
- 方法要点：基于奖励模型和一致性信号，在线顺序路由生成至不同LLM
- 实验或效果：在推理基准上优于单模型best-of-n，准确率提升达3.4%

## 摘要（原文）

> Best-of-$n$ is a widely used test-time scaling approach for LLM inference. Yet despite evidence that LLMs exhibit complementary strengths across tasks, traditionally best-of-$n$ relies on a single model to generate responses. We propose RoBoN (Routed Online Best-of-$n$), a sequential multi-LLM alternative to the prevailing single-model best-of-$n$. Given a suite of models $\{m_i\}_{i=1}^M$, RoBoN sequentially routes generations one-by-one across models, based on scores computed using a reward model and an agreement signal on the predicted responses. This online routing requires no additional training, keeps compute parity, and works with any plug-in reward model. Across reasoning benchmarks (MATH500, OlympiadBench, MinervaMath, GSM8K, MMLU), RoBoN consistently outperforms standard best-of-$n$ applied to each individual model for larger $n$, with gains of up to 3.4\% in absolute accuracy, and also improves over a uniform multi-model portfolio baseline. Our results indicate that diversity across models can be exploited at inference to improve best-of-$n$ performance over any constituent model alone, providing a simple, training-free path to test-time scaling with multiple LLMs.

