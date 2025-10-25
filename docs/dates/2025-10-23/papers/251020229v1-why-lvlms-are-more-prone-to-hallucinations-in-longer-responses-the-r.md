---
layout: default
title: Why LVLMs Are More Prone to Hallucinations in Longer Responses: The Role of Context
---

# Why LVLMs Are More Prone to Hallucinations in Longer Responses: The Role of Context
**arXiv**：[2510.20229v1](https://arxiv.org/abs/2510.20229) · [PDF](https://arxiv.org/pdf/2510.20229.pdf)  
**作者**：Ge Zheng, Jiaye Qian, Jiajin Tang, Sibei Yang  

**一句话要点**：提出诱导-检测-抑制框架以减少LVLM长响应中的幻觉

**关键词**：大型视觉语言模型, 幻觉抑制, 上下文依赖, 诱导检测框架, 对象级幻觉

## 3 点简述
- 核心问题：LVLM长响应中幻觉增加源于对上下文的过度依赖，而非长度本身
- 方法要点：通过设计上下文主动诱导幻觉，用于早期检测高风险案例
- 实验或效果：在多个基准测试中实现一致且显著的幻觉抑制改进

## 摘要（原文）

> Large Vision-Language Models (LVLMs) have made significant progress in recent
> years but are also prone to hallucination issues. They exhibit more
> hallucinations in longer, free-form responses, often attributed to accumulated
> uncertainties. In this paper, we ask: Does increased hallucination result
> solely from length-induced errors, or is there a deeper underlying mechanism?
> After a series of preliminary experiments and findings, we suggest that the
> risk of hallucinations is not caused by length itself but by the increased
> reliance on context for coherence and completeness in longer responses.
> Building on these insights, we propose a novel "induce-detect-suppress"
> framework that actively induces hallucinations through deliberately designed
> contexts, leverages induced instances for early detection of high-risk cases,
> and ultimately suppresses potential object-level hallucinations during actual
> decoding. Our approach achieves consistent, significant improvements across all
> benchmarks, demonstrating its efficacy. The strong detection and improved
> hallucination mitigation not only validate our framework but, more importantly,
> re-validate our hypothesis on context. Rather than solely pursuing performance
> gains, this study aims to provide new insights and serves as a first step
> toward a deeper exploration of hallucinations in LVLMs' longer responses.

