---
layout: default
title: VERM: Leveraging Foundation Models to Create a Virtual Eye for Efficient 3D Robotic Manipulation
---

# VERM: Leveraging Foundation Models to Create a Virtual Eye for Efficient 3D Robotic Manipulation
**arXiv**：[2512.16724v1](https://arxiv.org/abs/2512.16724) · [PDF](https://arxiv.org/pdf/2512.16724.pdf)  
**作者**：Yixiang Chen, Yan Huang, Keji He, Peiyan Li, Liang Wang  

**一句话要点**：提出VERM方法，利用基础模型生成虚拟任务自适应视图以提升3D机器人操作效率

**关键词**：3D机器人操作, 基础模型, 虚拟视图生成, 深度感知, 动态粗到细过程, 计算效率提升

## 3 点简述
- 核心问题：多摄像头设置引入冗余信息，增加计算成本和训练时间
- 方法要点：基于3D点云想象虚拟视图，结合深度感知模块和动态粗到细过程
- 实验或效果：在RLBench和真实世界评估中超越SOTA，训练和推理速度分别提升1.89倍和1.54倍

## 摘要（原文）

> When performing 3D manipulation tasks, robots have to execute action planning based on perceptions from multiple fixed cameras. The multi-camera setup introduces substantial redundancy and irrelevant information, which increases computational costs and forces the model to spend extra training time extracting crucial task-relevant details. To filter out redundant information and accurately extract task-relevant features, we propose the VERM (Virtual Eye for Robotic Manipulation) method, leveraging the knowledge in foundation models to imagine a virtual task-adaptive view from the constructed 3D point cloud, which efficiently captures necessary information and mitigates occlusion. To facilitate 3D action planning and fine-grained manipulation, we further design a depth-aware module and a dynamic coarse-to-fine procedure. Extensive experimental results on both simulation benchmark RLBench and real-world evaluations demonstrate the effectiveness of our method, surpassing previous state-of-the-art methods while achieving 1.89x speedup in training time and 1.54x speedup in inference speed. More results can be found on our project website at https://verm-ral.github.io .

