---
layout: default
title: GraspLDP: Towards Generalizable Grasping Policy via Latent Diffusion
---

# GraspLDP: Towards Generalizable Grasping Policy via Latent Diffusion
**arXiv**：[2602.22862v1](https://arxiv.org/abs/2602.22862) · [PDF](https://arxiv.org/pdf/2602.22862.pdf)  
**作者**：Enda Xiang, Haoxiang Ma, Xinzhu Ma, Zicheng Liu, Di Huang  

**一句话要点**：提出GraspLDP，通过潜在扩散策略结合抓取先验知识，提升模仿学习抓取策略的精度与泛化能力。

**关键词**：机器人抓取, 扩散策略, 模仿学习, 潜在扩散, 抓取先验, 泛化能力

## 3 点简述
- 核心问题：模仿学习抓取策略存在执行不精确、空间泛化有限和物体泛化差的问题。
- 方法要点：采用潜在扩散策略，结合抓取姿态先验指导动作解码，并引入自监督重建目标嵌入抓取性先验。
- 实验或效果：仿真与真实机器人实验显示，方法显著优于基线，展现出强动态抓取能力。

## 摘要（原文）

> This paper focuses on enhancing the grasping precision and generalization of manipulation policies learned via imitation learning. Diffusion-based policy learning methods have recently become the mainstream approach for robotic manipulation tasks. As grasping is a critical subtask in manipulation, the ability of imitation-learned policies to execute precise and generalizable grasps merits particular attention. Existing imitation learning techniques for grasping often suffer from imprecise grasp executions, limited spatial generalization, and poor object generalization. To address these challenges, we incorporate grasp prior knowledge into the diffusion policy framework. In particular, we employ a latent diffusion policy to guide action chunk decoding with grasp pose prior, ensuring that generated motion trajectories adhere closely to feasible grasp configurations. Furthermore, we introduce a self-supervised reconstruction objective during diffusion to embed the graspness prior: at each reverse diffusion step, we reconstruct wrist-camera images back-projected the graspness from the intermediate representations. Both simulation and real robot experiments demonstrate that our approach significantly outperforms baseline methods and exhibits strong dynamic grasping capabilities.

