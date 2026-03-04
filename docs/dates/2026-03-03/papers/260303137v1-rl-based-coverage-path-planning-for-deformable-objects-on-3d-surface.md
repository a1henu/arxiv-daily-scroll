---
layout: default
title: RL-Based Coverage Path Planning for Deformable Objects on 3D Surfaces
---

# RL-Based Coverage Path Planning for Deformable Objects on 3D Surfaces
**arXiv**：[2603.03137v1](https://arxiv.org/abs/2603.03137) · [PDF](https://arxiv.org/pdf/2603.03137.pdf)  
**作者**：Yuhang Zhang, Jinming Ma, Feng Wu  

**一句话要点**：提出基于强化学习的覆盖路径规划方法，用于在3D表面上操纵可变形物体执行擦拭任务。

**关键词**：强化学习, 覆盖路径规划, 可变形物体操纵, 3D表面擦拭, 谐波UV映射, SGCNN

## 3 点简述
- 核心问题：可变形物体在接触密集任务（如表面擦拭）中的感知与精确操纵挑战，现有算法存在遮挡等问题。
- 方法要点：在模拟器中训练强化学习代理，使用谐波UV映射简化状态表示，处理接触反馈并采用SGCNN高效提取特征。
- 实验或效果：方法在路径长度和覆盖面积上优于先前方法，并在Kinova Gen3机械臂上验证了可行性。

## 摘要（原文）

> Currently, manipulation tasks for deformable objects often focus on activities like folding clothes, handling ropes, and manipulating bags. However, research on contact-rich tasks involving deformable objects remains relatively underdeveloped. When humans use cloth or sponges to wipe surfaces, they rely on both vision and tactile feedback. Yet, current algorithms still face challenges with issues like occlusion, while research on tactile perception for manipulation is still evolving. Tasks such as covering surfaces with deformable objects demand not only perception but also precise robotic manipulation. To address this, we propose a method that leverages efficient and accessible simulators for task execution. Specifically, we train a reinforcement learning agent in a simulator to manipulate deformable objects for surface wiping tasks. We simplify the state representation of object surfaces using harmonic UV mapping, process contact feedback from the simulator on 2D feature maps, and use scaled grouped convolutions (SGCNN) to extract features efficiently. The agent then outputs actions in a reduced-dimensional action space to generate coverage paths. Experiments demonstrate that our method outperforms previous approaches in key metrics, including total path length and coverage area. We deploy these paths on a Kinova Gen3 manipulator to perform wiping experiments on the back of a torso model, validating the feasibility of our approach.

