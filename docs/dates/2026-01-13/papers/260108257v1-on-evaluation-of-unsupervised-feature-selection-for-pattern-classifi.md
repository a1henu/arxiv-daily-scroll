---
layout: default
title: On Evaluation of Unsupervised Feature Selection for Pattern Classification
---

# On Evaluation of Unsupervised Feature Selection for Pattern Classification
**arXiv**：[2601.08257v1](https://arxiv.org/abs/2601.08257) · [PDF](https://arxiv.org/pdf/2601.08257.pdf)  
**作者**：Gyu-Il Kim, Dae-Won Kim, Jaesung Lee  

**一句话要点**：采用多标签分类框架重新评估无监督特征选择方法，揭示单标签评估的局限性。

**关键词**：无监督特征选择, 多标签分类, 评估方法, 模式识别, 特征选择评估

## 3 点简述
- 核心问题：现有无监督特征选择方法评估依赖单标签数据集，评估结果受标签选择影响，可能不反映真实判别能力。
- 方法要点：提出基于多标签分类框架的评估范式，避免单标签评估的随机性，实现更公平可靠的比较。
- 实验或效果：在21个多标签数据集上测试代表性方法，发现性能排名与单标签设置显著不同，验证多标签评估的有效性。

## 摘要（原文）

> Unsupervised feature selection aims to identify a compact subset of features that captures the intrinsic structure of data without supervised label. Most existing studies evaluate the performance of methods using the single-label dataset that can be instantiated by selecting a label from multi-label data while maintaining the original features. Because the chosen label can vary arbitrarily depending on the experimental setting, the superiority among compared methods can be changed with regard to which label happens to be selected. Thus, evaluating unsupervised feature selection methods based solely on single-label accuracy is unreasonable for assessing their true discriminative ability. This study revisits this evaluation paradigm by adopting a multi-label classification framework. Experiments on 21 multi-label datasets using several representative methods demonstrate that performance rankings differ markedly from those reported under single-label settings, suggesting the possibility of multi-label evaluation settings for fair and reliable comparison of unsupervised feature selection methods.

