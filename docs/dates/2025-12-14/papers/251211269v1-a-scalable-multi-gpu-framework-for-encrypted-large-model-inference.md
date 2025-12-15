---
layout: default
title: A Scalable Multi-GPU Framework for Encrypted Large-Model Inference
---

# A Scalable Multi-GPU Framework for Encrypted Large-Model Inference
**arXiv**：[2512.11269v1](https://arxiv.org/abs/2512.11269) · [PDF](https://arxiv.org/pdf/2512.11269.pdf)  
**作者**：Siddharth Jayashankar, Joshua Kim, Michael B. Sullivan, Wenting Zheng, Dimitrios Skarlatos  

**一句话要点**：提出Cerium多GPU框架以解决全同态加密大模型推理的性能与内存挑战

**关键词**：全同态加密, 大模型推理, 多GPU框架, 编译器优化, 内存管理, 并行计算

## 3 点简述
- 核心问题：全同态加密推理性能慢，大模型内存需求远超单GPU容量，GPU平台难以匹敌ASIC性能
- 方法要点：集成领域特定语言、优化编译器和运行时系统，自动生成GPU内核，管理TB级内存，多GPU并行计算
- 实验或效果：性能超越手工优化库2.25倍，匹配先进FHE ASIC，首次实现BERT-Base和Llama3-8B加密推理

## 摘要（原文）

> Encrypted AI using fully homomorphic encryption (FHE) provides strong privacy guarantees; but its slow performance has limited practical deployment. Recent works proposed ASICs to accelerate FHE, but require expensive advanced manufacturing processes that constrain their accessibility. GPUs are a far more accessible platform, but achieving ASIC-level performance using GPUs has remained elusive. Furthermore, state-of-the-art approaches primarily focus on small models that fit comfortably within a single device. Supporting large models such as LLMs in FHE introduces a dramatic increase in computational complexity that requires optimized GPU kernels, along with managing terabyte-scale memory footprints that far exceed the capacity of a single GPU. This paper presents Cerium, a multi-GPU framework for FHE inference on large models. Cerium integrates a domain-specific language, an optimizing compiler, and a runtime system to automatically generate high-performance GPU kernels, manage terabyte-scale memory footprints, and parallelize computation across multiple GPUs. It introduces new IR constructs, compiler passes, sparse polynomial representations, memory-efficient data layouts, and communication-aware parallelization techniques that together enable encrypted inference for models ranging from small CNNs to Llama3-8B. We build Cerium on NVIDIA GPUs and demonstrate significant performance gains. For small models, Cerium outperforms expert-written hand-optimized GPU libraries by up to 2.25 times. Cerium achieves performance competitive with state-of-the-art FHE ASICs, outright matching prior FHE ASIC CraterLake. It is the first GPU system to execute bootstrapping in under 10 milliseconds, achieving 7.5 milliseconds, and is the first to demonstrate encrypted inference for BERT-Base and Llama3-8B in 8 seconds and 134 seconds, respectively.

