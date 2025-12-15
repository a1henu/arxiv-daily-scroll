---
layout: default
title: A General Algorithm for Detecting Higher-Order Interactions via Random Sequential Additions
---

# A General Algorithm for Detecting Higher-Order Interactions via Random Sequential Additions
**arXiv**：[2512.11793v1](https://arxiv.org/abs/2512.11793) · [PDF](https://arxiv.org/pdf/2512.11793.pdf)  
**作者**：Ahmad Shamail, Claire McWhite  

**一句话要点**：提出基于随机顺序添加的几何方法，以检测特征间的高阶交互与冗余

**关键词**：交互检测, 几何方法, 高阶交互, 冗余分析, 随机顺序添加, L分数

## 3 点简述
- 核心问题：系统组件间存在复杂交互，如协同、冗余或独立，需量化检测
- 方法要点：通过随机顺序添加元素并绘制贡献图，利用L形模式量化交互结构
- 实验或效果：定义L分数从-1到+1连续度量交互，适用于任何可增量评估性能的领域

## 摘要（原文）

> Many systems exhibit complex interactions between their components: some features or actions amplify each other's effects, others provide redundant information, and some contribute independently. We present a simple geometric method for discovering interactions and redundancies: when elements are added in random sequential orders and their contributions plotted over many trials, characteristic L-shaped patterns emerge that directly reflect interaction structure. The approach quantifies how the contribution of each element depends on those added before it, revealing patterns that distinguish interaction, independence, and redundancy on a unified scale. When pairwise contributions are visualized as two--dimensional point clouds, redundant pairs form L--shaped patterns where only the first-added element contributes, while synergistic pairs form L--shaped patterns where only elements contribute together. Independent elements show order--invariant distributions. We formalize this with the L--score, a continuous measure ranging from $-1$ (perfect synergy, e.g. $Y=X_1X_2$) to $0$ (independence) to $+1$ (perfect redundancy, $X_1 \approx X_2$). The relative scaling of the L--shaped arms reveals feature dominance in which element consistently provides more information. Although computed only from pairwise measurements, higher--order interactions among three or more elements emerge naturally through consistent cross--pair relationships (e.g. AB, AC, BC). The method is metric--agnostic and broadly applicable to any domain where performance can be evaluated incrementally over non-repeating element sequences, providing a unified geometric approach to uncovering interaction structure.

