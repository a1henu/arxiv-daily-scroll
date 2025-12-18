---
layout: default
title: ISS Policy : Scalable Diffusion Policy with Implicit Scene Supervision
---

# ISS Policy : Scalable Diffusion Policy with Implicit Scene Supervision
**arXiv**：[2512.15020v1](https://arxiv.org/abs/2512.15020) · [PDF](https://arxiv.org/pdf/2512.15020.pdf)  
**作者**：Wenlong Xia, Jinhao Zhang, Ce Zhang, Yaojia Wang, Youmin Gong, Jie Mei  

**一句话要点**：提出ISS Policy，通过隐式场景监督提升基于点云的扩散策略性能与泛化能力。

**关键词**：扩散策略, 隐式场景监督, 点云观测, 机器人操作, 模仿学习, 3D视觉

## 3 点简述
- 核心问题：基于视觉的模仿学习依赖物体外观，忽略3D场景结构，导致训练效率低、泛化差。
- 方法要点：扩展DiT，引入隐式场景监督模块，使模型输出与场景几何演化一致。
- 实验或效果：在MetaWorld和Adroit任务中达到SOTA，真实世界实验显示强泛化与鲁棒性。

## 摘要（原文）

> Vision-based imitation learning has enabled impressive robotic manipulation skills, but its reliance on object appearance while ignoring the underlying 3D scene structure leads to low training efficiency and poor generalization. To address these challenges, we introduce \emph{Implicit Scene Supervision (ISS) Policy}, a 3D visuomotor DiT-based diffusion policy that predicts sequences of continuous actions from point cloud observations. We extend DiT with a novel implicit scene supervision module that encourages the model to produce outputs consistent with the scene's geometric evolution, thereby improving the performance and robustness of the policy. Notably, ISS Policy achieves state-of-the-art performance on both single-arm manipulation tasks (MetaWorld) and dexterous hand manipulation (Adroit). In real-world experiments, it also demonstrates strong generalization and robustness. Additional ablation studies show that our method scales effectively with both data and parameters. Code and videos will be released.

