---
layout: default
title: A Geometric Probe of the Accuracy-Robustness Trade-off: Sharp Boundaries in Symmetry-Breaking Dimensional Expansion
---

# A Geometric Probe of the Accuracy-Robustness Trade-off: Sharp Boundaries in Symmetry-Breaking Dimensional Expansion
**arXiv**：[2602.17948v1](https://arxiv.org/abs/2602.17948) · [PDF](https://arxiv.org/pdf/2602.17948.pdf)  
**作者**：Yu Bai, Zhe Wang, Jiarui Zhang, Dong-Xiao Zhang, Yinjun Gao, Jun-Jie Zhang  

**一句话要点**：提出对称破缺维度扩展作为几何探针，揭示深度学习精度与鲁棒性权衡的尖锐边界机制

**关键词**：精度鲁棒性权衡, 对称破缺维度扩展, 几何解释, 对抗攻击, 深度学习优化

## 3 点简述
- 核心问题：深度学习精度与对抗鲁棒性权衡的几何起源未知
- 方法要点：通过插入常量像素扩展输入维度，打破平移对称性以提升精度
- 实验或效果：在CIFAR-10上精度提升，但对抗攻击鲁棒性下降，掩码投影可恢复鲁棒性

## 摘要（原文）

> The trade-off between clean accuracy and adversarial robustness is a pervasive phenomenon in deep learning, yet its geometric origin remains elusive. In this work, we utilize Symmetry-Breaking Dimensional Expansion (SBDE) as a controlled probe to investigate the mechanism underlying this trade-off. SBDE expands input images by inserting constant-valued pixels, which breaks translational symmetry and consistently improves clean accuracy (e.g., from $90.47\%$ to $95.63\%$ on CIFAR-10 with ResNet-18) by reducing parameter degeneracy. However, this accuracy gain comes at the cost of reduced robustness against iterative white-box attacks. By employing a test-time \emph{mask projection} that resets the inserted auxiliary pixels to their training values, we demonstrate that the vulnerability stems almost entirely from the inserted dimensions. The projection effectively neutralizes the attacks and restores robustness, revealing that the model achieves high accuracy by creating \emph{sharp boundaries} (steep loss gradients) specifically along the auxiliary axes. Our findings provide a concrete geometric explanation for the accuracy-robustness paradox: the optimization landscape deepens the basin of attraction to improve accuracy but inevitably erects steep walls along the auxiliary degrees of freedom, creating a fragile sensitivity to off-manifold perturbations.

