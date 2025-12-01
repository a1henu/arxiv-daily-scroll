---
layout: default
title: ClearGCD: Mitigating Shortcut Learning For Robust Generalized Category Discovery
---

# ClearGCD: Mitigating Shortcut Learning For Robust Generalized Category Discovery
**arXiv**：[2511.22892v1](https://arxiv.org/abs/2511.22892) · [PDF](https://arxiv.org/pdf/2511.22892.pdf)  
**作者**：Kailin Lyu, Jianwei He, Long Xiao, Jianing Zeng, Liang Fan, Lin Shu, Jie Hao  

**一句话要点**：提出ClearGCD框架以缓解广义类别发现中的捷径学习问题

**关键词**：广义类别发现, 捷径学习, 语义视图对齐, 捷径抑制正则化, 原型混淆, 开放世界场景

## 3 点简述
- 核心问题：现有方法因捷径学习导致原型混淆，削弱泛化能力并遗忘已知类别
- 方法要点：通过语义视图对齐和捷径抑制正则化，减少对非语义线索的依赖
- 实验或效果：在多个基准测试中优于先进方法，可无缝集成到参数化GCD方法

## 摘要（原文）

> In open-world scenarios, Generalized Category Discovery (GCD) requires identifying both known and novel categories within unlabeled data. However, existing methods often suffer from prototype confusion caused by shortcut learning, which undermines generalization and leads to forgetting of known classes. We propose ClearGCD, a framework designed to mitigate reliance on non-semantic cues through two complementary mechanisms. First, Semantic View Alignment (SVA) generates strong augmentations via cross-class patch replacement and enforces semantic consistency using weak augmentations. Second, Shortcut Suppression Regularization (SSR) maintains an adaptive prototype bank that aligns known classes while encouraging separation of potential novel ones. ClearGCD can be seamlessly integrated into parametric GCD approaches and consistently outperforms state-of-the-art methods across multiple benchmarks.

