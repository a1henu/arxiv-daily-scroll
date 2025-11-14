---
layout: default
title: Physics-informed Machine Learning for Static Friction Modeling in Robotic Manipulators Based on Kolmogorov-Arnold Networks
---

# Physics-informed Machine Learning for Static Friction Modeling in Robotic Manipulators Based on Kolmogorov-Arnold Networks
**arXiv**：[2511.10079v1](https://arxiv.org/abs/2511.10079) · [PDF](https://arxiv.org/pdf/2511.10079.pdf)  
**作者**：Yizheng Wang, Timon Rabczuk, Yinghua Liu  

**一句话要点**：提出基于KAN的物理启发机器学习方法，用于机器人关节静态摩擦建模。

**关键词**：静态摩擦建模, Kolmogorov-Arnold网络, 物理启发机器学习, 符号回归, 机器人控制

## 3 点简述
- 传统静态摩擦模型需预设函数形式，难以处理未知结构。
- 方法结合样条激活与符号回归，实现高精度与可解释性。
- 实验在合成和真实数据上验证，决定系数大于0.95。

## 摘要（原文）

> Friction modeling plays a crucial role in achieving high-precision motion control in robotic operating systems. Traditional static friction models (such as the Stribeck model) are widely used due to their simple forms; however, they typically require predefined functional assumptions, which poses significant challenges when dealing with unknown functional structures. To address this issue, this paper proposes a physics-inspired machine learning approach based on the Kolmogorov Arnold Network (KAN) for static friction modeling of robotic joints. The method integrates spline activation functions with a symbolic regression mechanism, enabling model simplification and physical expression extraction through pruning and attribute scoring, while maintaining both high prediction accuracy and interpretability. We first validate the method's capability to accurately identify key parameters under known functional models, and further demonstrate its robustness and generalization ability under conditions with unknown functional structures and noisy data. Experiments conducted on both synthetic data and real friction data collected from a six-degree-of-freedom industrial manipulator show that the proposed method achieves a coefficient of determination greater than 0.95 across various tasks and successfully extracts concise and physically meaningful friction expressions. This study provides a new perspective for interpretable and data-driven robotic friction modeling with promising engineering applicability.

