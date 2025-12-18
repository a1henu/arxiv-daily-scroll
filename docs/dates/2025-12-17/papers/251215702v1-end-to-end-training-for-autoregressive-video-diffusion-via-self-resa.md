---
layout: default
title: End-to-End Training for Autoregressive Video Diffusion via Self-Resampling
---

# End-to-End Training for Autoregressive Video Diffusion via Self-Resampling
**arXiv**：[2512.15702v1](https://arxiv.org/abs/2512.15702) · [PDF](https://arxiv.org/pdf/2512.15702.pdf)  
**作者**：Yuwei Guo, Ceyuan Yang, Hao He, Yang Zhao, Meng Wei, Zhenheng Yang, Weilin Huang, Dahua Lin  

**一句话要点**：提出自重采样强制框架，以端到端训练解决自回归视频扩散模型的曝光偏差问题。

**关键词**：自回归视频扩散, 曝光偏差, 端到端训练, 自重采样, 长视频生成, 时间一致性

## 3 点简述
- 核心问题：自回归视频扩散模型存在训练-测试不匹配导致的曝光偏差，影响长视频生成质量。
- 方法要点：引入自重采样方案模拟推理错误，结合稀疏因果掩码实现并行训练，并采用历史路由机制提升长序列生成效率。
- 实验或效果：在性能上与基于蒸馏的基线相当，且在长视频上展现出更优的时间一致性。

## 摘要（原文）

> Autoregressive video diffusion models hold promise for world simulation but are vulnerable to exposure bias arising from the train-test mismatch. While recent works address this via post-training, they typically rely on a bidirectional teacher model or online discriminator. To achieve an end-to-end solution, we introduce Resampling Forcing, a teacher-free framework that enables training autoregressive video models from scratch and at scale. Central to our approach is a self-resampling scheme that simulates inference-time model errors on history frames during training. Conditioned on these degraded histories, a sparse causal mask enforces temporal causality while enabling parallel training with frame-level diffusion loss. To facilitate efficient long-horizon generation, we further introduce history routing, a parameter-free mechanism that dynamically retrieves the top-k most relevant history frames for each query. Experiments demonstrate that our approach achieves performance comparable to distillation-based baselines while exhibiting superior temporal consistency on longer videos owing to native-length training.

