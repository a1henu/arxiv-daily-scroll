---
layout: default
title: Vision-Language-Action Models for Selective Robotic Disassembly: A Case Study on Critical Component Extraction from Desktops
---

# Vision-Language-Action Models for Selective Robotic Disassembly: A Case Study on Critical Component Extraction from Desktops
**arXiv**：[2512.04446v1](https://arxiv.org/abs/2512.04446) · [PDF](https://arxiv.org/pdf/2512.04446.pdf)  
**作者**：Chang Liu, Sibo Tian, Sara Behdad, Xiao Liang, Minghui Zheng  

**一句话要点**：提出结合视觉-语言-动作模型与规则控制器的混合策略，以解决台式机关键部件自动拆卸的复杂性问题。

**关键词**：视觉-语言-动作模型, 机器人拆卸, 混合策略, 台式机关键部件, 微调, 自动化

## 3 点简述
- 核心问题：台式机关键部件拆卸自动化面临产品变异性、操作序列性和精确性挑战，现有方法泛化能力有限。
- 方法要点：收集定制数据集，微调OpenVLA和OpenVLA-OFT模型，并引入混合策略增强模型在复杂拆卸任务中的表现。
- 实验或效果：微调模型能完成早期步骤，但关键子任务失败；混合策略成功实现完整拆卸，揭示VLA模型在灵巧性方面的局限。

## 摘要（原文）

> Automating disassembly of critical components from end-of-life (EoL) desktops, such as high-value items like RAM modules and CPUs, as well as sensitive parts like hard disk drives, remains challenging due to the inherent variability and uncertainty of these products. Moreover, their disassembly requires sequential, precise, and dexterous operations, further increasing the complexity of automation. Current robotic disassembly processes are typically divided into several stages: perception, sequence planning, task planning, motion planning, and manipulation. Each stage requires explicit modeling, which limits generalization to unfamiliar scenarios. Recent development of vision-language-action (VLA) models has presented an end-to-end approach for general robotic manipulation tasks. Although VLAs have demonstrated promising performance on simple tasks, the feasibility of applying such models to complex disassembly remains largely unexplored. In this paper, we collected a customized dataset for robotic RAM and CPU disassembly and used it to fine-tune two well-established VLA approaches, OpenVLA and OpenVLA-OFT, as a case study. We divided the whole disassembly task into several small steps, and our preliminary experimental results indicate that the fine-tuned VLA models can faithfully complete multiple early steps but struggle with certain critical subtasks, leading to task failure. However, we observed that a simple hybrid strategy that combines VLA with a rule-based controller can successfully perform the entire disassembly operation. These findings highlight the current limitations of VLA models in handling the dexterity and precision required for robotic EoL product disassembly. By offering a detailed analysis of the observed results, this study provides insights that may inform future research to address current challenges and advance end-to-end robotic automated disassembly.

