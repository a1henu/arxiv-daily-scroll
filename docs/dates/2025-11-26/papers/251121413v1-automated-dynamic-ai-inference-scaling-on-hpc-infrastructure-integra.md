---
layout: default
title: Automated Dynamic AI Inference Scaling on HPC-Infrastructure: Integrating Kubernetes, Slurm and vLLM
---

# Automated Dynamic AI Inference Scaling on HPC-Infrastructure: Integrating Kubernetes, Slurm and vLLM
**arXiv**：[2511.21413v1](https://arxiv.org/abs/2511.21413) · [PDF](https://arxiv.org/pdf/2511.21413.pdf)  
**作者**：Tim Trappen, Robert Keßler, Roland Pabel, Viktor Achter, Stefan Wesner  

**一句话要点**：提出集成vLLM、Slurm和Kubernetes的解决方案，以在HPC上高效服务动态AI推理。

**关键词**：AI推理, 高性能计算, Kubernetes集成, vLLM, Slurm, 动态扩展

## 3 点简述
- 核心问题：HPC传统模式不适应同步、用户面动态AI推理的高需求。
- 方法要点：在超级计算机RAMSES上整合vLLM、Slurm和Kubernetes。
- 实验或效果：基准测试显示，100至1000并发请求下延迟仅增约500毫秒。

## 摘要（原文）

> Due to rising demands for Artificial Inteligence (AI) inference, especially in higher education, novel solutions utilising existing infrastructure are emerging. The utilisation of High-Performance Computing (HPC) has become a prevalent approach for the implementation of such solutions. However, the classical operating model of HPC does not adapt well to the requirements of synchronous, user-facing dynamic AI application workloads. In this paper, we propose our solution that serves LLMs by integrating vLLM, Slurm and Kubernetes on the supercomputer \textit{RAMSES}. The initial benchmark indicates that the proposed architecture scales efficiently for 100, 500 and 1000 concurrent requests, incurring only an overhead of approximately 500 ms in terms of end-to-end latency.

