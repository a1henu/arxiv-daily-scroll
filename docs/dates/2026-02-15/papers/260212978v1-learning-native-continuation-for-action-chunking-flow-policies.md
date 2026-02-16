---
layout: default
title: Learning Native Continuation for Action Chunking Flow Policies
---

# Learning Native Continuation for Action Chunking Flow Policies
**arXiv**：[2602.12978v1](https://arxiv.org/abs/2602.12978) · [PDF](https://arxiv.org/pdf/2602.12978.pdf)  
**作者**：Yufeng Liu, Hang Yu, Juntu Zhao, Bocheng Li, Di Zhang, Mingzhu Li, Wenxuan Wu, Yingdong Hu, Junyuan Xie, Junliang Guo, Dequan Wang, Yang Gao  

**一句话要点**：提出Legato训练方法以解决动作分块VLA策略中的执行不连续问题

**关键词**：动作分块, 视觉语言动作模型, 流策略, 去噪训练, 实时执行, 轨迹平滑

## 3 点简述
- 核心问题：动作分块执行在块边界处产生不连续性，外部实时分块方法导致虚假多模态切换和轨迹不平滑。
- 方法要点：通过初始化去噪为已知动作与噪声的混合，并重塑流动态，确保训练与推理一致性，支持可变延迟。
- 实验效果：在五个操作任务中，Legato比RTC提升约10%的轨迹平滑度和任务完成时间，减少犹豫。

## 摘要（原文）

> Action chunking enables Vision Language Action (VLA) models to run in real time, but naive chunked execution often exhibits discontinuities at chunk boundaries. Real-Time Chunking (RTC) alleviates this issue but is external to the policy, leading to spurious multimodal switching and trajectories that are not intrinsically smooth. We propose Legato, a training-time continuation method for action-chunked flow-based VLA policies. Specifically, Legato initializes denoising from a schedule-shaped mixture of known actions and noise, exposing the model to partial action information. Moreover, Legato reshapes the learned flow dynamics to ensure that the denoising process remains consistent between training and inference under per-step guidance. Legato further uses randomized schedule condition during training to support varying inference delays and achieve controllable smoothness. Empirically, Legato produces smoother trajectories and reduces spurious multimodal switching during execution, leading to less hesitation and shorter task completion time. Extensive real-world experiments show that Legato consistently outperforms RTC across five manipulation tasks, achieving approximately 10% improvements in both trajectory smoothness and task completion time.

