---
layout: default
title: Trust The Typical
---

# Trust The Typical
**arXiv**：[2602.04581v1](https://arxiv.org/abs/2602.04581) · [PDF](https://arxiv.org/pdf/2602.04581.pdf)  
**作者**：Debargha Ganguly, Sreehari Sankar, Biyao Zhang, Vikash Singh, Kanan Gupta, Harshini Kavuru, Alan Luo, Weicong Chen, Warren Morningstar, Raghu Machiraju, Vipin Chaudhary  

**一句话要点**：提出Trust The Typical框架，将LLM安全视为分布外检测问题，无需有害样本训练即可实现高效防护。

**关键词**：LLM安全, 分布外检测, 语义空间建模, 多语言防护, 低开销部署

## 3 点简述
- 核心问题：现有LLM安全方法依赖枚举有害内容，脆弱且易被绕过。
- 方法要点：通过语义空间学习安全提示分布，将显著偏差标记为潜在威胁。
- 实验或效果：在18个基准测试中达到SOTA，假阳性率降低达40倍，支持多语言和低开销部署。

## 摘要（原文）

> Current approaches to LLM safety fundamentally rely on a brittle cat-and-mouse game of identifying and blocking known threats via guardrails. We argue for a fresh approach: robust safety comes not from enumerating what is harmful, but from deeply understanding what is safe. We introduce Trust The Typical (T3), a framework that operationalizes this principle by treating safety as an out-of-distribution (OOD) detection problem. T3 learns the distribution of acceptable prompts in a semantic space and flags any significant deviation as a potential threat. Unlike prior methods, it requires no training on harmful examples, yet achieves state-of-the-art performance across 18 benchmarks spanning toxicity, hate speech, jailbreaking, multilingual harms, and over-refusal, reducing false positive rates by up to 40x relative to specialized safety models. A single model trained only on safe English text transfers effectively to diverse domains and over 14 languages without retraining. Finally, we demonstrate production readiness by integrating a GPU-optimized version into vLLM, enabling continuous guardrailing during token generation with less than 6% overhead even under dense evaluation intervals on large-scale workloads.

