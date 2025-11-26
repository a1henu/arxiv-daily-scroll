---
layout: default
title: DP-MicroAdam: Private and Frugal Algorithm for Training and Fine-tuning
---

# DP-MicroAdam: Private and Frugal Algorithm for Training and Fine-tuning
**arXiv**：[2511.20509v1](https://arxiv.org/abs/2511.20509) · [PDF](https://arxiv.org/pdf/2511.20509.pdf)  
**作者**：Mihaela Hudişteanu, Edwige Cyffers, Nikita P. Kalinin  

**一句话要点**：提出DP-MicroAdam以改进差分隐私训练的性能与效率

**关键词**：差分隐私优化, 自适应优化器, 内存效率, 稀疏感知训练, 非凸优化收敛

## 3 点简述
- 差分隐私训练依赖DP-SGD，计算成本高且需大量调参
- DP-MicroAdam为内存高效、稀疏感知的自适应优化器
- 在CIFAR-10等基准测试中，性能优于现有方法，收敛稳定

## 摘要（原文）

> Adaptive optimizers are the de facto standard in non-private training as they often enable faster convergence and improved performance. In contrast, differentially private (DP) training is still predominantly performed with DP-SGD, typically requiring extensive compute and hyperparameter tuning. We propose DP-MicroAdam, a memory-efficient and sparsity-aware adaptive DP optimizer. We prove that DP-MicroAdam converges in stochastic non-convex optimization at the optimal $\mathcal{O}(1/\sqrt{T})$ rate, up to privacy-dependent constants. Empirically, DP-MicroAdam outperforms existing adaptive DP optimizers and achieves competitive or superior accuracy compared to DP-SGD across a range of benchmarks, including CIFAR-10, large-scale ImageNet training, and private fine-tuning of pretrained transformers. These results demonstrate that adaptive optimization can improve both performance and stability under differential privacy.

