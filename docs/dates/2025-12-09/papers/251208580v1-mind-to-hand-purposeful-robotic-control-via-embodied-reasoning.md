---
layout: default
title: Mind to Hand: Purposeful Robotic Control via Embodied Reasoning
---

# Mind to Hand: Purposeful Robotic Control via Embodied Reasoning
**arXiv**：[2512.08580v1](https://arxiv.org/abs/2512.08580) · [PDF](https://arxiv.org/pdf/2512.08580.pdf)  
**作者**：Peijun Tang, Shangjin Xie, Binyan Sun, Baifu Huang, Kuncheng Luo, Haotian Yang, Weiqi Jin, Jianan Wang  

**一句话要点**：提出Lumo-1模型，通过三阶段预训练统一机器人推理与动作，以解决AI系统在物理动作中的推理落地挑战。

**关键词**：具身推理, 视觉语言动作模型, 机器人控制, 三阶段预训练, 长时程任务, 跨具身数据

## 3 点简述
- 核心问题：AI系统虽具备广泛推理能力，但难以在物理动作中有效落地，机器人控制需结合上下文与意图。
- 方法要点：基于预训练视觉语言模型，分三阶段扩展至具身推理与动作预测，包括增强推理技能、跨具身数据协同训练和动作训练。
- 实验或效果：Lumo-1在具身视觉语言推理中表现显著提升，在真实世界机器人任务中超越基线，尤其在长时程任务和自然指令响应中表现出色。

## 摘要（原文）

> Humans act with context and intention, with reasoning playing a central role. While internet-scale data has enabled broad reasoning capabilities in AI systems, grounding these abilities in physical action remains a major challenge. We introduce Lumo-1, a generalist vision-language-action (VLA) model that unifies robot reasoning ("mind") with robot action ("hand"). Our approach builds upon the general multi-modal reasoning capabilities of pre-trained vision-language models (VLMs), progressively extending them to embodied reasoning and action prediction, and ultimately towards structured reasoning and reasoning-action alignment. This results in a three-stage pre-training pipeline: (1) Continued VLM pre-training on curated vision-language data to enhance embodied reasoning skills such as planning, spatial understanding, and trajectory prediction; (2) Co-training on cross-embodiment robot data alongside vision-language data; and (3) Action training with reasoning process on trajectories collected on Astribot S1, a bimanual mobile manipulator with human-like dexterity and agility. Finally, we integrate reinforcement learning to further refine reasoning-action consistency and close the loop between semantic inference and motor control. Extensive experiments demonstrate that Lumo-1 achieves significant performance improvements in embodied vision-language reasoning, a critical component for generalist robotic control. Real-world evaluations further show that Lumo-1 surpasses strong baselines across a wide range of challenging robotic tasks, with strong generalization to novel objects and environments, excelling particularly in long-horizon tasks and responding to human-natural instructions that require reasoning over strategy, concepts and space.

