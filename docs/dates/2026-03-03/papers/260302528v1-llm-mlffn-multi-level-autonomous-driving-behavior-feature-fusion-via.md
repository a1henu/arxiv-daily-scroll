---
layout: default
title: LLM-MLFFN: Multi-Level Autonomous Driving Behavior Feature Fusion via Large Language Model
---

# LLM-MLFFN: Multi-Level Autonomous Driving Behavior Feature Fusion via Large Language Model
**arXiv**：[2603.02528v1](https://arxiv.org/abs/2603.02528) · [PDF](https://arxiv.org/pdf/2603.02528.pdf)  
**作者**：Xiangyu Li, Tianyi Wang, Xi Cheng, Rakesh Chowdary Machineni, Zhaomiao Guo, Sikai Chen, Junfeng Jiao, Christian Claudel  

**一句话要点**：提出LLM-MLFFN以解决自动驾驶行为分类中语义抽象不足的问题

**关键词**：自动驾驶行为分类, 大语言模型, 多级特征融合, 语义抽象, 加权注意力机制, Waymo数据集

## 3 点简述
- 核心问题：现有方法依赖数值时间序列建模，缺乏语义抽象，影响复杂交通环境下的可解释性和鲁棒性。
- 方法要点：结合多级特征提取、LLM语义描述和双通道加权注意力融合，整合数值与语义特征。
- 实验或效果：在Waymo数据集上分类准确率超过94%，优于现有机器学习模型，消融研究验证多级融合和LLM贡献。

## 摘要（原文）

> Accurate classification of autonomous vehicle (AV) driving behaviors is critical for safety validation, performance diagnosis, and traffic integration analysis. However, existing approaches primarily rely on numerical time-series modeling and often lack semantic abstraction, limiting interpretability and robustness in complex traffic environments. This paper presents LLM-MLFFN, a novel large language model (LLM)-enhanced multi-level feature fusion network designed to address the complexities of multi-dimensional driving data. The proposed LLM-MLFFN framework integrates priors from largescale pre-trained models and employs a multi-level approach to enhance classification accuracy. LLM-MLFFN comprises three core components: (1) a multi-level feature extraction module that extracts statistical, behavioral, and dynamic features to capture the quantitative aspects of driving behaviors; (2) a semantic description module that leverages LLMs to transform raw data into high-level semantic features; and (3) a dual-channel multi-level feature fusion network that combines numerical and semantic features using weighted attention mechanisms to improve robustness and prediction accuracy. Evaluation on the Waymo open trajectory dataset demonstrates the superior performance of the proposed LLM-MLFFN, achieving a classification accuracy of over 94%, surpassing existing machine learning models. Ablation studies further validate the critical contributions of multi-level fusion, feature extraction strategies, and LLM-derived semantic reasoning. These results suggest that integrating structured feature modeling with language-driven semantic abstraction provides a principled and interpretable pathway for robust autonomous driving behavior classification.

