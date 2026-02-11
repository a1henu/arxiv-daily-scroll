---
layout: default
title: Preference Aligned Visuomotor Diffusion Policies for Deformable Object Manipulation
---

# Preference Aligned Visuomotor Diffusion Policies for Deformable Object Manipulation
**arXiv**：[2602.09583v1](https://arxiv.org/abs/2602.09583) · [PDF](https://arxiv.org/pdf/2602.09583.pdf)  
**作者**：Marco Moletta, Michael C. Welle, Danica Kragic  

**一句话要点**：提出RKO偏好对齐方法，结合RPO与KTO框架，优化可变形物体操作中的个性化机器人行为。

**关键词**：偏好学习, 可变形物体操作, 视觉运动策略, 扩散模型, 机器人个性化, 衣物折叠

## 3 点简述
- 核心问题：机器人操作中用户偏好难以表达，尤其在可变形物体如衣物上，影响个性化与满意度。
- 方法要点：基于预训练视觉运动扩散策略，利用有限演示，通过RKO方法对齐偏好，结合RPO和KTO优势。
- 实验或效果：在真实世界衣物折叠任务中，RKO相比标准微调，展现更优性能和样本效率，验证偏好学习的可行性。

## 摘要（原文）

> Humans naturally develop preferences for how manipulation tasks should be performed, which are often subtle, personal, and difficult to articulate. Although it is important for robots to account for these preferences to increase personalization and user satisfaction, they remain largely underexplored in robotic manipulation, particularly in the context of deformable objects like garments and fabrics. In this work, we study how to adapt pretrained visuomotor diffusion policies to reflect preferred behaviors using limited demonstrations. We introduce RKO, a novel preference-alignment method that combines the benefits of two recent frameworks: RPO and KTO. We evaluate RKO against common preference learning frameworks, including these two, as well as a baseline vanilla diffusion policy, on real-world cloth-folding tasks spanning multiple garments and preference settings. We show that preference-aligned policies (particularly RKO) achieve superior performance and sample efficiency compared to standard diffusion policy fine-tuning. These results highlight the importance and feasibility of structured preference learning for scaling personalized robot behavior in complex deformable object manipulation tasks.

