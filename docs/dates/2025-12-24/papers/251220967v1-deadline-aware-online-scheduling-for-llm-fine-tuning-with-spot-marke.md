---
layout: default
title: Deadline-Aware Online Scheduling for LLM Fine-Tuning with Spot Market Predictions
---

# Deadline-Aware Online Scheduling for LLM Fine-Tuning with Spot Market Predictions
**arXiv**：[2512.20967v1](https://arxiv.org/abs/2512.20967) · [PDF](https://arxiv.org/pdf/2512.20967.pdf)  
**作者**：Linggao Kong, Yuedong Xu, Lei Jiao, Chuan Xu  

**一句话要点**：提出基于现货市场预测的在线调度框架，以混合实例优化大模型微调成本与截止时间约束。

**关键词**：大模型微调, GPU调度, 现货市场预测, 在线算法, 成本优化, 截止时间约束

## 3 点简述
- 核心问题：大模型微调成本高，GPU现货实例价格与可用性波动大，需在截止时间内调度。
- 方法要点：利用现货市场预测，设计在线分配算法与无预测补充算法，通过策略选择自适应优化。
- 实验或效果：框架在动态市场中自适应选择最佳策略，相比基线提升效用达54.8%。

## 摘要（原文）

> As foundation models grow in size, fine-tuning them becomes increasingly expensive. While GPU spot instances offer a low-cost alternative to on-demand resources, their volatile prices and availability make deadline-aware scheduling particularly challenging. We tackle this difficulty by using a mix of spot and on-demand instances. Distinctively, we show the predictability of prices and availability in a spot instance market, the power of prediction in enabling cost-efficient scheduling and its sensitivity to estimation errors. An integer programming problem is formulated to capture the use of mixed instances under both the price and availability dynamics. We propose an online allocation algorithm with prediction based on the committed horizon control approach that leverages a \emph{commitment level} to enforce the partial sequence of decisions. When this prediction becomes inaccurate, we further present a complementary online algorithm without predictions. An online policy selection algorithm is developed that learns the best policy from a pool constructed by varying the parameters of both algorithms. We prove that the prediction-based algorithm achieves tighter performance bounds as prediction error decreases, while the policy selection algorithm possesses a regret bound of $\mathcal{O}(\sqrt{T})$. Experimental results demonstrate that our online framework can adaptively select the best policy under varying spot market dynamics and prediction quality, consistently outperforming baselines and improving utility by up to 54.8\%.

