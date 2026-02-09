---
layout: default
title: AEGIS: Adversarial Target-Guided Retention-Data-Free Robust Concept Erasure from Diffusion Models
---

# AEGIS: Adversarial Target-Guided Retention-Data-Free Robust Concept Erasure from Diffusion Models
**arXiv**：[2602.06771v1](https://arxiv.org/abs/2602.06771) · [PDF](https://arxiv.org/pdf/2602.06771.pdf)  
**作者**：Fengpeng Li, Kemou Li, Qizhou Wang, Bo Han, Jiantao Zhou  

**一句话要点**：提出AEGIS框架以解决扩散模型中概念擦除的鲁棒性与保留性权衡问题

**关键词**：扩散模型, 概念擦除, 鲁棒性, 保留性, 对抗性训练

## 3 点简述
- 核心问题：现有概念擦除方法在鲁棒性和保留性之间存在权衡，难以同时优化
- 方法要点：AEGIS采用对抗性擦除与梯度信息协同，无需保留数据，提升鲁棒性和保留性
- 实验或效果：未知具体实验细节，但声称在鲁棒性和保留性方面均有进展

## 摘要（原文）

> Concept erasure helps stop diffusion models (DMs) from generating harmful content; but current methods face robustness retention trade off. Robustness means the model fine-tuned by concept erasure methods resists reactivation of erased concepts, even under semantically related prompts. Retention means unrelated concepts are preserved so the model's overall utility stays intact. Both are critical for concept erasure in practice, yet addressing them simultaneously is challenging, as existing works typically improve one factor while sacrificing the other. Prior work typically strengthens one while degrading the other, e.g., mapping a single erased prompt to a fixed safe target leaves class level remnants exploitable by prompt attacks, whereas retention-oriented schemes underperform against adaptive adversaries. This paper introduces Adversarial Erasure with Gradient Informed Synergy (AEGIS), a retention-data-free framework that advances both robustness and retention.

