---
layout: default
title: Few Tokens Matter: Entropy Guided Attacks on Vision-Language Models
---

# Few Tokens Matter: Entropy Guided Attacks on Vision-Language Models
**arXiv**：[2512.21815v1](https://arxiv.org/abs/2512.21815) · [PDF](https://arxiv.org/pdf/2512.21815.pdf)  
**作者**：Mengqi He, Xinyu Tian, Xin Shen, Jinhong Ni, Shu Zou, Zhaoyuan Yang, Jing Zhang  

**一句话要点**：提出熵引导攻击方法，针对视觉语言模型的关键高熵令牌进行选择性扰动，以高效实现语义破坏和安全风险暴露。

**关键词**：视觉语言模型, 对抗攻击, 熵引导, 令牌选择性, 安全风险, 可转移性

## 3 点简述
- 核心问题：传统熵攻击假设所有令牌对生成不稳定性贡献均等，但实际仅约20%高熵令牌主导输出轨迹。
- 方法要点：通过集中对抗扰动于关键高熵位置，实现与全局方法相当的语义退化，同时显著降低攻击预算。
- 实验或效果：在多种视觉语言模型上，选择性攻击将35-49%良性输出转为有害，并展示17-26%的跨模型可转移性。

## 摘要（原文）

> Vision-language models (VLMs) achieve remarkable performance but remain vulnerable to adversarial attacks. Entropy, a measure of model uncertainty, is strongly correlated with the reliability of VLM. Prior entropy-based attacks maximize uncertainty at all decoding steps, implicitly assuming that every token contributes equally to generation instability. We show instead that a small fraction (about 20%) of high-entropy tokens, i.e., critical decision points in autoregressive generation, disproportionately governs output trajectories. By concentrating adversarial perturbations on these positions, we achieve semantic degradation comparable to global methods while using substantially smaller budgets. More importantly, across multiple representative VLMs, such selective attacks convert 35-49% of benign outputs into harmful ones, exposing a more critical safety risk. Remarkably, these vulnerable high-entropy forks recur across architecturally diverse VLMs, enabling feasible transferability (17-26% harmful rates on unseen targets). Motivated by these findings, we propose Entropy-bank Guided Adversarial attacks (EGA), which achieves competitive attack success rates (93-95%) alongside high harmful conversion, thereby revealing new weaknesses in current VLM safety mechanisms.

