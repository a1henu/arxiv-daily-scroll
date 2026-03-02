---
layout: default
title: BTTackler: A Diagnosis-based Framework for Efficient Deep Learning Hyperparameter Optimization
---

# BTTackler: A Diagnosis-based Framework for Efficient Deep Learning Hyperparameter Optimization
**arXiv**：[2602.23630v1](https://arxiv.org/abs/2602.23630) · [PDF](https://arxiv.org/pdf/2602.23630.pdf)  
**作者**：Zhongyi Pei, Zhiyao Cen, Yipeng Huang, Chen Wang, Lin Liu, Philip Yu, Mingsheng Long  

**一句话要点**：提出BTTackler框架，通过训练诊断提升深度学习超参数优化效率

**关键词**：超参数优化, 训练诊断, 深度学习, 自动化方法, 效率提升

## 3 点简述
- 核心问题：传统基于准确率的HPO方法在早期训练中难以检测梯度消失等严重问题，导致资源浪费和优化效率低下。
- 方法要点：BTTackler引入训练诊断，通过量化指标自动识别训练问题，并触发早期终止以处理不良试验。
- 实验或效果：在代表性任务中，BTTackler平均减少40.33%时间达到相同准确率，并在给定时间内增加44.5%的top-10试验。

## 摘要（原文）

> Hyperparameter optimization (HPO) is known to be costly in deep learning, especially when leveraging automated approaches. Most of the existing automated HPO methods are accuracy-based, i.e., accuracy metrics are used to guide the trials of different hyperparameter configurations amongst a specific search space. However, many trials may encounter severe training problems, such as vanishing gradients and insufficient convergence, which can hardly be reflected by accuracy metrics in the early stages of the training and often result in poor performance. This leads to an inefficient optimization trajectory because the bad trials occupy considerable computation resources and reduce the probability of finding excellent hyperparameter configurations within a time limitation. In this paper, we propose \textbf{Bad Trial Tackler (BTTackler)}, a novel HPO framework that introduces training diagnosis to identify training problems automatically and hence tackles bad trials. BTTackler diagnoses each trial by calculating a set of carefully designed quantified indicators and triggers early termination if any training problems are detected. Evaluations are performed on representative HPO tasks consisting of three classical deep neural networks (DNN) and four widely used HPO methods. To better quantify the effectiveness of an automated HPO method, we propose two new measurements based on accuracy and time consumption. Results show the advantage of BTTackler on two-fold: (1) it reduces 40.33\% of time consumption to achieve the same accuracy comparable to baseline methods on average and (2) it conducts 44.5\% more top-10 trials than baseline methods on average within a given time budget. We also released an open-source Python library that allows users to easily apply BTTackler to automated HPO processes with minimal code changes.

