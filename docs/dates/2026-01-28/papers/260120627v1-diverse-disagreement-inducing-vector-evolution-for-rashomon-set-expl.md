---
layout: default
title: DIVERSE: Disagreement-Inducing Vector Evolution for Rashomon Set Exploration
---

# DIVERSE: Disagreement-Inducing Vector Evolution for Rashomon Set Exploration
**arXiv**：[2601.20627v1](https://arxiv.org/abs/2601.20627) · [PDF](https://arxiv.org/pdf/2601.20627.pdf)  
**作者**：Gilles Eerlings, Brent Zoomers, Jori Liesenborgs, Gustavo Rovelo Ruiz, Kris Luyten  

**一句话要点**：提出DIVERSE框架以高效探索深度神经网络的Rashomon集合

**关键词**：Rashomon集合探索, 模型多样性, 进化策略, 特征调制, 深度神经网络

## 3 点简述
- 核心问题：如何系统探索Rashomon集合，即预测行为不同但精度匹配的模型集合
- 方法要点：通过FiLM层增强预训练模型，使用CMA-ES搜索调制空间生成多样变体
- 实验或效果：在MNIST等数据集上发现高性能且功能不同的模型，计算成本较低

## 摘要（原文）

> We propose DIVERSE, a framework for systematically exploring the Rashomon set of deep neural networks, the collection of models that match a reference model's accuracy while differing in their predictive behavior. DIVERSE augments a pretrained model with Feature-wise Linear Modulation (FiLM) layers and uses Covariance Matrix Adaptation Evolution Strategy (CMA-ES) to search a latent modulation space, generating diverse model variants without retraining or gradient access. Across MNIST, PneumoniaMNIST, and CIFAR-10, DIVERSE uncovers multiple high-performing yet functionally distinct models. Our experiments show that DIVERSE offers a competitive and efficient exploration of the Rashomon set, making it feasible to construct diverse sets that maintain robustness and performance while supporting well-balanced model multiplicity. While retraining remains the baseline to generate Rashomon sets, DIVERSE achieves comparable diversity at reduced computational cost.

