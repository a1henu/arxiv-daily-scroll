---
layout: default
title: VedicTHG: Symbolic Vedic Computation for Low-Resource Talking-Head Generation in Educational Avatars
---

# VedicTHG: Symbolic Vedic Computation for Low-Resource Talking-Head Generation in Educational Avatars
**arXiv**：[2602.08775v1](https://arxiv.org/abs/2602.08775) · [PDF](https://arxiv.org/pdf/2602.08775.pdf)  
**作者**：Vineet Kumar Rakesh, Ahana Bhattacharjee, Soumya Mazumdar, Tapas Samanta, Hemendra Kumar Pandey, Amitabha Das, Sarbajit Pal  

**一句话要点**：提出基于符号吠陀计算的确定性框架，用于低资源教育头像的说话头生成，以降低计算负载和延迟。

**关键词**：说话头生成, 低资源计算, 符号计算, 教育技术, CPU实时渲染, 视素映射

## 3 点简述
- 核心问题：现有说话头生成方法依赖GPU、大数据或高容量模型，难以在离线或资源受限环境中部署。
- 方法要点：采用符号吠陀计算，将语音转换为音素流，映射到紧凑视素库，并通过符号协同发音生成平滑轨迹，结合轻量2D渲染器实现CPU实时合成。
- 实验或效果：在仅CPU执行下评估同步准确性、时间稳定性和身份一致性，结果显示可接受唇同步质量，显著减少计算负载和延迟。

## 摘要（原文）

> Talking-head avatars are increasingly adopted in educational technology to deliver content with social presence and improved engagement. However, many recent talking-head generation (THG) methods rely on GPU-centric neural rendering, large training sets, or high-capacity diffusion models, which limits deployment in offline or resource-constrained learning environments. A deterministic and CPU-oriented THG framework is described, termed Symbolic Vedic Computation, that converts speech to a time-aligned phoneme stream, maps phonemes to a compact viseme inventory, and produces smooth viseme trajectories through symbolic coarticulation inspired by Vedic sutra Urdhva Tiryakbhyam. A lightweight 2D renderer performs region-of-interest (ROI) warping and mouth compositing with stabilization to support real-time synthesis on commodity CPUs. Experiments report synchronization accuracy, temporal stability, and identity consistency under CPU-only execution, alongside benchmarking against representative CPU-feasible baselines. Results indicate that acceptable lip-sync quality can be achieved while substantially reducing computational load and latency, supporting practical educational avatars on low-end hardware. GitHub: https://vineetkumarrakesh.github.io/vedicthg

