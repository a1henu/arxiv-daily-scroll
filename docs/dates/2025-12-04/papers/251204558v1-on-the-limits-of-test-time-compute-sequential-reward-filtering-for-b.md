---
layout: default
title: On the Limits of Test-Time Compute: Sequential Reward Filtering for Better Inference
---

# On the Limits of Test-Time Compute: Sequential Reward Filtering for Better Inference
**arXiv**：[2512.04558v1](https://arxiv.org/abs/2512.04558) · [PDF](https://arxiv.org/pdf/2512.04558.pdf)  
**作者**：Yue Yu, Qiwei Di, Quanquan Gu, Dongruo Zhou  

**一句话要点**：提出奖励过滤顺序推理以优化测试时计算，提升大语言模型性能

**关键词**：测试时计算, 顺序推理, 奖励过滤, 大语言模型优化, 理论分析, 基准评估

## 3 点简述
- 分析测试时计算范式，证明标准最佳-n采样存在固有次优性
- 引入奖励过滤机制，选择性整合高奖励生成以集中计算资源
- 理论证明优于标准方法，实验验证在多个基准上实现一致改进

## 摘要（原文）

> Test-time compute (TTC) has become an increasingly prominent paradigm for enhancing large language models (LLMs). Despite the empirical success of methods such as best-of-$n$ (BoN) sampling and sequential revision, their fundamental limits remain unclear. We address this gap by analyzing a mixture-of-reference policy model and proving that standard BoN is inherently suboptimal. To move closer to the optimal frontier, we study reward-filtered sequential inference, a simple procedure that selectively incorporates only high-reward generations into the context. This mechanism concentrates computation on superior policy candidates and suppresses inferior ones. On the theoretical side, we show that reward-filtered sequential inference yields strictly stronger guarantees than standard TTC paradigms. On the empirical side, we evaluate such an inference strategy across diverse benchmarks and observe consistent improvements over widely used approaches, demonstrating the practical effectiveness of our framework.

