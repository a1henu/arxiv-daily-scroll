---
layout: default
title: Attention via Synaptic Plasticity is All You Need: A Biologically Inspired Spiking Neuromorphic Transformer
---

# Attention via Synaptic Plasticity is All You Need: A Biologically Inspired Spiking Neuromorphic Transformer
**arXiv**：[2511.14691v1](https://arxiv.org/abs/2511.14691) · [PDF](https://arxiv.org/pdf/2511.14691.pdf)  
**作者**：Kallol Mondal, Ankush Kumar  

**一句话要点**：提出基于STDP的脉冲Transformer，实现节能高效的神经形态注意力机制。

**关键词**：脉冲神经网络, 神经形态计算, 注意力机制, STDP学习, 节能AI, 硬件友好模型

## 3 点简述
- Transformer注意力机制依赖点积相似性，导致高能耗和硬件瓶颈。
- 使用脉冲时序依赖可塑性实现自注意力，将查询-键相关性嵌入突触权重。
- 在CIFAR数据集上实现高精度和88.47%能耗降低，增强可解释性。

## 摘要（原文）

> Attention is the brain's ability to selectively focus on a few specific aspects while ignoring irrelevant ones. This biological principle inspired the attention mechanism in modern Transformers. Transformers now underpin large language models (LLMs) such as GPT, but at the cost of massive training and inference energy, leading to a large carbon footprint. While brain attention emerges from neural circuits, Transformer attention relies on dot-product similarity to weight elements in the input sequence. Neuromorphic computing, especially spiking neural networks (SNNs), offers a brain-inspired path to energy-efficient intelligence. Despite recent work on attention-based spiking Transformers, the core attention layer remains non-neuromorphic. Current spiking attention (i) relies on dot-product or element-wise similarity suited to floating-point operations, not event-driven spikes; (ii) keeps attention matrices that suffer from the von Neumann bottleneck, limiting in-memory computing; and (iii) still diverges from brain-like computation. To address these issues, we propose the Spiking STDP Transformer (S$^{2}$TDPT), a neuromorphic Transformer that implements self-attention through spike-timing-dependent plasticity (STDP), embedding query--key correlations in synaptic weights. STDP, a core mechanism of memory and learning in the brain and widely studied in neuromorphic devices, naturally enables in-memory computing and supports non-von Neumann hardware. On CIFAR-10 and CIFAR-100, our model achieves 94.35\% and 78.08\% accuracy with only four timesteps and 0.49 mJ on CIFAR-100, an 88.47\% energy reduction compared to a standard ANN Transformer. Grad-CAM shows that the model attends to semantically relevant regions, enhancing interpretability. Overall, S$^{2}$TDPT illustrates how biologically inspired attention can yield energy-efficient, hardware-friendly, and explainable neuromorphic models.

