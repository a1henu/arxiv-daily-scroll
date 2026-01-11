---
layout: default
title: DP-MGTD: Privacy-Preserving Machine-Generated Text Detection via Adaptive Differentially Private Entity Sanitization
---

# DP-MGTD: Privacy-Preserving Machine-Generated Text Detection via Adaptive Differentially Private Entity Sanitization
**arXiv**：[2601.04641v1](https://arxiv.org/abs/2601.04641) · [PDF](https://arxiv.org/pdf/2601.04641.pdf)  
**作者**：Lionel Z. Wang, Yusheng Zhao, Jiabin Luo, Xinfeng Li, Lixu Wang, Yinan Peng, Haoyang Li, XiaoFeng Wang, Wei Dong  

**一句话要点**：提出DP-MGTD框架，通过自适应差分隐私实体净化解决机器生成文本检测中的隐私保护问题。

**关键词**：差分隐私, 机器生成文本检测, 隐私保护, 自适应算法, 实体净化

## 3 点简述
- 核心问题：机器生成文本检测需处理敏感数据，隐私保护与检测准确性存在冲突。
- 方法要点：采用两阶段自适应差分隐私算法，对数值和文本实体分别应用拉普拉斯和指数机制。
- 实验或效果：在MGTBench-2.0数据集上实现高检测精度，优于非隐私基线，满足严格隐私保证。

## 摘要（原文）

> The deployment of Machine-Generated Text (MGT) detection systems necessitates processing sensitive user data, creating a fundamental conflict between authorship verification and privacy preservation. Standard anonymization techniques often disrupt linguistic fluency, while rigorous Differential Privacy (DP) mechanisms typically degrade the statistical signals required for accurate detection. To resolve this dilemma, we propose \textbf{DP-MGTD}, a framework incorporating an Adaptive Differentially Private Entity Sanitization algorithm. Our approach utilizes a two-stage mechanism that performs noisy frequency estimation and dynamically calibrates privacy budgets, applying Laplace and Exponential mechanisms to numerical and textual entities respectively. Crucially, we identify a counter-intuitive phenomenon where the application of DP noise amplifies the distinguishability between human and machine text by exposing distinct sensitivity patterns to perturbation. Extensive experiments on the MGTBench-2.0 dataset show that our method achieves near-perfect detection accuracy, significantly outperforming non-private baselines while satisfying strict privacy guarantees.

