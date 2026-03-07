---
layout: default
title: WaterSIC: information-theoretically (near) optimal linear layer quantization
---

# WaterSIC: information-theoretically (near) optimal linear layer quantization
**arXiv**：[2603.04956v1](https://arxiv.org/abs/2603.04956) · [PDF](https://arxiv.org/pdf/2603.04956.pdf)  
**作者**：Egor Lifar, Semyon Savkin, Or Ordentlich, Yury Polyanskiy  

**一句话要点**：提出WaterSIC算法以优化线性层量化，实现信息理论近最优压缩

**关键词**：线性层量化, 信息理论极限, 水填充算法, 低精度压缩, 大语言模型优化

## 3 点简述
- 分析线性层量化中压缩长度与输出误差的信息理论极限
- 提出WaterSIC算法，基于水填充原理分配不同列量化率，接近理论极限
- 在Llama和Qwen模型上应用，1-4位量化均达到新最优性能

## 摘要（原文）

> This paper considers the problem of converting a given dense linear layer to low precision. The tradeoff between compressed length and output discrepancy is analyzed information theoretically (IT). It is shown that a popular GPTQ algorithm may have an arbitrarily large gap to the IT limit. To alleviate this problem, a novel algorithm, termed ''WaterSIC'', is proposed and is shown to be within a rate gap of 0.255 bits to the IT limit, uniformly over all possible covariance matrices of input activations. The key innovation of WaterSIC's is to allocate different quantization rates to different columns (in-features) of the weight matrix, mimicking the classical IT solution known as ''waterfilling''. Applying WaterSIC to the Llama and Qwen family of LLMs establishes new state-of-the-art performance for all quantization rates from 1 to 4 bits.

