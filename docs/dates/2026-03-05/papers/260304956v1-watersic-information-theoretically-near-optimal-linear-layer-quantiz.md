---
layout: default
title: WaterSIC: information-theoretically (near) optimal linear layer quantization
---

# WaterSIC: information-theoretically (near) optimal linear layer quantization
**arXiv**：[2603.04956v1](https://arxiv.org/abs/2603.04956) · [PDF](https://arxiv.org/pdf/2603.04956.pdf)  
**作者**：Egor Lifar, Semyon Savkin, Or Ordentlich, Yury Polyanskiy  

**一句话要点**：提出WaterSIC算法，在线性层量化中实现信息理论近最优压缩，提升大模型低精度性能。

**关键词**：线性层量化, 信息理论优化, 水填充算法, 大模型压缩, 低精度计算

## 3 点简述
- 研究密集线性层量化问题，分析压缩长度与输出误差的信息理论权衡。
- 提出WaterSIC算法，基于水填充原理分配不同量化率，接近理论极限。
- 在Llama和Qwen大模型上应用，1-4位量化均达到最优性能。

## 摘要（原文）

> This paper considers the problem of converting a given dense linear layer to low precision. The tradeoff between compressed length and output discrepancy is analyzed information theoretically (IT). It is shown that a popular GPTQ algorithm may have an arbitrarily large gap to the IT limit. To alleviate this problem, a novel algorithm, termed ''WaterSIC'', is proposed and is shown to be within a rate gap of 0.255 bits to the IT limit, uniformly over all possible covariance matrices of input activations. The key innovation of WaterSIC's is to allocate different quantization rates to different columns (in-features) of the weight matrix, mimicking the classical IT solution known as ''waterfilling''. Applying WaterSIC to the Llama and Qwen family of LLMs establishes new state-of-the-art performance for all quantization rates from 1 to 4 bits.

