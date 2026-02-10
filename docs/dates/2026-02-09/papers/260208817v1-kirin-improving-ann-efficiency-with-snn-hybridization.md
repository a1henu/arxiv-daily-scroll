---
layout: default
title: Kirin: Improving ANN efficiency with SNN Hybridization
---

# Kirin: Improving ANN efficiency with SNN Hybridization
**arXiv**：[2602.08817v1](https://arxiv.org/abs/2602.08817) · [PDF](https://arxiv.org/pdf/2602.08817.pdf)  
**作者**：Chenyu Wang, Zhanglu Yan, Zhi Zhou, Xu Chen, Weng-Fai Wong  

**一句话要点**：提出Kirin混合整数与脉冲的SNN，实现无损ANN转换并提升时间与能效

**关键词**：脉冲神经网络, ANN-SNN转换, 量化优化, 能效提升, 混合编码

## 3 点简述
- 核心问题：ANN转SNN中量化导致高延迟，单脉冲与多脉冲方案存在信息损失与能耗权衡
- 方法要点：采用脉冲矩阵混合策略，低比特参数编码为脉冲，高比特保留整数，结合静默阈值机制确保输出等效
- 实验或效果：在W4A4&8量化下，接近FP16精度，能耗降低84.66%，时间步缩短93.75%

## 摘要（原文）

> Artificial neural networks (ANNs), particularly large language models (LLMs), demonstrate powerful inference capabilities but consume substantial energy. Conversely, spiking neural networks (SNNs) exhibit exceptional energy efficiency due to their binary and event-driven characteristics, thus motivating the study of ANN-to-SNN conversion. In this process, quantization plays a pivotal role, mapping LLMs' floating-point parameters to discrete SNN parameters via the temporal dimension of the time window. However, several challenges remain in the conversion process: (i) converting high bit-width quantization values into binary spikes requires longer time windows, increasing system latency; and (ii) the inherent trade-off between the information loss of single-spike schemes and the energy costs of multi-spike ones in SNN. To address these challenges, we propose Kirin, a integer and spike hybrid based SNN to achieve accuracy lossless ANN-to-SNN conversion with time and energy efficiency. Specifically, we first propose a Spike Matrix Hybridization strategy that encoding low bit-width parameters that leading to small time window size into binary spikes while preserving the rest in integer format, thereby reducing the overall latency of SNN execution. Second, we introduce a silence threshold mechanism to regulate the timing of single-spike firing, ensuring the output is mathematically equivalent to the LLM's output and preserves accuracy. Experimental results demonstrate that Kirin, under a W4A4\&8 quantization setting, achieves near-FP16 accuracy while reducing energy consumption by up to 84.66\% and shortening time steps by 93.75\%.

