---
layout: default
title: Prediction-Powered Risk Monitoring of Deployed Models for Detecting Harmful Distribution Shifts
---

# Prediction-Powered Risk Monitoring of Deployed Models for Detecting Harmful Distribution Shifts
**arXiv**：[2602.02229v1](https://arxiv.org/abs/2602.02229) · [PDF](https://arxiv.org/pdf/2602.02229.pdf)  
**作者**：Guangyi Zhang, Yunlong Cai, Guanding Yu, Osvaldo Simeone  

**一句话要点**：提出预测驱动风险监控方法，用于动态环境中有限标注数据下的模型性能监测

**关键词**：风险监控, 预测驱动推断, 半监督学习, 分布偏移检测, 模型部署

## 3 点简述
- 研究动态环境下模型性能监控问题，标注数据有限
- 基于预测驱动推断，结合合成标签与少量真实标签构建风险下界
- 通过图像分类、大语言模型和电信监控实验验证有效性

## 摘要（原文）

> We study the problem of monitoring model performance in dynamic environments where labeled data are limited. To this end, we propose prediction-powered risk monitoring (PPRM), a semi-supervised risk-monitoring approach based on prediction-powered inference (PPI). PPRM constructs anytime-valid lower bounds on the running risk by combining synthetic labels with a small set of true labels. Harmful shifts are detected via a threshold-based comparison with an upper bound on the nominal risk, satisfying assumption-free finite-sample guarantees in the probability of false alarm. We demonstrate the effectiveness of PPRM through extensive experiments on image classification, large language model (LLM), and telecommunications monitoring tasks.

