---
layout: default
title: Make Anything Match Your Target: Universal Adversarial Perturbations against Closed-Source MLLMs via Multi-Crop Routed Meta Optimization
---

# Make Anything Match Your Target: Universal Adversarial Perturbations against Closed-Source MLLMs via Multi-Crop Routed Meta Optimization
**arXiv**：[2601.23179v1](https://arxiv.org/abs/2601.23179) · [PDF](https://arxiv.org/pdf/2601.23179.pdf)  
**作者**：Hui Lu, Yi Yu, Yiming Yang, Chenyu Yi, Xueyi Ke, Qixing Zhang, Bingquan Shen, Alex Kot, Xudong Jiang  

**一句话要点**：提出MCRMO-Attack以解决闭源多模态大语言模型的通用目标对抗攻击难题

**关键词**：通用对抗攻击, 多模态大语言模型, 目标可转移性, 元优化, 令牌路由, 闭源模型安全

## 3 点简述
- 研究通用目标可转移对抗攻击，要求单扰动在未知商业MLLMs上一致引导任意输入至指定目标
- 方法结合多裁剪聚合、注意力引导裁剪、可对齐门控令牌路由和元学习扰动先验以稳定监督和提升可靠性
- 实验在GPT-4o和Gemini-2.0上显著提升未见图像攻击成功率，分别超过最强通用基线23.7%和19.9%

## 摘要（原文）

> Targeted adversarial attacks on closed-source multimodal large language models (MLLMs) have been increasingly explored under black-box transfer, yet prior methods are predominantly sample-specific and offer limited reusability across inputs. We instead study a more stringent setting, Universal Targeted Transferable Adversarial Attacks (UTTAA), where a single perturbation must consistently steer arbitrary inputs toward a specified target across unknown commercial MLLMs. Naively adapting existing sample-wise attacks to this universal setting faces three core difficulties: (i) target supervision becomes high-variance due to target-crop randomness, (ii) token-wise matching is unreliable because universality suppresses image-specific cues that would otherwise anchor alignment, and (iii) few-source per-target adaptation is highly initialization-sensitive, which can degrade the attainable performance. In this work, we propose MCRMO-Attack, which stabilizes supervision via Multi-Crop Aggregation with an Attention-Guided Crop, improves token-level reliability through alignability-gated Token Routing, and meta-learns a cross-target perturbation prior that yields stronger per-target solutions. Across commercial MLLMs, we boost unseen-image attack success rate by +23.7\% on GPT-4o and +19.9\% on Gemini-2.0 over the strongest universal baseline.

