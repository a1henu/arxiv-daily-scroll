---
layout: default
title: BlockVid: Block Diffusion for High-Quality and Consistent Minute-Long Video Generation
---

# BlockVid: Block Diffusion for High-Quality and Consistent Minute-Long Video Generation
**arXiv**：[2511.22973v1](https://arxiv.org/abs/2511.22973) · [PDF](https://arxiv.org/pdf/2511.22973.pdf)  
**作者**：Zeyu Zhang, Shuning Chang, Yuanyu He, Yizeng Han, Jiasheng Tang, Fan Wang, Bohan Zhuang  

**一句话要点**：提出BlockVid框架以解决分钟级长视频生成中的错误累积和一致性挑战

**关键词**：长视频生成, 块扩散, KV缓存优化, 时序一致性, 视频基准评测

## 3 点简述
- 核心问题：半自回归范式存在KV缓存导致的长期错误累积和缺乏细粒度长视频基准
- 方法要点：引入语义感知稀疏KV缓存、块强制训练策略及分块噪声调度以增强时序一致性
- 实验或效果：在VBench和LV-Bench上优于现有方法，LV-Bench中VDE Subject和Clarity分别提升22.2%和19.4%

## 摘要（原文）

> Generating minute-long videos is a critical step toward developing world models, providing a foundation for realistic extended scenes and advanced AI simulators. The emerging semi-autoregressive (block diffusion) paradigm integrates the strengths of diffusion and autoregressive models, enabling arbitrary-length video generation and improving inference efficiency through KV caching and parallel sampling. However, it yet faces two enduring challenges: (i) KV-cache-induced long-horizon error accumulation, and (ii) the lack of fine-grained long-video benchmarks and coherence-aware metrics. To overcome these limitations, we propose BlockVid, a novel block diffusion framework equipped with semantic-aware sparse KV cache, an effective training strategy called Block Forcing, and dedicated chunk-wise noise scheduling and shuffling to reduce error propagation and enhance temporal consistency. We further introduce LV-Bench, a fine-grained benchmark for minute-long videos, complete with new metrics evaluating long-range coherence. Extensive experiments on VBench and LV-Bench demonstrate that BlockVid consistently outperforms existing methods in generating high-quality, coherent minute-long videos. In particular, it achieves a 22.2% improvement on VDE Subject and a 19.4% improvement on VDE Clarity in LV-Bench over the state of the art approaches. Project website: https://ziplab.co/BlockVid. Inferix (Code): https://github.com/alibaba-damo-academy/Inferix.

