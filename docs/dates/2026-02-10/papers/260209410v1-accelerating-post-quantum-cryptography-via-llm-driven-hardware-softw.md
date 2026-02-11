---
layout: default
title: Accelerating Post-Quantum Cryptography via LLM-Driven Hardware-Software Co-Design
---

# Accelerating Post-Quantum Cryptography via LLM-Driven Hardware-Software Co-Design
**arXiv**：[2602.09410v1](https://arxiv.org/abs/2602.09410) · [PDF](https://arxiv.org/pdf/2602.09410.pdf)  
**作者**：Yuchao Liao, Tosiron Adegbija, Roman Lysecky  

**一句话要点**：提出基于大语言模型的软硬件协同设计框架，以加速后量子密码算法的FPGA实现。

**关键词**：后量子密码, 大语言模型, 软硬件协同设计, FPGA加速, FALCON签名方案, 性能优化

## 3 点简述
- 核心问题：后量子密码算法计算复杂，硬件实现效率低，需加速设计过程。
- 方法要点：利用大语言模型分析算法、识别关键组件，并生成FPGA硬件描述候选方案。
- 实验或效果：在FALCON签名方案中，人机协同的LLM生成加速器比传统HLS方法快2.6倍，但资源利用和功耗存在权衡。

## 摘要（原文）

> Post-quantum cryptography (PQC) is crucial for securing data against emerging quantum threats. However, its algorithms are computationally complex and difficult to implement efficiently on hardware. In this paper, we explore the potential of Large Language Models (LLMs) to accelerate the hardware-software co-design process for PQC, with a focus on the FALCON digital signature scheme. We present a novel framework that leverages LLMs to analyze PQC algorithms, identify performance-critical components, and generate candidate hardware descriptions for FPGA implementation. We present the first quantitative comparison between LLM-driven synthesis and conventional HLS-based approaches for low-level compute-intensive kernels in FALCON, showing that human-in-the-loop LLM-generated accelerators can achieve up to 2.6x speedup in kernel execution time with shorter critical paths, while highlighting trade-offs in resource utilization and power consumption. Our results suggest that LLMs can minimize design effort and development time by automating FPGA accelerator design iterations for PQC algorithms, offering a promising new direction for rapid and adaptive PQC accelerator design on FPGAs.

