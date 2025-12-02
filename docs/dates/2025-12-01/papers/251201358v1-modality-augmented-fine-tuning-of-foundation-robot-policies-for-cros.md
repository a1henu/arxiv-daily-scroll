---
layout: default
title: Modality-Augmented Fine-Tuning of Foundation Robot Policies for Cross-Embodiment Manipulation on GR1 and G1
---

# Modality-Augmented Fine-Tuning of Foundation Robot Policies for Cross-Embodiment Manipulation on GR1 and G1
**arXiv**：[2512.01358v1](https://arxiv.org/abs/2512.01358) · [PDF](https://arxiv.org/pdf/2512.01358.pdf)  
**作者**：Junsung Park, Hogun Kee, Songhwai Oh  

**一句话要点**：提出模态增强微调框架，以适配GR1和G1人形机器人的跨具身操作任务。

**关键词**：跨具身操作, 模态增强, 微调框架, 人形机器人, 多模态数据集

## 3 点简述
- 核心问题：基础机器人策略难以适应不同人形机器人具身，需跨具身操作能力。
- 方法要点：通过模态增强微调，包括后处理模态（如接触信号）和多模态数据集（如运动规划）。
- 实验或效果：GR1成功率从51%提升至63%，G1任务成功率从48%提升至94%，验证了模态增强的有效性。

## 摘要（原文）

> This paper presents a modality-augmented fine-tuning framework designed to adapt foundation robot policies to diverse humanoid embodiments. We validate our approach across two distinct settings: (i) the GR1 embodiment, utilizing public datasets where we introduce post-processed modalities, including binary contact signals and ZoeDepth-generated metric depth; and (ii) the Unitree G1 embodiment, for which we contribute a novel multi-modal dataset incorporating cuRobo motion planning, inverse kinematics, and ground-truth contact-force measurements. Our experiments demonstrate that modality augmentation consistently enhances policy performance across different embodiments. Specifically, for the GR1, integrating contact-state cues and RGB-D fusion improves online success rates from 51% to 63%. Furthermore, in the G1 "Pick Apple to Bowl" task, our contact-augmented model achieves a success rate of 94%, significantly outperforming the 48% achieved by standard fine-tuning and the 0% baseline of zero-shot transfer. These results highlight that lightweight post-processing effectively strengthens policies for GR1, while high-quality multi-modal data is crucial for reliable transfer to the Unitree G1. Consequently, this work establishes a unified, data-centric pathway for extending foundation robot policies through targeted modality design and multi-modal fine-tuning.

