---
layout: default
title: Mixture of Ranks with Degradation-Aware Routing for One-Step Real-World Image Super-Resolution
---

# Mixture of Ranks with Degradation-Aware Routing for One-Step Real-World Image Super-Resolution
**arXiv**：[2511.16024v1](https://arxiv.org/abs/2511.16024) · [PDF](https://arxiv.org/pdf/2511.16024.pdf)  
**作者**：Xiao He, Zhijun Tu, Kun Cheng, Mingrui Zhu, Jie Hu, Nannan Wang, Xinbo Gao  

**一句话要点**：提出混合秩架构与退化感知路由以解决一步真实世界图像超分辨率问题

**关键词**：图像超分辨率, 混合专家, 退化感知路由, 低秩适应, 一步重建

## 3 点简述
- 现有真实世界图像超分辨率方法难以自适应捕捉复杂退化样本的异质特征
- 引入混合秩架构，将LoRA秩作为专家，结合退化估计模块动态激活专家
- 实验验证框架在真实世界图像超分辨率中达到先进性能

## 摘要（原文）

> The demonstrated success of sparsely-gated Mixture-of-Experts (MoE) architectures, exemplified by models such as DeepSeek and Grok, has motivated researchers to investigate their adaptation to diverse domains. In real-world image super-resolution (Real-ISR), existing approaches mainly rely on fine-tuning pre-trained diffusion models through Low-Rank Adaptation (LoRA) module to reconstruct high-resolution (HR) images. However, these dense Real-ISR models are limited in their ability to adaptively capture the heterogeneous characteristics of complex real-world degraded samples or enable knowledge sharing between inputs under equivalent computational budgets. To address this, we investigate the integration of sparse MoE into Real-ISR and propose a Mixture-of-Ranks (MoR) architecture for single-step image super-resolution. We introduce a fine-grained expert partitioning strategy that treats each rank in LoRA as an independent expert. This design enables flexible knowledge recombination while isolating fixed-position ranks as shared experts to preserve common-sense features and minimize routing redundancy. Furthermore, we develop a degradation estimation module leveraging CLIP embeddings and predefined positive-negative text pairs to compute relative degradation scores, dynamically guiding expert activation. To better accommodate varying sample complexities, we incorporate zero-expert slots and propose a degradation-aware load-balancing loss, which dynamically adjusts the number of active experts based on degradation severity, ensuring optimal computational resource allocation. Comprehensive experiments validate our framework's effectiveness and state-of-the-art performance.

