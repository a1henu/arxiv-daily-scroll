---
layout: default
title: EgoLCD: Egocentric Video Generation with Long Context Diffusion
---

# EgoLCD: Egocentric Video Generation with Long Context Diffusion
**arXiv**：[2512.04515v1](https://arxiv.org/abs/2512.04515) · [PDF](https://arxiv.org/pdf/2512.04515.pdf)  
**作者**：Liuzhou Zhang, Jiarui Ye, Yuanlei Wang, Ming Zhong, Mingju Cao, Wanke Xia, Bowen Zeng, Zeyu Zhang, Hao Tang  

**一句话要点**：提出EgoLCD框架，通过长短期记忆管理解决第一人称长视频生成中的内容漂移问题。

**关键词**：第一人称视频生成, 长上下文扩散, 记忆管理, 内容一致性, 自回归模型改进

## 3 点简述
- 核心问题：现有自回归模型在生成长视频时易出现内容漂移，导致物体身份和场景语义随时间退化。
- 方法要点：结合长时稀疏KV缓存和基于注意力的短时记忆，引入LoRA扩展和记忆调节损失以增强一致性。
- 实验或效果：在EgoVid-5M基准测试中实现感知质量和时序一致性的最先进性能，有效缓解生成遗忘。

## 摘要（原文）

> Generating long, coherent egocentric videos is difficult, as hand-object interactions and procedural tasks require reliable long-term memory. Existing autoregressive models suffer from content drift, where object identity and scene semantics degrade over time. To address this challenge, we introduce EgoLCD, an end-to-end framework for egocentric long-context video generation that treats long video synthesis as a problem of efficient and stable memory management. EgoLCD combines a Long-Term Sparse KV Cache for stable global context with an attention-based short-term memory, extended by LoRA for local adaptation. A Memory Regulation Loss enforces consistent memory usage, and Structured Narrative Prompting provides explicit temporal guidance. Extensive experiments on the EgoVid-5M benchmark demonstrate that EgoLCD achieves state-of-the-art performance in both perceptual quality and temporal consistency, effectively mitigating generative forgetting and representing a significant step toward building scalable world models for embodied AI. Code: https://github.com/AIGeeksGroup/EgoLCD. Website: https://aigeeksgroup.github.io/EgoLCD.

