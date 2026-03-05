---
layout: default
title: Discriminative Perception via Anchored Description for Reasoning Segmentation
---

# Discriminative Perception via Anchored Description for Reasoning Segmentation
**arXiv**：[2603.04002v1](https://arxiv.org/abs/2603.04002) · [PDF](https://arxiv.org/pdf/2603.04002.pdf)  
**作者**：Tao Yang, Qing Zhou, Yanliang Li, Qi Wang  

**一句话要点**：提出DPAD方法，通过锚定描述实现判别感知，以优化推理分割中的强化学习过程。

**关键词**：推理分割, 强化学习, 判别感知, 锚定描述, 多模态大语言模型

## 3 点简述
- 核心问题：现有强化学习奖励无法区分推理过程是否锚定目标区域，导致推理链冗长且不聚焦。
- 方法要点：强制模型生成目标对象的描述性标题，通过对比语义相关性实现判别感知，优化推理链。
- 实验或效果：在ReasonSeg基准上，cIoU提升3.09%，推理链长度减少约42%。

## 摘要（原文）

> Reasoning segmentation increasingly employs reinforcement learning to generate explanatory reasoning chains that guide Multimodal Large Language Models. While these geometric rewards are primarily confined to guiding the final localization, they are incapable of discriminating whether the reasoning process remains anchored on the referred region or strays into irrelevant context. Lacking this discriminative guidance, the model's reasoning often devolves into unfocused and verbose chains that ultimately fail to disambiguate and perceive the target in complex scenes. This suggests a need to complement the RL objective with Discriminative Perception, an ability to actively distinguish a target from its context. To realize this, we propose DPAD to compel the model to generate a descriptive caption of the referred object, which is then used to explicitly discriminate by contrasting the caption's semantic relevance to the referred object against the wider context. By optimizing for this discriminative capability, the model is forced to focus on the unique attributes of the target, leading to a more converged and efficient reasoning chain. The descriptive caption also serves as an interpretability rationale that aligns with the segmentation. Experiments on the benchmarks confirm the validity of our approach, delivering substantial performance gains, with the cIoU on ReasonSeg increasing by 3.09% and the reasoning chain length decreasing by approximately 42%. Code is available at https://github.com/mrazhou/DPAD

