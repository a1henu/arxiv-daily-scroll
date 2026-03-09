---
layout: default
title: Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration
---

# Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration
**arXiv**：[2603.06001v1](https://arxiv.org/abs/2603.06001) · [PDF](https://arxiv.org/pdf/2603.06001.pdf)  
**作者**：Ninghao Zhang, Bin Zhu, Shijie Zhou, Jingjing Chen  

**一句话要点**：提出无需训练的注意力重校准方法，以缓解视觉-语言-动作模型在分布外指令下的语言盲视问题。

**关键词**：视觉-语言-动作模型, 语言盲视, 注意力重校准, 分布外指令, 机器人操作

## 3 点简述
- 核心问题：VLA模型在视觉先验与语言指令矛盾时，优先视觉导致动作生成错误，称为语言盲视。
- 方法要点：引入ICBench诊断基准，并提出IGAR机制，在推理时重平衡注意力分布以增强语言影响。
- 实验或效果：在LIBERO任务和真实机器人上验证，IGAR显著减少错误执行，同时保持基线性能。

## 摘要（原文）

> Vision-Language-Action (VLA) models enable robots to perform manipulation tasks directly from natural language instructions and are increasingly viewed as a foundation for generalist robotic policies. However, their reliability under Out-of-Distribution (OOD) instructions remains underexplored. In this paper, we reveal a critical failure mode in which VLA policies continue executing visually plausible actions even when the language instruction contradicts the scene. We refer to this phenomenon as linguistic blindness, where VLA policies prioritize visual priors over instruction semantics during action generation. To systematically analyze this issue, we introduce ICBench, a diagnostic benchmark constructed from the LIBERO dataset that probes language-action coupling by injecting controlled OOD instruction contradictions while keeping the visual environment unchanged. Evaluations on three representative VLA architectures, including Pi0, Pi0.5 and OpenVLA OFT, show that these models frequently succeed at tasks despite logically impossible instructions, revealing a strong visual bias in action generation. To mitigate this issue, we propose Instruction-Guided Attention Recalibration (IGAR), a train-free inference-time mechanism that rebalances attention distributions to restore the influence of language instructions. IGAR operates without retraining or architectural modification and can be directly applied to existing VLA models. Experiments across 30 LIBERO tasks demonstrate that IGAR substantially reduces erroneous execution under OOD contradictory instructions while preserving baseline task performance. We additionally validate the approach on a real Franka robotic arm, where IGAR effectively prevents manipulation triggered by inconsistent instructions.

