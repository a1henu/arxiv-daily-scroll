---
layout: default
title: ODMA: On-Demand Memory Allocation Framework for LLM Serving on LPDDR-Class Accelerators
---

# ODMA: On-Demand Memory Allocation Framework for LLM Serving on LPDDR-Class Accelerators
**arXiv**：[2512.09427v1](https://arxiv.org/abs/2512.09427) · [PDF](https://arxiv.org/pdf/2512.09427.pdf)  
**作者**：Guoqiang Zou, Wanyu Wang, Hao Zheng, Longxiang Yin, Yinhe Han  

**一句话要点**：提出ODMA框架以解决随机访问受限加速器上LLM服务的内存分配问题

**关键词**：大语言模型服务, 内存管理, 随机访问受限加速器, 动态分配, 性能优化

## 3 点简述
- 核心问题：现有内存管理器在随机访问带宽差的加速器上导致内存浪费或性能低下
- 方法要点：结合轻量级长度预测器、动态桶分区和大桶保护机制，优化内存分配
- 实验或效果：在Cambricon MLU370-X4上，内存利用率从55.05%提升至72.45%，RPS和TPS提高约30%

## 摘要（原文）

> Serving large language models (LLMs) on accelerators with poor random-access bandwidth (e.g., LPDDR5-based) is limited by current memory managers. Static pre-allocation wastes memory, while fine-grained paging (e.g., PagedAttention) is ill-suited due to high random-access costs. Existing HBM-centric solutions do not exploit the characteristics of random-access-constrained memory (RACM) accelerators like Cambricon MLU370. We present ODMA, an on-demand memory allocation framework for RACM. ODMA addresses distribution drift and heavy-tailed requests by coupling a lightweight length predictor with dynamic bucket partitioning and a large-bucket safeguard. Boundaries are periodically updated from live traces to maximize utilization. On Alpaca and Google-NQ, ODMA improves prediction accuracy of prior work significantly (e.g., from 82.68% to 93.36%). Serving DeepSeek-R1-Distill-Qwen-7B on Cambricon MLU370-X4, ODMA raises memory utilization from 55.05% to 72.45% and improves RPS and TPS by 29% and 27% over static baselines. This demonstrates that hardware-aware allocation unlocks efficient LLM serving on RACM platforms.

