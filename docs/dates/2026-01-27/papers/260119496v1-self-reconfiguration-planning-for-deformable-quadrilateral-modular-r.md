---
layout: default
title: Self-Reconfiguration Planning for Deformable Quadrilateral Modular Robots
---

# Self-Reconfiguration Planning for Deformable Quadrilateral Modular Robots
**arXiv**：[2601.19496v1](https://arxiv.org/abs/2601.19496) · [PDF](https://arxiv.org/pdf/2601.19496.pdf)  
**作者**：Jie Gu, Hongrun Gao, Zhihao Xia, Yirun Sun, Chunxu Tian, Dan Zhang  

**一句话要点**：提出基于依赖反向树的自重配置规划算法，保证变形四边形模块机器人的稳定连接。

**关键词**：模块化自重构机器人, 自重配置规划, 稳定连接, 依赖反向树, 变形四边形模块

## 3 点简述
- 针对模块化自重构机器人，在自重配置中维持稳定连接是物理可行性和部署性的关键问题。
- 方法使用虚拟图表示构建可行连接/断开动作，并通过依赖反向树组织动作序列以解决依赖关系。
- 实验表明算法在效率和稳定性上优于改进的BiRRT算法，并在物理平台上验证了实际可行性。

## 摘要（原文）

> For lattice modular self-reconfigurable robots (MSRRs), maintaining stable connections during reconfiguration is crucial for physical feasibility and deployability. This letter presents a novel self-reconfiguration planning algorithm for deformable quadrilateral MSRRs that guarantees stable connection. The method first constructs feasible connect/disconnect actions using a virtual graph representation, and then organizes these actions into a valid execution sequence through a Dependence-based Reverse Tree (DRTree) that resolves interdependencies. We also prove that reconfiguration sequences satisfying motion characteristics exist for any pair of configurations with seven or more modules (excluding linear topologies). Finally, comparisons with a modified BiRRT algorithm highlight the superior efficiency and stability of our approach, while deployment on a physical robotic platform confirms its practical feasibility.

