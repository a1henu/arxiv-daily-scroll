---
layout: default
title: GRACE: Designing Generative Face Video Codec via Agile Hardware-Centric Workflow
---

# GRACE: Designing Generative Face Video Codec via Agile Hardware-Centric Workflow
**arXiv**：[2511.09272v1](https://arxiv.org/abs/2511.09272) · [PDF](https://arxiv.org/pdf/2511.09272.pdf)  
**作者**：Rui Wan, Qi Zheng, Ruoyu Zhang, Bu Chen, Jiaming Liu, Min Li, Minge Jing, Jinjia Zhou, Yibo Fan  

**一句话要点**：提出基于FPGA的生成式人脸视频编解码方案，以优化边缘设备部署。

**关键词**：生成式视频编解码, FPGA加速, 边缘计算, 网络压缩, 软硬件协同设计, 能效优化

## 3 点简述
- 核心问题：AGC解码器在边缘设备部署困难，参数多、算法不灵活、功耗高。
- 方法要点：采用网络压缩和软硬件协同设计，设计FPGA加速器优化并行计算。
- 实验或效果：在PYNQ-Z1平台实现原型，能效比CPU和GPU分别高24.9倍和4.1倍。

## 摘要（原文）

> The Animation-based Generative Codec (AGC) is an emerging paradigm for talking-face video compression. However, deploying its intricate decoder on resource and power-constrained edge devices presents challenges due to numerous parameters, the inflexibility to adapt to dynamically evolving algorithms, and the high power consumption induced by extensive computations and data transmission. This paper for the first time proposes a novel field programmable gate arrays (FPGAs)-oriented AGC deployment scheme for edge-computing video services. Initially, we analyze the AGC algorithm and employ network compression methods including post-training static quantization and layer fusion techniques. Subsequently, we design an overlapped accelerator utilizing the co-processor paradigm to perform computations through software-hardware co-design. The hardware processing unit comprises engines such as convolution, grid sampling, upsample, etc. Parallelization optimization strategies like double-buffered pipelines and loop unrolling are employed to fully exploit the resources of FPGA. Ultimately, we establish an AGC FPGA prototype on the PYNQ-Z1 platform using the proposed scheme, achieving \textbf{24.9$\times$} and \textbf{4.1$\times$} higher energy efficiency against commercial Central Processing Unit (CPU) and Graphic Processing Unit (GPU), respectively. Specifically, only \textbf{11.7} microjoules ($\upmu$J) are required for one pixel reconstructed by this FPGA system.

