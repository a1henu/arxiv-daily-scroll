---
layout: default
title: Model-agnostic Adversarial Attack and Defense for Vision-Language-Action Models
---

# Model-agnostic Adversarial Attack and Defense for Vision-Language-Action Models
**arXiv**：[2510.13237v1](https://arxiv.org/abs/2510.13237) · [PDF](https://arxiv.org/pdf/2510.13237.pdf)  
**作者**：Haochuan Xu, Yun Sing Koh, Shuhuai Huang, Zirun Zhou, Di Wang, Jun Sakuma, Jingfeng Zhang  

**一句话要点**：提出模型无关的对抗攻击EDPA与防御策略，提升视觉-语言-动作模型的鲁棒性。

**关键词**：对抗攻击, 模型无关防御, 视觉-语言-动作模型, 机器人学习, 语义对齐, 潜表示优化

## 3 点简述
- 核心问题：VLA模型在机器人任务中对抗鲁棒性不足，易受攻击导致任务失败。
- 方法要点：EDPA通过破坏视觉-文本语义对齐和最大化潜表示差异，生成可放置的对抗补丁。
- 实验或效果：在LIBERO基准上，EDPA显著增加任务失败率，防御策略有效缓解性能下降。

## 摘要（原文）

> Vision-Language-Action (VLA) models have achieved revolutionary progress in
> robot learning, enabling robots to execute complex physical robot tasks from
> natural language instructions. Despite this progress, their adversarial
> robustness remains underexplored. In this work, we propose both adversarial
> patch attack and corresponding defense strategies for VLA models. We first
> introduce the Embedding Disruption Patch Attack (EDPA), a model-agnostic
> adversarial attack that generates patches directly placeable within the
> camera's view. In comparison to prior methods, EDPA can be readily applied to
> different VLA models without requiring prior knowledge of the model
> architecture, or the controlled robotic manipulator. EDPA constructs these
> patches by (i) disrupting the semantic alignment between visual and textual
> latent representations, and (ii) maximizing the discrepancy of latent
> representations between adversarial and corresponding clean visual inputs.
> Through the optimization of these objectives, EDPA distorts the VLA's
> interpretation of visual information, causing the model to repeatedly generate
> incorrect actions and ultimately result in failure to complete the given
> robotic task. To counter this, we propose an adversarial fine-tuning scheme for
> the visual encoder, in which the encoder is optimized to produce similar latent
> representations for both clean and adversarially perturbed visual inputs.
> Extensive evaluations on the widely recognized LIBERO robotic simulation
> benchmark demonstrate that EDPA substantially increases the task failure rate
> of cutting-edge VLA models, while our proposed defense effectively mitigates
> this degradation. The codebase is accessible via the homepage at
> https://edpa-attack.github.io/.

