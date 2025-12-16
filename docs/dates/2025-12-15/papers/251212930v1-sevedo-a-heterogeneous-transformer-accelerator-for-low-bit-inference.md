---
layout: default
title: SeVeDo: A Heterogeneous Transformer Accelerator for Low-Bit Inference via Hierarchical Group Quantization and SVD-Guided Mixed Precision
---

# SeVeDo: A Heterogeneous Transformer Accelerator for Low-Bit Inference via Hierarchical Group Quantization and SVD-Guided Mixed Precision
**arXiv**：[2512.12930v1](https://arxiv.org/abs/2512.12930) · [PDF](https://arxiv.org/pdf/2512.12930.pdf)  
**作者**：Yuseon Choi, Sangjin Kim, Jungjun Oh, Byeongcheol Kim, Hoi-Jun Yoo  

**一句话要点**：提出SeVeDo异构加速器，通过分层组量化和SVD引导混合精度解决低比特推理中的激活异常值问题

**关键词**：低比特量化, 异构加速器, 分层组量化, SVD引导混合精度, 能效优化, Transformer推理

## 3 点简述
- 核心问题：低比特量化因激活异常值导致精度下降，现有方法能耗高
- 方法要点：异构架构分离异常值敏感组件，结合分层组量化和SVD引导混合精度
- 实验或效果：在ViT-Base和Llama2-7B上实现最高13.8TOPS/W的能效，超越传统设计

## 摘要（原文）

> Low-bit quantization is a promising technique for efficient transformer inference by reducing computational and memory overhead. However, aggressive bitwidth reduction remains challenging due to activation outliers, leading to accuracy degradation. Existing methods, such as outlier-handling and group quantization, achieve high accuracy but incur substantial energy consumption. To address this, we propose SeVeDo, an energy-efficient SVD-based heterogeneous accelerator that structurally separates outlier-sensitive components into a high-precision low-rank path, while the remaining computations are executed in a low-bit residual datapath with group quantization. To further enhance efficiency, Hierarchical Group Quantization (HGQ) combines coarse-grained floating-point scaling with fine-grained shifting, effectively reducing dequantization cost. Also, SVD-guided mixed precision (SVD-MP) statically allocates higher bitwidths to precision-sensitive components identified through low-rank decomposition, thereby minimizing floating-point operation cost. Experimental results show that SeVeDo achieves a peak energy efficiency of 13.8TOPS/W, surpassing conventional designs, with 12.7TOPS/W on ViT-Base and 13.4TOPS/W on Llama2-7B benchmarks.

