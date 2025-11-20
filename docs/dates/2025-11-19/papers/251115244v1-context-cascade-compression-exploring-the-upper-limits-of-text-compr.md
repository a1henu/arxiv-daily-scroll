---
layout: default
title: Context Cascade Compression: Exploring the Upper Limits of Text Compression
---

# Context Cascade Compression: Exploring the Upper Limits of Text Compression
**arXiv**：[2511.15244v1](https://arxiv.org/abs/2511.15244) · [PDF](https://arxiv.org/pdf/2511.15244.pdf)  
**作者**：Fanfan Liu, Haibo Qiu  

**一句话要点**：提出上下文级联压缩以解决长上下文任务中的计算与内存挑战

**关键词**：文本压缩, 上下文压缩, 级联模型, 潜在令牌, 解码准确率

## 3 点简述
- 长上下文任务中百万级令牌输入导致LLM计算与内存负担重
- 级联大小LLM进行压缩与解码，小模型压缩为潜在令牌，大模型解码
- 实验显示20倍压缩比下解码准确率达98%，40倍时保持约93%

## 摘要（原文）

> Million-level token inputs in long-context tasks pose significant computational and memory challenges for Large Language Models (LLMs). Recently, DeepSeek-OCR conducted research into the feasibility of Contexts Optical Compression and achieved preliminary results. Inspired by this, we introduce Context Cascade Compression C3 to explore the upper limits of text compression. Our method cascades two LLMs of different sizes to handle the compression and decoding tasks. Specifically, a small LLM, acting as the first stage, performs text compression by condensing a long context into a set of latent tokens (e.g., 32 or 64 in length), achieving a high ratio of text tokens to latent tokens. A large LLM, as the second stage, then executes the decoding task on this compressed context. Experiments show that at a 20x compression ratio (where the number of text tokens is 20 times the number of latent tokens), our model achieves 98% decoding accuracy, compared to approximately 60% for DeepSeek-OCR. When we further increase the compression ratio to 40x, the accuracy is maintained at around 93%. This indicates that in the domain of context compression, C3 Compression demonstrates superior performance and feasibility over optical character compression. C3 uses a simpler, pure-text pipeline that ignores factors like layout, color, and information loss from a visual encoder. This also suggests a potential upper bound for compression ratios in future work on optical character compression, OCR, and related fields. Codes and model weights are publicly accessible at https://github.com/liufanfanlff/C3-Context-Cascade-Compression

