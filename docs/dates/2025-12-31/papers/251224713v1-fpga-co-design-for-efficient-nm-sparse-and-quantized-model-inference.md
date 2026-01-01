---
layout: default
title: FPGA Co-Design for Efficient N:M Sparse and Quantized Model Inference
---

# FPGA Co-Design for Efficient N:M Sparse and Quantized Model Inference
**arXiv**：[2512.24713v1](https://arxiv.org/abs/2512.24713) · [PDF](https://arxiv.org/pdf/2512.24713.pdf)  
**作者**：Fen-Yu Hsieh, Yun-Chang Teng, Ding-Yong Hong, Jan-Jan Wu  

**一句话要点**：提出FPGA软硬件协同设计框架，结合N:M稀疏与量化以优化大语言模型推理效率。

**关键词**：大语言模型推理, 结构化稀疏, 低比特量化, FPGA加速器, 软硬件协同设计, 矩阵乘法优化

## 3 点简述
- 大语言模型部署面临高计算与内存需求挑战，需在资源受限环境中优化。
- 采用N:M结构化剪枝和4位整数量化减少存储，结合FPGA加速器提升推理性能。
- 实验显示在4096×4096矩阵上实现4倍存储减少和1.29倍端到端延迟降低。

## 摘要（原文）

> Large language models (LLMs) have demonstrated remarkable performance across a wide range of language processing tasks. However, this success comes at the cost of substantial computation and memory requirements, which significantly impedes their deployment in resource-constrained environments. To address this challenge, this work introduces an automation framework that leverages weight pruning and low-bit quantization, and presents a hardware-software co-design method that generates accelerators on the Field-Programmable Gate Array (FPGA) platform. In particular, we implement a unified pipeline that applies N:M structured pruning and 4-bit integer quantization to reduce the memory footprint, followed by optimized dequantization and matrix multiplication to enhance LLM inference on several hardware platforms, including CPUs, NVIDIA GPUs with Dense and 2:4 Sparse Tensor Cores, and a custom systolic-array-based FPGA accelerator. Utilizing 2:4 sparsity combined with quantization on $4096 \times 4096$ matrices, our approach achieves a reduction of up to $4\times$ in weight storage and a $1.71\times$ speedup in matrix multiplication, yielding a $1.29\times$ end-to-end latency reduction compared to dense GPU baselines. Scaling analysis on the LLaMA-7B model further shows that structured sparsity enhances the throughput per token by $1.36\times$. These results demonstrate the synergy of fine-grained N:M sparsity and quantization for enabling efficient and deployable LLM inference, while the proposed FPGA accelerator offers a flexible architectural path for supporting a broader class of sparsity patterns beyond the fixed 2:4 hardware constraints.

