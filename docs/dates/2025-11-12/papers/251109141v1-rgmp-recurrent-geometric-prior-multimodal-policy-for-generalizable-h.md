---
layout: default
title: RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation
---

# RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation
**arXiv**：[2511.09141v1](https://arxiv.org/abs/2511.09141) · [PDF](https://arxiv.org/pdf/2511.09141.pdf)  
**作者**：Xuetao Li, Wenke Huang, Nengyuan Pan, Kaiyan Zhao, Songhua Yang, Yiming Wang, Mengde Li, Mang Ye, Jifeng Xuan, Miao Li  

**一句话要点**：提出RGMP框架以解决人形机器人泛化操作中的数据效率与几何推理问题

**关键词**：人形机器人操作, 几何语义推理, 数据高效控制, 递归高斯网络, 技能选择器, 泛化性能

## 3 点简述
- 核心问题：数据驱动方法在未见场景中忽视几何推理，导致训练资源浪费和泛化能力不足
- 方法要点：结合几何先验技能选择器和自适应递归高斯网络，实现端到端几何语义推理与数据高效控制
- 实验或效果：在泛化测试中任务成功率87%，数据效率比现有最优模型高5倍

## 摘要（原文）

> Humanoid robots exhibit significant potential in executing diverse human-level skills. However, current research predominantly relies on data-driven approaches that necessitate extensive training datasets to achieve robust multimodal decision-making capabilities and generalizable visuomotor control. These methods raise concerns due to the neglect of geometric reasoning in unseen scenarios and the inefficient modeling of robot-target relationships within the training data, resulting in significant waste of training resources. To address these limitations, we present the Recurrent Geometric-prior Multimodal Policy (RGMP), an end-to-end framework that unifies geometric-semantic skill reasoning with data-efficient visuomotor control. For perception capabilities, we propose the Geometric-prior Skill Selector, which infuses geometric inductive biases into a vision language model, producing adaptive skill sequences for unseen scenes with minimal spatial common sense tuning. To achieve data-efficient robotic motion synthesis, we introduce the Adaptive Recursive Gaussian Network, which parameterizes robot-object interactions as a compact hierarchy of Gaussian processes that recursively encode multi-scale spatial relationships, yielding dexterous, data-efficient motion synthesis even from sparse demonstrations. Evaluated on both our humanoid robot and desktop dual-arm robot, the RGMP framework achieves 87% task success in generalization tests and exhibits 5x greater data efficiency than the state-of-the-art model. This performance underscores its superior cross-domain generalization, enabled by geometric-semantic reasoning and recursive-Gaussion adaptation.

