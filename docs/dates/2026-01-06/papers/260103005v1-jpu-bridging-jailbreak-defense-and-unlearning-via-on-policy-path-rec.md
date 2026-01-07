---
layout: default
title: JPU: Bridging Jailbreak Defense and Unlearning via On-Policy Path Rectification
---

# JPU: Bridging Jailbreak Defense and Unlearning via On-Policy Path Rectification
**arXiv**：[2601.03005v1](https://arxiv.org/abs/2601.03005) · [PDF](https://arxiv.org/pdf/2601.03005.pdf)  
**作者**：Xi Wang, Songlei Jian, Shasha Li, Xiaopeng Li, Zhaoye Li, Bin Ji, Baosheng Wang, Jie Yu  

**一句话要点**：提出JPU方法，通过动态路径修正增强大语言模型对越狱攻击的防御能力。

**关键词**：大语言模型安全, 越狱攻击防御, 机器遗忘, 动态路径修正, 对抗样本挖掘

## 3 点简述
- 核心问题：现有遗忘防御因无法修正动态越狱路径，导致对多样越狱攻击脆弱。
- 方法要点：JPU通过动态挖掘策略内对抗样本，识别并修正越狱路径至安全锚点。
- 实验或效果：实验显示JPU显著提升对动态攻击的抵抗力，同时保持模型实用性。

## 摘要（原文）

> Despite extensive safety alignment, Large Language Models (LLMs) often fail against jailbreak attacks. While machine unlearning has emerged as a promising defense by erasing specific harmful parameters, current methods remain vulnerable to diverse jailbreaks. We first conduct an empirical study and discover that this failure mechanism is caused by jailbreaks primarily activating non-erased parameters in the intermediate layers. Further, by probing the underlying mechanism through which these circumvented parameters reassemble into the prohibited output, we verify the persistent existence of dynamic $\textbf{jailbreak paths}$ and show that the inability to rectify them constitutes the fundamental gap in existing unlearning defenses. To bridge this gap, we propose $\textbf{J}$ailbreak $\textbf{P}$ath $\textbf{U}$nlearning (JPU), which is the first to rectify dynamic jailbreak paths towards safety anchors by dynamically mining on-policy adversarial samples to expose vulnerabilities and identify jailbreak paths. Extensive experiments demonstrate that JPU significantly enhances jailbreak resistance against dynamic attacks while preserving the model's utility.

