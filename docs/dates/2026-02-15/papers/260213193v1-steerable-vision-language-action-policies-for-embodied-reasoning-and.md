---
layout: default
title: Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control
---

# Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control
**arXiv**：[2602.13193v1](https://arxiv.org/abs/2602.13193) · [PDF](https://arxiv.org/pdf/2602.13193.pdf)  
**作者**：William Chen, Jagdeep Singh Bhatia, Catherine Glossop, Nikhil Mathihalli, Ria Doshi, Andy Tang, Danny Driess, Karl Pertsch, Sergey Levine  

**一句话要点**：提出可操控策略以增强视觉语言动作模型在机器人控制中的低层可控性

**关键词**：机器人控制, 视觉语言动作模型, 可操控策略, 低层可控性, 任务泛化, 长时任务

## 3 点简述
- 核心问题：视觉语言模型知识难以有效落地到机器人行为，现有方法因自然语言接口限制低层控制。
- 方法要点：训练视觉语言动作模型于多抽象层级的合成命令，如子任务、动作和像素坐标，提升低层可控性。
- 实验或效果：在真实世界操作实验中，结合高层推理器或现成视觉语言模型，优于先前方法，尤其在泛化和长时任务。

## 摘要（原文）

> Pretrained vision-language models (VLMs) can make semantic and visual inferences across diverse settings, providing valuable common-sense priors for robotic control. However, effectively grounding this knowledge in robot behaviors remains an open challenge. Prior methods often employ a hierarchical approach where VLMs reason over high-level commands to be executed by separate low-level policies, e.g., vision-language-action models (VLAs). The interface between VLMs and VLAs is usually natural language task instructions, which fundamentally limits how much VLM reasoning can steer low-level behavior. We thus introduce Steerable Policies: VLAs trained on rich synthetic commands at various levels of abstraction, like subtasks, motions, and grounded pixel coordinates. By improving low-level controllability, Steerable Policies can unlock pretrained knowledge in VLMs, enabling improved task generalization. We demonstrate this benefit by controlling our Steerable Policies with both a learned high-level embodied reasoner and an off-the-shelf VLM prompted to reason over command abstractions via in-context learning. Across extensive real-world manipulation experiments, these two novel methods outperform prior embodied reasoning VLAs and VLM-based hierarchical baselines, including on challenging generalization and long-horizon tasks.
>   Website: steerable-policies.github.io

