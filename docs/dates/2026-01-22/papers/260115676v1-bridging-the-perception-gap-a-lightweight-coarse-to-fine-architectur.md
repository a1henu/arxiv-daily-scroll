---
layout: default
title: Bridging the Perception Gap: A Lightweight Coarse-to-Fine Architecture for Edge Audio Systems
---

# Bridging the Perception Gap: A Lightweight Coarse-to-Fine Architecture for Edge Audio Systems
**arXiv**：[2601.15676v1](https://arxiv.org/abs/2601.15676) · [PDF](https://arxiv.org/pdf/2601.15676.pdf)  
**作者**：Hengfan Zhang, Yueqian Lin, Hai Helen Li, Yiran Chen  

**一句话要点**：提出CoFi-Agent混合架构以解决边缘音频系统中感知深度与计算效率的权衡问题。

**关键词**：边缘计算, 音频语言模型, 条件性精炼, 工具增强, 粗到细架构

## 3 点简述
- 核心问题：边缘部署音频语言模型时，轻量本地模型感知被动，而云卸载导致延迟、带宽和隐私风险。
- 方法要点：采用粗到细架构，本地快速感知后，云端控制器仅在不确定时触发条件性工具增强精炼。
- 实验或效果：在MMAR基准上，准确率从27.20%提升至53.60%，优于持续调查流水线。

## 摘要（原文）

> Deploying Audio-Language Models (Audio-LLMs) on edge infrastructure exposes a persistent tension between perception depth and computational efficiency. Lightweight local models tend to produce passive perception - generic summaries that miss the subtle evidence required for multi-step audio reasoning - while indiscriminate cloud offloading incurs unacceptable latency, bandwidth cost, and privacy risk. We propose CoFi-Agent (Tool-Augmented Coarse-to-Fine Agent), a hybrid architecture targeting edge servers and gateways. It performs fast local perception and triggers conditional forensic refinement only when uncertainty is detected. CoFi-Agent runs an initial single-pass on a local 7B Audio-LLM, then a cloud controller gates difficult cases and issues lightweight plans for on-device tools such as temporal re-listening and local ASR. On the MMAR benchmark, CoFi-Agent improves accuracy from 27.20% to 53.60%, while achieving a better accuracy-efficiency trade-off than an always-on investigation pipeline. Overall, CoFi-Agent bridges the perception gap via tool-enabled, conditional edge-cloud collaboration under practical system constraints.

