---
layout: default
title: Think Proprioceptively: Embodied Visual Reasoning for VLA Manipulation
---

# Think Proprioceptively: Embodied Visual Reasoning for VLA Manipulation
**arXiv**：[2602.06575v1](https://arxiv.org/abs/2602.06575) · [PDF](https://arxiv.org/pdf/2602.06575.pdf)  
**作者**：Fangyuan Wang, Peng Zhou, Jiaming Qi, Shipeng Lyu, David Navarro-Alarcon, Guodong Guo  

**一句话要点**：提出ThinkProprio，通过早期融合本体感知提升VLA模型在机器人操作中的视觉推理效率

**关键词**：视觉语言动作模型, 本体感知融合, 机器人操作, 视觉推理, 令牌选择, 推理效率

## 3 点简述
- 核心问题：VLA模型通常将本体感知作为后期条件信号，限制了机器人状态对指令理解和视觉注意的影响
- 方法要点：将本体感知转换为文本令牌，在输入层与任务指令融合，以引导视觉推理和令牌选择
- 实验或效果：在CALVIN、LIBERO和真实世界操作中，性能匹配或优于基线，推理延迟降低超50%

## 摘要（原文）

> Vision-language-action (VLA) models typically inject proprioception only as a late conditioning signal, which prevents robot state from shaping instruction understanding and from influencing which visual tokens are attended throughout the policy. We introduce ThinkProprio, which converts proprioception into a sequence of text tokens in the VLM embedding space and fuses them with the task instruction at the input. This early fusion lets embodied state participate in subsequent visual reasoning and token selection, biasing computation toward action-critical evidence while suppressing redundant visual tokens. In a systematic ablation over proprioception encoding, state entry point, and action-head conditioning, we find that text tokenization is more effective than learned projectors, and that retaining roughly 15% of visual tokens can match the performance of using the full token set. Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio matches or improves over strong baselines while reducing end-to-end inference latency over 50%.

