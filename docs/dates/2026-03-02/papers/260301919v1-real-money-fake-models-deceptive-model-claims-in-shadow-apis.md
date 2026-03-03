---
layout: default
title: Real Money, Fake Models: Deceptive Model Claims in Shadow APIs
---

# Real Money, Fake Models: Deceptive Model Claims in Shadow APIs
**arXiv**：[2603.01919v1](https://arxiv.org/abs/2603.01919) · [PDF](https://arxiv.org/pdf/2603.01919.pdf)  
**作者**：Yage Zhang, Yukun Jiang, Zeyuan Chen, Michael Backes, Xinyue Shen, Yang Zhang  

**一句话要点**：系统审计影子API，揭示其欺骗性模型声明与性能差异

**关键词**：影子API审计, 大语言模型验证, 性能差异分析, 科学研究可重复性, 第三方服务可靠性

## 3 点简述
- 核心问题：影子API声称提供官方LLM访问，但输出一致性未知，影响研究可靠性
- 方法要点：识别17个影子API，通过效用、安全性和模型验证进行多维审计
- 实验或效果：发现性能差异达47.21%，安全行为不可预测，45.83%指纹测试失败

## 摘要（原文）

> Access to frontier large language models (LLMs), such as GPT-5 and Gemini-2.5, is often hindered by high pricing, payment barriers, and regional restrictions. These limitations drive the proliferation of $\textit{shadow APIs}$, third-party services that claim to provide access to official model services without regional limitations via indirect access. Despite their widespread use, it remains unclear whether shadow APIs deliver outputs consistent with those of the official APIs, raising concerns about the reliability of downstream applications and the validity of research findings that depend on them. In this paper, we present the first systematic audit between official LLM APIs and corresponding shadow APIs. We first identify 17 shadow APIs that have been utilized in 187 academic papers, with the most popular one reaching 5,966 citations and 58,639 GitHub stars by December 6, 2025. Through multidimensional auditing of three representative shadow APIs across utility, safety, and model verification, we uncover both indirect and direct evidence of deception practices in shadow APIs. Specifically, we reveal performance divergence reaching up to $47.21\%$, significant unpredictability in safety behaviors, and identity verification failures in $45.83\%$ of fingerprint tests. These deceptive practices critically undermine the reproducibility and validity of scientific research, harm the interests of shadow API users, and damage the reputation of official model providers.

