---
layout: default
title: Efficient Adversarial Attacks on High-dimensional Offline Bandits
---

# Efficient Adversarial Attacks on High-dimensional Offline Bandits
**arXiv**：[2602.01658v1](https://arxiv.org/abs/2602.01658) · [PDF](https://arxiv.org/pdf/2602.01658.pdf)  
**作者**：Seyed Mohammad Hadi Hosseini, Amir Najafi, Mahdieh Soleymani Baghshah  

**一句话要点**：提出针对高维离线老虎机奖励模型的对抗攻击，揭示其脆弱性

**关键词**：离线老虎机, 对抗攻击, 奖励模型, 高维脆弱性, 生成模型评估

## 3 点简述
- 研究离线老虎机评估在奖励模型被对抗扰动时的安全性问题
- 理论证明高维下攻击所需扰动范数减小，实验验证针对美学质量和组合对齐评估器的攻击有效性
- 攻击通过精心设计的权重扰动实现高成功率，而随机扰动无效

## 摘要（原文）

> Bandit algorithms have recently emerged as a powerful tool for evaluating machine learning models, including generative image models and large language models, by efficiently identifying top-performing candidates without exhaustive comparisons. These methods typically rely on a reward model, often distributed with public weights on platforms such as Hugging Face, to provide feedback to the bandit. While online evaluation is expensive and requires repeated trials, offline evaluation with logged data has become an attractive alternative. However, the adversarial robustness of offline bandit evaluation remains largely unexplored, particularly when an attacker perturbs the reward model (rather than the training data) prior to bandit training. In this work, we fill this gap by investigating, both theoretically and empirically, the vulnerability of offline bandit training to adversarial manipulations of the reward model. We introduce a novel threat model in which an attacker exploits offline data in high-dimensional settings to hijack the bandit's behavior. Starting with linear reward functions and extending to nonlinear models such as ReLU neural networks, we study attacks on two Hugging Face evaluators used for generative model assessment: one measuring aesthetic quality and the other assessing compositional alignment. Our results show that even small, imperceptible perturbations to the reward model's weights can drastically alter the bandit's behavior. From a theoretical perspective, we prove a striking high-dimensional effect: as input dimensionality increases, the perturbation norm required for a successful attack decreases, making modern applications such as image evaluation especially vulnerable. Extensive experiments confirm that naive random perturbations are ineffective, whereas carefully targeted perturbations achieve near-perfect attack success rates ...

