---
layout: default
title: SteerVLA: Steering Vision-Language-Action Models in Long-Tail Driving Scenarios
---

# SteerVLA: Steering Vision-Language-Action Models in Long-Tail Driving Scenarios
**arXiv**：[2602.08440v1](https://arxiv.org/abs/2602.08440) · [PDF](https://arxiv.org/pdf/2602.08440.pdf)  
**作者**：Tian Gao, Celine Tan, Catherine Glossop, Timothy Gao, Jiankai Sun, Kyle Stachowicz, Shirley Wu, Oier Mees, Dorsa Sadigh, Sergey Levine, Chelsea Finn  

**一句话要点**：提出SteerVLA，利用视觉语言模型生成细粒度指令以引导视觉语言动作模型在长尾驾驶场景中实现稳健控制。

**关键词**：自动驾驶, 视觉语言动作模型, 长尾场景, 语言指令引导, 闭环评估, 数据增强

## 3 点简述
- 核心问题：自动驾驶需整合高层语义推理与低层反应控制，但视觉语言模型缺乏安全车辆控制的接地经验。
- 方法要点：通过视觉语言模型增强驾驶数据语言标注，建立高层与低层策略间的丰富语言接口以提升推理与可控性。
- 实验或效果：在闭环基准测试中，整体驾驶得分提升4.77分，长尾子集提升8.04分，优于现有方法。

## 摘要（原文）

> A fundamental challenge in autonomous driving is the integration of high-level, semantic reasoning for long-tail events with low-level, reactive control for robust driving. While large vision-language models (VLMs) trained on web-scale data offer powerful common-sense reasoning, they lack the grounded experience necessary for safe vehicle control. We posit that an effective autonomous agent should leverage the world knowledge of VLMs to guide a steerable driving policy toward robust control in driving scenarios. To this end, we propose SteerVLA, which leverages the reasoning capabilities of VLMs to produce fine-grained language instructions that steer a vision-language-action (VLA) driving policy. Key to our method is this rich language interface between the high-level VLM and low-level VLA, which allows the high-level policy to more effectively ground its reasoning in the control outputs of the low-level policy. To provide fine-grained language supervision aligned with vehicle control, we leverage a VLM to augment existing driving data with detailed language annotations, which we find to be essential for effective reasoning and steerability. We evaluate SteerVLA on a challenging closed-loop benchmark, where it outperforms state-of-the-art methods by 4.77 points in overall driving score and by 8.04 points on a long-tail subset. The project website is available at: https://steervla.github.io/.

