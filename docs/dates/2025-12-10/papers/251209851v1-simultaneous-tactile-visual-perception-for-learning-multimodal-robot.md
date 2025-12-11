---
layout: default
title: Simultaneous Tactile-Visual Perception for Learning Multimodal Robot Manipulation
---

# Simultaneous Tactile-Visual Perception for Learning Multimodal Robot Manipulation
**arXiv**：[2512.09851v1](https://arxiv.org/abs/2512.09851) · [PDF](https://arxiv.org/pdf/2512.09851.pdf)  
**作者**：Yuyang Li, Yinghan Chen, Zihang Zhao, Puhao Li, Tengyu Liu, Siyuan Huang, Yixin Zhu  

**一句话要点**：提出TacThru传感器与TacThru-UMI框架，实现同步触觉-视觉感知以提升机器人操作性能

**关键词**：透皮传感器, 多模态感知, 模仿学习, 机器人操作, 触觉视觉融合, 扩散策略

## 3 点简述
- 现有透皮传感器缺乏同步多模态感知且触觉跟踪不可靠，阻碍机器人操作学习
- TacThru传感器通过全透明弹性体、持续照明和关键线标记实现同步视觉与稳健触觉信号提取
- TacThru-UMI框架基于Transformer扩散策略整合多模态信号，在五项任务中平均成功率85.5%

## 摘要（原文）

> Robotic manipulation requires both rich multimodal perception and effective learning frameworks to handle complex real-world tasks. See-through-skin (STS) sensors, which combine tactile and visual perception, offer promising sensing capabilities, while modern imitation learning provides powerful tools for policy acquisition. However, existing STS designs lack simultaneous multimodal perception and suffer from unreliable tactile tracking. Furthermore, integrating these rich multimodal signals into learning-based manipulation pipelines remains an open challenge. We introduce TacThru, an STS sensor enabling simultaneous visual perception and robust tactile signal extraction, and TacThru-UMI, an imitation learning framework that leverages these multimodal signals for manipulation. Our sensor features a fully transparent elastomer, persistent illumination, novel keyline markers, and efficient tracking, while our learning system integrates these signals through a Transformer-based Diffusion Policy. Experiments on five challenging real-world tasks show that TacThru-UMI achieves an average success rate of 85.5%, significantly outperforming the baselines of alternating tactile-visual (66.3%) and vision-only (55.4%). The system excels in critical scenarios, including contact detection with thin and soft objects and precision manipulation requiring multimodal coordination. This work demonstrates that combining simultaneous multimodal perception with modern learning frameworks enables more precise, adaptable robotic manipulation.

