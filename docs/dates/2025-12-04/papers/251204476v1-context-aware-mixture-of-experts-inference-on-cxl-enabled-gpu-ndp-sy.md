---
layout: default
title: Context-Aware Mixture-of-Experts Inference on CXL-Enabled GPU-NDP Systems
---

# Context-Aware Mixture-of-Experts Inference on CXL-Enabled GPU-NDP Systems
**arXiv**：[2512.04476v1](https://arxiv.org/abs/2512.04476) · [PDF](https://arxiv.org/pdf/2512.04476.pdf)  
**作者**：Zehao Fan, Zhenyu Liu, Yunzhen Liu, Yayue Hou, Hadjer Benmeziane, Kaoutar El Maghraoui, Liu Liu  

**一句话要点**：提出上下文感知的MoE推理系统，利用CXL-NDP解决GPU内存受限问题

**关键词**：混合专家模型, CXL近数据处理, 上下文感知推理, 动态专家放置, 混合精度量化

## 3 点简述
- MoE模型推理在专家权重超出GPU内存时成为内存瓶颈，需频繁卸载权重。
- 采用CXL-NDP作为卸载层，基于预填充阶段激活统计动态放置专家，减少参数移动。
- 系统在GPU-NDP上实现最高8.7倍解码吞吐提升，平均精度仅下降0.13%。

## 摘要（原文）

> Mixture-of-Experts (MoE) models scale large language models through conditional computation, but inference becomes memory-bound once expert weights exceed the capacity of GPU memory. In this case, weights must be offloaded to external memory, and fetching them incurs costly and repeated transfers. We address this by adopting CXL-attached near-data processing (CXL-NDP) as the offloading tier to execute cold experts in place, converting expensive parameter movement into cheaper activation movement. Unlike prior GPU-NDP systems that are largely context-agnostic and reactive, we develop a context-aware MoE system that uses prefill-stage activation statistics to guide decoding-stage expert placement, dynamically pins hot experts in GPU-side HBM, and maps the remainder to CXL-NDP. To meet NDP's limited compute throughput, we introduce context-aware mixed-precision quantization that allocates per-expert bitwidths (1-4 bit) based on prefill stage. The resulting MoE inference system overlaps GPU and NDP execution while minimizing cross-device movement. The evaluation on the GPU-NDP system shows that our approach achieves up to an 8.7-fold decoding throughput improvement over the state-of-the-art method, while incurring only a 0.13% average accuracy drop.

