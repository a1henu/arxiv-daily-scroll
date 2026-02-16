---
layout: default
title: Unleashing Low-Bit Inference on Ascend NPUs: A Comprehensive Evaluation of HiFloat Formats
---

# Unleashing Low-Bit Inference on Ascend NPUs: A Comprehensive Evaluation of HiFloat Formats
**arXiv**：[2602.12635v1](https://arxiv.org/abs/2602.12635) · [PDF](https://arxiv.org/pdf/2602.12635.pdf)  
**作者**：Pengxiang Zhao, Hui-Ling Zhen, Xing Li, Han Bao, Weizhe Lin, Zhiyuan Yang, Ziwei Yu, Xin Wang, Mingxuan Yuan, Xianzhi Yu, Zhenhua Dong  

**一句话要点**：评估HiFloat低比特浮点格式以提升昇腾NPU上LLM推理效率

**关键词**：低比特推理, 浮点格式, 昇腾NPU, 后训练量化, LLM效率

## 3 点简述
- 核心问题：LLM规模扩大，需低比特格式如MXFP和NVFP4平衡精度与效率。
- 方法要点：针对昇腾NPU定制HiFloat格式（HiF8和HiF4），通过权重-激活和KV缓存任务进行严格比较。
- 实验或效果：HiF4的分层缩放避免整数格式的精度崩溃，HiFloat兼容先进后训练量化框架，提供高效推理方案。

## 摘要（原文）

> As LLMs scale, low-bit floating-point formats like MXFP and NVFP4 offer new opportunities for precision and efficiency. In this work, we evaluate HiFloat (HiF8 and HiF4), a family of formats tailored for Ascend NPUs. Through rigorous comparison across weight-activation and KV-cache tasks, we provide three key insights: (1) INT8 suits narrow-range data, while floating-point formats excel with high-variance data; (2) in 4-bit regimes, HiF4's hierarchical scaling prevents the accuracy collapse seen in integer formats; and (3) HiFloat is fully compatible with state-of-the-art post-training quantization frameworks. Overall, HiFloat provides a solution for high-efficiency LLM inference on NPUs.

