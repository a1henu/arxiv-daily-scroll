---
layout: default
title: HPM-KD: Hierarchical Progressive Multi-Teacher Framework for Knowledge Distillation and Efficient Model Compression
---

# HPM-KD: Hierarchical Progressive Multi-Teacher Framework for Knowledge Distillation and Efficient Model Compression
**arXiv**：[2512.09886v1](https://arxiv.org/abs/2512.09886) · [PDF](https://arxiv.org/pdf/2512.09886.pdf)  
**作者**：Gustavo Coelho Haase, Paulo Henrique Dourado da Silva  

**一句话要点**：提出HPM-KD框架以解决知识蒸馏中的超参数敏感、容量差距和多教师协调问题

**关键词**：知识蒸馏, 模型压缩, 多教师学习, 元学习, 并行处理

## 3 点简述
- 核心问题：知识蒸馏存在超参数敏感、容量差距、多教师协调差和计算资源低效问题
- 方法要点：集成自适应配置、渐进蒸馏链、注意力加权多教师集成等六组件
- 实验或效果：在CIFAR和表格数据集上实现10-15倍压缩，保持85%精度，减少30-40%训练时间

## 摘要（原文）

> Knowledge Distillation (KD) has emerged as a promising technique for model compression but faces critical limitations: (1) sensitivity to hyperparameters requiring extensive manual tuning, (2) capacity gap when distilling from very large teachers to small students, (3) suboptimal coordination in multi-teacher scenarios, and (4) inefficient use of computational resources. We present \textbf{HPM-KD}, a framework that integrates six synergistic components: (i) Adaptive Configuration Manager via meta-learning that eliminates manual hyperparameter tuning, (ii) Progressive Distillation Chain with automatically determined intermediate models, (iii) Attention-Weighted Multi-Teacher Ensemble that learns dynamic per-sample weights, (iv) Meta-Learned Temperature Scheduler that adapts temperature throughout training, (v) Parallel Processing Pipeline with intelligent load balancing, and (vi) Shared Optimization Memory for cross-experiment reuse. Experiments on CIFAR-10, CIFAR-100, and tabular datasets demonstrate that HPM-KD: achieves 10x-15x compression while maintaining 85% accuracy retention, eliminates the need for manual tuning, and reduces training time by 30-40% via parallelization. Ablation studies confirm independent contribution of each component (0.10-0.98 pp). HPM-KD is available as part of the open-source DeepBridge library.

