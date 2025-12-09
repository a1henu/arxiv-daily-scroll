---
layout: default
title: IFFair: Influence Function-driven Sample Reweighting for Fair Classification
---

# IFFair: Influence Function-driven Sample Reweighting for Fair Classification
**arXiv**：[2512.07249v1](https://arxiv.org/abs/2512.07249) · [PDF](https://arxiv.org/pdf/2512.07249.pdf)  
**作者**：Jingran Yang, Min Zhang, Lingfeng Zhang, Zhaohui Wang, Yonggang Zhang  

**一句话要点**：提出IFFair方法，基于影响函数动态调整样本权重以解决分类中的公平性问题。

**关键词**：公平分类, 影响函数, 样本重加权, 预处理方法, 机器学习公平性

## 3 点简述
- 核心问题：机器学习算法可能学习并加剧样本偏见，导致对弱势群体的歧视性决策。
- 方法要点：利用影响函数计算训练样本对不同群体的影响差异，动态调整样本权重，无需修改网络结构或数据特征。
- 实验或效果：在多个真实数据集上验证，IFFair能缓解多种公平性指标偏见，并在效用与公平性间取得更好权衡。

## 摘要（原文）

> Because machine learning has significantly improved efficiency and convenience in the society, it's increasingly used to assist or replace human decision-making. However, the data-based pattern makes related algorithms learn and even exacerbate potential bias in samples, resulting in discriminatory decisions against certain unprivileged groups, depriving them of the rights to equal treatment, thus damaging the social well-being and hindering the development of related applications. Therefore, we propose a pre-processing method IFFair based on the influence function. Compared with other fairness optimization approaches, IFFair only uses the influence disparity of training samples on different groups as a guidance to dynamically adjust the sample weights during training without modifying the network structure, data features and decision boundaries. To evaluate the validity of IFFair, we conduct experiments on multiple real-world datasets and metrics. The experimental results show that our approach mitigates bias of multiple accepted metrics in the classification setting, including demographic parity, equalized odds, equality of opportunity and error rate parity without conflicts. It also demonstrates that IFFair achieves better trade-off between multiple utility and fairness metrics compared with previous pre-processing methods.

