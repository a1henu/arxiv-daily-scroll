---
layout: default
title: Automatic Adjustment of HPA Parameters and Attack Prevention in Kubernetes Using Random Forests
---

# Automatic Adjustment of HPA Parameters and Attack Prevention in Kubernetes Using Random Forests
**arXiv**：[2601.13515v1](https://arxiv.org/abs/2601.13515) · [PDF](https://arxiv.org/pdf/2601.13515.pdf)  
**作者**：Hanlin Zhou, Huah Yong Chan, Jingfei Ni, Mengchun Wu, Qing Deng  

**一句话要点**：提出基于随机森林的Kubernetes HPA参数自动调整与攻击预防方法，以HTTP状态码为自定义指标管理攻击流量。

**关键词**：Kubernetes HPA, 随机森林分类, 攻击预防, 自定义指标, 蜜罐技术, 动态参数调整

## 3 点简述
- 核心问题：Kubernetes中HPA在攻击场景下易过度扩展，需动态调整参数以隔离攻击流量。
- 方法要点：集成随机森林算法预测攻击，动态调整HPA最大pod参数，并将攻击IP重定向至蜜罐pod。
- 实验或效果：实验显示能降低5XX状态码发生率，有效隔离攻击流量，避免HPA因攻击而过度扩展。

## 摘要（原文）

> In this paper, HTTP status codes are used as custom metrics within the HPA as the experimental scenario. By integrating the Random Forest classification algorithm from machine learning, attacks are assessed and predicted, dynamically adjusting the maximum pod parameter in the HPA to manage attack traffic. This approach enables the adjustment of HPA parameters using machine learning scripts in targeted attack scenarios while effectively managing attack traffic. All access from attacking IPs is redirected to honeypot pods, achieving a lower incidence of 5XX status codes through HPA pod adjustments under high load conditions. This method also ensures effective isolation of attack traffic, preventing excessive HPA expansion due to attacks. Additionally, experiments conducted under various conditions demonstrate the importance of setting appropriate thresholds for HPA adjustments.

