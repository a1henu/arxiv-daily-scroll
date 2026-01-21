---
layout: default
title: Quadratic Upper Bound for Boosting Robustness
---

# Quadratic Upper Bound for Boosting Robustness
**arXiv**：[2601.13645v1](https://arxiv.org/abs/2601.13645) · [PDF](https://arxiv.org/pdf/2601.13645.pdf)  
**作者**：Euijin You, Hyang-Won Lee  

**一句话要点**：提出二次上界损失函数以提升快速对抗训练中的鲁棒性

**关键词**：对抗训练, 快速对抗训练, 鲁棒性提升, 损失函数优化, 二次上界

## 3 点简述
- 核心问题：快速对抗训练因对抗空间探索不足导致鲁棒性下降
- 方法要点：推导对抗训练损失函数的二次上界，并应用于现有快速对抗训练方法
- 实验或效果：应用二次上界损失显著提升鲁棒性，可能源于损失景观平滑化

## 摘要（原文）

> Fast adversarial training (FAT) aims to enhance the robustness of models against adversarial attacks with reduced training time, however, FAT often suffers from compromised robustness due to insufficient exploration of adversarial space. In this paper, we develop a loss function to mitigate the problem of degraded robustness under FAT. Specifically, we derive a quadratic upper bound (QUB) on the adversarial training (AT) loss function and propose to utilize the bound with existing FAT methods. Our experimental results show that applying QUB loss to the existing methods yields significant improvement of robustness. Furthermore, using various metrics, we demonstrate that this improvement is likely to result from the smoothened loss landscape of the resulting model.

