---
layout: default
title: When to restart? Exploring escalating restarts on convergence
---

# When to restart? Exploring escalating restarts on convergence
**arXiv**：[2603.04117v1](https://arxiv.org/abs/2603.04117) · [PDF](https://arxiv.org/pdf/2603.04117.pdf)  
**作者**：Ayush K. Varshney, Šarūnas Girdzijauskas, Konstantinos Vandikas, Aneta Vulgarakis Feljan  

**一句话要点**：提出SGD-ER方法，通过自适应重启学习率以改善深度网络收敛性能。

**关键词**：学习率调度, 自适应重启, 深度网络优化, 收敛检测, 局部极小值逃离

## 3 点简述
- 现有学习率调度器依赖固定触发，忽略训练动态如停滞或收敛行为。
- SGD-ER监测训练进度，在检测到停滞时触发重启，线性提升学习率以逃离尖锐局部极小值。
- 在CIFAR-10/100和TinyImageNet上测试，SGD-ER相比标准调度器提升测试精度0.5-4.5%。

## 摘要（原文）

> Learning rate scheduling plays a critical role in the optimization of deep neural networks, directly influencing convergence speed, stability, and generalization. While existing schedulers such as cosine annealing, cyclical learning rates, and warm restarts have shown promise, they often rely on fixed or periodic triggers that are agnostic to the training dynamics, such as stagnation or convergence behavior. In this work, we propose a simple yet effective strategy, which we call Stochastic Gradient Descent with Escalating Restarts (SGD-ER). It adaptively increases the learning rate upon convergence. Our method monitors training progress and triggers restarts when stagnation is detected, linearly escalating the learning rate to escape sharp local minima and explore flatter regions of the loss landscape. We evaluate SGD-ER across CIFAR-10, CIFAR-100, and TinyImageNet on a range of architectures including ResNet-18/34/50, VGG-16, and DenseNet-101. Compared to standard schedulers, SGD-ER improves test accuracy by 0.5-4.5%, demonstrating the benefit of convergence-aware escalating restarts for better local optima.

