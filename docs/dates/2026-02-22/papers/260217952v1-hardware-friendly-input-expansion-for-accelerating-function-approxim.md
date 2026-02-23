---
layout: default
title: Hardware-Friendly Input Expansion for Accelerating Function Approximation
---

# Hardware-Friendly Input Expansion for Accelerating Function Approximation
**arXiv**：[2602.17952v1](https://arxiv.org/abs/2602.17952) · [PDF](https://arxiv.org/pdf/2602.17952.pdf)  
**作者**：Hu Lou, Yin-Jun Gao, Dong-Xiao Zhang, Tai-Jiao Du, Jun-Jie Zhang, Jia-Rui Zhang  

**一句话要点**：提出硬件友好的输入扩展方法以加速一维函数逼近，通过打破参数对称性提升训练效率与精度。

**关键词**：函数逼近, 输入扩展, 对称性打破, 硬件友好, 训练加速, 神经网络优化

## 3 点简述
- 核心问题：神经网络逼近一维函数时，参数对称性导致损失景观平坦，收敛慢且泛化差，尤其对高频分量。
- 方法要点：通过向一维输入添加常数（如π）扩展为高维向量，打破对称性而不增加网络参数，硬件友好。
- 实验或效果：在十类函数上测试，最优5D扩展平均减少12% LBFGS迭代，最终MSE降低66.3%，π常数表现最佳。

## 摘要（原文）

> One-dimensional function approximation is a fundamental problem in scientific computing and engineering applications. While neural networks possess powerful universal approximation capabilities, their optimization process is often hindered by flat loss landscapes induced by parameter-space symmetries, leading to slow convergence and poor generalization, particularly for high-frequency components. Inspired by the principle of \emph{symmetry breaking} in physics, this paper proposes a hardware-friendly approach for function approximation through \emph{input-space expansion}. The core idea involves augmenting the original one-dimensional input (e.g., $x$) with constant values (e.g., $π$) to form a higher-dimensional vector (e.g., $[π, π, x, π, π]$), effectively breaking parameter symmetries without increasing the network's parameter count. We evaluate the method on ten representative one-dimensional functions, including smooth, discontinuous, high-frequency, and non-differentiable functions. Experimental results demonstrate that input-space expansion significantly accelerates training convergence (reducing LBFGS iterations by 12\% on average) and enhances approximation accuracy (reducing final MSE by 66.3\% for the optimal 5D expansion). Ablation studies further reveal the effects of different expansion dimensions and constant selections, with $π$ consistently outperforming other constants. Our work proposes a low-cost, efficient, and hardware-friendly technique for algorithm design.

