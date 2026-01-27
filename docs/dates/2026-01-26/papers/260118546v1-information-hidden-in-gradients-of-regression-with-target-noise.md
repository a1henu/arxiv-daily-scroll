---
layout: default
title: Information Hidden in Gradients of Regression with Target Noise
---

# Information Hidden in Gradients of Regression with Target Noise
**arXiv**：[2601.18546v1](https://arxiv.org/abs/2601.18546) · [PDF](https://arxiv.org/pdf/2601.18546.pdf)  
**作者**：Arash Jamshidi, Katsiaryna Haitsiukevich, Kai Puolamäki  

**一句话要点**：提出目标噪声方差校准方法，仅利用梯度恢复Hessian以支持优化与诊断

**关键词**：梯度分析, 二阶信息恢复, 线性回归, 优化加速, 鲁棒性诊断, 分布式训练

## 3 点简述
- 核心问题：仅观测梯度时，如何恢复二阶信息如Hessian以用于优化和鲁棒性分析
- 方法要点：注入高斯噪声使总目标噪声方差等于批次大小，确保梯度协方差近似Hessian
- 实验或效果：理论保证在亚高斯输入下成立，实验验证在合成和真实数据上的有效性

## 摘要（原文）

> Second-order information -- such as curvature or data covariance -- is critical for optimisation, diagnostics, and robustness. However, in many modern settings, only the gradients are observable. We show that the gradients alone can reveal the Hessian, equalling the data covariance $Σ$ for the linear regression. Our key insight is a simple variance calibration: injecting Gaussian noise so that the total target noise variance equals the batch size ensures that the empirical gradient covariance closely approximates the Hessian, even when evaluated far from the optimum. We provide non-asymptotic operator-norm guarantees under sub-Gaussian inputs. We also show that without such calibration, recovery can fail by an $Ω(1)$ factor. The proposed method is practical (a "set target-noise variance to $n$" rule) and robust (variance $\mathcal{O}(n)$ suffices to recover $Σ$ up to scale). Applications include preconditioning for faster optimisation, adversarial risk estimation, and gradient-only training, for example, in distributed systems. We support our theoretical results with experiments on synthetic and real data.

