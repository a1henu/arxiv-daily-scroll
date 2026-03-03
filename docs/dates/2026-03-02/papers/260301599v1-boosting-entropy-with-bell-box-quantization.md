---
layout: default
title: Boosting Entropy with Bell Box Quantization
---

# Boosting Entropy with Bell Box Quantization
**arXiv**：[2603.01599v1](https://arxiv.org/abs/2603.01599) · [PDF](https://arxiv.org/pdf/2603.01599.pdf)  
**作者**：Ningfeng Yang, Tor M. Aamodt  

**一句话要点**：提出BBQ量化方法，在保持计算效率的同时实现信息理论最优量化，用于边缘设备神经网络压缩。

**关键词**：量化感知预训练, 信息理论最优量化, 计算高效量化, 边缘设备优化, 神经网络压缩

## 3 点简述
- 现有量化感知预训练方法在计算效率与信息理论最优性之间存在权衡，BBQ通过跨域映射解决此问题。
- BBQ在输入域进行信息理论最优量化，输出映射到计算高效域，无需牺牲计算效率。
- 实验显示，BBQ在1至4位量化模型中，困惑度降低显著，最高达18点，优于现有方法。

## 摘要（原文）

> Quantization-Aware Pre-Training (QAPT) is an effective technique to reduce the compute and memory overhead of Deep Neural Networks while improving their energy efficiency on edge devices. Existing QAPT methods produce models stored in compute-efficient data types (e.g. integers) that are not information theoretically optimal (ITO). On the other hand, existing ITO data types (e.g. Quantile/NormalFloat Quantization) are not compute-efficient. We propose BBQ, the first ITO quantization method that is also compute-efficient. BBQ builds on our key insight that since learning is domain-agnostic, the output of a quantizer does not need to reside in the same domain as its input. BBQ performs ITO quantization in its input domain, and returns its output in a compute-efficient domain where ITO data types are mapped to compute-efficient data types. Without sacrificing compute efficiency, BBQ outperforms prior SOTA QAPT methods by a perplexity reduction of up to 2 points for 4-bit models, up to 4 points for 3-bit models, up to 5 points for 2-bit models, and up to 18 points for 1-bit models. Code is available at https://github.com/1733116199/bbq.

