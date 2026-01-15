---
layout: default
title: Vision-Conditioned Variational Bayesian Last Layer Dynamics Models
---

# Vision-Conditioned Variational Bayesian Last Layer Dynamics Models
**arXiv**：[2601.09178v1](https://arxiv.org/abs/2601.09178) · [PDF](https://arxiv.org/pdf/2601.09178.pdf)  
**作者**：Paul Brunzema, Thomas Lew, Ray Zhang, Takeru Shirasawa, John Subosits, Marcus Greiff  

**一句话要点**：提出视觉条件变分贝叶斯末层动力学模型以解决自动驾驶赛车在快速变化环境中的前瞻性适应问题。

**关键词**：视觉条件动力学模型, 变分贝叶斯学习, 自动驾驶赛车, 环境适应, 最优控制, 车辆动力学预测

## 3 点简述
- 核心问题：传统方法难以捕捉系统行为的突变，自适应方法反应滞后，影响自动驾驶赛车在变化环境中的安全控制。
- 方法要点：模型学习名义车辆动力学，通过视觉上下文微调潜在特征的仿射变换，实现上下文感知的动力学预测。
- 实验或效果：在Lexus LC500赛车涉水实验中，视觉条件模型完成所有12圈，无视觉上下文的基线均失控，验证了前瞻性适应的重要性。

## 摘要（原文）

> Agile control of robotic systems often requires anticipating how the environment affects system behavior. For example, a driver must perceive the road ahead to anticipate available friction and plan actions accordingly. Achieving such proactive adaptation within autonomous frameworks remains a challenge, particularly under rapidly changing conditions. Traditional modeling approaches often struggle to capture abrupt variations in system behavior, while adaptive methods are inherently reactive and may adapt too late to ensure safety. We propose a vision-conditioned variational Bayesian last-layer dynamics model that leverages visual context to anticipate changes in the environment. The model first learns nominal vehicle dynamics and is then fine-tuned with feature-wise affine transformations of latent features, enabling context-aware dynamics prediction. The resulting model is integrated into an optimal controller for vehicle racing. We validate our method on a Lexus LC500 racing through water puddles. With vision-conditioning, the system completed all 12 attempted laps under varying conditions. In contrast, all baselines without visual context consistently lost control, demonstrating the importance of proactive dynamics adaptation in high-performance applications.

