---
layout: default
title: AutoDriDM: An Explainable Benchmark for Decision-Making of Vision-Language Models in Autonomous Driving
---

# AutoDriDM: An Explainable Benchmark for Decision-Making of Vision-Language Models in Autonomous Driving
**arXiv**：[2601.14702v1](https://arxiv.org/abs/2601.14702) · [PDF](https://arxiv.org/pdf/2601.14702.pdf)  
**作者**：Zecong Tang, Zixu Wang, Yifei Wang, Weitong Lian, Tianjian Gao, Haoran Li, Tengju Ru, Lingyi Meng, Zhejun Cui, Yichen Zhu, Qi Kang, Kaixuan Wang, Yu Zhang  

**一句话要点**：提出AutoDriDM基准以评估自动驾驶中视觉语言模型的决策能力

**关键词**：自动驾驶, 视觉语言模型, 决策评估, 基准测试, 可解释性分析

## 3 点简述
- 现有基准过度强调感知能力，未能充分评估决策过程
- 构建包含6,650个问题的决策中心化渐进基准，涵盖对象、场景和决策维度
- 评估主流模型并分析感知与决策性能的弱对齐，识别逻辑推理错误等失败模式

## 摘要（原文）

> Autonomous driving is a highly challenging domain that requires reliable perception and safe decision-making in complex scenarios. Recent vision-language models (VLMs) demonstrate reasoning and generalization abilities, opening new possibilities for autonomous driving; however, existing benchmarks and metrics overemphasize perceptual competence and fail to adequately assess decision-making processes. In this work, we present AutoDriDM, a decision-centric, progressive benchmark with 6,650 questions across three dimensions - Object, Scene, and Decision. We evaluate mainstream VLMs to delineate the perception-to-decision capability boundary in autonomous driving, and our correlation analysis reveals weak alignment between perception and decision-making performance. We further conduct explainability analyses of models' reasoning processes, identifying key failure modes such as logical reasoning errors, and introduce an analyzer model to automate large-scale annotation. AutoDriDM bridges the gap between perception-centered and decision-centered evaluation, providing guidance toward safer and more reliable VLMs for real-world autonomous driving.

