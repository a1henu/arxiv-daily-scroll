---
layout: default
title: Efficient Credal Prediction through Decalibration
---

# Efficient Credal Prediction through Decalibration
**arXiv**：[2603.08495v1](https://arxiv.org/abs/2603.08495) · [PDF](https://arxiv.org/pdf/2603.08495.pdf)  
**作者**：Paul Hofman, Timo Löhr, Maximilian Muschalik, Yusuf Sale, Eyke Hüllermeier  

**一句话要点**：提出基于去校准的高效信度预测方法，以解决复杂模型信度集构建的计算难题。

**关键词**：信度预测, 去校准, 概率区间, 计算效率, 基础模型, 不确定性表示

## 3 点简述
- 核心问题：信度集构建计算复杂，阻碍在基础模型等复杂架构中的应用。
- 方法要点：基于相对似然和去校准技术，为每个类别预测概率区间作为信度集。
- 实验或效果：在覆盖效率评估、分布外检测等任务中表现优异，适用于TabPFN和CLIP等模型。

## 摘要（原文）

> A reliable representation of uncertainty is essential for the application of modern machine learning methods in safety-critical settings. In this regard, the use of credal sets (i.e., convex sets of probability distributions) has recently been proposed as a suitable approach to representing epistemic uncertainty. However, as with other approaches to epistemic uncertainty, training credal predictors is computationally complex and usually involves (re-)training an ensemble of models. The resulting computational complexity prevents their adoption for complex models such as foundation models and multi-modal systems. To address this problem, we propose an efficient method for credal prediction that is grounded in the notion of relative likelihood and inspired by techniques for the calibration of probabilistic classifiers. For each class label, our method predicts a range of plausible probabilities in the form of an interval. To produce the lower and upper bounds of these intervals, we propose a technique that we refer to as decalibration. Extensive experiments show that our method yields credal sets with strong performance across diverse tasks, including coverage-efficiency evaluation, out-of-distribution detection, and in-context learning. Notably, we demonstrate credal prediction on models such as TabPFN and CLIP -- architectures for which the construction of credal sets was previously infeasible.

