---
layout: default
title: LeRobot: An Open-Source Library for End-to-End Robot Learning
---

# LeRobot: An Open-Source Library for End-to-End Robot Learning
**arXiv**：[2602.22818v1](https://arxiv.org/abs/2602.22818) · [PDF](https://arxiv.org/pdf/2602.22818.pdf)  
**作者**：Remi Cadene, Simon Aliberts, Francesco Capuano, Michel Aractingi, Adil Zouitine, Pepijn Kooijmans, Jade Choghari, Martino Russi, Caroline Pascal, Steven Palma, Mustafa Shukor, Jess Moss, Alexander Soare, Dana Aubakirova, Quentin Lhoest, Quentin Gallouédec, Thomas Wolf  

**一句话要点**：提出LeRobot开源库以整合机器人学习全栈，降低研究门槛并支持可扩展学习。

**关键词**：机器人学习, 开源库, 端到端集成, 可扩展学习, 数据集处理, 异步推理

## 3 点简述
- 核心问题：机器人学习领域因工具碎片化和闭源而发展缓慢，缺乏端到端解决方案。
- 方法要点：集成从底层电机控制到大规模数据集处理的完整栈，支持多种硬件平台和先进算法。
- 实验或效果：强调可扩展学习，通过更多数据和计算直接提升性能，促进可复现的先进研究。

## 摘要（原文）

> Robotics is undergoing a significant transformation powered by advances in high-level control techniques based on machine learning, giving rise to the field of robot learning. Recent progress in robot learning has been accelerated by the increasing availability of affordable teleoperation systems, large-scale openly available datasets, and scalable learning-based methods. However, development in the field of robot learning is often slowed by fragmented, closed-source tools designed to only address specific sub-components within the robotics stack. In this paper, we present \texttt{lerobot}, an open-source library that integrates across the entire robot learning stack, from low-level middleware communication for motor controls to large-scale dataset collection, storage and streaming. The library is designed with a strong focus on real-world robotics, supporting accessible hardware platforms while remaining extensible to new embodiments. It also supports efficient implementations for various state-of-the-art robot learning algorithms from multiple prominent paradigms, as well as a generalized asynchronous inference stack. Unlike traditional pipelines which heavily rely on hand-crafted techniques, \texttt{lerobot} emphasizes scalable learning approaches that improve directly with more data and compute. Designed for accessibility, scalability, and openness, \texttt{lerobot} lowers the barrier to entry for researchers and practitioners to robotics while providing a platform for reproducible, state-of-the-art robot learning.

