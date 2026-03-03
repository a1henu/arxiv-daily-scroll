---
layout: default
title: How Small Can 6G Reason? Scaling Tiny Language Models for AI-Native Networks
---

# How Small Can 6G Reason? Scaling Tiny Language Models for AI-Native Networks
**arXiv**：[2603.02156v1](https://arxiv.org/abs/2603.02156) · [PDF](https://arxiv.org/pdf/2603.02156.pdf)  
**作者**：Mohamed Amine Ferrag, Abderrahmane Lakas, Merouane Debbah  

**一句话要点**：评估小规模语言模型在AI原生6G网络中的缩放行为与部署效率，为边缘推理提供指导。

**关键词**：AI原生网络, 小规模语言模型, 缩放行为, 部署效率, 边缘推理, 6G-Bench基准

## 3 点简述
- 核心问题：前沿大语言模型计算开销大，难以部署在延迟敏感的6G边缘基础设施中。
- 方法要点：使用6G-Bench基准，系统评估从135M到7B参数模型的缩放行为和部署效率。
- 实验或效果：发现1.5B到3B参数模型在确定性稳定性和计算效率间达到最佳平衡。

## 摘要（原文）

> Emerging 6G visions, reflected in ongoing standardization efforts within 3GPP, IETF, ETSI, ITU-T, and the O-RAN Alliance, increasingly characterize networks as AI-native systems in which high-level semantic reasoning layers operate above standardized control and data-plane functions. Although frontier-scale large language models (LLMs) such as Qwen2.5-7B and Olmo-3-7B demonstrate strong reasoning capability, their computational footprint limits deployment in latency-sensitive, edge-native infrastructures. This paper presents a systematic empirical study of the scaling behavior and deployment efficiency of compact language models for network-level semantic reasoning in AI-native 6G systems. Using 6G-Bench, a standardization-aligned benchmark comprising 30 decision-making tasks across five capability domains, we evaluate models ranging from 135M (SmolLM2-135M) to 7B parameters (Qwen2.5-7B), including mid-scale architectures such as Llama-3.2-1B, Granite-1B, and Qwen2.5-3B. Deterministic accuracy (pass@1) increases from 0.224 at 135M to 0.707 at 7B, but scaling gains are highly non-uniform. A pronounced stability transition occurs in the 1 to 1.5B range, where accuracy rises from 0.373 (Llama-3.2-1B) to 0.531 (Qwen2.5-1.5B) and the instability gap Delta_5 contracts from 0.356 to 0.138. Beyond 3B parameters, improvements diminish (+0.064 from 3B to 7B). Through single-query inference profiling and an Edge Score metric that normalizes accuracy by latency and memory footprint, we show that semantic reliability per unit edge resource does not scale monotonically with parameter count. Instead, mid-scale models (approximately 1.5 to 3B) achieve the most favorable balance between deterministic stability and computational efficiency, providing deployment-relevant guidance for AI-native 6G architectures. All scripts and results are publicly available at https://github.com/maferrag/6G-Bench

