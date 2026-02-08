---
layout: default
title: Formal Synthesis of Certifiably Robust Neural Lyapunov-Barrier Certificates
---

# Formal Synthesis of Certifiably Robust Neural Lyapunov-Barrier Certificates
**arXiv**：[2602.05311v1](https://arxiv.org/abs/2602.05311) · [PDF](https://arxiv.org/pdf/2602.05311.pdf)  
**作者**：Chengxiao Wang, Haoze Wu, Gagandeep Singh  

**一句话要点**：提出鲁棒神经Lyapunov屏障证书形式化合成方法，以增强动态扰动下深度强化学习控制器的安全性与稳定性验证。

**关键词**：鲁棒性验证, 神经Lyapunov屏障证书, 深度强化学习, 形式化合成, 动态扰动, 安全控制

## 3 点简述
- 现有神经Lyapunov屏障证书方法仅适用于理想无扰动动态，限制了实际应用中的可靠性。
- 基于Lipschitz连续性定义鲁棒条件，通过对抗训练和正则化等目标强制证书在扰动下保持保证。
- 在倒立摆和二维对接环境中验证，显著提升认证鲁棒界和强扰动下的经验成功率。

## 摘要（原文）

> Neural Lyapunov and barrier certificates have recently been used as powerful tools for verifying the safety and stability properties of deep reinforcement learning (RL) controllers. However, existing methods offer guarantees only under fixed ideal unperturbed dynamics, limiting their reliability in real-world applications where dynamics may deviate due to uncertainties. In this work, we study the problem of synthesizing \emph{robust neural Lyapunov barrier certificates} that maintain their guarantees under perturbations in system dynamics. We formally define a robust Lyapunov barrier function and specify sufficient conditions based on Lipschitz continuity that ensure robustness against bounded perturbations. We propose practical training objectives that enforce these conditions via adversarial training, Lipschitz neighborhood bound, and global Lipschitz regularization. We validate our approach in two practically relevant environments, Inverted Pendulum and 2D Docking. The former is a widely studied benchmark, while the latter is a safety-critical task in autonomous systems. We show that our methods significantly improve both certified robustness bounds (up to $4.6$ times) and empirical success rates under strong perturbations (up to $2.4$ times) compared to the baseline. Our results demonstrate effectiveness of training robust neural certificates for safe RL under perturbations in dynamics.

