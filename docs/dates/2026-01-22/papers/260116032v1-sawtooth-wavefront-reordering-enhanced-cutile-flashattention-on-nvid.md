---
layout: default
title: Sawtooth Wavefront Reordering: Enhanced CuTile FlashAttention on NVIDIA GB10
---

# Sawtooth Wavefront Reordering: Enhanced CuTile FlashAttention on NVIDIA GB10
**arXiv**：[2601.16032v1](https://arxiv.org/abs/2601.16032) · [PDF](https://arxiv.org/pdf/2601.16032.pdf)  
**作者**：Yifan Zhu, Yekai Pan, Chen Ding  

**一句话要点**：提出锯齿波前重排序技术以提升NVIDIA GB10上CuTile FlashAttention的缓存性能

**关键词**：FlashAttention, 缓存优化, NVIDIA GB10, CuTile, 锯齿波前重排序, 大语言模型

## 3 点简述
- 分析CuTile FlashAttention在NVIDIA GB10上的内存行为，识别L2缓存未命中主因
- 引入锯齿波前重排序编程技术，优化缓存访问模式以减少L2未命中
- 在CUDA和CuTile中验证，L2未命中减少50%以上，吞吐量提升最高达60%

## 摘要（原文）

> High-performance attention kernels are essential for Large Language Models. This paper presents analysis of CuTile-based Flash Attention memory behavior and a technique to improve its cache performance. In particular, our analysis on the NVIDIA GB10 (Grace Blackwell) identifies the main cause of L2 cache miss. Leveraging this insight, we introduce a new programming technique called Sawtooth Wavefront Reordering that reduces L2 misses. We validate it in both CUDA and CuTile, observing 50\% or greater reduction in L2 misses and up to 60\% increase in throughput on GB10.

