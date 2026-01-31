---
layout: default
title: MoE-ACT: Improving Surgical Imitation Learning Policies through Supervised Mixture-of-Experts
---

# MoE-ACT: Improving Surgical Imitation Learning Policies through Supervised Mixture-of-Experts
**arXiv**：[2601.21971v1](https://arxiv.org/abs/2601.21971) · [PDF](https://arxiv.org/pdf/2601.21971.pdf)  
**作者**：Lorenzo Mazza, Ariel Rodriguez, Rayan Younis, Martin Lelis, Ortrun Hellig, Chenpan Li, Sebastian Bodenstedt, Martin Wagner, Stefanie Speidel  

**一句话要点**：提出监督混合专家架构以提升手术模仿学习策略在数据稀缺下的性能

**关键词**：手术机器人, 模仿学习, 混合专家, 动作分块变换器, 视觉语言动作模型, 零样本泛化

## 3 点简述
- 手术机器人模仿学习面临数据稀缺、安全要求高等挑战
- 采用监督混合专家架构增强动作分块变换器，仅需少于150次演示
- 在肠道抓取任务中优于基线，并展示出分布外鲁棒性和零样本泛化能力

## 摘要（原文）

> Imitation learning has achieved remarkable success in robotic manipulation, yet its application to surgical robotics remains challenging due to data scarcity, constrained workspaces, and the need for an exceptional level of safety and predictability. We present a supervised Mixture-of-Experts (MoE) architecture designed for phase-structured surgical manipulation tasks, which can be added on top of any autonomous policy. Unlike prior surgical robot learning approaches that rely on multi-camera setups or thousands of demonstrations, we show that a lightweight action decoder policy like Action Chunking Transformer (ACT) can learn complex, long-horizon manipulation from less than 150 demonstrations using solely stereo endoscopic images, when equipped with our architecture. We evaluate our approach on the collaborative surgical task of bowel grasping and retraction, where a robot assistant interprets visual cues from a human surgeon, executes targeted grasping on deformable tissue, and performs sustained retraction. We benchmark our method against state-of-the-art Vision-Language-Action (VLA) models and the standard ACT baseline. Our results show that generalist VLAs fail to acquire the task entirely, even under standard in-distribution conditions. Furthermore, while standard ACT achieves moderate success in-distribution, adopting a supervised MoE architecture significantly boosts its performance, yielding higher success rates in-distribution and demonstrating superior robustness in out-of-distribution scenarios, including novel grasp locations, reduced illumination, and partial occlusions. Notably, it generalizes to unseen testing viewpoints and also transfers zero-shot to ex vivo porcine tissue without additional training, offering a promising pathway toward in vivo deployment. To support this, we present qualitative preliminary results of policy roll-outs during in vivo porcine surgery.

