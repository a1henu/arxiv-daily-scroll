---
layout: default
title: PAS: A Training-Free Stabilizer for Temporal Encoding in Video LLMs
---

# PAS: A Training-Free Stabilizer for Temporal Encoding in Video LLMs
**arXiv**：[2511.10979v1](https://arxiv.org/abs/2511.10979) · [PDF](https://arxiv.org/pdf/2511.10979.pdf)  
**作者**：Bowen Sun, Yujun Cai, Ming-Hsuan Yang, Hang Wu, Yiwei Wang  

**一句话要点**：提出PAS以解决视频大语言模型中时序编码的不稳定性问题

**关键词**：视频大语言模型, 时序编码, 位置嵌入, 注意力机制, 训练免费方法, 鲁棒性提升

## 3 点简述
- 核心问题：视频LLMs中时序不一致，小帧时移导致注意力翻转和抑制相关帧
- 方法要点：使用相位聚合平滑，多相位偏移聚合输出，平滑时序核而不改编码结构
- 实验或效果：多基准测试显示一致改进，计算开销可忽略，提升时序鲁棒性

## 摘要（原文）

> Video LLMs suffer from temporal inconsistency: small shifts in frame timing can flip attention and suppress relevant frames. We trace this instability to the common extension of Rotary Position Embeddings to video through multimodal RoPE. The induced inverse Fourier time kernel exhibits frame-scale ripples that multiply adjacent frames by different factors, which perturbs attention that should otherwise be governed by the raw query key inner product. We present Phase Aggregated Smoothing (PAS), a simple, training-free mechanism that applies small opposed phase offsets across heads and then aggregates their outputs. PAS preserves the per-head spectrum magnitude, while the aggregation effectively smooths the temporal kernel and reduces phase sensitivity without changing the positional encoding structure. Our analysis shows that the RoPE rotated logit can be approximated as a content dot product scaled by a time kernel; smoothing this kernel yields Lipschitz stability of attention to small temporal shifts; multi phase averaging attenuates high frequency ripples while preserving per-head spectra under Nyquist-valid sampling. Experiments on multiple video understanding benchmarks under matched token budgets show consistent improvements with negligible computational overhead. PAS provides a plug and play upgrade for robust temporal encoding in Video LLMs.

