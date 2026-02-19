---
layout: default
title: Benchmarking Adversarial Robustness and Adversarial Training Strategies for Object Detection
---

# Benchmarking Adversarial Robustness and Adversarial Training Strategies for Object Detection
**arXiv**：[2602.16494v1](https://arxiv.org/abs/2602.16494) · [PDF](https://arxiv.org/pdf/2602.16494.pdf)  
**作者**：Alexis Winter, Jean-Vincent Martini, Romaric Audigier, Angelique Loesch, Bertrand Luvison  

**一句话要点**：提出统一基准框架以公平评估目标检测模型的对抗鲁棒性与训练策略

**关键词**：目标检测, 对抗鲁棒性, 基准评估, 对抗训练, Vision Transformer, 攻击迁移性

## 3 点简述
- 核心问题：目标检测模型对抗攻击评估缺乏标准化，阻碍防御方法比较。
- 方法要点：设计基准框架，引入分离定位与分类错误的指标，评估攻击成本。
- 实验或效果：发现攻击对Transformer架构迁移性差，混合攻击训练策略最有效。

## 摘要（原文）

> Object detection models are critical components of automated systems, such as autonomous vehicles and perception-based robots, but their sensitivity to adversarial attacks poses a serious security risk. Progress in defending these models lags behind classification, hindered by a lack of standardized evaluation. It is nearly impossible to thoroughly compare attack or defense methods, as existing work uses different datasets, inconsistent efficiency metrics, and varied measures of perturbation cost. This paper addresses this gap by investigating three key questions: (1) How can we create a fair benchmark to impartially compare attacks? (2) How well do modern attacks transfer across different architectures, especially from Convolutional Neural Networks to Vision Transformers? (3) What is the most effective adversarial training strategy for robust defense? To answer these, we first propose a unified benchmark framework focused on digital, non-patch-based attacks. This framework introduces specific metrics to disentangle localization and classification errors and evaluates attack cost using multiple perceptual metrics. Using this benchmark, we conduct extensive experiments on state-of-the-art attacks and a wide range of detectors. Our findings reveal two major conclusions: first, modern adversarial attacks against object detection models show a significant lack of transferability to transformer-based architectures. Second, we demonstrate that the most robust adversarial training strategy leverages a dataset composed of a mix of high-perturbation attacks with different objectives (e.g., spatial and semantic), which outperforms training on any single attack.

