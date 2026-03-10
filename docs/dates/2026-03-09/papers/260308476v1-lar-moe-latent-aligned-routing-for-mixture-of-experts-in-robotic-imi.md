---
layout: default
title: LAR-MoE: Latent-Aligned Routing for Mixture of Experts in Robotic Imitation Learning
---

# LAR-MoE: Latent-Aligned Routing for Mixture of Experts in Robotic Imitation Learning
**arXiv**：[2603.08476v1](https://arxiv.org/abs/2603.08476) · [PDF](https://arxiv.org/pdf/2603.08476.pdf)  
**作者**：Ariel Rodriguez, Chenpan Li, Lorenzo Mazza, Rayan Younis, Ortrun Hellig, Sebastian Bodenstedt, Martin Wagner, Stefanie Speidel  

**一句话要点**：提出LAR-MoE框架，通过潜在对齐路由解决机器人模仿学习中异构动态任务的专家混合模型技能分解问题。

**关键词**：机器人模仿学习, 专家混合模型, 潜在对齐路由, 技能分解, 无监督学习, 异构动态任务

## 3 点简述
- 核心问题：机器人模仿学习在异构动态任务中，模型易平均化演示中的不同行为模式，导致性能下降。
- 方法要点：采用两阶段框架，先通过师生协同训练学习观测与未来动作的联合潜在表示，再正则化专家路由以对齐潜在空间结构。
- 实验或效果：在LIBERO基准上达到95.2%平均成功率，在手术任务中无需阶段标注匹配监督基线，并零样本迁移至离体组织。

## 摘要（原文）

> Imitation learning enables robots to acquire manipulation skills from demonstrations, yet deploying a policy across tasks with heterogeneous dynamics remains challenging, as models tend to average over distinct behavioral modes present in the demonstrations. Mixture-of-Experts (MoE) architectures address this by activating specialized subnetworks, but requires meaningful skill decompositions for expert routing. We introduce Latent-Aligned Routing for Mixture of Experts (LAR-MoE), a two-stage framework that decouples unsupervised skill discovery from policy learning. In pre-training, we learn a joint latent representation between observations and future actions through student-teacher co-training. In a post-training stage, the expert routing is regularized to follow the structure of the learned latent space, preventing expert collapse while maintaining parameter efficiency. We evaluate LAR-MoE in simulation and on hardware. On the LIBERO benchmark, our method achieves a 95.2% average success rate with 150M parameters. On a surgical bowel grasping and retraction task, LAR-MoE matches a supervised MoE baseline without requiring any phase annotations, and transfers zero-shot to ex vivo porcine tissue. Our findings suggest that latent-aligned routing provides a principled alternative to supervised skill decomposition, enabling structured expert specialization from unlabeled demonstrations.

