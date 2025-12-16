---
layout: default
title: Behavior-Aware and Generalizable Defense Against Black-Box Adversarial Attacks for ML-Based IDS
---

# Behavior-Aware and Generalizable Defense Against Black-Box Adversarial Attacks for ML-Based IDS
**arXiv**：[2512.13501v1](https://arxiv.org/abs/2512.13501) · [PDF](https://arxiv.org/pdf/2512.13501.pdf)  
**作者**：Sabrine Ennaji, Elhadj Benkhelifa, Luigi Vincenzo Mancini  

**一句话要点**：提出自适应特征污染以防御基于机器学习的入侵检测系统中的黑盒对抗攻击

**关键词**：黑盒对抗攻击, 入侵检测系统, 自适应特征污染, 流量分析, 变化点检测, 攻击防御

## 3 点简述
- 核心问题：现有防御方法针对特定攻击、需模型访问或静态机制，难以泛化且影响检测性能。
- 方法要点：通过流量分析、变化点检测和自适应缩放，动态扰动攻击者可能利用的特征，破坏反馈循环。
- 实验或效果：评估显示能混淆攻击者、降低攻击效果并保持检测性能，具有通用性和不可检测性。

## 摘要（原文）

> Machine learning based intrusion detection systems are increasingly targeted by black box adversarial attacks, where attackers craft evasive inputs using indirect feedback such as binary outputs or behavioral signals like response time and resource usage. While several defenses have been proposed, including input transformation, adversarial training, and surrogate detection, they often fall short in practice. Most are tailored to specific attack types, require internal model access, or rely on static mechanisms that fail to generalize across evolving attack strategies. Furthermore, defenses such as input transformation can degrade intrusion detection system performance, making them unsuitable for real time deployment.
>   To address these limitations, we propose Adaptive Feature Poisoning, a lightweight and proactive defense mechanism designed specifically for realistic black box scenarios. Adaptive Feature Poisoning assumes that probing can occur silently and continuously, and introduces dynamic and context aware perturbations to selected traffic features, corrupting the attacker feedback loop without impacting detection capabilities. The method leverages traffic profiling, change point detection, and adaptive scaling to selectively perturb features that an attacker is likely exploiting, based on observed deviations.
>   We evaluate Adaptive Feature Poisoning against multiple realistic adversarial attack strategies, including silent probing, transferability based attacks, and decision boundary based attacks. The results demonstrate its ability to confuse attackers, degrade attack effectiveness, and preserve detection performance. By offering a generalizable, attack agnostic, and undetectable defense, Adaptive Feature Poisoning represents a significant step toward practical and robust adversarial resilience in machine learning based intrusion detection systems.

