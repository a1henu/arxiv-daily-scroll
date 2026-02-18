---
layout: default
title: 1-Bit Wonder: Improving QAT Performance in the Low-Bit Regime through K-Means Quantization
---

# 1-Bit Wonder: Improving QAT Performance in the Low-Bit Regime through K-Means Quantization
**arXiv**：[2602.15563v1](https://arxiv.org/abs/2602.15563) · [PDF](https://arxiv.org/pdf/2602.15563.pdf)  
**作者**：Sohir Maskey, Constantin Eichenberg, Johannes Messner, Douglas Orr  

**一句话要点**：提出基于K-Means的1位量化方法，在低比特量化感知训练中提升大语言模型下游任务性能

**关键词**：量化感知训练, 低比特量化, K-Means量化, 大语言模型, 下游任务性能, 内存优化

## 3 点简述
- 量化感知训练在低比特场景下，量化格式与比特宽度的选择缺乏系统探索，性能评估常依赖困惑度指标
- 采用K-Means权重量化优于整数格式，可在标准硬件上高效实现，优化内存占用
- 在固定推理内存预算下，1位量化权重在生成下游任务中表现最佳

## 摘要（原文）

> Quantization-aware training (QAT) is an effective method to drastically reduce the memory footprint of LLMs while keeping performance degradation at an acceptable level. However, the optimal choice of quantization format and bit-width presents a challenge in practice. The full design space of quantization is not fully explored in the context of QAT, and the precise trade-off between quantization and downstream performance is poorly understood, as comparisons often rely solely on perplexity-based evaluations. In this work, we address these shortcomings with an empirical study of QAT in the low-bit regime. We show that k-means based weight quantization outperforms integer formats and can be implemented efficiently on standard hardware. Furthermore, we find that, under a fixed inference memory budget, the best performance on generative downstream tasks is achieved with $1$-bit quantized weights.

