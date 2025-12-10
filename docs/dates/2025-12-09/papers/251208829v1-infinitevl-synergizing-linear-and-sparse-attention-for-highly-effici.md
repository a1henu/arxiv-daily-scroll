---
layout: default
title: InfiniteVL: Synergizing Linear and Sparse Attention for Highly-Efficient, Unlimited-Input Vision-Language Models
---

# InfiniteVL: Synergizing Linear and Sparse Attention for Highly-Efficient, Unlimited-Input Vision-Language Models
**arXiv**：[2512.08829v1](https://arxiv.org/abs/2512.08829) · [PDF](https://arxiv.org/pdf/2512.08829.pdf)  
**作者**：Hongyuan Tao, Bencheng Liao, Shaoyu Chen, Haoran Yin, Qian Zhang, Wenyu Liu, Xinggang Wang  

**一句话要点**：提出InfiniteVL，结合滑动窗口与线性注意力，实现高效无限输入视觉语言模型。

**关键词**：无限输入视觉语言模型, 线性复杂度注意力, 滑动窗口注意力, 长序列训练, 实时视频理解, 蒸馏预训练

## 3 点简述
- 问题：窗口注意力超窗性能下降，线性注意力信息密集型任务表现不足。
- 方法：融合滑动窗口注意力与Gated DeltaNet，设计三阶段训练策略。
- 效果：数据量少2%，性能匹配领先Transformer模型，推理加速3.6倍。

## 摘要（原文）

> Window attention and linear attention represent two principal strategies for mitigating the quadratic complexity and ever-growing KV cache in Vision-Language Models (VLMs). However, we observe that window-based VLMs suffer performance degradation when sequence length exceeds the window size, while linear attention underperforms on information-intensive tasks such as OCR and document understanding. To overcome these limitations, we propose InfiniteVL, a linear-complexity VLM architecture that synergizes sliding window attention (SWA) with Gated DeltaNet. For achieving competitive multimodal performance under constrained resources, we design a three-stage training strategy comprising distillation pretraining, instruction tuning, and long-sequence SFT. Remarkably, using less than 2\% of the training data required by leading VLMs, InfiniteVL not only substantially outperforms previous linear-complexity VLMs but also matches the performance of leading Transformer-based VLMs, while demonstrating effective long-term memory retention. Compared to similar-sized Transformer-based VLMs accelerated by FlashAttention-2, InfiniteVL achieves over 3.6\times inference speedup while maintaining constant latency and memory footprint. In streaming video understanding scenarios, it sustains a stable 24 FPS real-time prefill speed while preserving long-term memory cache. Code and models are available at https://github.com/hustvl/InfiniteVL.

