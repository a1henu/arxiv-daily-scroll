---
layout: default
title: RealPDEBench: A Benchmark for Complex Physical Systems with Real-World Data
---

# RealPDEBench: A Benchmark for Complex Physical Systems with Real-World Data
**arXiv**：[2601.01829v1](https://arxiv.org/abs/2601.01829) · [PDF](https://arxiv.org/pdf/2601.01829.pdf)  
**作者**：Peiyan Hu, Haodong Feng, Hongyuan Liu, Tongtong Yan, Wenhao Deng, Tianrun Gao, Rong Zheng, Haoren Zheng, Chenglei Yu, Chuanrui Wang, Kaiwen Li, Zhi-Ming Ma, Dezhi Zhou, Xingcai Lu, Dixia Fan, Tailin Wu  

**一句话要点**：提出RealPDEBench基准，整合真实世界测量与配对数值模拟，以解决科学机器学习中真实数据缺乏的问题。

**关键词**：科学机器学习, 基准测试, 真实世界数据, 偏微分方程, 模拟到真实迁移

## 3 点简述
- 核心问题：科学机器学习因缺乏真实世界数据，模型多基于模拟数据训练，限制了发展和评估。
- 方法要点：构建包含五个数据集、三个任务、八个指标和十个基线的基准，促进真实与模拟数据比较。
- 实验或效果：实验显示模拟与真实数据存在显著差异，模拟数据预训练能提升准确性和收敛性。

## 摘要（原文）

> Predicting the evolution of complex physical systems remains a central problem in science and engineering. Despite rapid progress in scientific Machine Learning (ML) models, a critical bottleneck is the lack of expensive real-world data, resulting in most current models being trained and validated on simulated data. Beyond limiting the development and evaluation of scientific ML, this gap also hinders research into essential tasks such as sim-to-real transfer. We introduce RealPDEBench, the first benchmark for scientific ML that integrates real-world measurements with paired numerical simulations. RealPDEBench consists of five datasets, three tasks, eight metrics, and ten baselines. We first present five real-world measured datasets with paired simulated datasets across different complex physical systems. We further define three tasks, which allow comparisons between real-world and simulated data, and facilitate the development of methods to bridge the two. Moreover, we design eight evaluation metrics, spanning data-oriented and physics-oriented metrics, and finally benchmark ten representative baselines, including state-of-the-art models, pretrained PDE foundation models, and a traditional method. Experiments reveal significant discrepancies between simulated and real-world data, while showing that pretraining with simulated data consistently improves both accuracy and convergence. In this work, we hope to provide insights from real-world data, advancing scientific ML toward bridging the sim-to-real gap and real-world deployment. Our benchmark, datasets, and instructions are available at https://realpdebench.github.io/.

