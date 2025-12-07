---
layout: default
title: Arbitrage: Efficient Reasoning via Advantage-Aware Speculation
---

# Arbitrage: Efficient Reasoning via Advantage-Aware Speculation
**arXiv**：[2512.05033v1](https://arxiv.org/abs/2512.05033) · [PDF](https://arxiv.org/pdf/2512.05033.pdf)  
**作者**：Monishwaran Maheswaran, Rishabh Tiwari, Yuezhou Hu, Kerem Dilmen, Coleman Hooper, Haocheng Xi, Nicholas Lee, Mehrdad Farajtabar, Michael W. Mahoney, Kurt Keutzer, Amir Gholami  

**一句话要点**：提出Arbitrage框架，通过动态路由提升推理任务中步级推测解码的效率

**关键词**：推测解码, 推理加速, 动态路由, 步级验证, 大语言模型, 效率优化

## 3 点简述
- 传统推测解码在推理任务中因语义等效步骤的令牌不匹配导致效率低下
- Arbitrage使用轻量级路由器动态选择草稿或目标模型生成步骤，优化效率-准确性权衡
- 在数学推理基准测试中，Arbitrage减少推理延迟约2倍，保持准确性

## 摘要（原文）

> Modern Large Language Models achieve impressive reasoning capabilities with long Chain of Thoughts, but they incur substantial computational cost during inference, and this motivates techniques to improve the performance-cost ratio. Among these techniques, Speculative Decoding accelerates inference by employing a fast but inaccurate draft model to autoregressively propose tokens, which are then verified in parallel by a more capable target model. However, due to unnecessary rejections caused by token mismatches in semantically equivalent steps, traditional token-level Speculative Decoding struggles in reasoning tasks. Although recent works have shifted to step-level semantic verification, which improve efficiency by accepting or rejecting entire reasoning steps, existing step-level methods still regenerate many rejected steps with little improvement, wasting valuable target compute. To address this challenge, we propose Arbitrage, a novel step-level speculative generation framework that routes generation dynamically based on the relative advantage between draft and target models. Instead of applying a fixed acceptance threshold, Arbitrage uses a lightweight router trained to predict when the target model is likely to produce a meaningfully better step. This routing approximates an ideal Arbitrage Oracle that always chooses the higher-quality step, achieving near-optimal efficiency-accuracy trade-offs. Across multiple mathematical reasoning benchmarks, Arbitrage consistently surpasses prior step-level Speculative Decoding baselines, reducing inference latency by up to $\sim2\times$ at matched accuracy.

