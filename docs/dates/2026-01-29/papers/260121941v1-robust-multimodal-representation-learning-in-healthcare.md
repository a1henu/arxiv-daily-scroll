---
layout: default
title: Robust Multimodal Representation Learning in Healthcare
---

# Robust Multimodal Representation Learning in Healthcare
**arXiv**：[2601.21941v1](https://arxiv.org/abs/2601.21941) · [PDF](https://arxiv.org/pdf/2601.21941.pdf)  
**作者**：Xiaoguang Zhu, Linxiao Gong, Lianlong Sun, Yang Liu, Haoyu Wang, Jing Liu  

**一句话要点**：提出双流特征去相关框架以解决医疗多模态表示学习中的系统性偏差问题

**关键词**：医疗多模态表示学习, 特征去相关, 结构因果分析, 双流神经网络, 系统性偏差处理

## 3 点简述
- 核心问题：真实医疗数据存在多源系统性偏差，影响多模态表示学习的泛化能力
- 方法要点：基于结构因果分析，通过双流神经网络分离因果特征与虚假相关性
- 实验或效果：在MIMIC-IV、eICU和ADNI数据集上验证了性能提升，框架模型无关

## 摘要（原文）

> Medical multimodal representation learning aims to integrate heterogeneous data into unified patient representations to support clinical outcome prediction. However, real-world medical datasets commonly contain systematic biases from multiple sources, which poses significant challenges for medical multimodal representation learning. Existing approaches typically focus on effective multimodal fusion, neglecting inherent biased features that affect the generalization ability. To address these challenges, we propose a Dual-Stream Feature Decorrelation Framework that identifies and handles the biases through structural causal analysis introduced by latent confounders. Our method employs a causal-biased decorrelation framework with dual-stream neural networks to disentangle causal features from spurious correlations, utilizing generalized cross-entropy loss and mutual information minimization for effective decorrelation. The framework is model-agnostic and can be integrated into existing medical multimodal learning methods. Comprehensive experiments on MIMIC-IV, eICU, and ADNI datasets demonstrate consistent performance improvements.

