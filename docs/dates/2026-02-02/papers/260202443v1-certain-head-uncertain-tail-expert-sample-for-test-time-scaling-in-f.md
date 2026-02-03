---
layout: default
title: Certain Head, Uncertain Tail: Expert-Sample for Test-Time Scaling in Fine-Grained MoE
---

# Certain Head, Uncertain Tail: Expert-Sample for Test-Time Scaling in Fine-Grained MoE
**arXiv**：[2602.02443v1](https://arxiv.org/abs/2602.02443) · [PDF](https://arxiv.org/pdf/2602.02443.pdf)  
**作者**：Yuanteng Chen, Peisong Wang, Nanxin Zeng, Yuantian Shao, Gang Li, Jing Liu, Jian Cheng  

**一句话要点**：提出Expert-Sample方法，在细粒度MoE中通过控制尾部不确定性提升测试时扩展性能。

**关键词**：细粒度混合专家, 测试时扩展, 路由不确定性, 多样生成, 训练免费方法

## 3 点简述
- 核心问题：测试时扩展中，细粒度MoE路由存在高置信度头部与低置信度尾部，影响多样性与稳定性。
- 方法要点：训练免费方法，保留头部高置信度专家，向尾部注入可控随机性以生成多样输出。
- 实验效果：在数学、知识推理和代码任务上，提升pass@n和验证准确率，如Qwen3-30B-A3B-Instruct在GPQA-Diamond上pass@32从85.4%升至91.9%。

## 摘要（原文）

> Test-time scaling improves LLM performance by generating multiple candidate solutions, yet token-level sampling requires temperature tuning that trades off diversity against stability. Fine-grained MoE, featuring hundreds of well-trained experts per layer and multi-expert activation per token, offers an unexplored alternative through its rich routing space. We empirically characterize fine-grained MoE routing and uncover an informative pattern: router scores exhibit a certain head of high-confidence experts followed by an uncertain tail of low-confidence candidates. While single-run greedy accuracy remains stable when fewer experts are activated, multi-sample pass@n degrades significantly-suggesting that the certain head governs core reasoning capability while the uncertain tail correlates with reasoning diversity. Motivated by these findings, we propose Expert-Sample, a training-free method that preserves high-confidence selections while injecting controlled stochasticity into the uncertain tail, enabling diverse generation without destabilizing outputs. Evaluated on multiple fine-grained MoE models across math, knowledge reasoning, and code tasks, Expert-Sample consistently improves pass@n and verification-based accuracy. On Qwen3-30B-A3B-Instruct evaluated on GPQA-Diamond with 32 parallel samples, pass@32 rises from 85.4% to 91.9%, and accuracy improves from 59.1% to 62.6% with Best-of-N verification.

