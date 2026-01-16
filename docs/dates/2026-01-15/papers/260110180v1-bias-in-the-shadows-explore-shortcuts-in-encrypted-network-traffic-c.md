---
layout: default
title: Bias in the Shadows: Explore Shortcuts in Encrypted Network Traffic Classification
---

# Bias in the Shadows: Explore Shortcuts in Encrypted Network Traffic Classification
**arXiv**：[2601.10180v1](https://arxiv.org/abs/2601.10180) · [PDF](https://arxiv.org/pdf/2601.10180.pdf)  
**作者**：Chuyi Wang, Xiaohui Xie, Tongze Wang, Yong Cui  

**一句话要点**：提出BiasSeeker框架以检测加密网络流量分类中的数据集特定捷径特征

**关键词**：加密网络流量分类, 捷径学习, 特征选择, 模型无关框架, 数据集诊断

## 3 点简述
- 核心问题：预训练模型在加密流量分类中易学捷径特征，依赖虚假相关性，泛化能力差
- 方法要点：BiasSeeker为模型无关、数据驱动的半自动化框架，通过统计相关分析识别捷径特征
- 实验或效果：在19个公开数据集上评估，强调上下文感知特征选择和数据集特定诊断

## 摘要（原文）

> Pre-trained models operating directly on raw bytes have achieved promising performance in encrypted network traffic classification (NTC), but often suffer from shortcut learning-relying on spurious correlations that fail to generalize to real-world data. Existing solutions heavily rely on model-specific interpretation techniques, which lack adaptability and generality across different model architectures and deployment scenarios.
>   In this paper, we propose BiasSeeker, the first semi-automated framework that is both model-agnostic and data-driven for detecting dataset-specific shortcut features in encrypted traffic. By performing statistical correlation analysis directly on raw binary traffic, BiasSeeker identifies spurious or environment-entangled features that may compromise generalization, independent of any classifier. To address the diverse nature of shortcut features, we introduce a systematic categorization and apply category-specific validation strategies that reduce bias while preserving meaningful information.
>   We evaluate BiasSeeker on 19 public datasets across three NTC tasks. By emphasizing context-aware feature selection and dataset-specific diagnosis, BiasSeeker offers a novel perspective for understanding and addressing shortcut learning in encrypted network traffic classification, raising awareness that feature selection should be an intentional and scenario-sensitive step prior to model training.

