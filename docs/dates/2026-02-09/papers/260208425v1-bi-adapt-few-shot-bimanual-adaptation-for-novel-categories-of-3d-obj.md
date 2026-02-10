---
layout: default
title: Bi-Adapt: Few-shot Bimanual Adaptation for Novel Categories of 3D Objects via Semantic Correspondence
---

# Bi-Adapt: Few-shot Bimanual Adaptation for Novel Categories of 3D Objects via Semantic Correspondence
**arXiv**：[2602.08425v1](https://arxiv.org/abs/2602.08425) · [PDF](https://arxiv.org/pdf/2602.08425.pdf)  
**作者**：Jinxian Zhou, Ruihai Wu, Yiwei Liu, Yiwen Hou, Xunzhe Zhou, Checheng Yu, Licheng Zhong, Lin Shao  

**一句话要点**：提出Bi-Adapt框架，通过语义对应实现少样本双手机器人操作对新类别3D物体的高效泛化。

**关键词**：双手机器人操作, 少样本学习, 语义对应, 3D物体泛化, 视觉基础模型

## 3 点简述
- 核心问题：双手机器人操作依赖大量数据训练，难以高效泛化到未见的新类别物体。
- 方法要点：利用视觉基础模型进行跨类别功能映射，通过少量数据微调实现零样本泛化。
- 实验或效果：在仿真和真实环境中验证有效性，以有限数据在新类别任务中达到高成功率。

## 摘要（原文）

> Bimanual manipulation is imperative yet challenging for robots to execute complex tasks, requiring coordinated collaboration between two arms. However, existing methods for bimanual manipulation often rely on costly data collection and training, struggling to generalize to unseen objects in novel categories efficiently. In this paper, we present Bi-Adapt, a novel framework designed for efficient generalization for bimanual manipulation via semantic correspondence. Bi-Adapt achieves cross-category affordance mapping by leveraging the strong capability of vision foundation models. Fine-tuning with restricted data on novel categories, Bi-Adapt exhibits notable generalization to out-of-category objects in a zero-shot manner. Extensive experiments conducted in both simulation and real-world environments validate the effectiveness of our approach and demonstrate its high efficiency, achieving a high success rate on different benchmark tasks across novel categories with limited data. Project website: https://biadapt-project.github.io/

