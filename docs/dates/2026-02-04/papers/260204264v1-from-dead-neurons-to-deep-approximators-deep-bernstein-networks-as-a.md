---
layout: default
title: From Dead Neurons to Deep Approximators: Deep Bernstein Networks as a Provable Alternative to Residual Layers
---

# From Dead Neurons to Deep Approximators: Deep Bernstein Networks as a Provable Alternative to Residual Layers
**arXiv**：[2602.04264v1](https://arxiv.org/abs/2602.04264) · [PDF](https://arxiv.org/pdf/2602.04264.pdf)  
**作者**：Ibrahim Albool, Malak Gamal El-Din, Salma Elmalaki, Yasser Shoukry  

**一句话要点**：提出深度伯恩斯坦网络以解决梯度消失和激活函数效率问题，替代残差连接。

**关键词**：深度伯恩斯坦网络, 伯恩斯坦多项式, 梯度消失, 激活函数优化, 残差连接替代, 函数近似理论

## 3 点简述
- 核心问题：残差连接结构受限且无法解决分段线性激活函数的固有低效性。
- 方法要点：使用伯恩斯坦多项式作为激活函数，提供理论下界保证梯度不消失，近似误差随深度指数衰减。
- 实验或效果：在HIGGS和MNIST上验证，死神经元率从90%降至5%，无需跳跃连接实现高性能训练。

## 摘要（原文）

> Residual connections are the de facto standard for mitigating vanishing gradients, yet they impose structural constraints and fail to address the inherent inefficiencies of piecewise linear activations. We show that Deep Bernstein Networks (which utilizes Bernstein polynomials as activation functions) can act as residual-free architecture while simultaneously optimize trainability and representation power. We provide a two-fold theoretical foundation for our approach. First, we derive a theoretical lower bound on the local derivative, proving it remains strictly bounded away from zero. This directly addresses the root cause of gradient stagnation; empirically, our architecture reduces ``dead'' neurons from 90\% in standard deep networks to less than 5\%, outperforming ReLU, Leaky ReLU, SeLU, and GeLU. Second, we establish that the approximation error for Bernstein-based networks decays exponentially with depth, a significant improvement over the polynomial rates of ReLU-based architectures. By unifying these results, we demonstrate that Bernstein activations provide a superior mechanism for function approximation and signal flow. Our experiments on HIGGS and MNIST confirm that Deep Bernstein Networks achieve high-performance training without skip-connections, offering a principled path toward deep, residual-free architectures with enhanced expressive capacity.

