---
layout: default
title: Learning Minimal Representations of Fermionic Ground States
---

# Learning Minimal Representations of Fermionic Ground States
**arXiv**：[2512.11767v1](https://arxiv.org/abs/2512.11767) · [PDF](https://arxiv.org/pdf/2512.11767.pdf)  
**作者**：Felix Frohnert, Emiel Koridon, Stefano Polla  

**一句话要点**：提出无监督机器学习框架以发现费米子多体基态的最优压缩表示

**关键词**：量子多体系统, 自编码器, 费米-哈伯德模型, 变分ansatz, 无监督学习, N-可表示性

## 3 点简述
- 核心问题：如何压缩量子多体基态表示，避免N-可表示性问题
- 方法要点：使用自编码器神经网络在费米-哈伯德模型数据上学习最小潜在空间
- 实验或效果：潜在空间维度为L-1时重建质量阈值尖锐，匹配系统内在自由度

## 摘要（原文）

> We introduce an unsupervised machine-learning framework that discovers optimally compressed representations of quantum many-body ground states. Using an autoencoder neural network architecture on data from $L$-site Fermi-Hubbard models, we identify minimal latent spaces with a sharp reconstruction quality threshold at $L-1$ latent dimensions, matching the system's intrinsic degrees of freedom. We demonstrate the use of the trained decoder as a differentiable variational ansatz to minimize energy directly within the latent space. Crucially, this approach circumvents the $N$-representability problem, as the learned manifold implicitly restricts the optimization to physically valid quantum states.

