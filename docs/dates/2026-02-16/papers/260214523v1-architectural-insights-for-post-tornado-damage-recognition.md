---
layout: default
title: Architectural Insights for Post-Tornado Damage Recognition
---

# Architectural Insights for Post-Tornado Damage Recognition
**arXiv**：[2602.14523v1](https://arxiv.org/abs/2602.14523) · [PDF](https://arxiv.org/pdf/2602.14523.pdf)  
**作者**：Robinson Umeike, Thang Dao, Shane Crawford, John van de Lindt, Blythe Johnston, Wanting, Wang, Trung Do, Ajibola Mofikoya, Sarbesh Banjara, Cuong Pham  

**一句话要点**：通过系统实验框架评估79个深度学习模型，优化器选择比架构更关键，提升龙卷风后建筑损伤识别性能。

**关键词**：龙卷风损伤识别, 深度学习模型评估, 优化器选择, 领域偏移, 类别不平衡, 建筑损伤评估

## 3 点简述
- 核心问题：龙卷风后建筑损伤识别面临领域偏移和类别不平衡，自动化方法性能受限。
- 方法要点：引入系统实验框架，评估79个CNN和Vision Transformer模型，使用新QSTD数据集进行2300+实验。
- 实验或效果：优化器从Adam切换到SGD可提升F1分数25-38点，低学习率1x10^(-4)提升平均F1 10.2点，ConvNeXt-Base模型在TMTD数据集上实现46.4% Macro F1。

## 摘要（原文）

> Rapid and accurate building damage assessment in the immediate aftermath of tornadoes is critical for coordinating life-saving search and rescue operations, optimizing emergency resource allocation, and accelerating community recovery. However, current automated methods struggle with the unique visual complexity of tornado-induced wreckage, primarily due to severe domain shift from standard pre-training datasets and extreme class imbalance in real-world disaster data. To address these challenges, we introduce a systematic experimental framework evaluating 79 open-source deep learning models, encompassing both Convolutional Neural Networks (CNNs) and Vision Transformers, across over 2,300 controlled experiments on our newly curated Quad-State Tornado Damage (QSTD) benchmark dataset. Our findings reveal that achieving operational-grade performance hinges on a complex interaction between architecture and optimization, rather than architectural selection alone. Most strikingly, we demonstrate that optimizer choice can be more consequential than architecture: switching from Adam to SGD provided dramatic F1 gains of +25 to +38 points for Vision Transformer and Swin Transformer families, fundamentally reversing their ranking from bottom-tier to competitive with top-performing CNNs. Furthermore, a low learning rate of 1x10^(-4) proved universally critical, boosting average F1 performance by +10.2 points across all architectures. Our champion model, ConvNeXt-Base trained with these optimized settings, demonstrated strong cross-event generalization on the held-out Tuscaloosa-Moore Tornado Damage (TMTD) dataset, achieving 46.4% Macro F1 (+34.6 points over baseline) and retaining 85.5% Ordinal Top-1 Accuracy despite temporal and sensor domain shifts.

