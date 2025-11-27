---
layout: default
title: LLaVA-UHD v3: Progressive Visual Compression for Efficient Native-Resolution Encoding in MLLMs
---

# LLaVA-UHD v3: Progressive Visual Compression for Efficient Native-Resolution Encoding in MLLMs
**arXiv**：[2511.21150v1](https://arxiv.org/abs/2511.21150) · [PDF](https://arxiv.org/pdf/2511.21150.pdf)  
**作者**：Shichu Sun, Yichen Zhang, Haolin Song, Zonghao Guo, Chi Chen, Yidan Zhang, Yuan Yao, Zhiyuan Liu, Maosong Sun  

**一句话要点**：提出渐进视觉压缩方法以解决多模态大模型中全局原生分辨率编码的高计算开销问题

**关键词**：渐进视觉压缩, 多模态大语言模型, 视觉Transformer, 令牌压缩, 高效编码, 原生分辨率

## 3 点简述
- 核心问题：全局原生分辨率视觉编码增强多模态大模型能力，但计算开销大
- 方法要点：渐进视觉压缩包括精炼补丁嵌入和窗口化令牌压缩模块
- 实验或效果：ViT-UHD在性能竞争下，TTFT降低2.4倍

## 摘要（原文）

> Visual encoding followed by token condensing has become the standard architectural paradigm in multi-modal large language models (MLLMs). Many recent MLLMs increasingly favor global native- resolution visual encoding over slice-based methods. To investigate this trend, we systematically compare their behavior on vision-language understanding and attention patterns, revealing that global encoding enhances overall capability but at the expense of greater computational overhead. To address this issue, we present LLaVA-UHD v3, an MLLM centered upon our proposed Progressive Visual Compression (PVC) method, which can be seamlessly integrated into standard Vision Transformer (ViT) to enable efficient native-resolution encoding. The PVC approach consists of two key modules: (i) refined patch embedding, which supports flexible patch-size scaling for fine-grained visual model- ing, (ii) windowed token compression, hierarchically deployed across ViT layers to progressively aggregate local token representations. Jointly modulated by these two modules, a widely pretrained ViT can be reconfigured into an efficient architecture while largely preserving generality. Evaluated across extensive benchmarks, the transformed ViT, termed ViT-UHD, demonstrates competitive performance with MoonViT while reducing TTFT (time-to-first-token) by 2.4x, when developed within an identical MLLM architecture. Building upon ViT-UHD, LLaVA-UHD v3 also achieves competitive performance to Qwen2-VL, while further reducing TTFT by 1.9x. We will release all code and checkpoints to support future research on efficient MLLMs.

