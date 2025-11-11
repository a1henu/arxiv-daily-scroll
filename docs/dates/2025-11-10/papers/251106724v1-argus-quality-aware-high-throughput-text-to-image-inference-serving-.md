---
layout: default
title: Argus: Quality-Aware High-Throughput Text-to-Image Inference Serving System
---

# Argus: Quality-Aware High-Throughput Text-to-Image Inference Serving System
**arXiv**：[2511.06724v1](https://arxiv.org/abs/2511.06724) · [PDF](https://arxiv.org/pdf/2511.06724.pdf)  
**作者**：Shubham Agarwal, Subrata Mitra, Saud Iqbal  

**一句话要点**：提出Argus系统以解决文本到图像推理的高吞吐量与质量平衡问题

**关键词**：文本到图像推理, 扩散模型, 近似计算, 质量感知, 高吞吐系统, 服务级别目标

## 3 点简述
- 核心问题：扩散模型推理时间长，难以在固定集群上实现高吞吐量
- 方法要点：根据提示智能选择近似模型和设置，避免质量下降
- 实验或效果：相比基线，延迟SLO违规减少10倍，质量提升10%，吞吐量提高40%

## 摘要（原文）

> Text-to-image (T2I) models have gained significant popularity. Most of these
> are diffusion models with unique computational characteristics, distinct from
> both traditional small-scale ML models and large language models. They are
> highly compute-bound and use an iterative denoising process to generate images,
> leading to very high inference time. This creates significant challenges in
> designing a high-throughput system. We discovered that a large fraction of
> prompts can be served using faster, approximated models. However, the
> approximation setting must be carefully calibrated for each prompt to avoid
> quality degradation. Designing a high-throughput system that assigns each
> prompt to the appropriate model and compatible approximation setting remains a
> challenging problem. We present Argus, a high-throughput T2I inference system
> that selects the right level of approximation for each prompt to maintain
> quality while meeting throughput targets on a fixed-size cluster. Argus
> intelligently switches between different approximation strategies to satisfy
> both throughput and quality requirements. Overall, Argus achieves 10x fewer
> latency service-level objective (SLO) violations, 10% higher average quality,
> and 40% higher throughput compared to baselines on two real-world workload
> traces.

