---
layout: default
title: Sceniris: A Fast Procedural Scene Generation Framework
---

# Sceniris: A Fast Procedural Scene Generation Framework
**arXiv**：[2512.16896v1](https://arxiv.org/abs/2512.16896) · [PDF](https://arxiv.org/pdf/2512.16896.pdf)  
**作者**：Jinghuan Shang, Harsh Patel, Ran Gong, Karl Schmeckpeper  

**一句话要点**：提出Sceniris框架以高效生成大规模无碰撞合成3D场景

**关键词**：程序化场景生成, 合成3D场景, 碰撞检测, 机器人操作, 数据集创建, 物理AI

## 3 点简述
- 现有程序化生成方法输出吞吐量低，阻碍数据集规模化创建
- Sceniris通过批量采样和cuRobo快速碰撞检查，实现至少234倍加速
- 支持对象级空间关系扩展和可选机器人可达性检查，提升场景多样性

## 摘要（原文）

> Synthetic 3D scenes are essential for developing Physical AI and generative models. Existing procedural generation methods often have low output throughput, creating a significant bottleneck in scaling up dataset creation. In this work, we introduce Sceniris, a highly efficient procedural scene generation framework for rapidly generating large-scale, collision-free scene variations. Sceniris also provides an optional robot reachability check, providing manipulation-feasible scenes for robot tasks. Sceniris is designed for maximum efficiency by addressing the primary performance limitations of the prior method, Scene Synthesizer. Leveraging batch sampling and faster collision checking in cuRobo, Sceniris achieves at least 234x speed-up over Scene Synthesizer. Sceniris also expands the object-wise spatial relationships available in prior work to support diverse scene requirements. Our code is available at https://github.com/rai-inst/sceniris

