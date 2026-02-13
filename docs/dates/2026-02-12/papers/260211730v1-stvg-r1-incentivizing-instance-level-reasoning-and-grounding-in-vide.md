---
layout: default
title: STVG-R1: Incentivizing Instance-Level Reasoning and Grounding in Videos via Reinforcement Learning
---

# STVG-R1: Incentivizing Instance-Level Reasoning and Grounding in Videos via Reinforcement Learning
**arXiv**：[2602.11730v1](https://arxiv.org/abs/2602.11730) · [PDF](https://arxiv.org/pdf/2602.11730.pdf)  
**作者**：Xiaowen Zhang, Zhi Gao, Licheng Jiao, Lingling Li, Qing Li  

**一句话要点**：提出STVG-R1强化学习框架，通过视觉提示和实例级ID解决视频时空定位中的幻觉问题。

**关键词**：视频时空定位, 视觉语言模型, 强化学习, 视觉提示, 实例级识别, 零样本泛化

## 3 点简述
- 核心问题：视觉语言模型在视频时空定位中因文本与坐标错位导致幻觉，现有方法增加模块成本高。
- 方法要点：将坐标预测转为实例级ID识别，嵌入视频作为视觉提示，并引入强化学习优化时空准确性和一致性。
- 实验或效果：在多个基准测试中超越基线，HCSTVG-v2上m_IoU提升20.9%，零样本泛化至多对象分割任务达SOTA。

## 摘要（原文）

> In vision-language models (VLMs), misalignment between textual descriptions and visual coordinates often induces hallucinations. This issue becomes particularly severe in dense prediction tasks such as spatial-temporal video grounding (STVG). Prior approaches typically focus on enhancing visual-textual alignment or attaching auxiliary decoders. However, these strategies inevitably introduce additional trainable modules, leading to significant annotation costs and computational overhead. In this work, we propose a novel visual prompting paradigm that avoids the difficult problem of aligning coordinates across modalities. Specifically, we reformulate per-frame coordinate prediction as a compact instance-level identification problem by assigning each object a unique, temporally consistent ID. These IDs are embedded into the video as visual prompts, providing explicit and interpretable inputs to the VLMs. Furthermore, we introduce STVG-R1, the first reinforcement learning framework for STVG, which employs a task-driven reward to jointly optimize temporal accuracy, spatial consistency, and structural format regularization. Extensive experiments on six benchmarks demonstrate the effectiveness of our approach. STVG-R1 surpasses the baseline Qwen2.5-VL-7B by a remarkable margin of 20.9% on m_IoU on the HCSTVG-v2 benchmark, establishing a new state of the art (SOTA). Surprisingly, STVG-R1 also exhibits strong zero-shot generalization to multi-object referring video object segmentation tasks, achieving a SOTA 47.3% J&F on MeViS.

