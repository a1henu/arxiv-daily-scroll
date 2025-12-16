---
layout: default
title: VLCache: Computing 2% Vision Tokens and Reusing 98% for Vision-Language Inference
---

# VLCache: Computing 2% Vision Tokens and Reusing 98% for Vision-Language Inference
**arXiv**：[2512.12977v1](https://arxiv.org/abs/2512.12977) · [PDF](https://arxiv.org/pdf/2512.12977.pdf)  
**作者**：Shengling Qin, Hao Yu, Chenxin Wu, Zheng Li, Yizhong Cao, Zhengyang Zhuge, Yuxin Zhou, Wentao Yao, Yi Zhang, Zhengheng Wang, Shuai Bai, Jianwei Zhang, Junyang Lin  

**一句话要点**：提出VLCache框架，通过复用多模态输入的KV缓存和编码器缓存，减少视觉语言推理中的重复计算。

**关键词**：视觉语言推理, 缓存复用, KV缓存, 编码器缓存, 动态重计算, 推理加速

## 3 点简述
- 核心问题：多模态输入重复出现时，传统方法需全量重计算，导致推理效率低下。
- 方法要点：形式化分析累积复用误差，提出动态层感知重计算策略，平衡精度与效率。
- 实验或效果：仅需计算2-5%的视觉令牌，实现1.2x-16x的首次令牌时间加速，精度与全重计算相当。

## 摘要（原文）

> This paper presents VLCache, a cache reuse framework that exploits both Key-Value (KV) cache and encoder cache from prior multimodal inputs to eliminate costly recomputation when the same multimodal inputs recur. Unlike previous heuristic approaches, we formally identify the cumulative reuse error effect and demonstrate how to minimize the non-prefix cache reuse error effectively. We further analyze the varying importance of model layers and propose a dynamic, layer-aware recomputation strategy to balance accuracy and efficiency. Experimental results show that VLCache achieves an accuracy on par with full recomputation, while requiring only 2-5% of the tokens to compute, yielding 1.2x-16x TTFT speedups. The proposed VLCache pipeline has been integrated into SGLang, enabling significantly faster inference in practical deployments.

