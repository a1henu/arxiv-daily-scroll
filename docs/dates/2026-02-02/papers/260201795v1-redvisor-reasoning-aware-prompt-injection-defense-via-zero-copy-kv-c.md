---
layout: default
title: RedVisor: Reasoning-Aware Prompt Injection Defense via Zero-Copy KV Cache Reuse
---

# RedVisor: Reasoning-Aware Prompt Injection Defense via Zero-Copy KV Cache Reuse
**arXiv**：[2602.01795v1](https://arxiv.org/abs/2602.01795) · [PDF](https://arxiv.org/pdf/2602.01795.pdf)  
**作者**：Mingrui Liu, Sixiao Zhang, Cheng Long, Kwok-Yan Lam  

**一句话要点**：提出RedVisor框架，通过零拷贝KV缓存重用防御提示注入攻击，兼顾检测与预防。

**关键词**：提示注入防御, KV缓存重用, 可解释分析, 轻量级适配器, vLLM集成

## 3 点简述
- 核心问题：LLMs易受提示注入攻击，现有防御方法在效用与效率间存在权衡。
- 方法要点：使用轻量级适配器生成可解释分析，定位威胁并引导安全响应，实现KV缓存重用。
- 实验或效果：在检测精度和吞吐量上优于现有方法，效用损失可忽略，集成至vLLM引擎。

## 摘要（原文）

> Large Language Models (LLMs) are increasingly vulnerable to Prompt Injection (PI) attacks, where adversarial instructions hidden within retrieved contexts hijack the model's execution flow. Current defenses typically face a critical trade-off: prevention-based fine-tuning often degrades general utility via the "alignment tax", while detection-based filtering incurs prohibitive latency and memory costs. To bridge this gap, we propose RedVisor, a unified framework that synthesizes the explainability of detection systems with the seamless integration of prevention strategies. To the best of our knowledge, RedVisor is the first approach to leverage fine-grained reasoning paths to simultaneously detect attacks and guide the model's safe response. We implement this via a lightweight, removable adapter positioned atop the frozen backbone. This adapter serves a dual function: it first generates an explainable analysis that precisely localizes the injection and articulates the threat, which then explicitly conditions the model to reject the malicious command. Uniquely, the adapter is active only during this reasoning phase and is effectively muted during the subsequent response generation. This architecture yields two distinct advantages: (1) it mathematically preserves the backbone's original utility on benign inputs; and (2) it enables a novel KV Cache Reuse strategy, eliminating the redundant prefill computation inherent to decoupled pipelines. We further pioneer the integration of this defense into the vLLM serving engine with custom kernels. Experiments demonstrate that RedVisor outperforms state-of-the-art defenses in detection accuracy and throughput while incurring negligible utility loss.

