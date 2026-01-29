---
layout: default
title: Open-Vocabulary Functional 3D Human-Scene Interaction Generation
---

# Open-Vocabulary Functional 3D Human-Scene Interaction Generation
**arXiv**：[2601.20835v1](https://arxiv.org/abs/2601.20835) · [PDF](https://arxiv.org/pdf/2601.20835.pdf)  
**作者**：Jie Liu, Yu Sun, Alpar Cseke, Yao Feng, Nicolas Heron, Michael J. Black, Yan Zhang  

**一句话要点**：提出FunHSI框架以解决开放词汇功能3D人-场景交互生成问题

**关键词**：3D人-场景交互, 功能感知推理, 开放词汇生成, 视觉语言模型, 物理优化

## 3 点简述
- 核心问题：现有方法缺乏对物体功能和接触的显式推理，导致交互不真实或功能错误。
- 方法要点：通过功能感知接触推理、视觉语言模型合成和阶段优化，实现训练无关的交互生成。
- 实验或效果：在多样室内外场景中生成功能正确且物理合理的人-场景交互，优于现有方法。

## 摘要（原文）

> Generating 3D humans that functionally interact with 3D scenes remains an open problem with applications in embodied AI, robotics, and interactive content creation. The key challenge involves reasoning about both the semantics of functional elements in 3D scenes and the 3D human poses required to achieve functionality-aware interaction. Unfortunately, existing methods typically lack explicit reasoning over object functionality and the corresponding human-scene contact, resulting in implausible or functionally incorrect interactions. In this work, we propose FunHSI, a training-free, functionality-driven framework that enables functionally correct human-scene interactions from open-vocabulary task prompts. Given a task prompt, FunHSI performs functionality-aware contact reasoning to identify functional scene elements, reconstruct their 3D geometry, and model high-level interactions via a contact graph. We then leverage vision-language models to synthesize a human performing the task in the image and estimate proposed 3D body and hand poses. Finally, the proposed 3D body configuration is refined via stage-wise optimization to ensure physical plausibility and functional correctness. In contrast to existing methods, FunHSI not only synthesizes more plausible general 3D interactions, such as "sitting on a sofa'', while supporting fine-grained functional human-scene interactions, e.g., "increasing the room temperature''. Extensive experiments demonstrate that FunHSI consistently generates functionally correct and physically plausible human-scene interactions across diverse indoor and outdoor scenes.

