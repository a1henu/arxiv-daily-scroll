---
layout: default
title: ReBA-Pred-Net: Weakly-Supervised Regional Brain Age Prediction on MRI
---

# ReBA-Pred-Net: Weakly-Supervised Regional Brain Age Prediction on MRI
**arXiv**：[2602.12751v1](https://arxiv.org/abs/2602.12751) · [PDF](https://arxiv.org/pdf/2602.12751.pdf)  
**作者**：Shuai Shao, Yan Wang, Shu Jiang, Shiyuan Zhao, Xinzhe Luo, Di Yang, Jiangtao Wang, Yutong Bai, Jianguo Zhang  

**一句话要点**：提出ReBA-Pred-Net以解决区域脑年龄预测问题，采用弱监督教师-学生框架。

**关键词**：区域脑年龄预测, 弱监督学习, 教师-学生框架, MRI分析, 脑健康生物标志物

## 3 点简述
- 核心问题：全脑年龄预测粗粒度，难以支持疾病表征和区域选择性变化研究。
- 方法要点：教师-学生框架生成软区域脑年龄，结合临床先验一致性约束指导预测。
- 实验或效果：引入间接指标评估统计和事实一致性，多骨干网络实验验证有效性。

## 摘要（原文）

> Brain age has become a prominent biomarker of brain health. Yet most prior work targets whole brain age (WBA), a coarse paradigm that struggles to support tasks such as disease characterization and research on development and aging patterns, because relevant changes are typically region-selective rather than brain-wide. Therefore, robust regional brain age (ReBA) estimation is critical, yet a widely generalizable model has yet to be established. In this paper, we propose the Regional Brain Age Prediction Network (ReBA-Pred-Net), a Teacher-Student framework designed for fine-grained brain age estimation. The Teacher produces soft ReBA to guide the Student to yield reliable ReBA estimates with a clinical-prior consistency constraint (regions within the same function should change similarly). For rigorous evaluation, we introduce two indirect metrics: Healthy Control Similarity (HCS), which assesses statistical consistency by testing whether regional brain-age-gap (ReBA minus chronological age) distributions align between training and unseen HC; and Neuro Disease Correlation (NDC), which assesses factual consistency by checking whether clinically confirmed patients show elevated brain-age-gap in disease-associated regions. Experiments across multiple backbones demonstrate the statistical and factual validity of our method.

