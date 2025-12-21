---
layout: default
title: cuPilot: A Strategy-Coordinated Multi-agent Framework for CUDA Kernel Evolution
---

# cuPilot: A Strategy-Coordinated Multi-agent Framework for CUDA Kernel Evolution
**arXiv**：[2512.16465v1](https://arxiv.org/abs/2512.16465) · [PDF](https://arxiv.org/pdf/2512.16465.pdf)  
**作者**：Jinwu Chen, Qidie Wu, Bin Li, Lin Ma, Xin Si, Yang Hu, Shouyi Yin, Jun Yang  

**一句话要点**：提出cuPilot多智能体框架，通过策略协调优化CUDA内核，提升性能。

**关键词**：CUDA内核优化, 多智能体框架, 进化算法, 硬件软件协同设计, 策略协调, 屋顶线模型

## 3 点简述
- 核心问题：现有方法因智能体设计和进化表示不匹配，导致CUDA内核优化性能不足。
- 方法要点：引入策略作为中间语义表示，采用策略协调进化算法和屋顶线引导提示。
- 实验或效果：在100个内核基准测试中，平均加速比PyTorch达3.09倍，GEMM任务实现硬件单元高利用率。

## 摘要（原文）

> Optimizing CUDA kernels is a challenging and labor-intensive task, given the need for hardware-software co-design expertise and the proprietary nature of high-performance kernel libraries. While recent large language models (LLMs) combined with evolutionary algorithms show promise in automatic kernel optimization, existing approaches often fall short in performance due to their suboptimal agent designs and mismatched evolution representations. This work identifies these mismatches and proposes cuPilot, a strategy-coordinated multi-agent framework that introduces strategy as an intermediate semantic representation for kernel evolution. Key contributions include a strategy-coordinated evolution algorithm, roofline-guided prompting, and strategy-level population initialization. Experimental results show that the generated kernels by cuPilot achieve an average speed up of 3.09$\times$ over PyTorch on a benchmark of 100 kernels. On the GEMM tasks, cuPilot showcases sophisticated optimizations and achieves high utilization of critical hardware units. The generated kernels are open-sourced at https://github.com/champloo2878/cuPilot-Kernels.git.

