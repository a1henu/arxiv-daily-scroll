---
layout: default
title: PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies
---

# PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies
**arXiv**：[2512.16881v1](https://arxiv.org/abs/2512.16881) · [PDF](https://arxiv.org/pdf/2512.16881.pdf)  
**作者**：Arhan Jain, Mingtong Zhang, Kanav Arora, William Chen, Marcel Torne, Muhammad Zubair Irshad, Sergey Zakharov, Yue Wang, Sergey Levine, Chelsea Finn, Wei-Chiu Ma, Dhruv Shah, Abhishek Gupta, Karl Pertsch  

**一句话要点**：提出PolaRiS框架，通过神经重建与协同训练实现机器人策略的高保真仿真评估。

**关键词**：机器人策略评估, 神经重建, 仿真环境, 协同训练, 零样本评估, 高保真仿真

## 3 点简述
- 核心问题：机器人策略评估面临真实世界实验的随机性、耗时性及仿真与现实的视觉物理差距。
- 方法要点：利用神经重建将真实场景视频转换为交互式仿真环境，并开发协同训练方法弥合剩余差距。
- 实验或效果：通过配对评估，PolaRiS仿真结果与真实世界性能相关性显著优于现有基准，支持快速创建多样环境。

## 摘要（原文）

> A significant challenge for robot learning research is our ability to accurately measure and compare the performance of robot policies. Benchmarking in robotics is historically challenging due to the stochasticity, reproducibility, and time-consuming nature of real-world rollouts. This challenge is exacerbated for recent generalist policies, which has to be evaluated across a wide variety of scenes and tasks. Evaluation in simulation offers a scalable complement to real world evaluations, but the visual and physical domain gap between existing simulation benchmarks and the real world has made them an unreliable signal for policy improvement. Furthermore, building realistic and diverse simulated environments has traditionally required significant human effort and expertise. To bridge the gap, we introduce Policy Evaluation and Environment Reconstruction in Simulation (PolaRiS), a scalable real-to-sim framework for high-fidelity simulated robot evaluation. PolaRiS utilizes neural reconstruction methods to turn short video scans of real-world scenes into interactive simulation environments. Additionally, we develop a simple simulation data co-training recipe that bridges remaining real-to-sim gaps and enables zero-shot evaluation in unseen simulation environments. Through extensive paired evaluations between simulation and the real world, we demonstrate that PolaRiS evaluations provide a much stronger correlation to real world generalist policy performance than existing simulated benchmarks. Its simplicity also enables rapid creation of diverse simulated environments. As such, this work takes a step towards distributed and democratized evaluation for the next generation of robotic foundation models.

