---
layout: default
title: FiLoRA: Focus-and-Ignore LoRA for Controllable Feature Reliance
---

# FiLoRA: Focus-and-Ignore LoRA for Controllable Feature Reliance
**arXiv**：[2602.02060v1](https://arxiv.org/abs/2602.02060) · [PDF](https://arxiv.org/pdf/2602.02060.pdf)  
**作者**：Hyunsuk Chung, Caren Han, Yerin Choi, Seungyeon Ji, Jinwoo Kim, Eun-Jung Holden, Kyungreem Han  

**一句话要点**：提出FiLoRA框架，通过指令条件门控控制多模态基础模型内部特征依赖

**关键词**：多模态基础模型, 特征依赖控制, 参数高效微调, 指令条件门控, 虚假特征鲁棒性

## 3 点简述
- 核心问题：多模态基础模型内部特征依赖机制不明确，现有方法难以在不改变任务语义下调控依赖
- 方法要点：基于LoRA分解特征组对齐模块，利用自然语言指令作为计算级控制信号进行门控
- 实验或效果：在文本-图像和音频-视觉基准上，FiLoRA能因果性调整特征依赖，提升虚假特征干预下的鲁棒性

## 摘要（原文）

> Multimodal foundation models integrate heterogeneous signals across modalities, yet it remains poorly understood how their predictions depend on specific internal feature groups and whether such reliance can be deliberately controlled. Existing studies of shortcut and spurious behavior largely rely on post hoc analyses or feature removal, offering limited insight into whether reliance can be modulated without altering task semantics. We introduce FiLoRA (Focus-and-Ignore LoRA), an instruction-conditioned, parameter-efficient adaptation framework that enables explicit control over internal feature reliance while keeping the predictive objective fixed. FiLoRA decomposes adaptation into feature group-aligned LoRA modules and applies instruction-conditioned gating, allowing natural language instructions to act as computation-level control signals rather than task redefinitions. Across text--image and audio--visual benchmarks, we show that instruction-conditioned gating induces consistent and causal shifts in internal computation, selectively amplifying or suppressing core and spurious feature groups without modifying the label space or training objective. Further analyses demonstrate that FiLoRA yields improved robustness under spurious feature interventions, revealing a principled mechanism to regulate reliance beyond correlation-driven learning.

