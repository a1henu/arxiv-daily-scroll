---
layout: default
title: Perturbing the Phase: Analyzing Adversarial Robustness of Complex-Valued Neural Networks
---

# Perturbing the Phase: Analyzing Adversarial Robustness of Complex-Valued Neural Networks
**arXiv**：[2602.06577v1](https://arxiv.org/abs/2602.06577) · [PDF](https://arxiv.org/pdf/2602.06577.pdf)  
**作者**：Florian Eilers, Christof Duhme, Xiaoyi Jiang  

**一句话要点**：提出相位攻击以分析复值神经网络在对抗攻击下的鲁棒性

**关键词**：复值神经网络, 对抗攻击, 相位攻击, 鲁棒性分析, 深度学习安全

## 3 点简述
- 研究复值神经网络在对抗攻击下的鲁棒性，聚焦相位信息
- 设计针对复值输入的相位攻击，并推导复值版本的常见对抗攻击
- 实验显示复值神经网络在某些场景下更鲁棒，但对相位变化敏感

## 摘要（原文）

> Complex-valued neural networks (CVNNs) are rising in popularity for all kinds of applications. To safely use CVNNs in practice, analyzing their robustness against outliers is crucial. One well known technique to understand the behavior of deep neural networks is to investigate their behavior under adversarial attacks, which can be seen as worst case minimal perturbations. We design Phase Attacks, a kind of attack specifically targeting the phase information of complex-valued inputs. Additionally, we derive complex-valued versions of commonly used adversarial attacks. We show that in some scenarios CVNNs are more robust than RVNNs and that both are very susceptible to phase changes with the Phase Attacks decreasing the model performance more, than equally strong regular attacks, which can attack both phase and magnitude.

