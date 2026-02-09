---
layout: default
title: DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos
---

# DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos
**arXiv**：[2602.06949v1](https://arxiv.org/abs/2602.06949) · [PDF](https://arxiv.org/pdf/2602.06949.pdf)  
**作者**：Shenyuan Gao, William Liang, Kaiyuan Zheng, Ayaan Malik, Seonghyeon Ye, Sihyun Yu, Wei-Cheng Tseng, Yuzhu Dong, Kaichun Mo, Chen-Hsuan Lin, Qianli Ma, Seungjun Nah, Loic Magne, Jiannan Xiang, Yuqi Xie, Ruijie Zheng, Dantong Niu, You Liang Tan, K. R. Zentner, George Kurian, Suneel Indupuru, Pooya Jannaty, Jinwei Gu, Jun Zhang, Jitendra Malik, Pieter Abbeel, Ming-Yu Liu, Yuke Zhu, Joel Jang, Linxi "Jim" Fan  

**一句话要点**：提出DreamDojo通用机器人世界模型，利用大规模人类视频学习交互与控制

**关键词**：世界模型, 大规模视频学习, 连续潜在动作, 机器人控制, 蒸馏加速, 开放世界任务

## 3 点简述
- 核心问题：机器人世界建模面临数据覆盖有限和动作标签稀缺的挑战
- 方法要点：从44k小时人类视频学习，引入连续潜在动作作为统一代理动作
- 实验或效果：在OOD基准上验证了物理理解和动作可控性，支持实时应用

## 摘要（原文）

> Being able to simulate the outcomes of actions in varied environments will revolutionize the development of generalist agents at scale. However, modeling these world dynamics, especially for dexterous robotics tasks, poses significant challenges due to limited data coverage and scarce action labels. As an endeavor towards this end, we introduce DreamDojo, a foundation world model that learns diverse interactions and dexterous controls from 44k hours of egocentric human videos. Our data mixture represents the largest video dataset to date for world model pretraining, spanning a wide range of daily scenarios with diverse objects and skills. To address the scarcity of action labels, we introduce continuous latent actions as unified proxy actions, enhancing interaction knowledge transfer from unlabeled videos. After post-training on small-scale target robot data, DreamDojo demonstrates a strong understanding of physics and precise action controllability. We also devise a distillation pipeline that accelerates DreamDojo to a real-time speed of 10.81 FPS and further improves context consistency. Our work enables several important applications based on generative world models, including live teleoperation, policy evaluation, and model-based planning. Systematic evaluation on multiple challenging out-of-distribution (OOD) benchmarks verifies the significance of our method for simulating open-world, contact-rich tasks, paving the way for general-purpose robot world models.

