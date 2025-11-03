---
layout: default
title: HyperClick: Advancing Reliable GUI Grounding via Uncertainty Calibration
---

# HyperClick: Advancing Reliable GUI Grounding via Uncertainty Calibration
**arXiv**：[2510.27266v1](https://arxiv.org/abs/2510.27266) · [PDF](https://arxiv.org/pdf/2510.27266.pdf)  
**作者**：Shaojie Zhang, Pei Fu, Ruoceng Zhang, Jiahui Yang, Anan Du, Xiuwen Xi, Shaokang Wang, Ying Huang, Bin Qin, Zhenbo Luo, Jian Luan  

**一句话要点**：提出HyperClick框架，通过不确定性校准提升GUI自动化中的可靠定位。

**关键词**：GUI定位, 不确定性校准, 强化微调, 置信建模, 自动化代理

## 3 点简述
- GUI代理在语言指令到屏幕坐标的定位中缺乏能力边界意识，导致过度自信和不可靠预测。
- 引入双奖励机制，结合二元奖励和高斯空间置信建模，使用Brier分数进行校准。
- 在七个挑战基准上实现最优性能，提供良好校准的置信度，减少过度自信。

## 摘要（原文）

> Autonomous Graphical User Interface (GUI) agents rely on accurate GUI
> grounding, which maps language instructions to on-screen coordinates, to
> execute user commands. However, current models, whether trained via supervised
> fine-tuning (SFT) or reinforcement fine-tuning (RFT), lack self-awareness of
> their capability boundaries, leading to overconfidence and unreliable
> predictions. We first systematically evaluate probabilistic and verbalized
> confidence in general and GUI-specific models, revealing a misalignment between
> confidence and actual accuracy, which is particularly critical in dynamic GUI
> automation tasks, where single errors can cause task failure. To address this,
> we propose HyperClick, a novel framework that enhances reliable GUI grounding
> through uncertainty calibration. HyperClick introduces a dual reward mechanism,
> combining a binary reward for correct actions with a truncated Gaussian-based
> spatial confidence modeling, calibrated using the Brier score. This approach
> jointly optimizes grounding accuracy and confidence reliability, fostering
> introspective self-criticism. Extensive experiments on seven challenge
> benchmarks show that HyperClick achieves state-of-the-art performance while
> providing well-calibrated confidence. By enabling explicit confidence
> calibration and introspective self-criticism, HyperClick reduces overconfidence
> and supports more reliable GUI automation.

