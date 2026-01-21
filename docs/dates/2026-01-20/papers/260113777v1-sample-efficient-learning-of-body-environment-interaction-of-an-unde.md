---
layout: default
title: Sample Efficient Learning of Body-Environment Interaction of an Under-Actuated System
---

# Sample Efficient Learning of Body-Environment Interaction of an Under-Actuated System
**arXiv**：[2601.13777v1](https://arxiv.org/abs/2601.13777) · [PDF](https://arxiv.org/pdf/2601.13777.pdf)  
**作者**：Zvi Chapnik, Yizhar Or, Shai Revzen  

**一句话要点**：比较学习方法以高效学习欠驱动系统在环境中的运动映射

**关键词**：几何力学, 欠驱动系统, 运动映射学习, 数据效率, 机器人运动学, 环境交互

## 3 点简述
- 核心问题：如何从运动跟踪数据中学习欠驱动系统在环境中的运动映射，以预测身体速度。
- 方法要点：比较四种建模方法，评估它们在相同步态、跨步态和跨速度下的预测能力。
- 实验或效果：发现简单方法在小数据集上更优，复杂方法在大数据集上更优，存在权衡。

## 摘要（原文）

> Geometric mechanics provides valuable insights into how biological and robotic systems use changes in shape to move by mechanically interacting with their environment. In high-friction environments it provides that the entire interaction is captured by the ``motility map''. Here we compare methods for learning the motility map from motion tracking data of a physical robot created specifically to test these methods by having under-actuated degrees of freedom and a hard to model interaction with its substrate. We compared four modeling approaches in terms of their ability to predict body velocity from shape change within the same gait, across gaits, and across speeds. Our results show a trade-off between simpler methods which are superior on small training datasets, and more sophisticated methods, which are superior when more training data is available.

