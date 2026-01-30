---
layout: default
title: PowerGenie: Analytically-Guided Evolutionary Discovery of Superior Reconfigurable Power Converters
---

# PowerGenie: Analytically-Guided Evolutionary Discovery of Superior Reconfigurable Power Converters
**arXiv**：[2601.21984v1](https://arxiv.org/abs/2601.21984) · [PDF](https://arxiv.org/pdf/2601.21984.pdf)  
**作者**：Jian Gao, Yiwei Zou, Abhishek Pradhan, Wenhao Huang, Yumin Su, Kaiyuan Yang, Xuan Zhang  

**一句话要点**：提出PowerGenie框架，通过分析引导进化方法自动发现高性能可重构电源转换器。

**关键词**：电源转换器设计, 自动化电路发现, 进化算法, 分析建模, 性能优化

## 3 点简述
- 核心问题：传统方法难以在指数级设计空间中自动发现高性能电路拓扑。
- 方法要点：结合自动化分析框架和进化微调，避免模式崩溃和过拟合。
- 实验效果：发现新型8模式转换器，FoM提升23%，SPICE仿真验证效率增益。

## 摘要（原文）

> Discovering superior circuit topologies requires navigating an exponentially large design space-a challenge traditionally reserved for human experts. Existing AI methods either select from predefined templates or generate novel topologies at a limited scale without rigorous verification, leaving large-scale performance-driven discovery underexplored. We present PowerGenie, a framework for automated discovery of higher-performance reconfigurable power converters at scale. PowerGenie introduces: (1) an automated analytical framework that determines converter functionality and theoretical performance limits without component sizing or SPICE simulation, and (2) an evolutionary finetuning method that co-evolves a generative model with its training distribution through fitness selection and uniqueness verification. Unlike existing methods that suffer from mode collapse and overfitting, our approach achieves higher syntax validity, function validity, novelty rate, and figure-of-merit (FoM). PowerGenie discovers a novel 8-mode reconfigurable converter with 23% higher FoM than the best training topology. SPICE simulations confirm average absolute efficiency gains of 10% across 8 modes and up to 17% at a single mode. Code is available at https://github.com/xz-group/PowerGenie.

