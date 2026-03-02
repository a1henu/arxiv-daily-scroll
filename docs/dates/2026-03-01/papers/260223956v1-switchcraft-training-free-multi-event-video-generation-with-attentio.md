---
layout: default
title: SwitchCraft: Training-Free Multi-Event Video Generation with Attention Controls
---

# SwitchCraft: Training-Free Multi-Event Video Generation with Attention Controls
**arXiv**：[2602.23956v1](https://arxiv.org/abs/2602.23956) · [PDF](https://arxiv.org/pdf/2602.23956.pdf)  
**作者**：Qianxun Xu, Chenxi Song, Yujun Cai, Chi Zhang  

**一句话要点**：提出SwitchCraft框架，通过注意力控制实现无需训练的多事件视频生成

**关键词**：多事件视频生成, 注意力控制, 训练免费框架, 文本到视频扩散模型, 事件对齐

## 3 点简述
- 核心问题：现有文本到视频扩散模型处理多事件提示时，常产生混合或崩溃场景，破坏叙事连贯性。
- 方法要点：引入事件对齐查询引导（EAQS）和自动平衡强度求解器（ABSS），以对齐事件与帧并保持一致性。
- 实验或效果：实验表明SwitchCraft显著提升提示对齐、事件清晰度和场景一致性，优于现有基线。

## 摘要（原文）

> Recent advances in text-to-video diffusion models have enabled high-fidelity and temporally coherent videos synthesis. However, current models are predominantly optimized for single-event generation. When handling multi-event prompts, without explicit temporal grounding, such models often produce blended or collapsed scenes that break the intended narrative. To address this limitation, we present SwitchCraft, a training-free framework for multi-event video generation. Our key insight is that uniform prompt injection across time ignores the correspondence between events and frames. To this end, we introduce Event-Aligned Query Steering (EAQS), which steers frame-level attention to align with relevant event prompts. Furthermore, we propose Auto-Balance Strength Solver (ABSS), which adaptively balances steering strength to preserve temporal consistency and visual fidelity. Extensive experiments demonstrate that SwitchCraft substantially improves prompt alignment, event clarity, and scene consistency compared with existing baselines, offering a simple yet effective solution for multi-event video generation.

