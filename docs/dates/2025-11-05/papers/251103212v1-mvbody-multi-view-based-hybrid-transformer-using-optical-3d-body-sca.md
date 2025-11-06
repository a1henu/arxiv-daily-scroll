---
layout: default
title: MvBody: Multi-View-Based Hybrid Transformer Using Optical 3D Body Scan for Explainable Cesarean Section Prediction
---

# MvBody: Multi-View-Based Hybrid Transformer Using Optical 3D Body Scan for Explainable Cesarean Section Prediction
**arXiv**：[2511.03212v1](https://arxiv.org/abs/2511.03212) · [PDF](https://arxiv.org/pdf/2511.03212.pdf)  
**作者**：Ruting Cheng, Boyuan Feng, Yijiang Zheng, Chuhui Qiu, Aizierjiang Aiersilan, Joaquin A. Calderon, Wentao Zhao, Qing Pan, James K. Hahn  

**一句话要点**：提出MvBody多视图Transformer，利用3D体扫预测剖宫产风险，适用于资源有限场景。

**关键词**：剖宫产预测, 多视图Transformer, 3D体扫分析, 度量学习, 可解释AI

## 3 点简述
- 核心问题：资源有限场景下剖宫产风险预测困难，现有模型依赖医院参数。
- 方法要点：结合自报医疗数据和3D光学体扫，引入度量学习提升泛化能力。
- 实验效果：独立测试集准确率84.62%，AUC-ROC 0.724，优于基线方法。

## 摘要（原文）

> Accurately assessing the risk of cesarean section (CS) delivery is critical,
> especially in settings with limited medical resources, where access to
> healthcare is often restricted. Early and reliable risk prediction allows
> better-informed prenatal care decisions and can improve maternal and neonatal
> outcomes. However, most existing predictive models are tailored for in-hospital
> use during labor and rely on parameters that are often unavailable in
> resource-limited or home-based settings. In this study, we conduct a pilot
> investigation to examine the feasibility of using 3D body shape for CS risk
> assessment for future applications with more affordable general devices. We
> propose a novel multi-view-based Transformer network, MvBody, which predicts CS
> risk using only self-reported medical data and 3D optical body scans obtained
> between the 31st and 38th weeks of gestation. To enhance training efficiency
> and model generalizability in data-scarce environments, we incorporate a metric
> learning loss into the network. Compared to widely used machine learning models
> and the latest advanced 3D analysis methods, our method demonstrates superior
> performance, achieving an accuracy of 84.62% and an Area Under the Receiver
> Operating Characteristic Curve (AUC-ROC) of 0.724 on the independent test set.
> To improve transparency and trust in the model's predictions, we apply the
> Integrated Gradients algorithm to provide theoretically grounded explanations
> of the model's decision-making process. Our results indicate that pre-pregnancy
> weight, maternal age, obstetric history, previous CS history, and body shape,
> particularly around the head and shoulders, are key contributors to CS risk
> prediction.

