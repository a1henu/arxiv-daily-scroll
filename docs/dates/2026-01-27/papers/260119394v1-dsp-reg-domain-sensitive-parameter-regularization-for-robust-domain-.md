---
layout: default
title: DSP-Reg: Domain-Sensitive Parameter Regularization for Robust Domain Generalization
---

# DSP-Reg: Domain-Sensitive Parameter Regularization for Robust Domain Generalization
**arXiv**：[2601.19394v1](https://arxiv.org/abs/2601.19394) · [PDF](https://arxiv.org/pdf/2601.19394.pdf)  
**作者**：Xudong Han, Senkang Hu, Yihang Tao, Yu Guo, Philip Birch, Sam Tak Wu Kwong, Yuguang Fang  

**一句话要点**：提出域敏感参数正则化以增强模型在未见域上的泛化能力

**关键词**：域泛化, 参数正则化, 协方差分析, 域敏感参数, 模型鲁棒性, 未见域泛化

## 3 点简述
- 现有域泛化方法聚焦域不变特征学习，忽视参数级分析，可能限制泛化性能
- 基于协方差的参数敏感性分析框架量化参数对域偏移的敏感度，指导模型优化
- 在PACS等基准测试中，DSP-Reg平均准确率达66.7%，优于现有方法

## 摘要（原文）

> Domain Generalization (DG) is a critical area that focuses on developing models capable of performing well on data from unseen distributions, which is essential for real-world applications. Existing approaches primarily concentrate on learning domain-invariant features, which assume that a model robust to variations in the source domains will generalize well to unseen target domains. However, these approaches neglect a deeper analysis at the parameter level, which makes the model hard to explicitly differentiate between parameters sensitive to domain shifts and those robust, potentially hindering its overall ability to generalize. In order to address these limitations, we first build a covariance-based parameter sensitivity analysis framework to quantify the sensitivity of each parameter in a model to domain shifts. By computing the covariance of parameter gradients across multiple source domains, we can identify parameters that are more susceptible to domain variations, which serves as our theoretical foundation. Based on this, we propose Domain-Sensitive Parameter Regularization (DSP-Reg), a principled framework that guides model optimization by a soft regularization technique that encourages the model to rely more on domain-invariant parameters while suppressing those that are domain-specific. This approach provides a more granular control over the model's learning process, leading to improved robustness and generalization to unseen domains. Extensive experiments on benchmarks, such as PACS, VLCS, OfficeHome, and DomainNet, demonstrate that DSP-Reg outperforms state-of-the-art approaches, achieving an average accuracy of 66.7\% and surpassing all baselines.

