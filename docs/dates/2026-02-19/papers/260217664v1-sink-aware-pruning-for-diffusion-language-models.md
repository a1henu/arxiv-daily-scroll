---
layout: default
title: Sink-Aware Pruning for Diffusion Language Models
---

# Sink-Aware Pruning for Diffusion Language Models
**arXiv**：[2602.17664v1](https://arxiv.org/abs/2602.17664) · [PDF](https://arxiv.org/pdf/2602.17664.pdf)  
**作者**：Aidar Myrzakhan, Tianyi Li, Bowei Guo, Shengkun Tang, Zhiqiang Shen  

**一句话要点**：提出Sink-Aware Pruning以解决扩散语言模型推理效率问题

**关键词**：扩散语言模型, 模型剪枝, 注意力机制, 推理优化, 高效生成

## 3 点简述
- 核心问题：扩散语言模型推理成本高，现有剪枝方法继承自自回归模型，错误假设注意力sink稳定
- 方法要点：基于sink位置在生成轨迹中高方差，自动识别并剪除不稳定sink，无需重训练
- 实验或效果：在匹配计算下，优于强基线，实现更好的质量-效率权衡

## 摘要（原文）

> Diffusion Language Models (DLMs) incur high inference cost due to iterative denoising, motivating efficient pruning. Existing pruning heuristics largely inherited from autoregressive (AR) LLMs, typically preserve attention sink tokens because AR sinks serve as stable global anchors. We show that this assumption does not hold for DLMs: the attention-sink position exhibits substantially higher variance over the full generation trajectory (measured by how the dominant sink locations shift across timesteps), indicating that sinks are often transient and less structurally essential than in AR models. Based on this observation, we propose ${\bf \texttt{Sink-Aware Pruning}}$, which automatically identifies and prunes unstable sinks in DLMs (prior studies usually keep sinks for AR LLMs). Without retraining, our method achieves a better quality-efficiency trade-off and outperforms strong prior pruning baselines under matched compute. Our code is available at https://github.com/VILA-Lab/Sink-Aware-Pruning.

