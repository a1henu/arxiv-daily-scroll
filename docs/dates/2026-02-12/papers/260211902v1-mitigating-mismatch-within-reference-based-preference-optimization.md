---
layout: default
title: Mitigating Mismatch within Reference-based Preference Optimization
---

# Mitigating Mismatch within Reference-based Preference Optimization
**arXiv**：[2602.11902v1](https://arxiv.org/abs/2602.11902) · [PDF](https://arxiv.org/pdf/2602.11902.pdf)  
**作者**：Suqin Yuan, Xingrui Yu, Jiyang Zheng, Lei Feng, Dadong Wang, Ivor Tsang, Tongliang Liu  

**一句话要点**：提出HyPO以解决基于参考的偏好优化中悲观对导致的训练-推理不匹配问题

**关键词**：偏好对齐, 直接偏好优化, 训练-推理不匹配, 参考策略, 条件去偏, 大语言模型

## 3 点简述
- 核心问题：DPO依赖参考策略，在悲观对（参考模型偏好被拒绝响应）中导致过早满足，引发训练-推理不匹配。
- 方法要点：HyPO通过条件应用参考，在悲观对中将参考视为中性，替换Δθ-Δref为Δθ-max{0,Δref}，增强学习信号。
- 实验或效果：HyPO在偏好对齐中提升推理对齐指标和成对胜率，保留DPO目标形式和计算成本。

## 摘要（原文）

> Direct Preference Optimization (DPO) has become the de facto standard for offline preference alignment of large language models, but its reliance on a reference policy introduces a critical tension. DPO weighs each update relative to a reference, which stabilizes the training by regularizing the updates within a trusted region. This reliance becomes problematic for pessimistic pairs, where the reference model prefers the rejected response. For these pairs, DPO prematurely attenuates the gradient as soon as the policy margin ($Δ_θ$) merely beats the reference margin ($Δ_{\mathrm{ref}}$) even if the policy is still wrong ($Δ_θ<0$). We name this failure premature satisfaction, which is a concrete form of the training-inference mismatch. Reference-free objectives remove this mismatch by optimizing the absolute margin, but at the cost of discarding the stabilizing signal of the reference. We mitigate this tension with Hybrid-DPO (HyPO), a drop-in modification to DPO that applies reference conditionally: HyPO behaves exactly like DPO when the reference is optimistic or neutral, and it treats the reference as neutral when it is pessimistic by replacing $Δ_θ-Δ_{\mathrm{ref}}$ with $Δ_θ-\max\{0,Δ_{\mathrm{ref}}\}$. This one-line change strictly strengthens per-example learning signals on pessimistic pairs while preserving DPO's objective form and computational cost. By conditionally debiasing the pessimistic reference signal, HyPO mitigates premature satisfaction; empirically, across preference alignment, HyPO improves inference-aligned metrics and achieves higher pairwise win rates. Our results provide evidence that direct preference alignment could be enhanced by conditionally debiasing the reference signal, rather than discarding it.

