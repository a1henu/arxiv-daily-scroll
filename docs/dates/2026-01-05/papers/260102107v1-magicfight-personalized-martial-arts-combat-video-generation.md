---
layout: default
title: MagicFight: Personalized Martial Arts Combat Video Generation
---

# MagicFight: Personalized Martial Arts Combat Video Generation
**arXiv**：[2601.02107v1](https://arxiv.org/abs/2601.02107) · [PDF](https://arxiv.org/pdf/2601.02107.pdf)  
**作者**：Jiancheng Huang, Mingfu Yan, Songyan Chen, Yi Huang, Shifeng Chen  

**一句话要点**：提出MagicFight方法以解决双人武术格斗视频生成中的身份混淆和动作不匹配问题。

**关键词**：个性化视频生成, 双人交互, 武术格斗, Unity数据集, 身份保持, 动作连贯性

## 3 点简述
- 核心问题：现有单人生成模型无法处理双人交互，导致身份混淆、肢体异常和动作不匹配。
- 方法要点：基于Unity游戏引擎生成定制数据集，并改进现有模型以生成高保真双人战斗视频。
- 实验或效果：生成视频保持个体身份和动作连贯性，为交互视频内容创作奠定基础。

## 摘要（原文）

> Amid the surge in generic text-to-video generation, the field of personalized human video generation has witnessed notable advancements, primarily concentrated on single-person scenarios. However, to our knowledge, the domain of two-person interactions, particularly in the context of martial arts combat, remains uncharted. We identify a significant gap: existing models for single-person dancing generation prove insufficient for capturing the subtleties and complexities of two engaged fighters, resulting in challenges such as identity confusion, anomalous limbs, and action mismatches. To address this, we introduce a pioneering new task, Personalized Martial Arts Combat Video Generation. Our approach, MagicFight, is specifically crafted to overcome these hurdles. Given this pioneering task, we face a lack of appropriate datasets. Thus, we generate a bespoke dataset using the game physics engine Unity, meticulously crafting a multitude of 3D characters, martial arts moves, and scenes designed to represent the diversity of combat. MagicFight refines and adapts existing models and strategies to generate high-fidelity two-person combat videos that maintain individual identities and ensure seamless, coherent action sequences, thereby laying the groundwork for future innovations in the realm of interactive video content creation.
>   Website: https://MingfuYAN.github.io/MagicFight/
>   Dataset: https://huggingface.co/datasets/MingfuYAN/KungFu-Fiesta

