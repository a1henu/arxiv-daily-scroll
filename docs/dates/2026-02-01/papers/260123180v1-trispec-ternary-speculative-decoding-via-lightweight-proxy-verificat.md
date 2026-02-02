---
layout: default
title: TriSpec: Ternary Speculative Decoding via Lightweight Proxy Verification
---

# TriSpec: Ternary Speculative Decoding via Lightweight Proxy Verification
**arXiv**：[2601.23180v1](https://arxiv.org/abs/2601.23180) · [PDF](https://arxiv.org/pdf/2601.23180.pdf)  
**作者**：Haoyun Jiang, Junqi He, Feng Hong, Xinlong Yang, Jianwei Zhang, Zheng Li, Zhengyang Zhuge, Zhiyong Chen, Bo Han, Junyang Lin, Jiangchao Yao  

**一句话要点**：提出TriSpec三元推测解码框架，通过轻量代理验证降低大语言模型推理成本。

**关键词**：推测解码, 轻量代理验证, 三元框架, 推理加速, 大语言模型优化

## 3 点简述
- 核心问题：推测解码中验证阶段计算成本高，限制大语言模型推理效率提升。
- 方法要点：引入轻量代理，仅对不确定令牌调用完整目标模型，减少验证开销。
- 实验或效果：在Qwen3和DeepSeek-R1-Distill-Qwen/LLaMA模型上，相比标准推测解码加速达35%，目标模型调用减少50%。

## 摘要（原文）

> Inference efficiency in Large Language Models (LLMs) is fundamentally limited by their serial, autoregressive generation, especially as reasoning becomes a key capability and response sequences grow longer. Speculative decoding (SD) offers a powerful solution, providing significant speed-ups through its lightweight drafting and parallel verification mechanism. While existing work has nearly saturated improvements in draft effectiveness and efficiency, this paper advances SD from a new yet critical perspective: the verification cost. We propose TriSpec, a novel ternary SD framework that, at its core, introduces a lightweight proxy to significantly reduce computational cost by approving easily verifiable draft sequences and engaging the full target model only when encountering uncertain tokens. TriSpec can be integrated with state-of-the-art SD methods like EAGLE-3 to further reduce verification costs, achieving greater acceleration. Extensive experiments on the Qwen3 and DeepSeek-R1-Distill-Qwen/LLaMA families show that TriSpec achieves up to 35\% speedup over standard SD, with up to 50\% fewer target model invocations while maintaining comparable accuracy.

