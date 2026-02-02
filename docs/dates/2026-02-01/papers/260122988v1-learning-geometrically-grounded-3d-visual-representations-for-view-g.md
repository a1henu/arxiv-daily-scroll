---
layout: default
title: Learning Geometrically-Grounded 3D Visual Representations for View-Generalizable Robotic Manipulation
---

# Learning Geometrically-Grounded 3D Visual Representations for View-Generalizable Robotic Manipulation
**arXiv**：[2601.22988v1](https://arxiv.org/abs/2601.22988) · [PDF](https://arxiv.org/pdf/2601.22988.pdf)  
**作者**：Di Zhang, Weicheng Duan, Dasen Gu, Hongye Lu, Hai Zhang, Hang Yu, Junqiao Zhao, Guang Chen  

**一句话要点**：提出MethodName框架，通过单视图3D预训练和多步蒸馏，解决机器人操作中视图泛化问题。

**关键词**：机器人操作, 3D视觉表示, 视图泛化, 单视图预训练, 蒸馏学习, 点云重建

## 3 点简述
- 核心问题：现有3D视觉表示依赖多视图推理，无法在单视图受限场景中实现鲁棒空间理解和视图泛化。
- 方法要点：引入单视图3D预训练，结合点云重建和前向高斯泼溅，学习整体几何表示；通过多步蒸馏保留几何知识并迁移至操作技能。
- 实验或效果：在RLBench任务上平均成功率提升12.7%，零样本视图泛化下成功率下降较小，优于现有方法。

## 摘要（原文）

> Real-world robotic manipulation demands visuomotor policies capable of robust spatial scene understanding and strong generalization across diverse camera viewpoints. While recent advances in 3D-aware visual representations have shown promise, they still suffer from several key limitations, including reliance on multi-view observations during inference which is impractical in single-view restricted scenarios, incomplete scene modeling that fails to capture holistic and fine-grained geometric structures essential for precise manipulation, and lack of effective policy training strategies to retain and exploit the acquired 3D knowledge. To address these challenges, we present MethodName, a unified representation-policy learning framework for view-generalizable robotic manipulation. MethodName introduces a single-view 3D pretraining paradigm that leverages point cloud reconstruction and feed-forward gaussian splatting under multi-view supervision to learn holistic geometric representations. During policy learning, MethodName performs multi-step distillation to preserve the pretrained geometric understanding and effectively transfer it to manipulation skills. We conduct experiments on 12 RLBench tasks, where our approach outperforms the previous state-of-the-art method by 12.7% in average success rate. Further evaluation on six representative tasks demonstrates strong zero-shot view generalization, with success rate drops of only 22.0% and 29.7% under moderate and large viewpoint shifts respectively, whereas the state-of-the-art method suffers larger decreases of 41.6% and 51.5%.

