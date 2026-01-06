---
layout: default
title: Deferred Commitment Decoding for Diffusion Language Models with Confidence-Aware Sliding Windows
---

# Deferred Commitment Decoding for Diffusion Language Models with Confidence-Aware Sliding Windows
**arXiv**：[2601.02076v1](https://arxiv.org/abs/2601.02076) · [PDF](https://arxiv.org/pdf/2601.02076.pdf)  
**作者**：Yingte Shu, Yuchuan Tian, Chao Xu, Yunhe Wang, Hanting Chen  

**一句话要点**：提出Deferred Commitment Decoding以解决扩散语言模型块解码中的边界诱导上下文截断问题

**关键词**：扩散语言模型, 并行文本生成, 解码策略, 置信度感知, 滑动窗口, 推理效率

## 3 点简述
- 核心问题：块解码导致边界附近未解码令牌被迫提前提交，缺乏未来上下文，降低解码置信度和生成质量
- 方法要点：基于置信度的滑动窗口，早期解决低不确定性令牌，延迟高不确定性令牌直至获得足够上下文证据
- 实验或效果：在多个模型和基准测试中，平均提升生成准确率1.39%，最大提升达9.0%，时间效率相当

## 摘要（原文）

> Diffusion language models (DLMs) have recently emerged as a strong alternative to autoregressive models by enabling parallel text generation. To improve inference efficiency and KV-cache compatibility, prior work commonly adopts block-based diffusion, decoding tokens block by block. However, this paradigm suffers from a structural limitation that we term Boundary-Induced Context Truncation (BICT): undecoded tokens near block boundaries are forced to commit without access to nearby future context, even when such context could substantially reduce uncertainty. This limitation degrades decoding confidence and generation quality, especially for tasks requiring precise reasoning, such as mathematical problem solving and code generation. We propose Deferred Commitment Decoding (DCD), a novel, training-free decoding strategy that mitigates this issue. DCD maintains a confidence-aware sliding window over masked tokens, resolving low-uncertainty tokens early while deferring high-uncertainty tokens until sufficient contextual evidence becomes available. This design enables effective bidirectional information flow within the decoding window without sacrificing efficiency. Extensive experiments across multiple diffusion language models, benchmarks, and caching configurations show that DCD improves generation accuracy by 1.39% with comparable time on average compared to fixed block-based diffusion methods, with the most significant improvement reaching 9.0%. These results demonstrate that deferring token commitment based on uncertainty is a simple yet effective principle for improving both the quality and efficiency of diffusion language model decoding.

